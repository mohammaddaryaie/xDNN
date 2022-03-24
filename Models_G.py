from __future__ import print_function
from tensorflow.keras import layers
from tensorflow.keras.layers import *
from tensorflow.keras import Model
import tensorflow.keras as tf
from tensorflow.keras.models import Sequential

def Build_Model():
    model = Sequential()
    model.add(layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(800, activation='relu'))
    model.add(layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(1200, activation='sigmoid'))
    model.add(layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(1200, activation='sigmoid'))
    model.add(layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(1200, activation='relu'))
    model.add(layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(800, activation='relu'))
    model.add(layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(200, activation='relu'))
    model.add(layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def Build_Model_with_last_layer(input_layer):
    input_layer = layers.Input(shape=input_layer,dtype='float32')
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
                                         scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
                                         moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(input_layer)

    model=Dense(200, activation='relu',)(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model=Dense(400, activation='sigmoid')(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model=Dense(200, activation='sigmoid')(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model=Dense(200, activation='relu')(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    last_layer_model = Dense(15, activation='sigmoid')(model)
    model=Dense(1, activation='sigmoid')(last_layer_model)

    model=Model(input_layer,model)
    return model,last_layer_model

def Combine_Models(input_layer_main,input_layer_cluster,main_last_layer,cluster_last_layer):
    input_layer  = tf.layers.Concatenate(axis=1)([main_last_layer,cluster_last_layer])
    model = layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, trainable=True,
                                      scale=True, beta_initializer="zeros", gamma_initializer="ones",
                                      moving_mean_initializer="zeros",
                                      moving_variance_initializer="ones", renorm=False, renorm_momentum=0.99)(input_layer)
    model = Dense(200, activation='relu')(model)
    model = layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, trainable=True,
                                      scale=True, beta_initializer="zeros", gamma_initializer="ones",
                                      moving_mean_initializer="zeros",
                                      moving_variance_initializer="ones", renorm=False, renorm_momentum=0.99)(model)
    model = Dense(400, activation='sigmoid')(model)
    model=layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, trainable=True,
                              scale=True, beta_initializer="zeros", gamma_initializer="ones",
                              moving_mean_initializer="zeros",
                              moving_variance_initializer="ones", renorm=False, renorm_momentum=0.99)(model)
    model = Dense(200, activation='sigmoid')(model)
    model = layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, trainable=True,
                                      scale=True, beta_initializer="zeros", gamma_initializer="ones",
                                      moving_mean_initializer="zeros",
                                      moving_variance_initializer="ones", renorm=False, renorm_momentum=0.99)(model)
    model = Dense(200, activation='relu')(model)
    model = layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, trainable=True,
                                      scale=True, beta_initializer="zeros", gamma_initializer="ones",
                                      moving_mean_initializer="zeros",
                                      moving_variance_initializer="ones", renorm=False, renorm_momentum=0.99)(model)
    model = Dense(15, activation='relu')(model)
    model = Dense(1, activation='sigmoid')(model)
    model1 = Model([input_layer_main,input_layer_cluster], model)

    return model1

def Build_Main_Model(input_layer):
    input_layer = layers.Input(shape=input_layer,dtype='float32')
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
                                         scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
                                         moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(input_layer)

    model=Dense(200, activation='relu',)(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model=Dense(400, activation='sigmoid')(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model=Dense(200, activation='sigmoid')(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model=Dense(200, activation='relu')(model)
    model=layers.BatchNormalization( axis=-1,momentum=0.99, epsilon=0.001, center=True,trainable=True,
        scale=True, beta_initializer="zeros", gamma_initializer="ones", moving_mean_initializer="zeros",
        moving_variance_initializer="ones",renorm=False,renorm_momentum=0.99)(model)
    model = Dense(15, activation='sigmoid')(model)
    model=Dense(1, activation='sigmoid')(model)

    model=Model(input_layer,model)
    return model
