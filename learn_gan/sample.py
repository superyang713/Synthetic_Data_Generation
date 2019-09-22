import os
from tensorflow import keras
from tensorflow.keras.preprocessing import image


latent_dim = 32
height = 32
width = 32
channels = 3

(x_train, y_train), (_, _) = keras.datasets.cifar10.load_data()
x_train = x_train[y_train.flatten() == 6]

x_train = x_train.reshape(
    (x_train.shape[0],) +
    (height, width, channels)).astype("float32") / 255.
