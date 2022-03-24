from __future__ import print_function
import sys
from builtins import input
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from random import randrange
from reportlab.graphics import samples
from tensorflow.keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import math
from sklearn.cluster import KMeans
import pickle

Home_Address='/media/fs_Linux_Files/'

#review feature
cluster_review_useful = []
cluster_review_funny = []
cluster_review_cool =[]
#user feature
cluster_user_review_count =[]
cluster_user_useful =[]
cluster_user_funny =[]
cluster_user_cool =[]
cluster_friends =[]
cluster_fans =[]
cluster_user_stars =[]
cluster_compliment_hot =[]
cluster_compliment_more =[]
cluster_compliment_profile =[]
cluster_compliment_cute =[]
cluster_compliment_list =[]
cluster_compliment_note =[]
cluster_compliment_plain =[]
cluster_compliment_cool =[]
cluster_compliment_funny =[]
cluster_compliment_writer =[]
cluster_compliment_photos =[]
#business
cluster_latitude = []
cluster_longitude = []
cluster_business_review_count = []

#Interpretability
cluster_list_main = []
cluster_list_cluster = []

#review feature
cluster_member_review_useful = {}
cluster_member_review_funny = {}
cluster_member_review_cool ={}
#user feature
cluster_member_user_review_count ={}
cluster_member_user_useful ={}
cluster_member_user_funny ={}
cluster_member_user_cool ={}
cluster_member_friends ={}
cluster_member_fans ={}
cluster_member_user_stars ={}
cluster_member_compliment_hot ={}
cluster_member_compliment_more ={}
cluster_member_compliment_profile ={}
cluster_member_compliment_cute ={}
cluster_member_compliment_list ={}
cluster_member_compliment_note ={}
cluster_member_compliment_plain ={}
cluster_member_compliment_cool ={}
cluster_member_compliment_funny ={}
cluster_member_compliment_writer ={}
cluster_member_compliment_photos ={}
#business
cluster_member_latitude = {}
cluster_member_longitude = {}
cluster_member_business_review_count = {}
#Interpretability
cluster_member_list_main={}
cluster_member_list_cluster={}

kmeans_review_useful=pickle.load(open(Home_Address + 'track2/yelp/kmeans_review_useful.pkl', 'rb'))
kmeans_review_funny=pickle.load( open(Home_Address + 'track2/yelp/kmeans_review_funny.pkl', 'rb'))
kmeans_review_cool=pickle.load( open(Home_Address + 'track2/yelp/kmeans_review_cool.pkl', 'rb'))
kmeans_user_review_count=pickle.load( open(Home_Address + "track2/yelp/kmeans_user_review_count.pkl", "rb"))
kmeans_user_useful=pickle.load( open(Home_Address + "track2/yelp/kmeans_user_useful.pkl", "rb"))
kmeans_user_funny=pickle.load( open(Home_Address + "track2/yelp/kmeans_user_funny.pkl", "rb"))
kmeans_user_cool=pickle.load( open(Home_Address + "track2/yelp/kmeans_user_cool.pkl", "rb"))
kmeans_friends=pickle.load( open(Home_Address + "track2/yelp/kmeans_friends.pkl", "rb"))
kmeans_fans=pickle.load( open(Home_Address + "track2/yelp/kmeans_fans.pkl", "rb"))
kmeans_user_stars=pickle.load( open(Home_Address + "track2/yelp/kmeans_user_stars.pkl", "rb"))
kmeans_compliment_hot=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_hot.pkl", "rb"))
kmeans_compliment_more=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_more.pkl", "rb"))
kmeans_compliment_profile=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_profile.pkl", "rb"))
kmeans_compliment_cute=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_cute.pkl", "rb"))
kmeans_compliment_list=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_list.pkl", "rb"))
kmeans_compliment_note=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_note.pkl", "rb"))
kmeans_compliment_plain=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_plain.pkl", "rb"))
kmeans_compliment_cool=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_cool.pkl", "rb"))
kmeans_compliment_funny=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_funny.pkl", "rb"))
kmeans_compliment_writer=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_writer.pkl", "rb"))
kmeans_compliment_photos=pickle.load( open(Home_Address + "track2/yelp/kmeans_compliment_photos.pkl", "rb"))
kmeans_latitude=pickle.load( open(Home_Address + "track2/yelp/kmeans_latitude.pkl", "rb"))
kmeans_longitude=pickle.load( open(Home_Address + "track2/yelp/kmeans_longitude.pkl", "rb"))
kmeans_business_review_count=pickle.load( open(Home_Address + "track2/yelp/kmeans_business_review_count.pkl", "rb"))
kmeans_list_main=pickle.load( open(Home_Address + "track2/yelp/kmeans_list_main.pkl", "rb"))
kmeans_list_cluster=pickle.load( open(Home_Address + "track2/yelp/kmeans_list_cluster.pkl", "rb"))

