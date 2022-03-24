from __future__ import print_function
import matplotlib
from numpy.core.defchararray import strip

from Advertising import plot
matplotlib.use('Agg')
matplotlib.use('TkAgg')
from sklearn.preprocessing import LabelBinarizer
import tensorflow.keras.models as keras_models
import yelp.Functions_RNN as Functions_RNN
import yelp.Generator_ads as Generator_ads
from sklearn.metrics import roc_auc_score
import pandas as pd
from keras import backend as K
from sklearn.metrics import log_loss

# Fill list and sictionary by each value and its clusters
Functions_RNN.Fill_cluster_ctr()

#Directories
Home_Address='/media/fs_Linux_Files/'
TEST_CSV = Home_Address+'track2/yelp/test.txt'
Model_file = Home_Address+'Log/yelp/action_21/Model/Combined'

#Start reading test dataset
f_test = open(TEST_CSV, "r")
y_test = []
count_line=863446
lines=[]
counter=0
for line in f_test:
    lines.append(line)
    line = line.strip().split(',')
    y_test.append('1' if float(line[1]) ==5 else '0')
    counter+=1
    if counter == 860000:
        break
f_test.close()
labels = set()
labels = {'0', '1'}
model = keras_models.load_model(Model_file)
lb = LabelBinarizer()
lb.fit(list(labels))
# Call data generator
main_testGen = Generator_ads.Training_Generator_main_for_test(TEST_CSV, 5000, lb, mode="train")#5000
cluster_testGen = Generator_ads.Training_Generator_main_for_test_JC(TEST_CSV, 5000, lb, mode="train")#5000

# Outputs for explanation
F_x=[]
CF_x=[]
CF_x_main=[]
G_x=[]
CG_x=[]
CG_x_main=[]
all_y_pred_keras=[]
# Load trained models
Model_file_Cluster = Home_Address+'Log/yelp/action_21/Model/Cluster'
Model_file_Main = Home_Address+'Log/yelp/action_21/Model/Main'
Model_file_Combined = Home_Address+'Log/yelp/action_21/Model/Combined'
model_Cluster = keras_models.load_model(Model_file_Cluster)
model_Main = keras_models.load_model(Model_file_Main)
model_Combined = keras_models.load_model(Model_file_Combined)

get_activations_15_main = K.function([model_Combined.layers[0].input,model_Combined.layers[1].input], model_Combined.layers[20].output)
get_activations_15_cluster = K.function([model_Combined.layers[0].input,model_Combined.layers[1].input], model_Combined.layers[21].output)
get_activations_target_main = K.function(model_Main.layers[0].input, model_Main.layers[11].output)
get_activations_target_cluster = K.function(model_Cluster.layers[0].input, model_Cluster.layers[11].output)

for i in range(0,172):
    main_input = next(main_testGen)
    cluster_input = next(cluster_testGen)
    activations_main_15_main = get_activations_15_main([main_input[0], cluster_input[0]])
    activations_cluster_15_main = get_activations_15_cluster([main_input[0], cluster_input[0]])
    activations_target_main = get_activations_target_main(main_input[0])
    activations_target_cluster = get_activations_target_cluster(cluster_input[0])

    y_pred_keras = model.predict([main_input[0],cluster_input[0]])
    all_y_pred_keras = all_y_pred_keras +  y_pred_keras.tolist()
    print(str(i))
    for cou in range(0, 5000):
        F_x.append(round(float(activations_target_main[cou]),6))
        G_x.append(round(float(activations_target_cluster[cou]),6))
        main_15=','.join(str(round(f, 6)) for f in activations_main_15_main[cou].tolist())
        cluster_15=','.join(str(round(f, 6)) for f in activations_cluster_15_main[cou].tolist())
        CF_x.append(Functions_RNN.cluster_list_main[Functions_RNN.kmeans_list_main.predict([activations_main_15_main[cou].tolist()])[0]].split(',')[1])
        CF_x_main.append(Functions_RNN.cluster_list_main[Functions_RNN.kmeans_list_main.predict([activations_main_15_main[cou].tolist()])[0]].split(',')[0])
        CG_x.append(Functions_RNN.cluster_list_cluster[Functions_RNN.kmeans_list_cluster.predict([activations_cluster_15_main[cou].tolist()])[0]].split(',')[1])
        CG_x_main.append(Functions_RNN.cluster_list_cluster[Functions_RNN.kmeans_list_cluster.predict([activations_cluster_15_main[cou].tolist()])[0]].split(',')[0])

#Evaluation
y_hat=[float(item) for item in all_y_pred_keras]
check=y_hat.copy()
val=roc_auc_score(y_test, check)
print(log_loss(y_test, check,normalize=True,labels=['0','1']))
print(str(val))

