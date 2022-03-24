import json
from sklearn import preprocessing
from scipy.constants import hour
import math
import numpy as np
import json
from scipy.constants import hour
from sklearn import preprocessing
import math
import numpy as np
import random
Home_Address='/media/fs_Linux_Files/'

################### User
def User_Preprocess():
    f = open(Home_Address+'track2/yelp/yelp_academic_dataset_user.json','r')
    f_w = open(Home_Address+'track2/yelp/user.txt','w')

    user_id= []
    review_count =[]
    review_useful =[]
    review_funny =[]
    review_cool =[]
    elite =[]
    friends=[]
    fans=[]
    average_stars =[]
    compliment_hot=[]
    compliment_more=[]
    compliment_profile=[]
    compliment_cute=[]
    compliment_list=[]
    compliment_note=[]
    compliment_plain=[]
    compliment_cool=[]
    compliment_funny=[]
    compliment_writer=[]
    compliment_photos=[]
    counter=0

    for line in f:
        j_line = json.loads(line)
        user_id.append(j_line['user_id'])
        review_count.append(j_line['review_count'])
        review_useful.append(j_line['review_useful'])
        review_funny.append(j_line['review_funny'])
        review_cool.append(j_line['review_cool'])
        elite.append(len(j_line['elite'].split(',')))
        friends.append(len(j_line['friends'].split(',')))
        fans.append(j_line['fans'])
        average_stars.append(j_line['average_stars'])
        compliment_hot.append(j_line['compliment_hot'])
        compliment_more.append(j_line['compliment_more'])
        compliment_profile.append(j_line['compliment_profile'])
        compliment_cute.append(j_line['compliment_cute'])
        compliment_list.append(j_line['compliment_list'])
        compliment_note.append(j_line['compliment_note'])
        compliment_plain.append(j_line['compliment_plain'])
        compliment_cool.append(j_line['compliment_cool'])
        compliment_funny.append(j_line['compliment_funny'])
        compliment_writer.append(j_line['compliment_writer'])
        compliment_photos.append(j_line['compliment_photos'])

        if counter%100000 ==0:
            print(counter)
        counter += 1
    f.close()

    norm_review_count = preprocessing.normalize([review_count])
    norm_useful = preprocessing.normalize([review_useful])
    norm_funny = preprocessing.normalize([review_funny])
    norm_cool = preprocessing.normalize([review_cool])
    norm_elite = preprocessing.normalize([elite])
    norm_friends = preprocessing.normalize([friends])
    norm_fans = preprocessing.normalize([fans])
    norm_average_stars = preprocessing.normalize([average_stars])
    norm_compliment_hot = preprocessing.normalize([compliment_hot])
    norm_compliment_more = preprocessing.normalize([compliment_more])
    norm_compliment_profile = preprocessing.normalize([compliment_profile])
    norm_compliment_cute = preprocessing.normalize([compliment_cute])
    norm_compliment_list = preprocessing.normalize([compliment_list])
    norm_compliment_note = preprocessing.normalize([compliment_note])
    norm_compliment_plain = preprocessing.normalize([compliment_plain])
    norm_compliment_cool = preprocessing.normalize([compliment_cool])
    norm_compliment_funny = preprocessing.normalize([compliment_funny])
    norm_compliment_writer = preprocessing.normalize([compliment_writer])
    norm_compliment_photos = preprocessing.normalize([compliment_photos])

    for i in range(0,len(norm_review_count[0])):
        total_line=user_id[i]+','+str(round(norm_review_count[0][i],6))+','+str(round(norm_useful[0][i],6))+','+str(round(norm_funny[0][i],6))+','+str(round(norm_cool[0][i],6))+','\
                   +str(round(norm_elite[0][i],6))+','+str(round(norm_friends[0][i],6))+','+str(round(norm_fans[0][i],6))+','+str(round(norm_average_stars[0][i],6))+','+\
                    str(round(norm_compliment_hot[0][i],6))+','+str(round(norm_compliment_more[0][i],6))+','+str(round(norm_compliment_profile[0][i],6))+','+str(round(norm_compliment_cute[0][i],6))+','+\
                    str(round(norm_compliment_list[0][i],6))+','+str(round(norm_compliment_note[0][i],6))+','+str(round(norm_compliment_plain[0][i],6))+','+str(round(norm_compliment_cool[0][i],6))+','+\
                    str(round(norm_compliment_funny[0][i],6))+','+str(round(norm_compliment_writer[0][i],6))+','+str(round(norm_compliment_photos[0][i],6))+'\n'
        f_w.write(total_line)
    f_w.close()
