import pandas as pd
import xlsxwriter
from pandasql import sqldf
from  contexttimer import timer
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from data_store_objects import UserRequirement
import json
import requests
import logging as lg
import smautosettings as smauto_settings
import psycopg2
from jinja2 import Template
import datetime 
import numpy as np
class SmautoDataServices():
	def __init__(self):
		self.smautoData = pd.DataFrame()
		self._POSTGRE_HOSTNAME  =os.getenv("POSTGRE_HOSTNAME")
		self._POSTGRE_PORT_NO=os.getenv("POSTGRE_PORT_NO")
		self._POSTGRE_DBNAME=os.getenv("POSTGRE_DBNAME")
		self._POSTGRE_USERNAME=os.getenv("POSTGRE_USERNAME")
		self._POSTGRE_PWD=os.getenv("POSTGRE_PWD")

		self._TABLE_NAME = os.getenv("POSTGRE_TABLE_NAME")
		self.lg = lg
		self.lg.basicConfig(level=lg.DEBUG)
	@timer()
	def connectToSource(self):
		host=self._POSTGRE_HOSTNAME
		port=self._POSTGRE_PORT_NO
		dbname=self._POSTGRE_DBNAME
		username= self._POSTGRE_USERNAME
		pwd=self._POSTGRE_PWD
		table_name="new_car_master_data"

		conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={} sslmode='require'".format(host,port,dbname,username,pwd))
		# keep the connection object
		self.smautoData= conn
		print("self.smautoData",self.smautoData)
		return 0
	#done
	@timer()
	def executeQuery(self,select_clause, where_clause="1=1", column_tuple="", group_by_clause="",order_limit_by_clause="",table_name=""):
		conn = self.smautoData
		#print("client",client)
		# made this adjustment so that table name can be passed for similar cars 
		if len(table_name) == 0:
			table_name = self._TABLE_NAME
		

		
		query_string = "select {1} from {0} where {2} {3} {4}".format(table_name,select_clause,where_clause,group_by_clause, order_limit_by_clause)
		print("Query_string:",query_string)
		#result = client.sql(query_string,page_size=10000)
		result = pd.read_sql_query(query_string, conn)
		#print("result",result)
		result_df= pd.DataFrame(result, columns=column_tuple)
		return result_df

	#done
	#measures time
	@timer()
	def getManufacturerList(self):

		select_clause = "DISTINCT manufacturer, manufacturer_code,replace(manufacturer,'_',' ') manufacturer_disp  "
		where_clause = "1=1"
		column_tuple = ['manufacturer','manufacturer_code','manufacturer_disp']

		subset_df= self.executeQuery(select_clause,where_clause,column_tuple)
		return [(x, y,z) for x, y,z in zip(subset_df['manufacturer'],subset_df['manufacturer_code'],subset_df['manufacturer_disp'])]

	#done
	# measures time
	@timer()
	def modelBaseInfo(self,manu_id):

		select_clause = """model_name, model_image_name, model_code, manufacturer, manufacturer_code, 
cast(max(cost_of_variant)as int) max_variant_price, cast(min(cost_of_variant)as int) min_variant_price, 
count(DISTINCT variant_code)no_unique_variants,replace(manufacturer,'_',' ') manufacturer_disp, max(launch_dt) as launch_dt """
		where_clause = "manufacturer_code = '{0}'".format(manu_id)
		column_tuple = ['model_name', 'model_image_name', 'model_code', 'manufacturer','manufacturer_code', 'max_variant_price', 'min_variant_price', 'no_unique_variants','manufacturer_disp','launch_dt']
		group_by_clause = " GROUP BY model_code,model_name, model_image_name, model_code, manufacturer, manufacturer_code"
		mysmalldf= self.executeQuery(select_clause,where_clause,column_tuple,group_by_clause=group_by_clause).reset_index(drop=True)
		# print("mysmalldf",mysmalldf)
		return mysmalldf

	#done
	@timer()
	def modelVarInfo(self,model_cd,var_cd,df=False):
		select_clause = """ smauto_broad_feature_variant_specific_rank rnk, Broad_feature as "Broad_feature" ,Exact_Feature as "Exact_Feature",variant_name,data_value,variant_code,manufacturer_code,model_image_name,manufacturer,replace(manufacturer,'_',' ') manufacturer_disp  """
		where_clause = " model_code = '{0}' and variant_code ='{1}' and smauto_broad_feature_variant_specific_rank is not null  ".format(model_cd,var_cd)
		column_tuple = ['rnk','Broad_feature','Exact_Feature','variant_name','data_value','variant_code','manufacturer_code','model_image_name','manufacturer','manufacturer_disp']

		subset_df= self.executeQuery(select_clause,where_clause,column_tuple)
		#print("subset_df",subset_df.head(2))
		subset_df.fillna('',inplace=True)
		# IF WE DONT REMOVE, WE WILL GET JSON PARSING ERROR IN JAVASCRIPT, AM USING '' BUT WE CAN USE ANY OTHER KNOWN CODE LIKE 999999 FOR MISSING VALUES
		if df:
			return subset_df
		else :
			return subset_df.reset_index(drop=True).to_dict()

	#done
	@timer()
	def modelVarsList(self,model_cd,df=False):
		select_clause = """ distinct model_code, variant_code, variant_name, model_name, model_image_name, manufacturer,manufacturer_code,replace(manufacturer,'_',' ') manufacturer_disp,manufacturer_real_code  """
		where_clause = "model_code = '{0}'".format(model_cd)
		column_tuple = ['model_code', 'variant_code', 'variant_name', 'model_name', 'model_image_name', 'manufacturer','manufacturer_code','manufacturer_disp','manufacturer_real_code']
		subset_df= self.executeQuery(select_clause,where_clause,column_tuple)
		print("subset_df",subset_df)
		if df:
			return subset_df
		else:
			return subset_df.reset_index(drop=True).to_dict()


	# working on this

	@timer()
	def getColumnsListforSum(self,lst_elements):
		column_dict ={'petrol':'fuel_type_pet_score','diesel':'fuel_type_diesel_score',
					  'mileage':'mileage_score','safety':'safety_var_score',
					  'comfort':'comfort_var_score',
					  'city':'city_score', 'highway':'highway_score', 'offroad':'offrd_score',
					  'styling':'style_var_score',
					  'performance_1':'engine_cc_score','performance_2':'trans_score' }
		col_list_for_sum=[]

		for mdata in lst_elements:
			if mdata in column_dict.keys():
				col_list_for_sum.append(column_dict[mdata])

		return col_list_for_sum
	@timer() # working on this
	def myCarVarsList(self,userReqObj):
		smautoData = self.smautoData
		#options=userReqObj['options'] +['colours']
		options = userReqObj['options']
		MAX_NO_TOTAL_CAR_VAR = 150
		budget = userReqObj['budget']

		select_clause = """ distinct variant_name, variant_code, model_name,model_image_name, model_code, manufacturer, cast(cost_of_variant as int) """
		where_clause = "cost_of_variant < {0} ".format(budget)
		column_tuple = ['variant_name', 'variant_code', 'model_name','model_image_name', 'model_code', 'manufacturer', 'cost_of_variant','final_composite_score']
		order_limit_by_clause =  " order by final_composite_score desc limit {0} ".format(MAX_NO_TOTAL_CAR_VAR)

		user_settings_lst=[]
		for setting_var in userReqObj:
			if type(userReqObj[setting_var])==list:
				lg.debug("Reading the Options List")
				user_settings_lst = user_settings_lst + userReqObj[setting_var]
			else:
				user_settings_lst.append(userReqObj[setting_var])
		if 'performance' in user_settings_lst:
			user_settings_lst.append('performance_1')
			user_settings_lst.append('performance_2')

		col_list_for_sum= self.getColumnsListforSum(user_settings_lst)
		print("col_list_for_sum: ",col_list_for_sum)

		if len(col_list_for_sum)> 0 :
			final_composite_score_str = ",cast(" + "+".join(col_list_for_sum) + " as int) as final_composite_score"
		else :
			final_composite_score_str = ",0  as final_composite_score "
		select_clause+=final_composite_score_str
		final_result= self.executeQuery(select_clause,where_clause,column_tuple,order_limit_by_clause)

		final_result.reset_index()
		#print((final_result))
		variant_cd_lst = final_result.drop_duplicates(subset="model_code")
		return variant_cd_lst
	#done
	# @timer()
	# def es_search(self,query_string):
		# search_flds=['manufacturer','model_name','variant_name','Broad_feature','Exact_Feature','fuel_type','body','transmission_type']
		# mod_flds=[ "(" + x +":*" + query_string+ "*)"  for x in search_flds]
		# query_clause = " OR ".join(mod_flds)
		# MAX_NO_REORDS_FRM_SEARCH = 250
		# url = 'https://search-smauto-elasticsearch-dvrcidjde63mqv7z3mefckibay.us-east-1.es.amazonaws.com/smauto_ind_latest_data/_search?size={}&q=_{}'.format(MAX_NO_REORDS_FRM_SEARCH,query_clause)
		# print(url)
		# m_response = requests.post(url)
		# resp_json = m_response.json()['hits']['hits']
		# res_rows = []
		# for each_hit in resp_json:
			# res_rows.append(each_hit['_source'])
		# lg.info(ahit['_source'])
		# es_result_df = pd.DataFrame(res_rows)
		# print(es_result_df)
		# return es_result_df
	#done
	# @timer()
	# def get_unique(self):
	# 	col_string = 'Colours'
	# 	# war_string = 'Warranty'
	# 	# cos_string = 'Cost'
	# 	engs_string = 'Engine'
	# 	dim_string = 'Dimensions'
	# 	sus_string = 'Suspension'
	#
	# 	select_clause = """ distinct BROAD_FEATURE """
	# 	where_clause = "SMAUTO_RECO_BROAD_FV NOT LIKE '{0}' and SMAUTO_RECO_BROAD_FV NOT LIKE 'Warranty' and SMAUTO_RECO_BROAD_FV NOT LIKE 'Cost' ".format(col_string)
	# 	column_tuple = ['broad_feature']
	# 	subset_df= self.executeQuery(select_clause,where_clause,column_tuple)
	# 	return subset_df
		# done
	@timer()
	def searchServiceGetCarVarList(self,search_string):
		select_clause = """distinct model_code, variant_code, variant_name, model_name, model_image_name, manufacturer,manufacturer_code,cost_of_variant """
		where_clause = "model_name LIKE '{0}' or EXACT_FEATURE LIKE '%{0}%' or manufacturer LIKE '{0}%' ".format(search_string)
		column_tuple = ['model_code', 'variant_code', 'variant_name', 'model_name', 'model_image_name', 'manufacturer','manufacturer_code','cost_of_variant']
		subset_df= self.executeQuery(select_clause,where_clause,column_tuple)
		# print("subset_df",subset_df)
		return subset_df

		#search_string = "seat"
		# SCORE_THRESHOLD = 60
		# MAX_NO_VARIANTS=5
		# MAX_NO_EXACT_FT_PER_VARINT=3
		# smautoData = self.smautoData
		# column_list = ['manufacturer','model_name','variant_name','model_image_name','variant_code', 'Exact_Feature', 'data_value','model_code','cost_of_variant']
		# final_result=self.es_search(search_string)
		# print("json",final_result)
		# print(len(final_result))
		# if len(final_result) == 0:
			# return empty data frame with column names
			# small_df = pd.DataFrame(data=None, columns=column_list)
			# return small_df
		# else:
			#return search results
			# final_result=final_result[column_list]
			#print("final_result",final_result)
		# variant_cd_lst = final_result
	
		# variant_cd_lst = final_result.drop_duplicates(subset="model_code")
		# print("json", variant_cd_lst.to_dict())
		# print(len(variant_cd_lst))
		# print(variant_cd_lst)
		# return variant_cd_lst
	#done
	@timer()
	def getCarListforEMI(self):

		select_clause = """ distinct manufacturer_code,variant_name, variant_code, model_name, model_code, manufacturer, cost_of_variant,replace(manufacturer,'_',' ') manufacturer_disp, manufacturer_real_code, variant_real_code,model_real_code"""
		column_tuple = ['manufacturer_code','variant_name', 'variant_code', 'model_name', 'model_code', 'manufacturer', 'cost_of_variant','manufacturer_disp', 'manufacturer_real_code', 'variant_real_code','model_real_code']
		master_data_df= self.executeQuery(select_clause,column_tuple=column_tuple)

		
		manufac_uniq_lst= list(master_data_df[['manufacturer','manufacturer_disp']].drop_duplicates().to_records())
		
		model_manuf_uniq_lst= list(master_data_df[['manufacturer','model_code','model_name','manufacturer_code']].drop_duplicates().to_records())
		var_model_uniq_lst=list(master_data_df[['model_code','variant_code','variant_name','cost_of_variant']].drop_duplicates().to_records())
		manufacturer_code_lst = list(master_data_df[['manufacturer_code']].drop_duplicates().to_records())

		model_manuf_real_uniq_lst= list(master_data_df[['manufacturer','model_real_code','model_name','manufacturer_real_code']].drop_duplicates().to_records())
		var_model_real_uniq_lst=list(master_data_df[['model_real_code','variant_real_code','variant_name','cost_of_variant']].drop_duplicates().to_records())
		manufacturer_code_real_lst = list(master_data_df[['manufacturer_real_code']].drop_duplicates().to_records())
		

		manu_mod_var_lst=[manufac_uniq_lst,model_manuf_uniq_lst,var_model_uniq_lst,manufacturer_code_lst,model_manuf_real_uniq_lst,var_model_real_uniq_lst,manufacturer_code_real_lst]
		return (manu_mod_var_lst)
	#done
	@timer()
	def getCarColor(self,variant_code):
		select_clause = """ distinct model_name,variant_name,smauto_reco_broad_fv,smauto_comp_exact_fv,manufacturer,manufacturer_code,model_real_code,variant_real_code """
		where_clause = "smauto_reco_broad_fv = 'Colours' and variant_code ='{0}' ".format(variant_code)
		column_tuple = ['model_name', 'variant_name','smauto_reco_broad_fv','smauto_comp_exact_fv','manufacturer','manufacturer_code','model_real_code','variant_real_code']
		subset_df= self.executeQuery(select_clause,where_clause,column_tuple)
		return subset_df.reset_index(drop=True).to_dict()
	#done

	@timer()
	def getSimilarCars(self):
		select_clause = "variant_code,nearest_variants"
		where_clause = "1=1"
		column_tuple = ['variant_code','nearest_variants']
		# order_limit_by_clause = " limit 2 "
		table_name= "new_car_car_compare"
		smallDataDf= self.executeQuery(select_clause,where_clause,column_tuple,table_name=table_name)
		# smallDataDf= self.executeQuery(select_clause,where_clause,column_tuple,order_limit_by_clause=order_limit_by_clause,table_name=table_name)
		# print(dict(smallDataDf.values.tolist()))
		return dict(smallDataDf.values.tolist())

	@timer()
	def getCarCompareData(self,lst_variants):
		similar_cars_dict= self.getSimilarCars()
		print("Selected List - Org",set(lst_variants))
		similar_cars=set()
		for org_car in set(lst_variants):
			print("similar_cars_dict[org_car]",similar_cars_dict[org_car])
			similar_cars.add(similar_cars_dict[org_car].split(',')[0])
		print("similar_cars_set",similar_cars)
		lst_variants=lst_variants+ list(similar_cars)
		print("lst_variants",lst_variants)
		lst_variants_quoted = ["\'{0}\'".format(i) for i in lst_variants]
		print("lst_variants_quoted",lst_variants_quoted)
		print("lst_variants_quoted_set",set(lst_variants_quoted))
		#print("lst_variants_quoted",lst_variants_quoted)
		select_clause = """ distinct Broad_feature as "Broad_feature", Exact_Feature as "Exact_Feature", variant_code, data_value, model_code """
		where_clause = "variant_code in  ({0})".format(','.join(lst_variants_quoted))
		print("where_clause",where_clause)
		column_tuple = ['Broad_feature', 'Exact_Feature', 'variant_code', 'data_value','model_code']
		smallDataDf= self.executeQuery(select_clause,where_clause,column_tuple)


		smallDataDf['combined_feature'] = smallDataDf['Broad_feature'].astype(str).str.strip() + ':' + smallDataDf['Exact_Feature'].astype(str).str.strip()
		# smallDataDf.drop_duplicates(subset=['combined_feature','variant_code'],inplace=True)
		# #smallDataDf.to_clipboard()
		# print("smallDataDf.columns",smallDataDf.columns)
		var_cd_mod_cd_dict=dict(zip(smallDataDf.variant_code, smallDataDf.model_code))
		# print("var_cd_mod_cd_dict",var_cd_mod_cd_dict)
		smallDataDf.drop(columns=['Broad_feature','Exact_Feature'],inplace=True)
		# print(smallDataDf.head(10))
		smallDataDf.drop_duplicates(subset=['combined_feature','variant_code'],inplace=True)
		subdf = smallDataDf.pivot(index='combined_feature', columns=['variant_code'], values='data_value')
		# order is important, in data we have to put no for non existent, but we get nan when we pivot
		# so lets replace and then do uniform treatemtnt 
		subdf.replace('No', np.NaN,inplace=True)
		# so first replace No with Nan
		
		rm_null_fields = list(set(subdf.columns) - set(['combined_feature']))
		subdf=subdf.dropna(how='all',subset=rm_null_fields)

		subdf.fillna('No',inplace=True)
		
		# subdf['feature_combined']= smallDataDf.index
		# subdf.reset_index(inplace=True)
		# #subdf.to_clipboard()
		# print(subdf.head(10))
		# print(subdf.columns)
		# subdf.rename(columns = {"variant_code":"Your Variants"},inplace=True)
		subdf.columns.names = ['Variants']
		
		subdf.index.names = ['Feature Description']
		
		cols_ren={}
		for variant in lst_variants:
			
			concat_str= f' <a rel="noopener" target="_blank" href="/car-model/{var_cd_mod_cd_dict[variant]}/{variant}"><button class="btn btn-primary btn-sm">More</button></a>'
			# print("variant", variant)
			if variant in list(similar_cars):
					print("Entered concat block",variant)
					# print("simlr_vriant has " + similar_cars)
					cols_ren[variant] = variant + "*" 
			else :
					cols_ren[variant] = variant
			cols_ren[variant] = cols_ren[variant] + concat_str		
		# print("cols_ren[variant] is " + variant," contains " + cols_ren[variant])
				
		# print(cols_ren)	

		subdf.rename(columns=cols_ren,inplace=True)
		
		return subdf.to_html(table_id="compr_res",classes='table  table-striped table-hover table-responsive  table-bordered',index=True,escape=False)
		#return subdf.to_dict(orient='index')

	@timer()
	def getSeoData(self):
		url_list =['https://ownacar.in',
		'https://ownacar.in/dealer-login',
		'https://ownacar.in/car-insurance-details',
		'https://ownacar.in/aboutus',
		# 'https://ownacar.in/all-cars',
		'https://ownacar.in/car-compare',
		'https://ownacar.in/start-new',
		'https://ownacar.in/dealer-register',
		'https://ownacar.in/car-recommender',
		'https://ownacar.in/terms-conditions',
		'https://ownacar.in/car-emi-calculator',
		'https://ownacar.in/article/how-to-go-digital',
		'https://ownacar.in/article/reasons-to-go-digital',
		'https://ownacar.in/car-advanced-research',
		'https://ownacar.in/car-advanced-research'
		]

		url_df = pd.DataFrame(url_list)
		url_df.columns=['url_list']
		print(url_df)

		# get models from database and add links
		select_clause = """ distinct model_code  """
		where_clause = " 1= 1"
		print("where_claue",where_clause)
		column_tuple = ['model_code']
		smallDataDf= self.executeQuery(select_clause,where_clause,column_tuple)
		smallDataDf.columns=['url_list']

		pre_str = "https://ownacar.in/car-model/"
		smallDataDf['url_list']=pre_str + smallDataDf['url_list']

		url_df=url_df.append(smallDataDf)
		
		# get manufacters from database and add links
		select_clause = """ distinct concat('latest-models-from/',manufacturer_code) as url_list  """
		where_clause = " 1= 1"
		print("where_claue",where_clause)
		column_tuple = ['url_list']
		smallDataDf= self.executeQuery(select_clause,where_clause,column_tuple)
		pre_str = "https://ownacar.in/"
		smallDataDf['url_list']=pre_str + smallDataDf['url_list']

		url_df=url_df.append(smallDataDf)

		# get variant data from database along with model and add that also 
		select_clause = """ distinct concat('car-model/',model_code, '/', variant_code) as url_list  """
		where_clause = " 1= 1"
		print("where_claue",where_clause)
		column_tuple = ['url_list']
		smallDataDf= self.executeQuery(select_clause,where_clause,column_tuple)
		# smallDataDf.columns=['url_list']
		pre_str = "https://ownacar.in/"
		smallDataDf['url_list']=pre_str + smallDataDf['url_list']

		


		url_df=url_df.append(smallDataDf)
		# debugging on dev 
		#url_df["url_list"]= url_df["url_list"].str.replace("https://ownacar.in", "http://192.168.0.119:9000", case = False) 
		print(url_df)







		sitemap_template='''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {% for page in pages %}
    <url>
        <loc>{{page[1]|safe}}</loc>
        <lastmod>{{page[2]}}</lastmod>
        <changefreq>{{page[3]}}</changefreq>
        <priority>{{page[4]}}</priority>        
    </url>
    {% endfor %}
</urlset>'''

		template = Template(sitemap_template)
		# Get Today's Date to add as Lastmod
		lastmod_date = datetime.datetime.now().strftime('%Y-%m-%d')
		# Fill the Sitemap Template and Write File
		url_df.loc[:,'lastmod'] = lastmod_date      # ... add Lastmod date
		url_df.loc[:,'changefreq'] = 'daily'        # ... add changefreq
		url_df.loc[:,'priority'] = '1.0'            # ... add priority 

			# Render each row / column in the sitemap
		sitemap_output = template.render(pages = url_df.itertuples())
		#print(sitemap_output)
		
		return(sitemap_output)


