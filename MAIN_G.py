from __future__ import print_function
import datetime
from sklearn.preprocessing import LabelBinarizer
import tensorflow.keras.models as keras_models
from random import randrange
import yelp.Functions_G as Functions_G
import yelp.Generator_G as Generator_G
import yelp.Models as Models_G
from tensorflow.keras import layers

# The directories of train, test, validation, and the log files
Home_Address='/media/fs_Linux_Files'
# initialize the paths to our training and testing CSV files
Main_Model_Weights = Home_Address+'/Model/'
TRAIN_CSV = Home_Address+'/track2/yelp/train.txt'
validation_CSV = Home_Address+'/track2/yelp/validation.txt'
TEST_CSV = Home_Address+'/track2/train/yelp/test.txt'
SAVE_MODEL = '/home/Project/yelp/Model/'
Log_file = '/home/Project/yelp/Log/'
Counter_file = '/home/Project/yelp/Log/'
Model_file = '/home/Project/yelp/Model/'

# initialize the number of epochs to train for and batch size
NUM_EPOCHS = 100
BS = 500
# labels in the dataset along with the testing labels
labels = set()
labels = {'0', '1'}

lb = LabelBinarizer()
lb.fit(list(labels))
print('Start Reading From Training Dataset')
Functions_G.Fill_cluster_ctr()
# Build Models
Shadow_Model_RI ,main_last_layer= Models_G.Build_Model_with_last_layer(119)
Shadow_Model_SI,cluster_last_layer= Models_G.Build_Model_with_last_layer(119)
Shadow_Model_RI .compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
Shadow_Model_SI.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
Shadow_Model_RI .trainable = False
Shadow_Model_SI.trainable = False
combined_model = Models_G.Combine_Models(Shadow_Model_RI .input, Shadow_Model_SI.input, main_last_layer, cluster_last_layer)
combined_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Call data generators
trainGen_main = Generator_G.Training_Generator_Main(TRAIN_CSV, BS, lb, mode="train")
validationGen_main = Generator_G.Test_Generator_Main(validation_CSV, BS, lb, mode="train")
trainGen_cluster = Generator_G.Training_Generator_Main_JC(TRAIN_CSV, BS, lb, mode="train")
validationGen_cluster = Generator_G.Test_Generator_Main_JC(validation_CSV, BS, lb, mode="train")

# Start training
f_parameters = open(Log_file + 'params.txt', 'w')
for i in range(0,13818):
    main_x_input = next(trainGen_main)
    main_y_input = next(validationGen_main)
    history = Shadow_Model_RI.fit(x=main_x_input[0], y=main_x_input[1], validation_data=main_y_input, validation_steps=1,epochs=1, steps_per_epoch=1)
    cluster_x_input = next(trainGen_cluster)
    cluster_y_input = next(validationGen_cluster)
    history = Shadow_Model_SI.fit(x=cluster_x_input[0], y=cluster_x_input[1], validation_data=cluster_y_input,validation_steps=1, epochs=1, steps_per_epoch=1)
    history = combined_model.fit(x=[main_x_input[0], cluster_x_input[0]], y=cluster_x_input[1], epochs=1, steps_per_epoch=1)
    f_parameters.write(str(i) + ',' + str(round(history.history['loss'][0], 4)) + ',' + str(round(history.history['accuracy'][0], 4))  + '\n')

f_parameters.close()

# Saving Models
Shadow_Model_RI.save(SAVE_MODEL+'Main/', overwrite=True, include_optimizer=True)
Shadow_Model_SI.save(SAVE_MODEL+'Cluster/', overwrite=True, include_optimizer=True)
combined_model.save(SAVE_MODEL+'Combined/', overwrite=True, include_optimizer=True)



