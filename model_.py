#Gerekli kütüphanelerin içe aktarılması
import pandas as pd
import numpy as np
import os
import tensorflow as tf
import cv2
from tensorflow import keras
from tensorflow.keras.layers import Dense, Input, InputLayer, Flatten
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from  matplotlib import pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.optimizers import RMSprop




# Data Generator
train = ImageDataGenerator(rescale=1/255)
test = ImageDataGenerator(rescale=1/255)



# Eğitim verisetinin okunması
train_dataset = train.flow_from_directory('/home/mehmet/Masaüstü/cnn_deneme/bing/data_2/train',target_size=(150,150), class_mode='binary', batch_size=64)


# Doğrulama verisetinin okunması
validation_dataset = test.flow_from_directory('/home/mehmet/Masaüstü/cnn_deneme/bing/data_2/test',target_size=(150,150), class_mode='binary', batch_size=64)


# Sınıflar
print(train_dataset.classes)


# MODEL
model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation="relu", input_shape=(150,150,3)),
                                        tf.keras.layers.MaxPooling2D(2,2),
                                        tf.keras.layers.Conv2D(32,(3,3), activation="relu"),
                                        tf.keras.layers.MaxPooling2D(2,2),
                                        tf.keras.layers.Conv2D(64,(3,3), activation="relu"),
                                        tf.keras.layers.MaxPooling2D(2,2),
                                        tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(64, activation="relu"),
                                        tf.keras.layers.Dense(1, activation="sigmoid")])








model.compile(loss="binary_crossentropy",optimizer=RMSprop(lr=0.001),metrics=['accuracy'])



history = model.fit_generator(train_dataset,epochs=20,validation_data = validation_dataset)

# Doğruluk tablosu
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


# Kayıp değer tablosu
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