################### Business
def Business_Preprocess():
    business_id=[]
    latitude=[]
    longitude=[]
    stars=[]
    review_count=[]
    is_open=[]
    attributes=[]
    categories=[]
    hours=[]
    #attributes
    NoiseLevel=[]
    DogsAllowed=[]
    WheelchairAccessible=[]
    AgesAllowed=[]
    RestaurantsTableService=[]
    CoatCheck=[]
    GoodForKids=[]
    Open24Hours=[]
    RestaurantsDelivery=[]
    DietaryRestrictions=[]
    RestaurantsReservations=[]
    OutdoorSeating=[]
    BYOB=[]
    RestaurantsGoodForGroups=[]
    HappyHour=[]
    WiFi=[]
    BYOBCorkage=[]
    Caters=[]
    GoodForMeal=[]
    ByAppointmentOnly=[]
    RestaurantsTakeOut=[]
    RestaurantsCounterService=[]
    RestaurantsAttire=[]
    Alcohol=[]
    HairSpecializesIn=[]
    Corkage=[]
    AcceptsInsurance=[]
    Smoking=[]
    Ambience=[]
    RestaurantsPriceRange2=[]
    BestNights=[]
    BikeParking=[]
    BusinessAcceptsCreditCards=[]
    GoodForDancing=[]
    BusinessAcceptsBitcoin=[]
    BusinessParking=[]
    DriveThru=[]
    Music=[]
    HasTV=[]
    #attributs_GoodForMeal
    GoodForMeal_dessert =[]
    GoodForMeal_latenight =[]
    GoodForMeal_lunch =[]
    GoodForMeal_dinner =[]
    GoodForMeal_brunch =[]
    GoodForMeal_breakfast =[]
    #attributs_BestNights
    BestNights_monday=[]
    BestNights_tuesday=[]
    BestNights_friday=[]
    BestNights_wednesday=[]
    BestNights_thursday=[]
    BestNights_sunday=[]
    BestNights_saturday=[]
    #attributs_BusinessParking
    BusinessParking_garage=[]
    BusinessParking_street=[]
    BusinessParking_validated=[]
    BusinessParking_lot=[]
    BusinessParking_valet=[]
    #attributes_HairSpecializesIn
    HairSpecializesIn_straightperms=[]
    HairSpecializesIn_coloring=[]
    HairSpecializesIn_extensions=[]
    HairSpecializesIn_africanamerican=[]
    HairSpecializesIn_curly=[]
    HairSpecializesIn_kids=[]
    HairSpecializesIn_perms=[]
    HairSpecializesIn_asian=[]
    #attributes_Music
    Music_dj=[]
    Music_background_music=[]
    Music_no_music=[]
    Music_jukebox=[]
    Music_live=[]
    Music_video=[]
    Music_karaoke=[]
    #attributes_DietaryRestrictions
    DietaryRestrictions_dairy_free=[]
    DietaryRestrictions_gluten_free=[]
    DietaryRestrictions_vegan=[]
    DietaryRestrictions_kosher=[]
    DietaryRestrictions_halal=[]
    DietaryRestrictions_soy_free=[]
    DietaryRestrictions_vegetarian=[]
    #attributes_Ambience
    Ambience_touristy=[]
    Ambience_hipster=[]
    Ambience_romantic=[]
    Ambience_divey=[]
    Ambience_intimate=[]
    Ambience_trendy=[]
    Ambience_upscale=[]
    Ambience_classy=[]
    Ambience_casual=[]

    f = open(Home_Address+'track2/yelp/yelp_academic_dataset_business.json','r')
    counter=0
    for line in f:
        j_line = json.loads(line)
        business_id.append(j_line['business_id'])
        latitude.append(j_line['latitude'])
        longitude.append(j_line['longitude'])
        stars.append(j_line['stars'])
        review_count.append(j_line['review_count'])
        is_open.append(j_line['is_open'])
        attributes.append(0 if None==j_line['attributes'] else len(j_line['attributes'].keys()))
        categories.append(0 if None==j_line['categories'] else len(j_line['categories'].split(',')))
        hours.append(0 if None==j_line['hours'] else len(j_line['hours'].keys()))
        #if None!=j_line['attributes'] :
        NoiseLevel.append(1 if None!=j_line['attributes'] and 'NoiseLevel' in j_line['attributes'].keys()  else 0)
        DogsAllowed.append(1 if None!=j_line['attributes'] and 'DogsAllowed' in j_line['attributes'].keys()  else 0)
        WheelchairAccessible.append(1 if None!=j_line['attributes'] and 'WheelchairAccessible' in j_line['attributes'].keys()  else 0)
        AgesAllowed.append(1 if None!=j_line['attributes'] and 'AgesAllowed' in j_line['attributes'].keys()  else 0)
        RestaurantsTableService.append(1 if None!=j_line['attributes'] and 'NoiseLevel' in j_line['attributes'].keys()  else 0)
        CoatCheck.append(1 if None!=j_line['attributes'] and 'CoatCheck' in j_line['attributes'].keys()  else 0)
        GoodForKids.append(1 if None!=j_line['attributes'] and 'GoodForKids' in j_line['attributes'].keys()  else 0)
        Open24Hours.append(1 if None!=j_line['attributes'] and 'Open24Hours' in j_line['attributes'].keys()  else 0)
        RestaurantsDelivery.append(1 if None!=j_line['attributes'] and 'RestaurantsDelivery' in j_line['attributes'].keys()  else 0)
        RestaurantsReservations.append(1 if None!=j_line['attributes'] and 'RestaurantsReservations' in j_line['attributes'].keys()  else 0)
        OutdoorSeating.append(1 if None!=j_line['attributes'] and 'OutdoorSeating' in j_line['attributes'].keys()  else 0)
        BYOB.append(1 if None!=j_line['attributes'] and 'BYOB' in j_line['attributes'].keys()  else 0)
        RestaurantsGoodForGroups.append(1 if None!=j_line['attributes'] and  'RestaurantsGoodForGroups' in j_line['attributes'].keys()  else 0)
        HappyHour.append(1 if None!=j_line['attributes'] and  'HappyHour' in j_line['attributes'].keys()  else 0)
        WiFi.append(1 if None!=j_line['attributes'] and  'WiFi' in j_line['attributes'].keys()  else 0)
        BYOBCorkage.append(1 if None!=j_line['attributes'] and  'BYOBCorkage' in j_line['attributes'].keys()  else 0)
        Caters.append(1 if None!=j_line['attributes'] and  'Caters' in j_line['attributes'].keys()  else 0)
        ByAppointmentOnly.append(1 if None!=j_line['attributes'] and  'ByAppointmentOnly' in j_line['attributes'].keys()  else 0)
        RestaurantsTakeOut.append(1 if None!=j_line['attributes'] and  'RestaurantsTakeOut' in j_line['attributes'].keys()  else 0)
        RestaurantsCounterService.append(1 if None!=j_line['attributes'] and  'RestaurantsCounterService' in j_line['attributes'].keys()  else 0)
        RestaurantsAttire.append(1 if None!=j_line['attributes'] and  'RestaurantsAttire' in j_line['attributes'].keys()  else 0)
        Alcohol.append(1 if None!=j_line['attributes'] and  'Alcohol' in j_line['attributes'].keys()  else 0)
        Corkage.append(1 if None!=j_line['attributes'] and  'Corkage' in j_line['attributes'].keys()  else 0)
        AcceptsInsurance.append(1 if None!=j_line['attributes'] and  'AcceptsInsurance' in j_line['attributes'].keys()  else 0)
        Smoking.append(1 if None!=j_line['attributes'] and  'Smoking' in j_line['attributes'].keys()  else 0)
        RestaurantsPriceRange2.append(1 if None!=j_line['attributes'] and  'RestaurantsPriceRange2' in j_line['attributes'].keys()  else 0)
        BikeParking.append(1 if None!=j_line['attributes'] and  'BikeParking' in j_line['attributes'].keys()  else 0)
        BusinessAcceptsCreditCards.append(1 if None!=j_line['attributes'] and  'BusinessAcceptsCreditCards' in j_line['attributes'].keys()  else 0)
        GoodForDancing.append(1 if None!=j_line['attributes'] and  'GoodForDancing' in j_line['attributes'].keys()  else 0)
        BusinessAcceptsBitcoin.append(1 if None!=j_line['attributes'] and  'BusinessAcceptsBitcoin' in j_line['attributes'].keys()  else 0)
        DriveThru.append(1 if None!=j_line['attributes'] and  'DriveThru' in j_line['attributes'].keys()  else 0)
        HasTV.append(1 if None!=j_line['attributes'] and  'HasTV' in j_line['attributes'].keys()  else 0)

        BusinessParking.append(j_line['attributes']['BusinessParking'].count('True') if None != j_line['attributes'] and 'BusinessParking' in j_line['attributes'].keys() else 0)
        GoodForMeal.append(j_line['attributes']['GoodForMeal'].count('True') if None != j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() else 0)
        BestNights.append(j_line['attributes']['BestNights'].count('True') if None != j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() else 0)
        HairSpecializesIn.append(j_line['attributes']['HairSpecializesIn'].count('True') if None != j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() else 0)
        Music.append(j_line['attributes']['Music'].count('True') if None != j_line['attributes'] and 'Music' in j_line['attributes'].keys() else 0)
        DietaryRestrictions.append(j_line['attributes']['DietaryRestrictions'].count('True') if None != j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() else 0)
        Ambience.append(j_line['attributes']['Ambience'].count('True') if None != j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() else 0)
        # attributs_GoodForMeal
        # if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys():
        GoodForMeal_dessert.append(1 if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() and "'dessert': True" in j_line['attributes']['GoodForMeal'] else 0)
        GoodForMeal_latenight.append(1 if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() and  "'latenight': True" in j_line['attributes']['GoodForMeal'] else 0)
        GoodForMeal_lunch.append(1 if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() and  "'lunch': True" in j_line['attributes']['GoodForMeal'] else 0)
        GoodForMeal_dinner.append(1 if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() and  "'dinner': True" in j_line['attributes']['GoodForMeal'] else 0)
        GoodForMeal_brunch.append(1 if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() and  "'brunch': True" in j_line['attributes']['GoodForMeal'] else 0)
        GoodForMeal_breakfast.append(1 if None!=j_line['attributes'] and 'GoodForMeal' in j_line['attributes'].keys() and  "'breakfast': True" in j_line['attributes']['GoodForMeal'] else 0)
        # attributs_BestNights
            #if 'BestNights' in j_line['attributes'].keys():
        BestNights_monday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'monday': True" in j_line['attributes']['BestNights'] else 0)
        BestNights_tuesday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'tuesday': True" in j_line['attributes']['BestNights'] else 0)
        BestNights_friday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'friday': True" in j_line['attributes']['BestNights'] else 0)
        BestNights_wednesday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'wednesday': True" in j_line['attributes']['BestNights'] else 0)
        BestNights_thursday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'thursday': True" in j_line['attributes']['BestNights'] else 0)
        BestNights_sunday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'sunday': True" in j_line['attributes']['BestNights'] else 0)
        BestNights_saturday.append(1 if None!=j_line['attributes'] and 'BestNights' in j_line['attributes'].keys() and  "'saturday': True" in j_line['attributes']['BestNights'] else 0)
        # attributs_BusinessParking
            #if 'BusinessParking' in j_line['attributes'].keys():
        BusinessParking_garage.append(1 if None!=j_line['attributes'] and 'BusinessParking' in j_line['attributes'].keys() and  "'garage': True" in j_line['attributes']['BusinessParking'] else 0)
        BusinessParking_street.append(1 if None!=j_line['attributes'] and 'BusinessParking' in j_line['attributes'].keys() and  "'street': True" in j_line['attributes']['BusinessParking'] else 0)
        BusinessParking_validated.append(1 if None!=j_line['attributes'] and 'BusinessParking' in j_line['attributes'].keys() and  "'validated': True" in j_line['attributes']['BusinessParking'] else 0)
        BusinessParking_lot.append(1 if None!=j_line['attributes'] and 'BusinessParking' in j_line['attributes'].keys() and  "'lot': True" in j_line['attributes']['BusinessParking'] else 0)
        BusinessParking_valet.append(1 if None!=j_line['attributes'] and 'BusinessParking' in j_line['attributes'].keys() and  "'valet': True" in j_line['attributes']['BusinessParking'] else 0)
        # attributes_HairSpecializesIn
            #if 'HairSpecializesIn' in j_line['attributes'].keys():
        HairSpecializesIn_straightperms.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'straightperms': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_coloring.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'coloring': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_extensions.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'extensions': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_africanamerican.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'africanamerican': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_curly.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'curly': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_kids.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'kids': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_perms.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'perms': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        HairSpecializesIn_asian.append(1 if None!=j_line['attributes'] and 'HairSpecializesIn' in j_line['attributes'].keys() and  "'asian': True" in j_line['attributes']['HairSpecializesIn'] else 0)
        # attributes_Music
            #if 'Music' in j_line['attributes'].keys():
        Music_dj.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'dj': True" in j_line['attributes']['Music'] else 0)
        Music_background_music.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'background_music': True" in j_line['attributes']['Music'] else 0)
        Music_no_music.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'no_music': True" in j_line['attributes']['Music'] else 0)
        Music_jukebox.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'jukebox': True" in j_line['attributes']['Music'] else 0)
        Music_live.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'live': True" in j_line['attributes']['Music'] else 0)
        Music_video.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'video': True" in j_line['attributes']['Music'] else 0)
        Music_karaoke.append(1 if None!=j_line['attributes'] and 'Music' in j_line['attributes'].keys() and  "'karaoke': True" in j_line['attributes']['Music'] else 0)
        # attributes_DietaryRestrictions
            #if 'DietaryRestrictions' in j_line['attributes'].keys():
        DietaryRestrictions_dairy_free.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'dairy-free': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        DietaryRestrictions_gluten_free.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'gluten-free': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        DietaryRestrictions_vegan.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'vegan': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        DietaryRestrictions_kosher.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'kosher': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        DietaryRestrictions_halal.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'halal': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        DietaryRestrictions_soy_free.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'soy-free': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        DietaryRestrictions_vegetarian.append(1 if None!=j_line['attributes'] and 'DietaryRestrictions' in j_line['attributes'].keys() and  "'vegetarian': True" in j_line['attributes']['DietaryRestrictions'] else 0)
        # attributes_Ambience
            #if 'Ambience' in j_line['attributes'].keys():
        Ambience_touristy.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'touristy': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_hipster.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'hipster': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_romantic.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'romantic': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_divey.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'divey': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_intimate.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'intimate': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_trendy.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'trendy': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_upscale.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'upscale': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_classy.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'classy': True" in j_line['attributes']['Ambience'] else 0)
        Ambience_casual.append(1 if None!=j_line['attributes'] and 'Ambience' in j_line['attributes'].keys() and  "'casual': True" in j_line['attributes']['Ambience'] else 0)

        if counter%1000 ==0:
            print(counter)
        counter += 1
    f.close()

    f_w = open(Home_Address+'track2/yelp/business.txt','w')
    norm_latitude = preprocessing.normalize([latitude])
    norm_longitude = preprocessing.normalize([longitude])
    norm_stars= preprocessing.normalize([stars])
    norm_review_count = preprocessing.normalize([review_count])
    norm_attributes= preprocessing.normalize([attributes])
    norm_categories= preprocessing.normalize([categories])
    norm_hours= preprocessing.normalize([hours])
    norm_BusinessParking= preprocessing.normalize([BusinessParking])
    norm_GoodForMeal= preprocessing.normalize([GoodForMeal])
    norm_BestNights= preprocessing.normalize([BestNights])
    norm_HairSpecializesIn= preprocessing.normalize([HairSpecializesIn])
    norm_Music= preprocessing.normalize([Music])
    norm_DietaryRestrictions= preprocessing.normalize([DietaryRestrictions])
    norm_Ambience= preprocessing.normalize([Ambience])

    for i  in range(0,len(norm_latitude[0])):
        total_feature=str(business_id[i])+','+str(round(norm_latitude[0][i],6))+','+str(round(norm_longitude[0][i],6))+','+str(round(norm_stars[0][i],6))+','+str(round(norm_review_count[0][i],6))+','+\
                      str(is_open[i])+','+str(round(norm_attributes[0][i],6))+','+str(round(norm_categories[0][i],6))+','+str(round(norm_hours[0][i],6))+','+\
                      str(NoiseLevel[i])+','+str(DogsAllowed[i])+','+str(WheelchairAccessible[i])+','+str(AgesAllowed[i])+','+\
                      str(RestaurantsTableService[i])+','+str(CoatCheck[i])+','+str(GoodForKids[i])+','+str(Open24Hours[i])+','+\
                      str(RestaurantsDelivery[i])+','+str(RestaurantsReservations[i])+','+str(OutdoorSeating[i])+','+str(BYOB[i])+','+\
                      str(RestaurantsGoodForGroups[i])+','+str(HappyHour[i])+','+str(WiFi[i])+','+str(BYOBCorkage[i])+','+str(Caters[i])+','+\
                      str(ByAppointmentOnly[i])+','+str(RestaurantsTakeOut[i])+','+str(RestaurantsCounterService[i])+','+\
                      str(RestaurantsAttire[i])+','+str(Alcohol[i])+','+str(Corkage[i])+','+str(AcceptsInsurance[i])+','+\
                      str(Smoking[i])+','+str(RestaurantsPriceRange2[i])+','+str(BikeParking[i])+','+str(BusinessAcceptsCreditCards[i])+','+\
                      str(GoodForDancing[i])+','+str(BusinessAcceptsBitcoin[i])+','+str(DriveThru[i])+','+str(HasTV[i])+','+\
                      str(round(norm_BusinessParking[0][i],6))+','+str(round(norm_GoodForMeal[0][i],6))+','+\
                      str(round(norm_BestNights[0][i],6))+','+str(round(norm_HairSpecializesIn[0][i],6))+','+\
                      str(round(norm_Music[0][i],6))+','+str(round(norm_DietaryRestrictions[0][i],6))+','+\
                      str(round(norm_Ambience[0][i],6))+','+\
                      str(GoodForMeal_dessert[i])+','+str(GoodForMeal_latenight[i])+','+str(GoodForMeal_lunch[i])+','+\
                      str(GoodForMeal_dinner[i])+','+str(GoodForMeal_brunch[i])+','+str(GoodForMeal_breakfast[i])+','+\
                      str(BestNights_monday[i])+','+str(BestNights_tuesday[i])+','+str(BestNights_friday[i])+','+\
                      str(BestNights_wednesday[i])+','+str(BestNights_thursday[i])+','+str(BestNights_sunday[i])+','+str(BestNights_saturday[i])+','+\
                      str(BusinessParking_garage[i])+','+str(BusinessParking_street[i])+','+str(BusinessParking_validated[i])+','+\
                      str(BusinessParking_lot[i])+','+str(BusinessParking_valet[i])+','+\
                      str(HairSpecializesIn_straightperms[i])+','+str(HairSpecializesIn_coloring[i])+','+str(HairSpecializesIn_extensions[i])+','+\
                      str(HairSpecializesIn_africanamerican[i])+','+str(HairSpecializesIn_curly[i])+','+\
                      str(HairSpecializesIn_kids[i])+','+str(HairSpecializesIn_perms[i])+','+str(HairSpecializesIn_asian[i])+','+\
                      str(Music_dj[i])+','+str(Music_background_music[i])+','+str(Music_no_music[i])+','+\
                      str(Music_jukebox[i])+','+str(Music_live[i])+','+str(Music_video[i])+','+\
                      str(Music_karaoke[i])+','+str(DietaryRestrictions_dairy_free[i])+','+str(DietaryRestrictions_gluten_free[i])+','+\
                      str(DietaryRestrictions_vegan[i])+','+str(DietaryRestrictions_kosher[i])+','+\
                      str(DietaryRestrictions_halal[i])+','+str(DietaryRestrictions_soy_free[i])+','+\
                      str(DietaryRestrictions_vegetarian[i])+','+\
                      str(Ambience_touristy[i])+','+str(Ambience_hipster[i])+','+str(Ambience_romantic[i])+','+\
                      str(Ambience_divey[i])+','+str(Ambience_intimate[i])+','+str(Ambience_trendy[i])+','+\
                      str(Ambience_upscale[i])+','+str(Ambience_classy[i])+','+str(Ambience_casual[i])+'\n'
        f_w.write(total_feature)

    f_w.close()
