# xDNN
# This project is the implementation of "Explainable Deep Neural Network in Recommender Systems".
# The codes are for the Yelp dataset.
# This repository contains six files:
# yelp_preprocess: This file contains the codes that compute the CTR for each feature. Finally, it separates the data into train, dev, and test datasets, and prepares the inputs data.
# Generator: I prepare this code just for a huge amount of the data. If your dataset is so great and you can not load them into RAM you can use a data generator. Moreover, it provides an input matrix for the neural network.
# Models: The structure of the neural network including the number of hidden layers, activation functions, regularization, and so on are built in this file.
# Functions: This file fills the RAM with different data, clusters members, CTR, ...
# Main: The training process and saving Models is done in this file.
# Test_Main: The evaluation and the AUC and LOGLOSS are processed here.
