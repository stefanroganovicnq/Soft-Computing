#https://datascience.stackexchange.com/questions/11704/reshaping-of-data-for-deep-learning-using-keras
import numpy as np
np.random.seed(123)                          
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten	
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

from matplotlib import pyplot as plt

from keras.datasets import mnist
from keras import backend as Ker
Ker.set_image_dim_ordering('th')                  

def kreiraj_Sacuvaj_Cnn():
 
    (X_train, y_train), (X_test, y_test) = mnist.load_data() 

    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    
    X_train /= 255
    X_test /= 255

    Y_train = np_utils.to_categorical(y_train, 10)
    Y_test = np_utils.to_categorical(y_test, 10)


    model = napravi_model()

    model.fit(X_train, Y_train, batch_size=32, nb_epoch=10, verbose=1) 

    score = model.evaluate(X_test, Y_test, verbose=0)          

    print(score)
  
    # serialize and dumps all weights to HDF5
    model.save_weights("model.h5")

    return 1,model

def napravi_model():

    model = Sequential()

    #ulazni sloj zadajemo 
    model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(1,28,28)))
    
    #dodajemo slojeve nasem modelu
    model.add(Convolution2D(32, 3, 3, activation='relu'))

    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(128, activation='relu'))

    #model.add(Dropout(0.5))

    #izlazni sloj
    model.add(Dense(10, activation='softmax'))

    #funkcija gubitka
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    return model