################CheckIn
def CheckIn_Preprocess():
    f = open(Home_Address+'track2/yelp/yelp_academic_dataset_checkin.json','r')
    f_w = open(Home_Address+'track2/yelp/checkin.txt','w')

    business_id=[]
    date_count=[]
    counter=0

    for line in f:
        j_line = json.loads(line)
        business_id.append(j_line['business_id'])
        date_count.append(len(j_line['date'].split(',')))
        if counter%1000 ==0:
            print(counter)
        counter += 1
    f.close()
    norm_date_count= preprocessing.normalize([date_count])
    for i  in range(0,len(date_count)):
        total_feature=str(business_id[i])+','+str(round(norm_date_count[0][i],6))+'\n'
        f_w.write(total_feature)

    f_w.close()
################Review
def Review_Preprocess():
    f = open(Home_Address+'track2/yelp/yelp_academic_dataset_review.json','r')

    review_id=[]
    stars=[]
    review_useful=[]
    review_funny=[]
    review_cool=[]
    counter=0

    for line in f:
        j_line = json.loads(line)
        review_id.append(j_line['review_id'])
        review_useful.append(j_line['review_useful'])
        review_funny.append(j_line['review_funny'])
        review_cool.append(j_line['review_cool'])

        if counter%10000 ==0:
            print(counter)
        counter += 1
    f.close()

    norm_useful= preprocessing.normalize([review_useful])
    norm_funny= preprocessing.normalize([review_funny])
    norm_cool= preprocessing.normalize([review_cool])

    f = open(Home_Address+'track2/yelp/yelp_academic_dataset_review.json','r')
    f_w = open(Home_Address+'track2/yelp/review.json','w')
    counter=0
    for line in f:
        j_line = json.loads(line)
        j_line['review_useful']= round(norm_useful[0][counter],6)
        j_line['review_funny'] = round(norm_funny[0][counter], 6)
        j_line['review_cool'] = round(norm_cool[0][counter], 6)
        #j_line['text'] = "Nothing"
        f_w.write(json.dumps(j_line)+'\n')
        if counter%10000 ==0:
            print(counter)
        counter += 1

    f.close()
    f_w.close()
####################Split data
def Build_Train_Test_Val_Dataset():
    #review_id, stars, review_useful, review_funny, review_cool, user_id, business_id, business_id
    Home_Address='/media/fs_Linux_Files/'
    f = open(Home_Address+'track2/yelp/review.json','r')
    stars=[]
    remain=[]

    counter=0
    for line in f:
        j_line = json.loads(line)
        #line_s=line.strip().split(',')
        if float(j_line['stars'])==5:
            stars.append(line)
        else:
            remain.append(line)
        counter += 1
        if counter%100000==0:
            print(counter)
    f.close()
    d=random.SystemRandom()
    length=int(0.1*len(stars))
    test=d.choices(stars,k=length)
    set_test=set(test)
    set_stars =set(stars)
    stars_remain= set_stars - set_test
    test2=d.choices(list(stars_remain),k=length-len(set_test) )
    star_test=list(set(list(set(test2)) +  list(set_test)))

    stars_remain= list(set(stars) - set(star_test))
    validation=d.choices(stars_remain,k=length)
    set_validation=set(validation)
    set_stars =set(stars_remain)
    stars_remain= set_stars - set_validation
    validation2=d.choices(list(stars_remain),k=length-len(set_validation) )
    star_validation=list(set(list(set(validation2)) +  list(set_validation)))


    remain_stars= set(stars) - set(star_validation)
    remain_stars= list(remain_stars - set(star_test))

    d=random.SystemRandom()
    length=int(0.1*len(remain))
    test=d.choices(remain,k=length)
    set_test=set(test)
    set_remain =set(remain)
    stars_remain= set_remain - set_test
    test2=d.choices(list(stars_remain),k=length-len(set_test) )
    remain_test=list(set(list(set(test2)) +  list(set_test)))

    stars_remain= list(set(remain) - set(remain_test))
    validation=d.choices(stars_remain,k=length)
    set_validation=set(validation)
    set_stars =set(stars_remain)
    stars_remain= set_stars - set_validation
    validation2=d.choices(list(stars_remain),k=length-len(set_validation) )
    remain_validation=list(set(list(set(validation2)) +  list(set_validation)))


    remain_remain= set(remain) - set(remain_validation)
    remain_remain= list(remain_remain - set(remain_test))

    validation_data = list(remain_validation) + list(star_validation)
    test_data = list(remain_test) + list(star_test)
    train_data = list(remain_remain) + list(remain_stars)
    random.shuffle(validation_data)
    random.shuffle(test_data)
    random.shuffle(train_data)

    f_train = open(Home_Address+'track2/yelp/train.json','w')
    f_test = open(Home_Address+'track2/yelp/test.json','w')
    f_validation = open(Home_Address+'track2/yelp/validation.json','w')

    counter=0
    for line in train_data:
        f_train.write(line)
        counter += 1
        if counter%1000==0:
            print(counter)
    f_train.close()

    counter=0
    for line in test_data:
        f_test.write(line)
        counter += 1
        if counter%1000==0:
            print(counter)
    f_test.close()

    counter=0
    for line in validation_data:
        f_validation.write(line)
        counter += 1
        if counter%1000==0:
            print(counter)
    f_validation.close()
