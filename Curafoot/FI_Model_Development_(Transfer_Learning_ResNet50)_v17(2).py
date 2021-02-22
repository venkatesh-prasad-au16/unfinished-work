from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import copy
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tqdm import tqdm_notebook as tqdm
from sklearn.preprocessing import LabelEncoder
import PIL
from PIL import Image
import random
from scipy import ndarray

# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io
from skimage.util import img_as_ubyte, img_as_float
from skimage.transform import warp, AffineTransform, ProjectiveTransform
from skimage.exposure import equalize_adapthist, equalize_hist, rescale_intensity, adjust_gamma, adjust_log, adjust_sigmoid
from skimage.filters import gaussian
from skimage.util import random_noise

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.preprocessing.image import ImageDataGenerator
import h5py

device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  print(
      '\n\nThis error most likely means that this notebook is not '
      'configured to use a GPU.  Change this in Notebook Settings via the '
      'command palette (cmd/ctrl-shift-P) or the Edit menu.\n\n')
  raise SystemError('GPU device not found')

# Load the Drive helper and mount
# from google.colab import drive
# drive.mount('/content/drive/')
# drive.mount('/content/drive/', force_remount=True) #DC updated
FI_train_dir = "/home/venkatesh/Desktop/Curafoot/Foots/TRAIN"
FI_val_dir = "/home/venkatesh/Desktop/Curafoot/Foots/VAL"

print(os.listdir(FI_train_dir ))

"""
image=[]
labels=[]
for f in os.listdir(FI_train_dir):
  if f=='MILD':
    for c in os.listdir(os.path.join(FI_train_dir, f)):
      image.append(os.path.join(FI_train_dir, f,c))
      labels.append('MILD')
  if f=='SEVERE':
    for c in os.listdir(os.path.join(FI_train_dir, f)):
      image.append(os.path.join(FI_train_dir, f,c))
      labels.append('SEVERE')
  if f=='MODERATE':
    for c in os.listdir(os.path.join(FI_train_dir, f)):
      image.append(os.path.join(FI_train_dir, f,c))
      labels.append('MODERATE')
  if f=='HIGH ARCH':
      for c in os.listdir(os.path.join(FI_train_dir, f)):
        image.append(os.path.join(FI_train_dir, f,c))
        labels.append('HIGH ARCH')
  if f=='NORMAL ARCH':
      for c in os.listdir(os.path.join(FI_train_dir, f)):
        image.append(os.path.join(FI_train_dir, f,c))
        labels.append('NORMAL ARCH')
imagedata = {'Images':image, 'labels':labels} 
image_data = pd.DataFrame(imagedata) 
"""

batch_size = 16
image_size = (224, 224)

# this is the augmentation configuration we will use for training
datagen = ImageDataGenerator(
        rescale=1./255)

# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data
train_generator = datagen.flow_from_directory(
        FI_train_dir,  # this is the target directory
        target_size=image_size, 
        batch_size=batch_size,
        class_mode='categorical')  
# this is a similar generator, for validation data
validation_generator = datagen.flow_from_directory(
        FI_val_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical')
classnames = list(train_generator.class_indices.keys())
print("class names: ", classnames)

from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout ,GlobalAveragePooling2D
#from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.layers import BatchNormalization
from tensorflow.keras import applications
from tensorflow.keras import Model


base_model = keras.applications.resnet.ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
print(base_model.summary())

# Freeze the already-trained layers in the base model
for layer in base_model.layers:
  layer.trainable = False

#for layer in base_model.layers[:-5]:
#  layer.trainable=False

# Create prediction layer for classification of our images
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.7)(x)
x = Flatten()(x)
x = Dense(1024, activation='relu')(x)
prediction_layer = Dense(5, activation='softmax')(x) 
model = Model(inputs=base_model.input, outputs=prediction_layer)

EPOCHS = 150
INIT_LR = 1e-4
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)

# Compile the model
model.compile(loss='categorical_crossentropy',optimizer=opt,
              metrics=['accuracy'])

# Now print the full model, which will include the layers of the base model plus the dense layer we added
print(model.summary())

history = model.fit(
    train_generator,
    steps_per_epoch = train_generator.samples // batch_size,
    validation_data = validation_generator, 
    validation_steps = validation_generator.samples // batch_size,
    epochs = EPOCHS)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(len(history.history['val_loss']))

plt.figure(figsize=(15, 15))
plt.subplot(2, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

from keras.models import model_from_json

# serialize model to JSON
model_json = model.to_json()

with open("/home/venkatesh/Desktop/Curafoot/modelv4.json", "w") as json_file:
  json_file.write(model_json)
model.save_weights("model_v4.h5")
print("Saved model to disk")
   

#saved_model=FI_train_dir + '/saved_model2'
#model.save(saved_model,save_format='tf')

#from google.colab import drive
#drive.mount('/content/drive')


#from google.colab import files
#files.download("saved_model4.zip")  

#zip -r /content/saved_model4.zip /content/saved_model4
