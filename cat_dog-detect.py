import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten
import matplotlib.pyplot as plt
import random

X_train = np.loadtxt(r'F:\machine learning\cats and dog\csv\input.csv',delimiter=',')
Y_train = np.loadtxt(r'F:\machine learning\cats and dog\csv\labels.csv',delimiter=',')

X_test = np.loadtxt(r'F:\machine learning\cats and dog\csv\input_test.csv',delimiter=',')
Y_test = np.loadtxt(r'F:\machine learning\cats and dog\csv\labels_test.csv',delimiter=',')

X_train=X_train.reshape(len(X_train), 100,100,3)
Y_train=Y_train.reshape(len(Y_train),1)

X_test=X_test.reshape(len(X_test), 100,100,3)
Y_test=Y_test.reshape(len(Y_test),1)

X_train =X_train /255
X_test=X_test/255

#idx=random.randint(0, len(X_train))
#plt.imshow(X_train[idx,:])

model=Sequential([
    
    Conv2D(32, (3,3),activation='relu',input_shape=(100,100,3)),
    MaxPooling2D((2,2)),
    
    Conv2D(32, (3,3),activation='relu'),
    MaxPooling2D((2,2)),
    
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
    
    ])
        
#model.compile(loss='binary_crossentropy' , optimizer='adam', metrics=['accuracy'])
#model.fit(X_train,Y_train, epochs=10, batch_size=64)
#model.evaluate(X_test,Y_test)
   
           
idx=random.randint(0, len(Y_test))
plt.imshow(X_test[idx,:])           
plt.show()

y_pred=model.predict(X_test[idx,:].reshape(1,100,100,3))
y_pred=y_pred>0.5
if (y_pred==0):
    pred='dog'
else:
    pred='cat'

print('model says:',pred)
           
           
           
           
           
           
           
           
           
           