##########################Cluster Features
def build_Shadow_Inputs():
    from sklearn.cluster import KMeans, MiniBatchKMeans
    import pickle
    import pandas as pd
    import json
    from scipy.constants import hour
    from sklearn import preprocessing
    import math
    import numpy as np
    '''
        review_id[0],stars[1],review_useful[2],review_funny[3],review_cool[4],user_id[5],review_count[6],user_useful[7],
        user_funny[8],user_cool[9],elite[10],friends[11],
        fans[12],user_stars[13],compliment_hot[14],compliment_more[15],compliment_profile[16],compliment_cute[17],compliment_list[18],
        compliment_note[19],compliment_plain[20],compliment_cool[21],compliment_funny[22],compliment_writer[23],compliment_photos[24],
        business_id[25],latitude[26],longitude[27],business_stars[28],review_count[29],is_open[30],attributes[31],categories[32],hours[33],
        NoiseLevel[34],DogsAllowed[35],WheelchairAccessible[36],AgesAllowed[37],RestaurantsTableService[38],CoatCheck[39],GoodForKids[40],
        Open24Hours[41],RestaurantsDelivery[42],DietaryRestrictions[43],RestaurantsReservations[44],OutdoorSeating[45],BYOB[46],
        RestaurantsGoodForGroups[47],HappyHour[48],WiFi[49],BYOBCorkage[50],Caters[51],GoodForMeal[52],ByAppointmentOnly[53],
        RestaurantsTakeOut[54],RestaurantsCounterService[55],RestaurantsAttire[56],Alcohol[57],HairSpecializesIn[58],Corkage[59],
        AcceptsInsurance[60],Smoking[61],Ambience[62],RestaurantsPriceRange2[63],BestNights[64],BikeParking[65],BusinessAcceptsCreditCards[66],
        GoodForDancing[67],BusinessAcceptsBitcoin[68],BusinessParking[69],DriveThru[70],Music[71],HasTV[72],GoodForMeal_dessert[73],
        GoodForMeal_latenight[74],GoodForMeal_lunch[75],GoodForMeal_dinner[76],GoodForMeal_brunch[77],GoodForMeal_breakfast[78],
        BestNights_monday[79],BestNights_tuesday[80],BestNights_friday[81],BestNights_wednesday[82],BestNights_thursday[83],
        BestNights_sunday[84],BestNights_saturday[85],BusinessParking_garage[86],BusinessParking_street[87],BusinessParking_validated[88],
        BusinessParking_lot[89],BusinessParking_valet[90],HairSpecializesIn_straightperms[91],HairSpecializesIn_coloring[92],
        HairSpecializesIn_extensions[93],HairSpecializesIn_africanamerican[94],HairSpecializesIn_curly[95],HairSpecializesIn_kids[96],
        HairSpecializesIn_perms[97],HairSpecializesIn_asian[98],Music_dj[99],Music_background_music[100],Music_no_music[101],
        Music_jukebox[102],Music_live[103],Music_video[104],Music_karaoke[105],DietaryRestrictions_dairy_free[106],
        DietaryRestrictions_gluten_free[107],DietaryRestrictions_vegan[108],DietaryRestrictions_kosher[109],
        DietaryRestrictions_halal[110],DietaryRestrictions_soy_free[111],DietaryRestrictions_vegetarian[112],Ambience_touristy[113],
        Ambience_hipster[114],Ambience_romantic[115],Ambience_divey[116],Ambience_intimate[117],Ambience_trendy[118],Ambience_upscale[119],
        Ambience_classy[120],Ambience_casual[121],business_id[122],date_count[123]
        '''
    Home_Address='/media/fs_Linux_Files/'
    f_t = open(Home_Address+'track2/yelp/train.txt', "r")
    counter=0
    #review feature
    review_useful = []
    review_funny = []
    review_cool =[]
    #user feature
    user_review_count =[]
    user_useful =[]
    user_funny =[]
    user_cool =[]
    elite =[]
    friends =[]
    fans =[]
    user_stars =[]
    compliment_hot =[]
    compliment_more =[]
    compliment_profile =[]
    compliment_cute =[]
    compliment_list =[]
    compliment_note =[]
    compliment_plain =[]
    compliment_cool =[]
    compliment_funny =[]
    compliment_writer =[]
    compliment_photos =[]
    #business
    latitude = []
    longitude = []
    business_review_count = []
    business_stars= []
    attributes= []
    categories= []
    hours= []
    BusinessParking= []
    GoodForMeal= []
    BestNights= []
    HairSpecializesIn= []
    Music= []
    DietaryRestrictions= []
    Ambience= []
    #elite2,business_stars2,attributes2,categories2,hours2,
    # BusinessParking2,GoodForMeal2,BestNights2,HairSpecializesIn2
    #Music2,DietaryRestrictions2,Ambience2
    for line in f_t:
        line_sp = line.strip().split(',')
        review_useful.append(float(line_sp[2]))
        review_funny.append(float(line_sp[3]))
        review_cool.append(float(line_sp[4]))
        #user
        user_review_count.append(float(line_sp[6]))
        user_useful.append(float(line_sp[7]))
        user_funny.append(float(line_sp[8]))
        user_cool.append(float(line_sp[9]))
        elite.append(float(line_sp[10]))
        friends.append(float(line_sp[11]))
        fans.append(float(line_sp[12]))
        user_stars.append(float(line_sp[13]))
        compliment_hot.append(float(line_sp[14]))
        compliment_more.append(float(line_sp[15]))
        compliment_profile.append(float(line_sp[16]))
        compliment_cute.append(float(line_sp[17]))
        compliment_list.append(float(line_sp[18]))
        compliment_note.append(float(line_sp[19]))
        compliment_plain.append(float(line_sp[20]))
        compliment_cool.append(float(line_sp[21]))
        compliment_funny.append(float(line_sp[22]))
        compliment_writer.append(float(line_sp[23]))
        compliment_photos.append(float(line_sp[24]))
        # business
        latitude.append(float(line_sp[26]))
        longitude.append(float(line_sp[27]))
        business_stars.append(float(line_sp[28]))
        business_review_count.append(float(line_sp[29]))
        attributes.append(float(line_sp[31]))
        categories.append(float(line_sp[32]))
        hours.append(float(line_sp[33]))

        BusinessParking.append(float(line_sp[66]))
        GoodForMeal.append(float(line_sp[67]))
        BestNights.append(float(line_sp[68]))
        HairSpecializesIn.append(float(line_sp[69]))
        Music.append(float(line_sp[70]))
        DietaryRestrictions.append(float(line_sp[71]))
        Ambience.append(float(line_sp[72]))

        counter = counter + 1
        if counter % 10000== 0:
            print(str(counter))
            review_useful = list(set(review_useful))
            review_funny = list(set(review_funny))
            review_cool = list(set(review_cool))
            # user
            user_review_count= list(set(user_review_count))
            user_useful= list(set(user_useful))
            user_funny= list(set(user_funny))
            user_cool= list(set(user_cool))
            elite= list(set(elite))
            friends= list(set(friends))
            fans= list(set(fans))
            user_stars= list(set(user_stars))
            compliment_hot= list(set(compliment_hot))
            compliment_more= list(set(compliment_more))
            compliment_profile= list(set(compliment_profile))
            compliment_cute= list(set(compliment_cute))
            compliment_list= list(set(compliment_list))
            compliment_note= list(set(compliment_note))
            compliment_plain= list(set(compliment_plain))
            compliment_cool= list(set(compliment_cool))
            compliment_funny= list(set(compliment_funny))
            compliment_writer= list(set(compliment_writer))
            compliment_photos= list(set(compliment_photos))
            # business
            latitude= list(set(latitude))
            longitude= list(set(longitude))
            business_stars= list(set(business_stars))
            business_review_count= list(set(business_review_count))
            attributes= list(set(attributes))
            categories= list(set(categories))
            hours= list(set(hours))

            BusinessParking= list(set(BusinessParking))
            GoodForMeal= list(set(GoodForMeal))
            BestNights= list(set(BestNights))
            HairSpecializesIn= list(set(HairSpecializesIn))
            Music= list(set(Music))
            DietaryRestrictions= list(set(DietaryRestrictions))
            Ambience= list(set(Ambience))
    f_t.close()

    review_useful = list(set(review_useful))
    review_funny = list(set(review_funny))
    review_cool = list(set(review_cool))
    user_review_count= list(set(user_review_count))
    user_useful= list(set(user_useful))
    user_funny= list(set(user_funny))
    user_cool= list(set(user_cool))
    elite= list(set(elite))
    friends= list(set(friends))
    fans= list(set(fans))
    user_stars= list(set(user_stars))
    compliment_hot= list(set(compliment_hot))
    compliment_more= list(set(compliment_more))
    compliment_profile= list(set(compliment_profile))
    compliment_cute= list(set(compliment_cute))
    compliment_list= list(set(compliment_list))
    compliment_note= list(set(compliment_note))
    compliment_plain= list(set(compliment_plain))
    compliment_cool= list(set(compliment_cool))
    compliment_funny= list(set(compliment_funny))
    compliment_writer= list(set(compliment_writer))
    compliment_photos= list(set(compliment_photos))
    # business
    latitude= list(set(latitude))
    longitude= list(set(longitude))
    business_stars= list(set(business_stars))
    business_review_count= list(set(business_review_count))
    attributes= list(set(attributes))
    categories= list(set(categories))
    hours= list(set(hours))

    BusinessParking= list(set(BusinessParking))
    GoodForMeal= list(set(GoodForMeal))
    BestNights= list(set(BestNights))
    HairSpecializesIn= list(set(HairSpecializesIn))
    Music= list(set(Music))
    DietaryRestrictions= list(set(DietaryRestrictions))
    Ambience= list(set(Ambience))

    review_useful2=[]
    review_useful2 = [[x] for x in review_useful]
    review_useful2.sort()

    review_funny2=[]
    review_funny2 = [[x] for x in review_funny]
    review_funny2.sort()

    review_cool2=[]
    review_cool2 = [[x] for x in review_cool]
    review_cool2.sort()

    user_review_count2 = []
    user_review_count2 = [[x] for x in user_review_count]
    user_review_count2.sort()

    user_useful2 = []
    user_useful2 = [[x] for x in user_useful]
    user_useful2.sort()

    user_funny2 = []
    user_funny2 = [[x] for x in user_funny]
    user_funny2.sort()

    user_cool2 = []
    user_cool2 = [[x] for x in user_cool]
    user_cool2.sort()

    elite2 = []
    elite2 = [[x] for x in elite]
    elite2.sort()

    friends2 = []
    friends2 = [[x] for x in friends]
    friends2.sort()

    fans2 = []
    fans2 = [[x] for x in fans]
    fans2.sort()

    user_stars2 = []
    user_stars2 = [[x] for x in user_stars]
    user_stars2.sort()

    compliment_hot2 = []
    compliment_hot2 = [[x] for x in compliment_hot]
    compliment_hot2.sort()

    compliment_more2 = []
    compliment_more2 = [[x] for x in compliment_more]
    compliment_more2.sort()

    compliment_profile2 = []
    compliment_profile2 = [[x] for x in compliment_profile]
    compliment_profile2.sort()

    compliment_cute2 = []
    compliment_cute2 = [[x] for x in compliment_cute]
    compliment_cute2.sort()

    compliment_list2 = []
    compliment_list2 = [[x] for x in compliment_list]
    compliment_list2.sort()

    compliment_note2 = []
    compliment_note2 = [[x] for x in compliment_note]
    compliment_note2.sort()

    compliment_plain2 = []
    compliment_plain2 = [[x] for x in compliment_plain]
    compliment_plain2.sort()

    compliment_cool2 = []
    compliment_cool2 = [[x] for x in compliment_cool]
    compliment_cool2.sort()

    compliment_funny2 = []
    compliment_funny2 = [[x] for x in compliment_funny]
    compliment_funny2.sort()

    compliment_writer2 = []
    compliment_writer2 = [[x] for x in compliment_writer]
    compliment_writer2.sort()

    compliment_photos2 = []
    compliment_photos2 = [[x] for x in compliment_photos]
    compliment_photos2.sort()

    latitude2 = []
    latitude2 = [[x] for x in latitude]
    latitude2.sort()

    longitude2 = []
    longitude2 = [[x] for x in longitude]
    longitude2.sort()

    business_review_count2 = []
    business_review_count2 = [[x] for x in business_review_count]
    business_review_count2.sort()

    business_stars2 = []
    business_stars2 = [[x] for x in business_stars]
    business_stars2.sort()

    attributes2 = []
    attributes2 = [[x] for x in attributes]
    attributes2.sort()

    categories2 = []
    categories2 = [[x] for x in categories]
    categories2.sort()

    hours2 = []
    hours2 = [[x] for x in hours]
    hours2.sort()

    BusinessParking2 = []
    BusinessParking2 = [[x] for x in BusinessParking]
    BusinessParking2.sort()

    GoodForMeal2 = []
    GoodForMeal2 = [[x] for x in GoodForMeal]
    GoodForMeal2.sort()

    BestNights2 = []
    BestNights2 = [[x] for x in BestNights]
    BestNights2.sort()

    HairSpecializesIn2 = []
    HairSpecializesIn2 = [[x] for x in HairSpecializesIn]
    HairSpecializesIn2.sort()

    Music2 = []
    Music2 = [[x] for x in Music]
    Music2.sort()

    DietaryRestrictions2 = []
    DietaryRestrictions2 = [[x] for x in DietaryRestrictions]
    DietaryRestrictions2.sort()

    Ambience2 = []
    Ambience2 = [[x] for x in Ambience]
    Ambience2.sort()

    kmeans_review_useful = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_review_useful.fit(review_useful2)
    pickle.dump(kmeans_review_useful, open(Home_Address + 'track2/yelp/kmeans_review_useful.pkl', 'wb'))
    f_w = open(Home_Address+'track2/yelp/cluster_member_review_useful.txt','w')
    list_label = kmeans_review_useful.labels_
    for i in range(0, len(review_useful2)):
        f_w.write(str(review_useful2[i][0]) + ',' + str(list_label[i]) + '\n')
    f_w.close()
    kmeans_review_funny = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_review_funny.fit(review_funny2)
    pickle.dump(kmeans_review_funny, open(Home_Address + 'track2/yelp/kmeans_review_funny.pkl', 'wb'))
    f_w = open(Home_Address+'track2/yelp/cluster_member_review_funny.txt','w')
    list_label = kmeans_review_funny.labels_
    for i in range(0, len(review_funny2)):
        f_w.write(str(review_funny2[i][0]) + ',' + str(list_label[i]) + '\n')
    f_w.close()
    kmeans_review_cool = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_review_cool.fit(review_cool2)
    pickle.dump(kmeans_review_cool, open(Home_Address + 'track2/yelp/kmeans_review_cool.pkl', 'wb'))
    f_w = open(Home_Address+'track2/yelp/cluster_member_review_cool.txt','w')
    list_label = kmeans_review_cool.labels_
    for i in range(0, len(review_cool2)):
        f_w.write(str(review_cool2[i][0]) + ',' + str(list_label[i]) + '\n')
    f_w.close()
    kmeans_user_review_count = KMeans(init="k-means++", n_clusters=200, n_init=10)
    kmeans_user_review_count.fit(user_review_count2)
    pickle.dump(kmeans_user_review_count, open(Home_Address + "track2/yelp/kmeans_user_review_count.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_review_count.txt","w")
    list_label = kmeans_user_review_count.labels_
    for i in range(0, len(user_review_count2)):
        f_w.write(str(user_review_count2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_user_useful = KMeans(init="k-means++", n_clusters=500, n_init=10)
    kmeans_user_useful.fit(user_useful2)
    pickle.dump(kmeans_user_useful, open(Home_Address + "track2/yelp/kmeans_user_useful.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_useful.txt","w")
    list_label = kmeans_user_useful.labels_
    for i in range(0, len(user_useful2)):
        f_w.write(str(user_useful2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_user_funny = KMeans(init="k-means++", n_clusters=300, n_init=10)
    kmeans_user_funny.fit(user_funny2)
    pickle.dump(kmeans_user_funny, open(Home_Address + "track2/yelp/kmeans_user_funny.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_funny.txt","w")
    list_label = kmeans_user_funny.labels_
    for i in range(0, len(user_funny2)):
        f_w.write(str(user_funny2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_user_cool = KMeans(init="k-means++", n_clusters=400, n_init=10)
    kmeans_user_cool.fit(user_cool2)
    pickle.dump(kmeans_user_cool, open(Home_Address + "track2/yelp/kmeans_user_cool.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_cool.txt","w")
    list_label = kmeans_user_cool.labels_
    for i in range(0, len(user_cool2)):
        f_w.write(str(user_cool2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_friends = KMeans(init="k-means++", n_clusters=250, n_init=10)
    kmeans_friends.fit(friends2)
    pickle.dump(kmeans_friends, open(Home_Address + "track2/yelp/kmeans_friends.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_friends.txt","w")
    list_label = kmeans_friends.labels_
    for i in range(0, len(friends2)):
        f_w.write(str(friends2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_fans = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_fans.fit(fans2)
    pickle.dump(kmeans_fans, open(Home_Address + "track2/yelp/kmeans_fans.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_fans.txt","w")
    list_label = kmeans_fans.labels_
    for i in range(0, len(fans2)):
        f_w.write(str(fans2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_user_stars = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_user_stars.fit(user_stars2)
    pickle.dump(kmeans_user_stars, open(Home_Address + "track2/yelp/kmeans_user_stars.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_stars.txt","w")
    list_label = kmeans_user_stars.labels_
    for i in range(0, len(user_stars2)):
        f_w.write(str(user_stars2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_hot = KMeans(init="k-means++", n_clusters=100, n_init=10)
    kmeans_compliment_hot.fit(compliment_hot2)
    pickle.dump(kmeans_compliment_hot, open(Home_Address + "track2/yelp/kmeans_compliment_hot.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_hot.txt","w")
    list_label = kmeans_compliment_hot.labels_
    for i in range(0, len(compliment_hot2)):
        f_w.write(str(compliment_hot2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_more = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_compliment_more.fit(compliment_more2)
    pickle.dump(kmeans_compliment_more, open(Home_Address + "track2/yelp/kmeans_compliment_more.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_more.txt","w")
    list_label = kmeans_compliment_more.labels_
    for i in range(0, len(compliment_more2)):
        f_w.write(str(compliment_more2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_profile = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_compliment_profile.fit(compliment_profile2)
    pickle.dump(kmeans_compliment_profile, open(Home_Address + "track2/yelp/kmeans_compliment_profile.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_profile.txt","w")
    list_label = kmeans_compliment_profile.labels_
    for i in range(0, len(compliment_profile2)):
        f_w.write(str(compliment_profile2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_cute = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_compliment_cute.fit(compliment_cute2)
    pickle.dump(kmeans_compliment_cute, open(Home_Address + "track2/yelp/kmeans_compliment_cute.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_cute.txt","w")
    list_label = kmeans_compliment_cute.labels_
    for i in range(0, len(compliment_cute2)):
        f_w.write(str(compliment_cute2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_list = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_compliment_list.fit(compliment_list2)
    pickle.dump(kmeans_compliment_list, open(Home_Address + "track2/yelp/kmeans_compliment_list.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_list.txt","w")
    list_label = kmeans_compliment_list.labels_
    for i in range(0, len(compliment_list2)):
        f_w.write(str(compliment_list2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_note = KMeans(init="k-means++", n_clusters=100, n_init=10)
    kmeans_compliment_note.fit(compliment_note2)
    pickle.dump(kmeans_compliment_note, open(Home_Address + "track2/yelp/kmeans_compliment_note.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_note.txt","w")
    list_label = kmeans_compliment_note.labels_
    for i in range(0, len(compliment_note2)):
        f_w.write(str(compliment_note2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_plain = KMeans(init="k-means++", n_clusters=150, n_init=10)
    kmeans_compliment_plain.fit(compliment_plain2)
    pickle.dump(kmeans_compliment_plain, open(Home_Address + "track2/yelp/kmeans_compliment_plain.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_plain.txt","w")
    list_label = kmeans_compliment_plain.labels_
    for i in range(0, len(compliment_plain2)):
        f_w.write(str(compliment_plain2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_cool = KMeans(init="k-means++", n_clusters=150, n_init=10)
    kmeans_compliment_cool.fit(compliment_cool2)
    pickle.dump(kmeans_compliment_cool, open(Home_Address + "track2/yelp/kmeans_compliment_cool.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_cool.txt","w")
    list_label = kmeans_compliment_cool.labels_
    for i in range(0, len(compliment_cool2)):
        f_w.write(str(compliment_cool2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_funny = KMeans(init="k-means++", n_clusters=150, n_init=10)
    kmeans_compliment_funny.fit(compliment_funny2)
    pickle.dump(kmeans_compliment_funny, open(Home_Address + "track2/yelp/kmeans_compliment_funny.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_funny.txt","w")
    list_label = kmeans_compliment_funny.labels_
    for i in range(0, len(compliment_funny2)):
        f_w.write(str(compliment_funny2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_writer = KMeans(init="k-means++", n_clusters=100, n_init=10)
    kmeans_compliment_writer.fit(compliment_writer2)
    pickle.dump(kmeans_compliment_writer, open(Home_Address + "track2/yelp/kmeans_compliment_writer.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_writer.txt","w")
    list_label = kmeans_compliment_writer.labels_
    for i in range(0, len(compliment_writer2)):
        f_w.write(str(compliment_writer2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_compliment_photos = KMeans(init="k-means++", n_clusters=100, n_init=10)
    kmeans_compliment_photos.fit(compliment_photos2)
    pickle.dump(kmeans_compliment_photos, open(Home_Address + "track2/yelp/kmeans_compliment_photos.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_photos.txt","w")
    list_label = kmeans_compliment_photos.labels_
    for i in range(0, len(compliment_photos2)):
        f_w.write(str(compliment_photos2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_latitude = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_latitude.fit(latitude2)
    pickle.dump(kmeans_latitude, open(Home_Address + "track2/yelp/kmeans_latitude.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_latitude.txt","w")
    list_label = kmeans_latitude.labels_
    for i in range(0, len(latitude2)):
        f_w.write(str(latitude2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_longitude = KMeans(init="k-means++", n_clusters=50, n_init=10)
    kmeans_longitude.fit(longitude2)
    pickle.dump(kmeans_longitude, open(Home_Address + "track2/yelp/kmeans_longitude.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_longitude.txt","w")
    list_label = kmeans_longitude.labels_
    for i in range(0, len(longitude2)):
        f_w.write(str(longitude2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()
    kmeans_business_review_count = KMeans(init="k-means++", n_clusters=100, n_init=10)
    kmeans_business_review_count.fit(business_review_count2)
    pickle.dump(kmeans_business_review_count, open(Home_Address + "track2/yelp/kmeans_business_review_count.pkl", "wb"))
    f_w = open(Home_Address+"track2/yelp/cluster_member_business_review_count.txt","w")
    list_label = kmeans_business_review_count.labels_
    for i in range(0, len(business_review_count2)):
        f_w.write(str(business_review_count2[i][0]) + "," + str(list_label[i]) + "\n")
    f_w.close()

    review_useful2 = [x[0] for x in review_useful2]
    df_review_useful =pd.DataFrame({'value':review_useful2, 'label':kmeans_review_useful.labels_})
    df_review_useful= df_review_useful.groupby(['label']).mean()
    f_w =open(Home_Address+'track2/yelp/cluster_review_useful_rate.txt','w')
    for row in df_review_useful.iterrows():
        f_w.write(str(row[0])+','+str(row[1]['value'])+'\n')
    f_w.close()
    review_funny2 = [x[0] for x in review_funny2]
    df_review_funny =pd.DataFrame({'value':review_funny2, 'label':kmeans_review_funny.labels_})
    df_review_funny= df_review_funny.groupby(['label']).mean()
    f_w =open(Home_Address+'track2/yelp/cluster_review_funny_rate.txt','w')
    for row in df_review_funny.iterrows():
        f_w.write(str(row[0])+','+str(row[1]['value'])+'\n')
    f_w.close()
    review_cool2 = [x[0] for x in review_cool2]
    df_review_cool =pd.DataFrame({'value':review_cool2, 'label':kmeans_review_cool.labels_})
    df_review_cool= df_review_cool.groupby(['label']).mean()
    f_w =open(Home_Address+'track2/yelp/cluster_review_cool_rate.txt','w')
    for row in df_review_cool.iterrows():
        f_w.write(str(row[0])+','+str(row[1]['value'])+'\n')
    f_w.close()
    user_review_count2 = [x[0] for x in user_review_count2]
    df_user_review_count =pd.DataFrame({"value":user_review_count2, "label":kmeans_user_review_count.labels_})
    df_user_review_count= df_user_review_count.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_user_review_count_rate.txt","w")
    for row in df_user_review_count.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    user_useful2 = [x[0] for x in user_useful2]
    df_user_useful =pd.DataFrame({"value":user_useful2, "label":kmeans_user_useful.labels_})
    df_user_useful= df_user_useful.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_user_useful_rate.txt","w")
    for row in df_user_useful.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    user_funny2 = [x[0] for x in user_funny2]
    df_user_funny =pd.DataFrame({"value":user_funny2, "label":kmeans_user_funny.labels_})
    df_user_funny= df_user_funny.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_user_funny_rate.txt","w")
    for row in df_user_funny.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    user_cool2 = [x[0] for x in user_cool2]
    df_user_cool =pd.DataFrame({"value":user_cool2, "label":kmeans_user_cool.labels_})
    df_user_cool= df_user_cool.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_user_cool_rate.txt","w")
    for row in df_user_cool.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    friends2 = [x[0] for x in friends2]
    df_friends =pd.DataFrame({"value":friends2, "label":kmeans_friends.labels_})
    df_friends= df_friends.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_friends_rate.txt","w")
    for row in df_friends.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    fans2 = [x[0] for x in fans2]
    df_fans =pd.DataFrame({"value":fans2, "label":kmeans_fans.labels_})
    df_fans= df_fans.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_fans_rate.txt","w")
    for row in df_fans.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    user_stars2 = [x[0] for x in user_stars2]
    df_user_stars =pd.DataFrame({"value":user_stars2, "label":kmeans_user_stars.labels_})
    df_user_stars= df_user_stars.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_user_stars_rate.txt","w")
    for row in df_user_stars.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_hot2 = [x[0] for x in compliment_hot2]
    df_compliment_hot =pd.DataFrame({"value":compliment_hot2, "label":kmeans_compliment_hot.labels_})
    df_compliment_hot= df_compliment_hot.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_hot_rate.txt","w")
    for row in df_compliment_hot.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_more2 = [x[0] for x in compliment_more2]
    df_compliment_more =pd.DataFrame({"value":compliment_more2, "label":kmeans_compliment_more.labels_})
    df_compliment_more= df_compliment_more.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_more_rate.txt","w")
    for row in df_compliment_more.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_profile2 = [x[0] for x in compliment_profile2]
    df_compliment_profile =pd.DataFrame({"value":compliment_profile2, "label":kmeans_compliment_profile.labels_})
    df_compliment_profile= df_compliment_profile.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_profile_rate.txt","w")
    for row in df_compliment_profile.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_cute2 = [x[0] for x in compliment_cute2]
    df_compliment_cute =pd.DataFrame({"value":compliment_cute2, "label":kmeans_compliment_cute.labels_})
    df_compliment_cute= df_compliment_cute.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_cute_rate.txt","w")
    for row in df_compliment_cute.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_list2 = [x[0] for x in compliment_list2]
    df_compliment_list =pd.DataFrame({"value":compliment_list2, "label":kmeans_compliment_list.labels_})
    df_compliment_list= df_compliment_list.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_list_rate.txt","w")
    for row in df_compliment_list.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_note2 = [x[0] for x in compliment_note2]
    df_compliment_note =pd.DataFrame({"value":compliment_note2, "label":kmeans_compliment_note.labels_})
    df_compliment_note= df_compliment_note.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_note_rate.txt","w")
    for row in df_compliment_note.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_plain2 = [x[0] for x in compliment_plain2]
    df_compliment_plain =pd.DataFrame({"value":compliment_plain2, "label":kmeans_compliment_plain.labels_})
    df_compliment_plain= df_compliment_plain.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_plain_rate.txt","w")
    for row in df_compliment_plain.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_cool2 = [x[0] for x in compliment_cool2]
    df_compliment_cool =pd.DataFrame({"value":compliment_cool2, "label":kmeans_compliment_cool.labels_})
    df_compliment_cool= df_compliment_cool.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_cool_rate.txt","w")
    for row in df_compliment_cool.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_funny2 = [x[0] for x in compliment_funny2]
    df_compliment_funny =pd.DataFrame({"value":compliment_funny2, "label":kmeans_compliment_funny.labels_})
    df_compliment_funny= df_compliment_funny.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_funny_rate.txt","w")
    for row in df_compliment_funny.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_writer2 = [x[0] for x in compliment_writer2]
    df_compliment_writer =pd.DataFrame({"value":compliment_writer2, "label":kmeans_compliment_writer.labels_})
    df_compliment_writer= df_compliment_writer.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_writer_rate.txt","w")
    for row in df_compliment_writer.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    compliment_photos2 = [x[0] for x in compliment_photos2]
    df_compliment_photos =pd.DataFrame({"value":compliment_photos2, "label":kmeans_compliment_photos.labels_})
    df_compliment_photos= df_compliment_photos.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_compliment_photos_rate.txt","w")
    for row in df_compliment_photos.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    latitude2 = [x[0] for x in latitude2]
    df_latitude =pd.DataFrame({"value":latitude2, "label":kmeans_latitude.labels_})
    df_latitude= df_latitude.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_latitude_rate.txt","w")
    for row in df_latitude.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    longitude2 = [x[0] for x in longitude2]
    df_longitude =pd.DataFrame({"value":longitude2, "label":kmeans_longitude.labels_})
    df_longitude= df_longitude.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_longitude_rate.txt","w")
    for row in df_longitude.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()
    business_review_count2 = [x[0] for x in business_review_count2]
    df_business_review_count =pd.DataFrame({"value":business_review_count2, "label":kmeans_business_review_count.labels_})
    df_business_review_count= df_business_review_count.groupby(["label"]).mean()
    f_w =open(Home_Address+"track2/yelp/cluster_business_review_count_rate.txt","w")
    for row in df_business_review_count.iterrows():
        f_w.write(str(row[0])+","+str(round(row[1]["value"],10))+"\n")
    f_w.close()

    pickle.dump(kmeans_review_useful, open(Home_Address + 'track2/yelp/kmeans_review_useful.pkl', 'wb'))
    pickle.dump(kmeans_review_funny, open(Home_Address + 'track2/yelp/kmeans_review_funny.pkl', 'wb'))
    pickle.dump(kmeans_review_cool, open(Home_Address + 'track2/yelp/kmeans_review_cool.pkl', 'wb'))
    pickle.dump(kmeans_user_review_count, open(Home_Address + "track2/yelp/kmeans_user_review_count.pkl", "wb"))
    pickle.dump(kmeans_user_useful, open(Home_Address + "track2/yelp/kmeans_user_useful.pkl", "wb"))
    pickle.dump(kmeans_user_funny, open(Home_Address + "track2/yelp/kmeans_user_funny.pkl", "wb"))
    pickle.dump(kmeans_user_cool, open(Home_Address + "track2/yelp/kmeans_user_cool.pkl", "wb"))
    pickle.dump(kmeans_friends, open(Home_Address + "track2/yelp/kmeans_friends.pkl", "wb"))
    pickle.dump(kmeans_fans, open(Home_Address + "track2/yelp/kmeans_fans.pkl", "wb"))
    pickle.dump(kmeans_user_stars, open(Home_Address + "track2/yelp/kmeans_user_stars.pkl", "wb"))
    pickle.dump(kmeans_compliment_hot, open(Home_Address + "track2/yelp/kmeans_compliment_hot.pkl", "wb"))
    pickle.dump(kmeans_compliment_more, open(Home_Address + "track2/yelp/kmeans_compliment_more.pkl", "wb"))
    pickle.dump(kmeans_compliment_profile, open(Home_Address + "track2/yelp/kmeans_compliment_profile.pkl", "wb"))
    pickle.dump(kmeans_compliment_cute, open(Home_Address + "track2/yelp/kmeans_compliment_cute.pkl", "wb"))
    pickle.dump(kmeans_compliment_list, open(Home_Address + "track2/yelp/kmeans_compliment_list.pkl", "wb"))
    pickle.dump(kmeans_compliment_note, open(Home_Address + "track2/yelp/kmeans_compliment_note.pkl", "wb"))
    pickle.dump(kmeans_compliment_plain, open(Home_Address + "track2/yelp/kmeans_compliment_plain.pkl", "wb"))
    pickle.dump(kmeans_compliment_cool, open(Home_Address + "track2/yelp/kmeans_compliment_cool.pkl", "wb"))
    pickle.dump(kmeans_compliment_funny, open(Home_Address + "track2/yelp/kmeans_compliment_funny.pkl", "wb"))
    pickle.dump(kmeans_compliment_writer, open(Home_Address + "track2/yelp/kmeans_compliment_writer.pkl", "wb"))
    pickle.dump(kmeans_compliment_photos, open(Home_Address + "track2/yelp/kmeans_compliment_photos.pkl", "wb"))
    pickle.dump(kmeans_latitude, open(Home_Address + "track2/yelp/kmeans_latitude.pkl", "wb"))
    pickle.dump(kmeans_longitude, open(Home_Address + "track2/yelp/kmeans_longitude.pkl", "wb"))
    pickle.dump(kmeans_business_review_count, open(Home_Address + "track2/yelp/kmeans_business_review_count.pkl", "wb"))

    f = open(Home_Address+'track2/yelp/cluster_member_review_useful.txt', "r")
    review_useful_list=[]
    for line in f:
        line=line.strip()
        review_useful_list.append(line)
    f.close()
    review_useful_list = list(set(review_useful_list))
    f = open(Home_Address+'track2/yelp/cluster_member_review_funny.txt', "r")
    review_funny_list=[]
    for line in f:
        line=line.strip()
        review_funny_list.append(line)
    f.close()
    review_funny_list = list(set(review_funny_list))
    f = open(Home_Address+'track2/yelp/cluster_member_review_cool.txt', "r")
    review_cool_list =[]
    for line in f:
        line=line.strip()
        review_cool_list.append(line)
    f.close()
    review_cool_list = list(set(review_cool_list))
    f = open(Home_Address+"track2/yelp/cluster_member_user_review_count.txt", "r")
    user_review_count_list=[]
    for line in f:
        line=line.strip()
        user_review_count_list.append(line)
    f.close()
    user_review_count_list = list(set(user_review_count_list))
    f = open(Home_Address+"track2/yelp/cluster_member_user_useful.txt", "r")
    user_useful_list=[]
    for line in f:
        line=line.strip()
        user_useful_list.append(line)
    f.close()
    user_useful_list = list(set(user_useful_list))
    f = open(Home_Address+"track2/yelp/cluster_member_user_funny.txt", "r")
    user_funny_list=[]
    for line in f:
        line=line.strip()
        user_funny_list.append(line)
    f.close()
    user_funny_list = list(set(user_funny_list))
    f = open(Home_Address+"track2/yelp/cluster_member_user_cool.txt", "r")
    user_cool_list=[]
    for line in f:
        line=line.strip()
        user_cool_list.append(line)
    f.close()
    user_cool_list = list(set(user_cool_list))
    f = open(Home_Address+"track2/yelp/cluster_member_friends.txt", "r")
    friends_list=[]
    for line in f:
        line=line.strip()
        friends_list.append(line)
    f.close()
    friends_list = list(set(friends_list))
    f = open(Home_Address+"track2/yelp/cluster_member_fans.txt", "r")
    fans_list=[]
    for line in f:
        line=line.strip()
        fans_list.append(line)
    f.close()
    fans_list = list(set(fans_list))
    f = open(Home_Address+"track2/yelp/cluster_member_user_stars.txt", "r")
    user_stars_list=[]
    for line in f:
        line=line.strip()
        user_stars_list.append(line)
    f.close()
    user_stars_list = list(set(user_stars_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_hot.txt", "r")
    compliment_hot_list=[]
    for line in f:
        line=line.strip()
        compliment_hot_list.append(line)
    f.close()
    compliment_hot_list = list(set(compliment_hot_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_more.txt", "r")
    compliment_more_list=[]
    for line in f:
        line=line.strip()
        compliment_more_list.append(line)
    f.close()
    compliment_more_list = list(set(compliment_more_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_profile.txt", "r")
    compliment_profile_list=[]
    for line in f:
        line=line.strip()
        compliment_profile_list.append(line)
    f.close()
    compliment_profile_list = list(set(compliment_profile_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_cute.txt", "r")
    compliment_cute_list=[]
    for line in f:
        line=line.strip()
        compliment_cute_list.append(line)
    f.close()
    compliment_cute_list = list(set(compliment_cute_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_list.txt", "r")
    compliment_list_list=[]
    for line in f:
        line=line.strip()
        compliment_list_list.append(line)
    f.close()
    compliment_list_list = list(set(compliment_list_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_note.txt", "r")
    compliment_note_list=[]
    for line in f:
        line=line.strip()
        compliment_note_list.append(line)
    f.close()
    compliment_note_list = list(set(compliment_note_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_plain.txt", "r")
    compliment_plain_list=[]
    for line in f:
        line=line.strip()
        compliment_plain_list.append(line)
    f.close()
    compliment_plain_list = list(set(compliment_plain_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_cool.txt", "r")
    compliment_cool_list=[]
    for line in f:
        line=line.strip()
        compliment_cool_list.append(line)
    f.close()
    compliment_cool_list = list(set(compliment_cool_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_funny.txt", "r")
    compliment_funny_list=[]
    for line in f:
        line=line.strip()
        compliment_funny_list.append(line)
    f.close()
    compliment_funny_list = list(set(compliment_funny_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_writer.txt", "r")
    compliment_writer_list=[]
    for line in f:
        line=line.strip()
        compliment_writer_list.append(line)
    f.close()
    compliment_writer_list = list(set(compliment_writer_list))
    f = open(Home_Address+"track2/yelp/cluster_member_compliment_photos.txt", "r")
    compliment_photos_list=[]
    for line in f:
        line=line.strip()
        compliment_photos_list.append(line)
    f.close()
    compliment_photos_list = list(set(compliment_photos_list))
    f = open(Home_Address+"track2/yelp/cluster_member_latitude.txt", "r")
    latitude_list=[]
    for line in f:
        line=line.strip()
        latitude_list.append(line)
    f.close()
    latitude_list = list(set(latitude_list))
    f = open(Home_Address+"track2/yelp/cluster_member_longitude.txt", "r")
    longitude_list=[]
    for line in f:
        line=line.strip()
        longitude_list.append(line)
    f.close()
    longitude_list = list(set(longitude_list))
    f = open(Home_Address+"track2/yelp/cluster_member_business_review_count.txt", "r")
    business_review_count_list=[]
    for line in f:
        line=line.strip()
        business_review_count_list.append(line)
    f.close()
    business_review_count_list = list(set(business_review_count_list))


    counter=0
    f_v = open(Home_Address+'track2/yelp/validation.txt', "r")
    for line in f_v:
        line_sp = line.strip().split(',')
        review_useful_list.append(str(line_sp[2]) + ',' + str(kmeans_review_useful.predict([[float(line_sp[2])]])[0]))
        review_funny_list.append(str(line_sp[3]) + ',' + str(kmeans_review_funny.predict([[float(line_sp[3])]])[0]))
        review_cool_list.append(str(line_sp[4]) + ',' + str(kmeans_review_cool.predict([[float(line_sp[4])]])[0]))
        user_review_count_list.append(str(line_sp[6]) + "," + str(kmeans_user_review_count.predict([[float(line_sp[6])]])[0]))
        user_useful_list.append(str(line_sp[7]) + "," + str(kmeans_user_useful.predict([[float(line_sp[7])]])[0]))
        user_funny_list.append(str(line_sp[8]) + "," + str(kmeans_user_funny.predict([[float(line_sp[8])]])[0]))
        user_cool_list.append(str(line_sp[9]) + "," + str(kmeans_user_cool.predict([[float(line_sp[9])]])[0]))
        friends_list.append(str(line_sp[11]) + "," + str(kmeans_friends.predict([[float(line_sp[11])]])[0]))
        fans_list.append(str(line_sp[12]) + "," + str(kmeans_fans.predict([[float(line_sp[12])]])[0]))
        user_stars_list.append(str(line_sp[13]) + "," + str(kmeans_user_stars.predict([[float(line_sp[13])]])[0]))
        compliment_hot_list.append(str(line_sp[14]) + "," + str(kmeans_compliment_hot.predict([[float(line_sp[14])]])[0]))
        compliment_more_list.append(str(line_sp[15]) + "," + str(kmeans_compliment_more.predict([[float(line_sp[15])]])[0]))
        compliment_profile_list.append(str(line_sp[16]) + "," + str(kmeans_compliment_profile.predict([[float(line_sp[16])]])[0]))
        compliment_cute_list.append(str(line_sp[17]) + "," + str(kmeans_compliment_cute.predict([[float(line_sp[17])]])[0]))
        compliment_list_list.append(str(line_sp[18]) + "," + str(kmeans_compliment_list.predict([[float(line_sp[18])]])[0]))
        compliment_note_list.append(str(line_sp[19]) + "," + str(kmeans_compliment_note.predict([[float(line_sp[19])]])[0]))
        compliment_plain_list.append(str(line_sp[20]) + "," + str(kmeans_compliment_plain.predict([[float(line_sp[20])]])[0]))
        compliment_cool_list.append(str(line_sp[21]) + "," + str(kmeans_compliment_cool.predict([[float(line_sp[21])]])[0]))
        compliment_funny_list.append(str(line_sp[22]) + "," + str(kmeans_compliment_funny.predict([[float(line_sp[22])]])[0]))
        compliment_writer_list.append(str(line_sp[23]) + "," + str(kmeans_compliment_writer.predict([[float(line_sp[23])]])[0]))
        compliment_photos_list.append(str(line_sp[24]) + "," + str(kmeans_compliment_photos.predict([[float(line_sp[24])]])[0]))
        latitude_list.append(str(line_sp[26]) + "," + str(kmeans_latitude.predict([[float(line_sp[26])]])[0]))
        longitude_list.append(str(line_sp[27]) + "," + str(kmeans_longitude.predict([[float(line_sp[27])]])[0]))
        business_review_count_list.append(str(line_sp[29]) + "," + str(kmeans_business_review_count.predict([[float(line_sp[29])]])[0]))

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
        counter = counter + 1
        if counter % 1000== 0:
            print(str(counter))
            review_useful_list = list(set(review_useful_list))
            review_funny_list = list(set(review_funny_list))
            review_cool_list = list(set(review_cool_list))
            user_review_count_list = list(set(user_review_count_list))
            user_useful_list = list(set(user_useful_list))
            user_funny_list = list(set(user_funny_list))
            user_cool_list = list(set(user_cool_list))
            friends_list = list(set(friends_list))
            fans_list = list(set(fans_list))
            user_stars_list = list(set(user_stars_list))
            compliment_hot_list = list(set(compliment_hot_list))
            compliment_more_list = list(set(compliment_more_list))
            compliment_profile_list = list(set(compliment_profile_list))
            compliment_cute_list = list(set(compliment_cute_list))
            compliment_list_list = list(set(compliment_list_list))
            compliment_note_list = list(set(compliment_note_list))
            compliment_plain_list = list(set(compliment_plain_list))
            compliment_cool_list = list(set(compliment_cool_list))
            compliment_funny_list = list(set(compliment_funny_list))
            compliment_writer_list = list(set(compliment_writer_list))
            compliment_photos_list = list(set(compliment_photos_list))
            latitude_list = list(set(latitude_list))
            longitude_list = list(set(longitude_list))
            business_review_count_list = list(set(business_review_count_list))

    f_v.close()

    review_useful_list = list(set(review_useful_list))
    review_funny_list = list(set(review_funny_list))
    review_cool_list = list(set(review_cool_list))
    user_review_count_list = list(set(user_review_count_list))
    user_useful_list = list(set(user_useful_list))
    user_funny_list = list(set(user_funny_list))
    user_cool_list = list(set(user_cool_list))
    friends_list = list(set(friends_list))
    fans_list = list(set(fans_list))
    user_stars_list = list(set(user_stars_list))
    compliment_hot_list = list(set(compliment_hot_list))
    compliment_more_list = list(set(compliment_more_list))
    compliment_profile_list = list(set(compliment_profile_list))
    compliment_cute_list = list(set(compliment_cute_list))
    compliment_list_list = list(set(compliment_list_list))
    compliment_note_list = list(set(compliment_note_list))
    compliment_plain_list = list(set(compliment_plain_list))
    compliment_cool_list = list(set(compliment_cool_list))
    compliment_funny_list = list(set(compliment_funny_list))
    compliment_writer_list = list(set(compliment_writer_list))
    compliment_photos_list = list(set(compliment_photos_list))
    latitude_list = list(set(latitude_list))
    longitude_list = list(set(longitude_list))
    business_review_count_list = list(set(business_review_count_list))

    f_w = open(Home_Address+'track2/yelp/cluster_member_review_useful_2.txt','w')
    for i in range(0, len(review_useful_list)):
        f_w.write(review_useful_list[i] + '\n')
    f_w.close()
    f_w = open(Home_Address+'track2/yelp/cluster_member_review_funny_2.txt','w')
    for i in range(0, len(review_funny_list)):
        f_w.write(review_funny_list[i] + '\n')
    f_w.close()
    f_w = open(Home_Address+'track2/yelp/cluster_member_review_cool_2.txt','w')
    for i in range(0, len(review_cool_list)):
        f_w.write(review_cool_list[i] + '\n')
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_review_count_2.txt","w")
    for i in range(0, len(user_review_count_list)):
        f_w.write(user_review_count_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_useful_2.txt","w")
    for i in range(0, len(user_useful_list)):
        f_w.write(user_useful_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_funny_2.txt","w")
    for i in range(0, len(user_funny_list)):
        f_w.write(user_funny_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_cool_2.txt","w")
    for i in range(0, len(user_cool_list)):
        f_w.write(user_cool_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_friends_2.txt","w")
    for i in range(0, len(friends_list)):
        f_w.write(friends_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_fans_2.txt","w")
    for i in range(0, len(fans_list)):
        f_w.write(fans_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_user_stars_2.txt","w")
    for i in range(0, len(user_stars_list)):
        f_w.write(user_stars_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_hot_2.txt","w")
    for i in range(0, len(compliment_hot_list)):
        f_w.write(compliment_hot_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_more_2.txt","w")
    for i in range(0, len(compliment_more_list)):
        f_w.write(compliment_more_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_profile_2.txt","w")
    for i in range(0, len(compliment_profile_list)):
        f_w.write(compliment_profile_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_cute_2.txt","w")
    for i in range(0, len(compliment_cute_list)):
        f_w.write(compliment_cute_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_list_2.txt","w")
    for i in range(0, len(compliment_list_list)):
        f_w.write(compliment_list_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_note_2.txt","w")
    for i in range(0, len(compliment_note_list)):
        f_w.write(compliment_note_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_plain_2.txt","w")
    for i in range(0, len(compliment_plain_list)):
        f_w.write(compliment_plain_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_cool_2.txt","w")
    for i in range(0, len(compliment_cool_list)):
        f_w.write(compliment_cool_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_funny_2.txt","w")
    for i in range(0, len(compliment_funny_list)):
        f_w.write(compliment_funny_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_writer_2.txt","w")
    for i in range(0, len(compliment_writer_list)):
        f_w.write(compliment_writer_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_compliment_photos_2.txt","w")
    for i in range(0, len(compliment_photos_list)):
        f_w.write(compliment_photos_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_latitude_2.txt","w")
    for i in range(0, len(latitude_list)):
        f_w.write(latitude_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_longitude_2.txt","w")
    for i in range(0, len(longitude_list)):
        f_w.write(longitude_list[i] + "\n")
    f_w.close()
    f_w = open(Home_Address+"track2/yelp/cluster_member_business_review_count_2.txt","w")
    for i in range(0, len(business_review_count_list)):
        f_w.write(business_review_count_list[i] + "\n")
    f_w.close()
################ extract vectors of training data
def Extract_LF_Train_Dataset():
    from __future__ import print_function
    import sys
    print("Python %s on %s" % (sys.version, sys.platform))
    sys.path.extend(["/media/fs_Linux_Files/yelp"])
    import numpy as np
    from sklearn.preprocessing import LabelBinarizer
    import tensorflow.keras.models as keras_models
    from random import randrange
    import yelp.Functions_RNN as Functions_RNN
    import yelp.Generator_ads as Generator_ads
    import yelp.Models as Models
    from keras import backend as K
    from sklearn.cluster import KMeans, MiniBatchKMeans
    import pickle

    Functions_RNN.Fill_cluster_ctr()
    Home_Address='/media/fs_Linux_Files/'
    TEST_CSV = Home_Address+'track2/yelp/test.txt'
    Model_file_Cluster = Home_Address+'Log/yelp/action_21/Model/Cluster'
    Model_file_Main = Home_Address+'Log/yelp/action_21/Model/Main'
    Model_file_Combined = Home_Address+'Log/yelp/action_21/Model/Combined'
    model_Cluster = keras_models.load_model(Model_file_Cluster)
    model_Main = keras_models.load_model(Model_file_Main)
    model_Combined = keras_models.load_model(Model_file_Combined)

    labels = set()
    labels = {'0', '1'}
    lb = LabelBinarizer()
    lb.fit(list(labels))
    #get_activations = K.function([model.layers[0].input], model.layers[20].output(train=False),allow_input_downcast=True)
    get_LF_F_z = K.function([model_Combined.layers[0].input,model_Combined.layers[1].input], model_Combined.layers[20].output)
    get_LF_G_z = K.function([model_Combined.layers[0].input,model_Combined.layers[1].input], model_Combined.layers[21].output)
    get_F_z = K.function(model_Main.layers[0].input, model_Main.layers[11].output)
    get_G_z = K.function(model_Cluster.layers[0].input, model_Cluster.layers[11].output)
    get_Y_hat = K.function([model_Combined.layers[0].input,model_Combined.layers[1].input], model_Combined.layers[32].output)

    TRAIN_CSV = Home_Address+'/track2/yelp/train.txt'
    trainGen_main = Generator_ads.Training_Generator_main_for_test(TRAIN_CSV, 500, lb, mode="train")
    trainGen_cluster = Generator_ads.Training_Generator_main_for_test_JC(TRAIN_CSV, 500, lb, mode="train")
    f_activation = open(Home_Address+'/track2/yelp/cluster/activation.txt', 'w')
    for i in range(0,13818):
        Real_Inputs = next(trainGen_main)
        Shadow_input = next(trainGen_cluster)
        activations_LF_F_z = get_LF_F_z([Real_Inputs[0], Shadow_input[0]])
        activations_LF_G_z = get_LF_G_z([Real_Inputs[0], Shadow_input[0]])
        activations_F_z = get_F_z(Real_Inputs[0])
        activations_G_z = get_G_z(Shadow_input[0])
        activations_Y_hat = get_Y_hat([Real_Inputs[0], Shadow_input[0]])
        for cou in range(0, 500):
            main_15=','.join(str(round(f, 6)) for f in activations_LF_F_z[cou].tolist())
            cluster_15=','.join(str(round(f, 6)) for f in activations_LF_G_z[cou].tolist())
            f_activation.write(str(float(Real_Inputs[1][cou]))+','+str(round(float(activations_Y_hat[cou]),6))+','+\
                               str(round(float(activations_F_z[cou]),6))+','+str(round(float(activations_G_z[cou]),6))+','+ \
                                main_15+','+ cluster_15+ '\n')

    f_activation.close()
########Cluster the vectors main
def Cluster_LF_F_z_Train_Dataset():
    from __future__ import print_function
    import sys
    print("Python %s on %s" % (sys.version, sys.platform))
    sys.path.extend(["/media/fs_Linux_Files/yelp"])
    import numpy as np
    from sklearn.preprocessing import LabelBinarizer
    import tensorflow.keras.models as keras_models
    from random import randrange
    import yelp.Functions_RNN as Functions_RNN
    import yelp.Generator_ads as Generator_ads
    import yelp.Models as Models
    from keras import backend as K
    import pandas as pd
    from sklearn.cluster import KMeans, MiniBatchKMeans
    import pickle
    Home_Address='/media/fs_Linux_Files/'
    f_activation = open(Home_Address+'/track2/yelp/cluster/activation.txt', 'r')
    list_main=[]
    list_targets=[]

    counter=0
    kmeans_list_main = MiniBatchKMeans(init="k-means++", n_clusters=5000, batch_size=1000000)
    for line in f_activation:
        line_sp=line.strip().split(',')
        list_targets.append([np.float32(f) for f in line_sp[0:4]])
        list_main.append([np.float32(f) for f in line_sp[4:19]])
        counter+=1
        if counter % 1000000==0:
            kmeans_list_main.partial_fit(list_main)
            #del list_main
            #list_main=[]
            print(str(counter))

    kmeans_list_main.partial_fit(list_main)
    pickle.dump(kmeans_list_main, open(Home_Address + 'track2/yelp/kmeans_list_main.pkl', 'wb'))

    list_targets_combined = [x[1] for x in list_targets]
    list_targets_main = [x[2] for x in list_targets]
    df_list_targets =pd.DataFrame({'value_m':list_targets_main,'value_co':list_targets_combined, 'label':kmeans_list_main.labels_})
    df_list_targets= df_list_targets.groupby(['label']).mean()

    f_w =open(Home_Address+'track2/yelp/cluster_list_main.txt','w')
    for row in df_list_targets.iterrows():
        f_w.write(str(row[0])+','+str(round(float(row[1]['value_co']),6))+','+str(round(float(row[1]['value_m']),6))+'\n')
    f_w.close()

    f_member =open(Home_Address+'track2/yelp/cluster_member_list_main.txt','w')
    counter=0
    for row in list_main:
        f_member.write(str(counter)+','+','.join(str(f) for f in row)+','+str(kmeans_list_main.labels_[counter])+'\n')
        counter+=1
    f_member.close()
########Cluster the vectors cluster
def Cluster_LF_G_z_Train_Dataset():
    from __future__ import print_function
    import sys
    print("Python %s on %s" % (sys.version, sys.platform))
    sys.path.extend(["/media/fs_Linux_Files/yelp"])
    import numpy as np
    from sklearn.preprocessing import LabelBinarizer
    import tensorflow.keras.models as keras_models
    from random import randrange
    import yelp.Functions_RNN as Functions_RNN
    import yelp.Generator_ads as Generator_ads
    import yelp.Models as Models
    from keras import backend as K
    import pandas as pd
    from sklearn.cluster import KMeans, MiniBatchKMeans
    import pickle
    Home_Address='/media/fs_Linux_Files/'
    f_activation = open(Home_Address+'/track2/yelp/cluster/activation.txt', 'r')
    list_cluster=[]
    list_targets=[]

    counter=0
    kmeans_list_cluster = MiniBatchKMeans(init="k-means++", n_clusters=5000, batch_size=1000000)
    for line in f_activation:
        line_sp=line.strip().split(',')
        list_targets.append([np.float32(f) for f in line_sp[0:4]])
        list_cluster.append([np.float32(f) for f in line_sp[19:34]])
        counter+=1
        if counter % 1000000==0:
            kmeans_list_cluster.partial_fit(list_cluster)
            print(str(counter))

    kmeans_list_cluster.partial_fit(list_cluster)
    pickle.dump(kmeans_list_cluster, open(Home_Address + 'track2/yelp/kmeans_list_cluster.pkl', 'wb'))

    list_targets_combined = [x[1] for x in list_targets]
    list_targets_cluster = [x[3] for x in list_targets]
    df_list_targets =pd.DataFrame({'value_c':list_targets_cluster,'value_co':list_targets_combined, 'label':kmeans_list_cluster.labels_})
    df_list_targets= df_list_targets.groupby(['label']).mean()

    f_w =open(Home_Address+'track2/yelp/cluster_list_cluster.txt','w')
    for row in df_list_targets.iterrows():
        f_w.write(str(row[0])+','+str(round(float(row[1]['value_co']),6))+','+str(round(float(row[1]['value_c']),6))+'\n')
    f_w.close()

    f_member =open(Home_Address+'track2/yelp/cluster_member_list_cluster.txt','w')
    counter=0
    for row in list_cluster:
        f_member.write(str(counter)+','+','.join(str(f) for f in row)+','+str(kmeans_list_cluster.labels_[counter])+'\n')
        counter+=1
    f_member.close()