def Fill_cluster_ctr():
	for i in range(0,50):
		cluster_review_useful.append(0)
		cluster_fans.append(0)
		cluster_user_stars.append(0)
		cluster_compliment_more.append(0)
		cluster_compliment_profile.append(0)
		cluster_compliment_cute.append(0)
		cluster_compliment_list.append(0)
		cluster_latitude.append(0)
		cluster_longitude.append(0)
	for i in range(0,50):
		cluster_review_funny.append(0)
		cluster_review_cool.append(0)
	for i in range(0, 100):
		cluster_compliment_writer.append(0)
		cluster_compliment_photos.append(0)
		cluster_business_review_count.append(0)
		cluster_compliment_hot.append(0)
		cluster_compliment_note.append(0)
	for i in range(0, 200):
		cluster_user_review_count.append(0)
	for i in range(0, 500):
		cluster_user_useful.append(0)
	for i in range(0, 300):
		cluster_user_funny.append(0)
	for i in range(0, 400):
		cluster_user_cool.append(0)
	for i in range(0, 250):
		cluster_friends.append(0)
	for i in range(0, 150):
		cluster_compliment_plain.append(0)
		cluster_compliment_cool.append(0)
		cluster_compliment_funny.append(0)
	for i in range(0, 5000):
		cluster_list_main.append(0)
		cluster_list_cluster.append(0)

	f_user = open(Home_Address + "track2/yelp/cluster_review_useful_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_review_useful[int(line[0])] = float(line[1])
		except:
			print("cluster_review_useful_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_review_funny_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_review_funny[int(line[0])] = float(line[1])
		except:
			print("cluster_review_funny_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_review_cool_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_review_cool[int(line[0])] = float(line[1])
		except:
			print("cluster_review_cool_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_user_review_count_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_user_review_count[int(line[0])] = float(line[1])
		except:
			print("cluster_user_review_count_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_user_useful_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_user_useful[int(line[0])] = float(line[1])
		except:
			print("cluster_user_useful_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_user_funny_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_user_funny[int(line[0])] = float(line[1])
		except:
			print("cluster_user_funny_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_user_cool_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_user_cool[int(line[0])] = float(line[1])
		except:
			print("cluster_user_cool_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_friends_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_friends[int(line[0])] = float(line[1])
		except:
			print("cluster_friends_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_fans_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_fans[int(line[0])] = float(line[1])
		except:
			print("cluster_fans_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_user_stars_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_user_stars[int(line[0])] = float(line[1])
		except:
			print("cluster_user_stars_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_hot_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_hot[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_hot_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_more_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_more[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_more_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_profile_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_profile[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_profile_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_cute_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_cute[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_cute_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_list_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_list[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_list_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_note_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_note[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_note_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_plain_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_plain[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_plain_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_cool_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_cool[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_cool_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_funny_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_funny[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_funny_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_writer_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_writer[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_writer_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_compliment_photos_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_compliment_photos[int(line[0])] = float(line[1])
		except:
			print("cluster_compliment_photos_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_latitude_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_latitude[int(line[0])] = float(line[1])
		except:
			print("cluster_latitude_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_longitude_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_longitude[int(line[0])] = float(line[1])
		except:
			print("cluster_longitude_rate error:  " + line_err)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_business_review_count_rate.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_business_review_count[int(line[0])] = float(line[1])
		except:
			print("cluster_business_review_count_rate error:  " + line_err)
	f_user.close()

	f_user = open(Home_Address + "track2/yelp/cluster_list_main.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_list_main[int(line[0])] = line[1]+','+line[2]
		except:
			print("cluster_list_main error:  " + line_err)
	f_user.close()

	f_user = open(Home_Address + "track2/yelp/cluster_list_cluster.txt", "r")
	for line in f_user:
		line_err = line
		line = line.strip().split(",")
		try:
			cluster_list_cluster[int(line[0])] = line[1] + ',' + line[2]
		except:
			print("cluster_list_main error:  " + line_err)
	f_user.close()

	f_user = open(Home_Address + "track2/yelp/cluster_member_review_useful_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_review_useful[float(line[0])] = int(line[1])
		except:
			print("cluster_member_review_useful_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_review_funny_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_review_funny[float(line[0])] = int(line[1])
		except:
			print("cluster_member_review_funny_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_review_cool_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_review_cool[float(line[0])] = int(line[1])
		except:
			print("cluster_member_review_cool_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_user_review_count_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_user_review_count[float(line[0])] = int(line[1])
		except:
			print("cluster_member_user_review_count_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_user_useful_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_user_useful[float(line[0])] = int(line[1])
		except:
			print("cluster_member_user_useful_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_user_funny_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_user_funny[float(line[0])] = int(line[1])
		except:
			print("cluster_member_user_funny_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_user_cool_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_user_cool[float(line[0])] = int(line[1])
		except:
			print("cluster_member_user_cool_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_friends_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_friends[float(line[0])] = int(line[1])
		except:
			print("cluster_member_friends_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_fans_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_fans[float(line[0])] = int(line[1])
		except:
			print("cluster_member_fans_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_user_stars_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_user_stars[float(line[0])] = int(line[1])
		except:
			print("cluster_member_user_stars_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_hot_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_hot[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_hot_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_more_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_more[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_more_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_profile_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_profile[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_profile_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_cute_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_cute[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_cute_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_list_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_list[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_list_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_note_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_note[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_note_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_plain_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_plain[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_plain_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_cool_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_cool[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_cool_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_funny_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_funny[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_funny_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_writer_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_writer[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_writer_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_compliment_photos_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_compliment_photos[float(line[0])] = int(line[1])
		except:
			print("cluster_member_compliment_photos_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_latitude_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_latitude[float(line[0])] = int(line[1])
		except:
			print("cluster_member_latitude_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_longitude_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_longitude[float(line[0])] = int(line[1])
		except:
			print("cluster_member_longitude_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_business_review_count_2.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_business_review_count[float(line[0])] = int(line[1])
		except:
			print("cluster_member_business_review_count_rate error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_list_main.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_list_main[','.join(str(f) for f in line[0:16])] = float(line[16])
		except:
			print("cluster_member_list_main error:  " + line)
	f_user.close()
	f_user = open(Home_Address + "track2/yelp/cluster_member_list_cluster.txt", "r")
	for line in f_user:
		line = line.strip().split(",")
		try:
			cluster_member_list_cluster[','.join(str(f) for f in line[0:16])] = float(line[16])
		except:
			print("cluster_member_list_main error:  " + line)
	f_user.close()

#Real Inputs
def main_func(line):
	line_error = line
	x=[]
	line = line.strip().split(",")

	'''
	review_id[0],stars[1],review_useful[2],review_funny[3],review_cool[4],user_id[5],review_count[6],review_useful[7],
	review_funny[8],review_cool[9],elite[10],friends[11],fans[12],stars[13],compliment_hot[14],compliment_more[15],
	compliment_profile[16],compliment_cute[17],compliment_list[18],compliment_note[19],compliment_plain[20],compliment_cool[21],
	compliment_funny[22],compliment_writer[23],compliment_photos[24],business_id[25],latitude[26],longitude[27],stars[28],
	review_count[29],is_open[30],attributes[31],categories[32],hours[33],NoiseLevel[34],DogsAllowed[35],WheelchairAccessible[36],
	AgesAllowed[37],RestaurantsTableService[38],CoatCheck[39],GoodForKids[40],OpenHours[41],RestaurantsDelivery[42],
	RestaurantsReservations[43],OutdoorSeating[44],BYOB[45],RestaurantsGoodForGroups[46],HappyHour[47],WiFi[48],BYOBCorkage[49],
	Caters[50],ByAppointmentOnly[51],RestaurantsTakeOut[52],RestaurantsCounterService[53],RestaurantsAttire[54],Alcohol[55],
	Corkage[56],AcceptsInsurance[57],Smoking[58],RestaurantsPriceRange2[59],BikeParking[60],BusinessAcceptsCreditCards[61],
	GoodForDancing[62],BusinessAcceptsBitcoin[63],DriveThru[64],HasTV[65],BusinessParking[66],GoodForMeal[67],BestNights[68],
	HairSpecializesIn[69],Music[70],DietaryRestrictions[71],Ambience[72],GoodForMeal_dessert[73],GoodForMeal_latenight[74],
	GoodForMeal_lunch[75],GoodForMeal_dinner[76],GoodForMeal_brunch[77],GoodForMeal_breakfast[78],BestNights_monday[79],
	BestNights_tuesday[80],BestNights_friday[81],BestNights_wednesday[82],BestNights_thursday[83],BestNights_sunday[84],
	BestNights_saturday[85],BusinessParking_garage[86],BusinessParking_street[87],BusinessParking_validated[88],
	BusinessParking_lot[89],BusinessParking_valet[90],HairSpecializesIn_straightperms[91],HairSpecializesIn_coloring[92],
	HairSpecializesIn_extensions[93],HairSpecializesIn_africanamerican[94],HairSpecializesIn_curly[95],HairSpecializesIn_kids[96],
	HairSpecializesIn_perms[97],HairSpecializesIn_asian[98],Music_dj[99],Music_background_music[100],Music_no_music[101],
	Music_jukebox[102],Music_live[103],Music_video[104],Music_karaoke[105],DietaryRestrictions_dairy_free[106],
	DietaryRestrictions_gluten_free[107],DietaryRestrictions_vegan[108],DietaryRestrictions_kosher[109],
	DietaryRestrictions_halal[110],DietaryRestrictions_soy_free[111],DietaryRestrictions_vegetarian[112],Ambience_touristy[113],
	Ambience_hipster[114],Ambience_romantic[115],Ambience_divey[116],Ambience_intimate[117],Ambience_trendy[118],Ambience_upscale[119],
	Ambience_classy[120],Ambience_casual[121],business_id[122],date_count[123]
	'''
	col_num =119
	#input_dl_matrix = np.zeros((1, col_num)).tolist()
	External_list = range(0,col_num)
	for n in External_list:
		x.append(0)
	try:
		x[0] = float(line[2])
		x[1] = float(line[3])
		x[2] = float(line[4])
		x[3] = float(line[6])
		x[4] = float(line[7])
		x[5] = float(line[8])
		x[6] = float(line[9])
		x[7] = float(line[10])
		x[8] = float(line[11])
		x[9] = float(line[12])
		x[10] = float(line[13])
		x[11] = float(line[14])
		x[12] = float(line[15])
		x[13] = float(line[16])
		x[14] = float(line[17])
		x[15] = float(line[18])
		x[16] = float(line[19])
		x[17] = float(line[20])
		x[18] = float(line[21])
		x[19] = float(line[22])
		x[20] = float(line[23])
		x[21] = float(line[24])
		x[22] = float(line[26])
		x[23] = float(line[27])
		x[24] = float(line[28])
		x[25] = float(line[29])
		x[26] = float(line[30])
		x[27] = float(line[31])
		x[28] = float(line[32])
		x[29] = float(line[33])
		x[30] = float(line[34])
		x[31] = float(line[35])
		x[32] = float(line[36])
		x[33] = float(line[37])
		x[34] = float(line[38])
		x[35] = float(line[39])
		x[36] = float(line[40])
		x[37] = float(line[41])
		x[38] = float(line[42])
		x[39] = float(line[43])
		x[40] = float(line[44])
		x[41] = float(line[45])
		x[42] = float(line[46])
		x[43] = float(line[47])
		x[44] = float(line[48])
		x[45] = float(line[49])
		x[46] = float(line[50])
		x[47] = float(line[51])
		x[48] = float(line[52])
		x[49] = float(line[53])
		x[50] = float(line[54])
		x[51] = float(line[55])
		x[52] = float(line[56])
		x[53] = float(line[57])
		x[54] = float(line[58])
		x[55] = float(line[59])
		x[56] = float(line[60])
		x[57] = float(line[61])
		x[58] = float(line[62])
		x[59] = float(line[63])
		x[60] = float(line[64])
		x[61] = float(line[65])
		x[62] = float(line[66])
		x[63] = float(line[67])
		x[64] = float(line[68])
		x[65] = float(line[69])
		x[66] = float(line[70])
		x[67] = float(line[71])
		x[68] = float(line[72])
		x[69] = float(line[73])
		x[70] = float(line[74])
		x[71] = float(line[75])
		x[72] = float(line[76])
		x[73] = float(line[77])
		x[74] = float(line[78])
		x[75] = float(line[79])
		x[76] = float(line[80])
		x[77] = float(line[81])
		x[78] = float(line[82])
		x[79] = float(line[83])
		x[80] = float(line[84])
		x[81] = float(line[85])
		x[82] = float(line[86])
		x[83] = float(line[87])
		x[84] = float(line[88])
		x[85] = float(line[89])
		x[86] = float(line[90])
		x[87] = float(line[91])
		x[88] = float(line[92])
		x[89] = float(line[93])
		x[90] = float(line[94])
		x[91] = float(line[95])
		x[92] = float(line[96])
		x[93] = float(line[97])
		x[94] = float(line[98])
		x[95] = float(line[99])
		x[96] = float(line[100])
		x[97] = float(line[101])
		x[98] = float(line[102])
		x[99] = float(line[103])
		x[100] = float(line[104])
		x[101] = float(line[105])
		x[102] = float(line[106])
		x[103] = float(line[107])
		x[104] = float(line[108])
		x[105] = float(line[109])
		x[106] = float(line[110])
		x[107] = float(line[111])
		x[108] = float(line[112])
		x[109] = float(line[113])
		x[110] = float(line[114])
		x[111] = float(line[115])
		x[112] = float(line[116])
		x[113] = float(line[117])
		x[114] = float(line[118])
		x[115] = float(line[119])
		x[116] = float(line[120])
		x[117] = float(line[121])
		x[118] = float(line[123])
	except Exception as e:
		print('Error: ' + line_error+'\n' + str(e))
	#x.append(input_dl_matrix.tolist())
	return np.array(x, dtype=np.float32)

#Shadow inputs
def main_func_with_cluster(line):
	line_error = line
	x=[]
	line = line.strip().split(",")

	'''
	review_id[0],stars[1],review_useful[2],review_funny[3],review_cool[4],user_id[5],review_count[6],review_useful[7],
	review_funny[8],review_cool[9],elite[10],friends[11],fans[12],stars[13],compliment_hot[14],compliment_more[15],
	compliment_profile[16],compliment_cute[17],compliment_list[18],compliment_note[19],compliment_plain[20],compliment_cool[21],
	compliment_funny[22],compliment_writer[23],compliment_photos[24],business_id[25],latitude[26],longitude[27],stars[28],
	review_count[29],is_open[30],attributes[31],categories[32],hours[33],NoiseLevel[34],DogsAllowed[35],WheelchairAccessible[36],
	AgesAllowed[37],RestaurantsTableService[38],CoatCheck[39],GoodForKids[40],OpenHours[41],RestaurantsDelivery[42],
	RestaurantsReservations[43],OutdoorSeating[44],BYOB[45],RestaurantsGoodForGroups[46],HappyHour[47],WiFi[48],BYOBCorkage[49],
	Caters[50],ByAppointmentOnly[51],RestaurantsTakeOut[52],RestaurantsCounterService[53],RestaurantsAttire[54],Alcohol[55],
	Corkage[56],AcceptsInsurance[57],Smoking[58],RestaurantsPriceRange2[59],BikeParking[60],BusinessAcceptsCreditCards[61],
	GoodForDancing[62],BusinessAcceptsBitcoin[63],DriveThru[64],HasTV[65],BusinessParking[66],GoodForMeal[67],BestNights[68],
	HairSpecializesIn[69],Music[70],DietaryRestrictions[71],Ambience[72],GoodForMeal_dessert[73],GoodForMeal_latenight[74],
	GoodForMeal_lunch[75],GoodForMeal_dinner[76],GoodForMeal_brunch[77],GoodForMeal_breakfast[78],BestNights_monday[79],
	BestNights_tuesday[80],BestNights_friday[81],BestNights_wednesday[82],BestNights_thursday[83],BestNights_sunday[84],
	BestNights_saturday[85],BusinessParking_garage[86],BusinessParking_street[87],BusinessParking_validated[88],
	BusinessParking_lot[89],BusinessParking_valet[90],HairSpecializesIn_straightperms[91],HairSpecializesIn_coloring[92],
	HairSpecializesIn_extensions[93],HairSpecializesIn_africanamerican[94],HairSpecializesIn_curly[95],HairSpecializesIn_kids[96],
	HairSpecializesIn_perms[97],HairSpecializesIn_asian[98],Music_dj[99],Music_background_music[100],Music_no_music[101],
	Music_jukebox[102],Music_live[103],Music_video[104],Music_karaoke[105],DietaryRestrictions_dairy_free[106],
	DietaryRestrictions_gluten_free[107],DietaryRestrictions_vegan[108],DietaryRestrictions_kosher[109],
	DietaryRestrictions_halal[110],DietaryRestrictions_soy_free[111],DietaryRestrictions_vegetarian[112],Ambience_touristy[113],
	Ambience_hipster[114],Ambience_romantic[115],Ambience_divey[116],Ambience_intimate[117],Ambience_trendy[118],Ambience_upscale[119],
	Ambience_classy[120],Ambience_casual[121],business_id[122],date_count[123]
	'''
	col_num =119
	#input_dl_matrix = np.zeros((1, col_num)).tolist()
	External_list = range(0,col_num)
	for n in External_list:
		x.append(0)
	try:
		x[0] = cluster_review_useful[cluster_member_review_useful[float(line[2])]]
		x[1] = cluster_review_funny[cluster_member_review_funny[float(line[3])]]
		x[2] = cluster_review_cool[cluster_member_review_cool[float(line[4])]]
		x[3] = cluster_user_review_count[cluster_member_user_review_count[float(line[6])]]
		x[4] = cluster_user_useful[cluster_member_user_useful[float(line[7])]]
		x[5] = cluster_user_funny[cluster_member_user_funny[float(line[8])]]
		x[6] = cluster_user_cool[cluster_member_user_cool[float(line[9])]]
		x[7] = float(line[10])
		x[8] = cluster_friends[cluster_member_friends[float(line[11])]]
		x[9] = cluster_fans[cluster_member_fans[float(line[12])]]
		x[10] = cluster_user_stars[cluster_member_user_stars[float(line[13])]]
		x[11] = cluster_compliment_hot[cluster_member_compliment_hot[float(line[14])]]
		x[12] = cluster_compliment_more[cluster_member_compliment_more[float(line[15])]]
		x[13] = cluster_compliment_profile[cluster_member_compliment_profile[float(line[16])]]
		x[14] = cluster_compliment_cute[cluster_member_compliment_cute[float(line[17])]]
		x[15] = cluster_compliment_list[cluster_member_compliment_list[float(line[18])]]
		x[16] = cluster_compliment_note[cluster_member_compliment_note[float(line[19])]]
		x[17] = cluster_compliment_plain[cluster_member_compliment_plain[float(line[20])]]
		x[18] = cluster_compliment_cool[cluster_member_compliment_cool[float(line[21])]]
		x[19] = cluster_compliment_funny[cluster_member_compliment_funny[float(line[22])]]
		x[20] = cluster_compliment_writer[cluster_member_compliment_writer[float(line[23])]]
		x[21] = cluster_compliment_photos[cluster_member_compliment_photos[float(line[24])]]
		x[22] = cluster_latitude[cluster_member_latitude[float(line[26])]]
		x[23] = cluster_longitude[cluster_member_longitude[float(line[27])]]
		x[24] = float(line[28])
		x[25] = cluster_business_review_count[cluster_member_business_review_count[float(line[29])]]
		x[26] = float(line[30])
		x[27] = float(line[31])
		x[28] = float(line[32])
		x[29] = float(line[33])
		x[30] = float(line[34])
		x[31] = float(line[35])
		x[32] = float(line[36])
		x[33] = float(line[37])
		x[34] = float(line[38])
		x[35] = float(line[39])
		x[36] = float(line[40])
		x[37] = float(line[41])
		x[38] = float(line[42])
		x[39] = float(line[43])
		x[40] = float(line[44])
		x[41] = float(line[45])
		x[42] = float(line[46])
		x[43] = float(line[47])
		x[44] = float(line[48])
		x[45] = float(line[49])
		x[46] = float(line[50])
		x[47] = float(line[51])
		x[48] = float(line[52])
		x[49] = float(line[53])
		x[50] = float(line[54])
		x[51] = float(line[55])
		x[52] = float(line[56])
		x[53] = float(line[57])
		x[54] = float(line[58])
		x[55] = float(line[59])
		x[56] = float(line[60])
		x[57] = float(line[61])
		x[58] = float(line[62])
		x[59] = float(line[63])
		x[60] = float(line[64])
		x[61] = float(line[65])
		x[62] = float(line[66])
		x[63] = float(line[67])
		x[64] = float(line[68])
		x[65] = float(line[69])
		x[66] = float(line[70])
		x[67] = float(line[71])
		x[68] = float(line[72])
		x[69] = float(line[73])
		x[70] = float(line[74])
		x[71] = float(line[75])
		x[72] = float(line[76])
		x[73] = float(line[77])
		x[74] = float(line[78])
		x[75] = float(line[79])
		x[76] = float(line[80])
		x[77] = float(line[81])
		x[78] = float(line[82])
		x[79] = float(line[83])
		x[80] = float(line[84])
		x[81] = float(line[85])
		x[82] = float(line[86])
		x[83] = float(line[87])
		x[84] = float(line[88])
		x[85] = float(line[89])
		x[86] = float(line[90])
		x[87] = float(line[91])
		x[88] = float(line[92])
		x[89] = float(line[93])
		x[90] = float(line[94])
		x[91] = float(line[95])
		x[92] = float(line[96])
		x[93] = float(line[97])
		x[94] = float(line[98])
		x[95] = float(line[99])
		x[96] = float(line[100])
		x[97] = float(line[101])
		x[98] = float(line[102])
		x[99] = float(line[103])
		x[100] = float(line[104])
		x[101] = float(line[105])
		x[102] = float(line[106])
		x[103] = float(line[107])
		x[104] = float(line[108])
		x[105] = float(line[109])
		x[106] = float(line[110])
		x[107] = float(line[111])
		x[108] = float(line[112])
		x[109] = float(line[113])
		x[110] = float(line[114])
		x[111] = float(line[115])
		x[112] = float(line[116])
		x[113] = float(line[117])
		x[114] = float(line[118])
		x[115] = float(line[119])
		x[116] = float(line[120])
		x[117] = float(line[121])
		x[118] = float(line[123])
	except Exception as e:
		print('Error: ' + line_error+'\n' + str(e))
	#x.append(input_dl_matrix.tolist())
	return np.array(x, dtype=np.float32)
def main_func_with_cluster_test(line):
	line_error = line
	x=[]
	line = line.strip().split(",")

	'''
	review_id[0],stars[1],review_useful[2],review_funny[3],review_cool[4],user_id[5],review_count[6],review_useful[7],
	review_funny[8],review_cool[9],elite[10],friends[11],fans[12],stars[13],compliment_hot[14],compliment_more[15],
	compliment_profile[16],compliment_cute[17],compliment_list[18],compliment_note[19],compliment_plain[20],compliment_cool[21],
	compliment_funny[22],compliment_writer[23],compliment_photos[24],business_id[25],latitude[26],longitude[27],stars[28],
	review_count[29],is_open[30],attributes[31],categories[32],hours[33],NoiseLevel[34],DogsAllowed[35],WheelchairAccessible[36],
	AgesAllowed[37],RestaurantsTableService[38],CoatCheck[39],GoodForKids[40],OpenHours[41],RestaurantsDelivery[42],
	RestaurantsReservations[43],OutdoorSeating[44],BYOB[45],RestaurantsGoodForGroups[46],HappyHour[47],WiFi[48],BYOBCorkage[49],
	Caters[50],ByAppointmentOnly[51],RestaurantsTakeOut[52],RestaurantsCounterService[53],RestaurantsAttire[54],Alcohol[55],
	Corkage[56],AcceptsInsurance[57],Smoking[58],RestaurantsPriceRange2[59],BikeParking[60],BusinessAcceptsCreditCards[61],
	GoodForDancing[62],BusinessAcceptsBitcoin[63],DriveThru[64],HasTV[65],BusinessParking[66],GoodForMeal[67],BestNights[68],
	HairSpecializesIn[69],Music[70],DietaryRestrictions[71],Ambience[72],GoodForMeal_dessert[73],GoodForMeal_latenight[74],
	GoodForMeal_lunch[75],GoodForMeal_dinner[76],GoodForMeal_brunch[77],GoodForMeal_breakfast[78],BestNights_monday[79],
	BestNights_tuesday[80],BestNights_friday[81],BestNights_wednesday[82],BestNights_thursday[83],BestNights_sunday[84],
	BestNights_saturday[85],BusinessParking_garage[86],BusinessParking_street[87],BusinessParking_validated[88],
	BusinessParking_lot[89],BusinessParking_valet[90],HairSpecializesIn_straightperms[91],HairSpecializesIn_coloring[92],
	HairSpecializesIn_extensions[93],HairSpecializesIn_africanamerican[94],HairSpecializesIn_curly[95],HairSpecializesIn_kids[96],
	HairSpecializesIn_perms[97],HairSpecializesIn_asian[98],Music_dj[99],Music_background_music[100],Music_no_music[101],
	Music_jukebox[102],Music_live[103],Music_video[104],Music_karaoke[105],DietaryRestrictions_dairy_free[106],
	DietaryRestrictions_gluten_free[107],DietaryRestrictions_vegan[108],DietaryRestrictions_kosher[109],
	DietaryRestrictions_halal[110],DietaryRestrictions_soy_free[111],DietaryRestrictions_vegetarian[112],Ambience_touristy[113],
	Ambience_hipster[114],Ambience_romantic[115],Ambience_divey[116],Ambience_intimate[117],Ambience_trendy[118],Ambience_upscale[119],
	Ambience_classy[120],Ambience_casual[121],business_id[122],date_count[123]
	'''
	col_num =119
	#input_dl_matrix = np.zeros((1, col_num)).tolist()
	External_list = range(0,col_num)
	for n in External_list:
		x.append(0)
	try:
		x[0] = cluster_review_useful[kmeans_review_useful.predict([[float(line[2])]])[0]]
		x[1] = cluster_review_funny[kmeans_review_funny.predict([[float(line[3])]])[0]]
		x[2] = cluster_review_cool[kmeans_review_cool.predict([[float(line[4])]])[0]]
		x[3] = cluster_user_review_count[kmeans_user_review_count.predict([[float(line[6])]])[0]]
		x[4] = cluster_user_useful[kmeans_user_useful.predict([[float(line[7])]])[0]]
		x[5] = cluster_user_funny[kmeans_user_funny.predict([[float(line[8])]])[0]]
		x[6] = cluster_user_cool[kmeans_user_cool.predict([[float(line[9])]])[0]]
		x[7] = float(line[10])
		x[8] = cluster_friends[kmeans_friends.predict([[float(line[11])]])[0]]
		x[9] = cluster_fans[kmeans_fans.predict([[float(line[12])]])[0]]
		x[10] = cluster_user_stars[kmeans_user_stars.predict([[float(line[13])]])[0]]
		x[11] = cluster_compliment_hot[kmeans_compliment_hot.predict([[float(line[14])]])[0]]
		x[12] = cluster_compliment_more[kmeans_compliment_more.predict([[float(line[15])]])[0]]
		x[13] = cluster_compliment_profile[kmeans_compliment_profile.predict([[float(line[16])]])[0]]
		x[14] = cluster_compliment_cute[kmeans_compliment_cute.predict([[float(line[17])]])[0]]
		x[15] = cluster_compliment_list[kmeans_compliment_list.predict([[float(line[18])]])[0]]
		x[16] = cluster_compliment_note[kmeans_compliment_note.predict([[float(line[19])]])[0]]
		x[17] = cluster_compliment_plain[kmeans_compliment_plain.predict([[float(line[20])]])[0]]
		x[18] = cluster_compliment_cool[kmeans_compliment_cool.predict([[float(line[21])]])[0]]
		x[19] = cluster_compliment_funny[kmeans_compliment_funny.predict([[float(line[22])]])[0]]
		x[20] = cluster_compliment_writer[kmeans_compliment_writer.predict([[float(line[23])]])[0]]
		x[21] = cluster_compliment_photos[kmeans_compliment_photos.predict([[float(line[24])]])[0]]
		x[22] = cluster_latitude[kmeans_latitude.predict([[float(line[26])]])[0]]
		x[23] = cluster_longitude[kmeans_longitude.predict([[float(line[27])]])[0]]
		x[24] = float(line[28])
		x[25] = cluster_business_review_count[kmeans_business_review_count.predict([[float(line[29])]])[0]]
		x[26] = float(line[30])
		x[27] = float(line[31])
		x[28] = float(line[32])
		x[29] = float(line[33])
		x[30] = float(line[34])
		x[31] = float(line[35])
		x[32] = float(line[36])
		x[33] = float(line[37])
		x[34] = float(line[38])
		x[35] = float(line[39])
		x[36] = float(line[40])
		x[37] = float(line[41])
		x[38] = float(line[42])
		x[39] = float(line[43])
		x[40] = float(line[44])
		x[41] = float(line[45])
		x[42] = float(line[46])
		x[43] = float(line[47])
		x[44] = float(line[48])
		x[45] = float(line[49])
		x[46] = float(line[50])
		x[47] = float(line[51])
		x[48] = float(line[52])
		x[49] = float(line[53])
		x[50] = float(line[54])
		x[51] = float(line[55])
		x[52] = float(line[56])
		x[53] = float(line[57])
		x[54] = float(line[58])
		x[55] = float(line[59])
		x[56] = float(line[60])
		x[57] = float(line[61])
		x[58] = float(line[62])
		x[59] = float(line[63])
		x[60] = float(line[64])
		x[61] = float(line[65])
		x[62] = float(line[66])
		x[63] = float(line[67])
		x[64] = float(line[68])
		x[65] = float(line[69])
		x[66] = float(line[70])
		x[67] = float(line[71])
		x[68] = float(line[72])
		x[69] = float(line[73])
		x[70] = float(line[74])
		x[71] = float(line[75])
		x[72] = float(line[76])
		x[73] = float(line[77])
		x[74] = float(line[78])
		x[75] = float(line[79])
		x[76] = float(line[80])
		x[77] = float(line[81])
		x[78] = float(line[82])
		x[79] = float(line[83])
		x[80] = float(line[84])
		x[81] = float(line[85])
		x[82] = float(line[86])
		x[83] = float(line[87])
		x[84] = float(line[88])
		x[85] = float(line[89])
		x[86] = float(line[90])
		x[87] = float(line[91])
		x[88] = float(line[92])
		x[89] = float(line[93])
		x[90] = float(line[94])
		x[91] = float(line[95])
		x[92] = float(line[96])
		x[93] = float(line[97])
		x[94] = float(line[98])
		x[95] = float(line[99])
		x[96] = float(line[100])
		x[97] = float(line[101])
		x[98] = float(line[102])
		x[99] = float(line[103])
		x[100] = float(line[104])
		x[101] = float(line[105])
		x[102] = float(line[106])
		x[103] = float(line[107])
		x[104] = float(line[108])
		x[105] = float(line[109])
		x[106] = float(line[110])
		x[107] = float(line[111])
		x[108] = float(line[112])
		x[109] = float(line[113])
		x[110] = float(line[114])
		x[111] = float(line[115])
		x[112] = float(line[116])
		x[113] = float(line[117])
		x[114] = float(line[118])
		x[115] = float(line[119])
		x[116] = float(line[120])
		x[117] = float(line[121])
		x[118] = float(line[123])
	except Exception as e:
		print('Error: ' + line_error+'\n' + str(e))
	#x.append(input_dl_matrix.tolist())
	return np.array(x, dtype=np.float32)

#Real Input + Shadow Input together
def main_func_main_cluster_inputs(line):
	line_error = line
	x=[]
	line = line.strip().split(",")

	'''
	review_id[0],stars[1],review_useful[2],review_funny[3],review_cool[4],user_id[5],review_count[6],review_useful[7],
	review_funny[8],review_cool[9],elite[10],friends[11],fans[12],stars[13],compliment_hot[14],compliment_more[15],
	compliment_profile[16],compliment_cute[17],compliment_list[18],compliment_note[19],compliment_plain[20],compliment_cool[21],
	compliment_funny[22],compliment_writer[23],compliment_photos[24],business_id[25],latitude[26],longitude[27],stars[28],
	review_count[29],is_open[30],attributes[31],categories[32],hours[33],NoiseLevel[34],DogsAllowed[35],WheelchairAccessible[36],
	AgesAllowed[37],RestaurantsTableService[38],CoatCheck[39],GoodForKids[40],OpenHours[41],RestaurantsDelivery[42],
	RestaurantsReservations[43],OutdoorSeating[44],BYOB[45],RestaurantsGoodForGroups[46],HappyHour[47],WiFi[48],BYOBCorkage[49],
	Caters[50],ByAppointmentOnly[51],RestaurantsTakeOut[52],RestaurantsCounterService[53],RestaurantsAttire[54],Alcohol[55],
	Corkage[56],AcceptsInsurance[57],Smoking[58],RestaurantsPriceRange2[59],BikeParking[60],BusinessAcceptsCreditCards[61],
	GoodForDancing[62],BusinessAcceptsBitcoin[63],DriveThru[64],HasTV[65],BusinessParking[66],GoodForMeal[67],BestNights[68],
	HairSpecializesIn[69],Music[70],DietaryRestrictions[71],Ambience[72],GoodForMeal_dessert[73],GoodForMeal_latenight[74],
	GoodForMeal_lunch[75],GoodForMeal_dinner[76],GoodForMeal_brunch[77],GoodForMeal_breakfast[78],BestNights_monday[79],
	BestNights_tuesday[80],BestNights_friday[81],BestNights_wednesday[82],BestNights_thursday[83],BestNights_sunday[84],
	BestNights_saturday[85],BusinessParking_garage[86],BusinessParking_street[87],BusinessParking_validated[88],
	BusinessParking_lot[89],BusinessParking_valet[90],HairSpecializesIn_straightperms[91],HairSpecializesIn_coloring[92],
	HairSpecializesIn_extensions[93],HairSpecializesIn_africanamerican[94],HairSpecializesIn_curly[95],HairSpecializesIn_kids[96],
	HairSpecializesIn_perms[97],HairSpecializesIn_asian[98],Music_dj[99],Music_background_music[100],Music_no_music[101],
	Music_jukebox[102],Music_live[103],Music_video[104],Music_karaoke[105],DietaryRestrictions_dairy_free[106],
	DietaryRestrictions_gluten_free[107],DietaryRestrictions_vegan[108],DietaryRestrictions_kosher[109],
	DietaryRestrictions_halal[110],DietaryRestrictions_soy_free[111],DietaryRestrictions_vegetarian[112],Ambience_touristy[113],
	Ambience_hipster[114],Ambience_romantic[115],Ambience_divey[116],Ambience_intimate[117],Ambience_trendy[118],Ambience_upscale[119],
	Ambience_classy[120],Ambience_casual[121],business_id[122],date_count[123]
	'''
	col_num =143
	#input_dl_matrix = np.zeros((1, col_num)).tolist()
	External_list = range(0,col_num)
	for n in External_list:
		x.append(0)
	try:
		x[0] = float(line[2])
		x[1] = float(line[3])
		x[2] = float(line[4])
		x[3] = float(line[6])
		x[4] = float(line[7])
		x[5] = float(line[8])
		x[6] = float(line[9])
		x[7] = float(line[10])
		x[8] = float(line[11])
		x[9] = float(line[12])
		x[10] = float(line[13])
		x[11] = float(line[14])
		x[12] = float(line[15])
		x[13] = float(line[16])
		x[14] = float(line[17])
		x[15] = float(line[18])
		x[16] = float(line[19])
		x[17] = float(line[20])
		x[18] = float(line[21])
		x[19] = float(line[22])
		x[20] = float(line[23])
		x[21] = float(line[24])
		x[22] = float(line[26])
		x[23] = float(line[27])
		x[24] = float(line[28])
		x[25] = float(line[29])
		x[26] = float(line[30])
		x[27] = float(line[31])
		x[28] = float(line[32])
		x[29] = float(line[33])
		x[30] = float(line[34])
		x[31] = float(line[35])
		x[32] = float(line[36])
		x[33] = float(line[37])
		x[34] = float(line[38])
		x[35] = float(line[39])
		x[36] = float(line[40])
		x[37] = float(line[41])
		x[38] = float(line[42])
		x[39] = float(line[43])
		x[40] = float(line[44])
		x[41] = float(line[45])
		x[42] = float(line[46])
		x[43] = float(line[47])
		x[44] = float(line[48])
		x[45] = float(line[49])
		x[46] = float(line[50])
		x[47] = float(line[51])
		x[48] = float(line[52])
		x[49] = float(line[53])
		x[50] = float(line[54])
		x[51] = float(line[55])
		x[52] = float(line[56])
		x[53] = float(line[57])
		x[54] = float(line[58])
		x[55] = float(line[59])
		x[56] = float(line[60])
		x[57] = float(line[61])
		x[58] = float(line[62])
		x[59] = float(line[63])
		x[60] = float(line[64])
		x[61] = float(line[65])
		x[62] = float(line[66])
		x[63] = float(line[67])
		x[64] = float(line[68])
		x[65] = float(line[69])
		x[66] = float(line[70])
		x[67] = float(line[71])
		x[68] = float(line[72])
		x[69] = float(line[73])
		x[70] = float(line[74])
		x[71] = float(line[75])
		x[72] = float(line[76])
		x[73] = float(line[77])
		x[74] = float(line[78])
		x[75] = float(line[79])
		x[76] = float(line[80])
		x[77] = float(line[81])
		x[78] = float(line[82])
		x[79] = float(line[83])
		x[80] = float(line[84])
		x[81] = float(line[85])
		x[82] = float(line[86])
		x[83] = float(line[87])
		x[84] = float(line[88])
		x[85] = float(line[89])
		x[86] = float(line[90])
		x[87] = float(line[91])
		x[88] = float(line[92])
		x[89] = float(line[93])
		x[90] = float(line[94])
		x[91] = float(line[95])
		x[92] = float(line[96])
		x[93] = float(line[97])
		x[94] = float(line[98])
		x[95] = float(line[99])
		x[96] = float(line[100])
		x[97] = float(line[101])
		x[98] = float(line[102])
		x[99] = float(line[103])
		x[100] = float(line[104])
		x[101] = float(line[105])
		x[102] = float(line[106])
		x[103] = float(line[107])
		x[104] = float(line[108])
		x[105] = float(line[109])
		x[106] = float(line[110])
		x[107] = float(line[111])
		x[108] = float(line[112])
		x[109] = float(line[113])
		x[110] = float(line[114])
		x[111] = float(line[115])
		x[112] = float(line[116])
		x[113] = float(line[117])
		x[114] = float(line[118])
		x[115] = float(line[119])
		x[116] = float(line[120])
		x[117] = float(line[121])
		x[118] = float(line[123])
		x[119] = cluster_review_useful[cluster_member_review_useful[float(line[2])]]
		x[120] = cluster_review_funny[cluster_member_review_funny[float(line[3])]]
		x[121] = cluster_review_cool[cluster_member_review_cool[float(line[4])]]
		x[122] = cluster_user_review_count[cluster_member_user_review_count[float(line[6])]]
		x[123] = cluster_user_useful[cluster_member_user_useful[float(line[7])]]
		x[124] = cluster_user_funny[cluster_member_user_funny[float(line[8])]]
		x[125] = cluster_user_cool[cluster_member_user_cool[float(line[9])]]
		x[126] = cluster_friends[cluster_member_friends[float(line[11])]]
		x[127] = cluster_fans[cluster_member_fans[float(line[12])]]
		x[128] = cluster_user_stars[cluster_member_user_stars[float(line[13])]]
		x[129] = cluster_compliment_hot[cluster_member_compliment_hot[float(line[14])]]
		x[130] = cluster_compliment_more[cluster_member_compliment_more[float(line[15])]]
		x[131] = cluster_compliment_profile[cluster_member_compliment_profile[float(line[16])]]
		x[132] = cluster_compliment_cute[cluster_member_compliment_cute[float(line[17])]]
		x[133] = cluster_compliment_list[cluster_member_compliment_list[float(line[18])]]
		x[134] = cluster_compliment_note[cluster_member_compliment_note[float(line[19])]]
		x[135] = cluster_compliment_plain[cluster_member_compliment_plain[float(line[20])]]
		x[136] = cluster_compliment_cool[cluster_member_compliment_cool[float(line[21])]]
		x[137] = cluster_compliment_funny[cluster_member_compliment_funny[float(line[22])]]
		x[138] = cluster_compliment_writer[cluster_member_compliment_writer[float(line[23])]]
		x[139] = cluster_compliment_photos[cluster_member_compliment_photos[float(line[24])]]
		x[140] = cluster_latitude[cluster_member_latitude[float(line[26])]]
		x[141] = cluster_longitude[cluster_member_longitude[float(line[27])]]
		x[142] = cluster_business_review_count[cluster_member_business_review_count[float(line[29])]]
	except Exception as e:
		print('Error: ' + line_error+'\n' + str(e))
	#x.append(input_dl_matrix.tolist())
	return np.array(x, dtype=np.float32)
def main_func_main_cluster_inputs_test(line):
	line_error = line
	x=[]
	line = line.strip().split(",")

	'''
	review_id[0],stars[1],review_useful[2],review_funny[3],review_cool[4],user_id[5],review_count[6],review_useful[7],
	review_funny[8],review_cool[9],elite[10],friends[11],fans[12],stars[13],compliment_hot[14],compliment_more[15],
	compliment_profile[16],compliment_cute[17],compliment_list[18],compliment_note[19],compliment_plain[20],compliment_cool[21],
	compliment_funny[22],compliment_writer[23],compliment_photos[24],business_id[25],latitude[26],longitude[27],stars[28],
	review_count[29],is_open[30],attributes[31],categories[32],hours[33],NoiseLevel[34],DogsAllowed[35],WheelchairAccessible[36],
	AgesAllowed[37],RestaurantsTableService[38],CoatCheck[39],GoodForKids[40],OpenHours[41],RestaurantsDelivery[42],
	RestaurantsReservations[43],OutdoorSeating[44],BYOB[45],RestaurantsGoodForGroups[46],HappyHour[47],WiFi[48],BYOBCorkage[49],
	Caters[50],ByAppointmentOnly[51],RestaurantsTakeOut[52],RestaurantsCounterService[53],RestaurantsAttire[54],Alcohol[55],
	Corkage[56],AcceptsInsurance[57],Smoking[58],RestaurantsPriceRange2[59],BikeParking[60],BusinessAcceptsCreditCards[61],
	GoodForDancing[62],BusinessAcceptsBitcoin[63],DriveThru[64],HasTV[65],BusinessParking[66],GoodForMeal[67],BestNights[68],
	HairSpecializesIn[69],Music[70],DietaryRestrictions[71],Ambience[72],GoodForMeal_dessert[73],GoodForMeal_latenight[74],
	GoodForMeal_lunch[75],GoodForMeal_dinner[76],GoodForMeal_brunch[77],GoodForMeal_breakfast[78],BestNights_monday[79],
	BestNights_tuesday[80],BestNights_friday[81],BestNights_wednesday[82],BestNights_thursday[83],BestNights_sunday[84],
	BestNights_saturday[85],BusinessParking_garage[86],BusinessParking_street[87],BusinessParking_validated[88],
	BusinessParking_lot[89],BusinessParking_valet[90],HairSpecializesIn_straightperms[91],HairSpecializesIn_coloring[92],
	HairSpecializesIn_extensions[93],HairSpecializesIn_africanamerican[94],HairSpecializesIn_curly[95],HairSpecializesIn_kids[96],
	HairSpecializesIn_perms[97],HairSpecializesIn_asian[98],Music_dj[99],Music_background_music[100],Music_no_music[101],
	Music_jukebox[102],Music_live[103],Music_video[104],Music_karaoke[105],DietaryRestrictions_dairy_free[106],
	DietaryRestrictions_gluten_free[107],DietaryRestrictions_vegan[108],DietaryRestrictions_kosher[109],
	DietaryRestrictions_halal[110],DietaryRestrictions_soy_free[111],DietaryRestrictions_vegetarian[112],Ambience_touristy[113],
	Ambience_hipster[114],Ambience_romantic[115],Ambience_divey[116],Ambience_intimate[117],Ambience_trendy[118],Ambience_upscale[119],
	Ambience_classy[120],Ambience_casual[121],business_id[122],date_count[123]
	'''
	col_num =143
	#input_dl_matrix = np.zeros((1, col_num)).tolist()
	External_list = range(0,col_num)
	for n in External_list:
		x.append(0)
	try:
		x[0] = float(line[2])
		x[1] = float(line[3])
		x[2] = float(line[4])
		x[3] = float(line[6])
		x[4] = float(line[7])
		x[5] = float(line[8])
		x[6] = float(line[9])
		x[7] = float(line[10])
		x[8] = float(line[11])
		x[9] = float(line[12])
		x[10] = float(line[13])
		x[11] = float(line[14])
		x[12] = float(line[15])
		x[13] = float(line[16])
		x[14] = float(line[17])
		x[15] = float(line[18])
		x[16] = float(line[19])
		x[17] = float(line[20])
		x[18] = float(line[21])
		x[19] = float(line[22])
		x[20] = float(line[23])
		x[21] = float(line[24])
		x[22] = float(line[26])
		x[23] = float(line[27])
		x[24] = float(line[28])
		x[25] = float(line[29])
		x[26] = float(line[30])
		x[27] = float(line[31])
		x[28] = float(line[32])
		x[29] = float(line[33])
		x[30] = float(line[34])
		x[31] = float(line[35])
		x[32] = float(line[36])
		x[33] = float(line[37])
		x[34] = float(line[38])
		x[35] = float(line[39])
		x[36] = float(line[40])
		x[37] = float(line[41])
		x[38] = float(line[42])
		x[39] = float(line[43])
		x[40] = float(line[44])
		x[41] = float(line[45])
		x[42] = float(line[46])
		x[43] = float(line[47])
		x[44] = float(line[48])
		x[45] = float(line[49])
		x[46] = float(line[50])
		x[47] = float(line[51])
		x[48] = float(line[52])
		x[49] = float(line[53])
		x[50] = float(line[54])
		x[51] = float(line[55])
		x[52] = float(line[56])
		x[53] = float(line[57])
		x[54] = float(line[58])
		x[55] = float(line[59])
		x[56] = float(line[60])
		x[57] = float(line[61])
		x[58] = float(line[62])
		x[59] = float(line[63])
		x[60] = float(line[64])
		x[61] = float(line[65])
		x[62] = float(line[66])
		x[63] = float(line[67])
		x[64] = float(line[68])
		x[65] = float(line[69])
		x[66] = float(line[70])
		x[67] = float(line[71])
		x[68] = float(line[72])
		x[69] = float(line[73])
		x[70] = float(line[74])
		x[71] = float(line[75])
		x[72] = float(line[76])
		x[73] = float(line[77])
		x[74] = float(line[78])
		x[75] = float(line[79])
		x[76] = float(line[80])
		x[77] = float(line[81])
		x[78] = float(line[82])
		x[79] = float(line[83])
		x[80] = float(line[84])
		x[81] = float(line[85])
		x[82] = float(line[86])
		x[83] = float(line[87])
		x[84] = float(line[88])
		x[85] = float(line[89])
		x[86] = float(line[90])
		x[87] = float(line[91])
		x[88] = float(line[92])
		x[89] = float(line[93])
		x[90] = float(line[94])
		x[91] = float(line[95])
		x[92] = float(line[96])
		x[93] = float(line[97])
		x[94] = float(line[98])
		x[95] = float(line[99])
		x[96] = float(line[100])
		x[97] = float(line[101])
		x[98] = float(line[102])
		x[99] = float(line[103])
		x[100] = float(line[104])
		x[101] = float(line[105])
		x[102] = float(line[106])
		x[103] = float(line[107])
		x[104] = float(line[108])
		x[105] = float(line[109])
		x[106] = float(line[110])
		x[107] = float(line[111])
		x[108] = float(line[112])
		x[109] = float(line[113])
		x[110] = float(line[114])
		x[111] = float(line[115])
		x[112] = float(line[116])
		x[113] = float(line[117])
		x[114] = float(line[118])
		x[115] = float(line[119])
		x[116] = float(line[120])
		x[117] = float(line[121])
		x[118] = float(line[123])
		x[119] = cluster_review_useful[kmeans_review_useful.predict([[float(line[2])]])[0]]
		x[120] = cluster_review_funny[kmeans_review_funny.predict([[float(line[3])]])[0]]
		x[121] = cluster_review_cool[kmeans_review_cool.predict([[float(line[4])]])[0]]
		x[122] = cluster_user_review_count[kmeans_user_review_count.predict([[float(line[6])]])[0]]
		x[123] = cluster_user_useful[kmeans_user_useful.predict([[float(line[7])]])[0]]
		x[124] = cluster_user_funny[kmeans_user_funny.predict([[float(line[8])]])[0]]
		x[125] = cluster_user_cool[kmeans_user_cool.predict([[float(line[9])]])[0]]
		x[126] = cluster_friends[kmeans_friends.predict([[float(line[11])]])[0]]
		x[127] = cluster_fans[kmeans_fans.predict([[float(line[12])]])[0]]
		x[128] = cluster_user_stars[kmeans_user_stars.predict([[float(line[13])]])[0]]
		x[129] = cluster_compliment_hot[kmeans_compliment_hot.predict([[float(line[14])]])[0]]
		x[130] = cluster_compliment_more[kmeans_compliment_more.predict([[float(line[15])]])[0]]
		x[131] = cluster_compliment_profile[kmeans_compliment_profile.predict([[float(line[16])]])[0]]
		x[132] = cluster_compliment_cute[kmeans_compliment_cute.predict([[float(line[17])]])[0]]
		x[133] = cluster_compliment_list[kmeans_compliment_list.predict([[float(line[18])]])[0]]
		x[134] = cluster_compliment_note[kmeans_compliment_note.predict([[float(line[19])]])[0]]
		x[135] = cluster_compliment_plain[kmeans_compliment_plain.predict([[float(line[20])]])[0]]
		x[136] = cluster_compliment_cool[kmeans_compliment_cool.predict([[float(line[21])]])[0]]
		x[137] = cluster_compliment_funny[kmeans_compliment_funny.predict([[float(line[22])]])[0]]
		x[138] = cluster_compliment_writer[kmeans_compliment_writer.predict([[float(line[23])]])[0]]
		x[139] = cluster_compliment_photos[kmeans_compliment_photos.predict([[float(line[24])]])[0]]
		x[140] = cluster_latitude[kmeans_latitude.predict([[float(line[26])]])[0]]
		x[141] = cluster_longitude[kmeans_longitude.predict([[float(line[27])]])[0]]
		x[142] = cluster_business_review_count[kmeans_business_review_count.predict([[float(line[29])]])[0]]
	except Exception as e:
		print('Error: ' + line_error+'\n' + str(e))
	#x.append(input_dl_matrix.tolist())
	return np.array(x, dtype=np.float32)