
# coding: utf-8

# In[3]:


import json
import csv
import numpy as np
import pandas as pd
import os
import math
import sys


# In[4]:


import json
import numpy as np
import pandas as pd
import os

path_to_videos = r"/home/ubuntu/VaishDir/Testing Data"

def convert_to_csv(path_to_video):
    columns = ['score_overall', 'nose_score', 'nose_x', 'nose_y', 'leftEye_score', 'leftEye_x', 'leftEye_y',
               'rightEye_score', 'rightEye_x', 'rightEye_y', 'leftEar_score', 'leftEar_x', 'leftEar_y',
               'rightEar_score', 'rightEar_x', 'rightEar_y', 'leftShoulder_score', 'leftShoulder_x', 'leftShoulder_y',
               'rightShoulder_score', 'rightShoulder_x', 'rightShoulder_y', 'leftElbow_score', 'leftElbow_x',
               'leftElbow_y', 'rightElbow_score', 'rightElbow_x', 'rightElbow_y', 'leftWrist_score', 'leftWrist_x',
               'leftWrist_y', 'rightWrist_score', 'rightWrist_x', 'rightWrist_y', 'leftHip_score', 'leftHip_x',
               'leftHip_y', 'rightHip_score', 'rightHip_x', 'rightHip_y', 'leftKnee_score', 'leftKnee_x', 'leftKnee_y',
               'rightKnee_score', 'rightKnee_x', 'rightKnee_y', 'leftAnkle_score', 'leftAnkle_x', 'leftAnkle_y',
               'rightAnkle_score', 'rightAnkle_x', 'rightAnkle_y']
    data = json.loads(open(path_to_video, 'r').read())
    csv_data = np.zeros((len(data), len(columns)))
    for i in range(csv_data.shape[0]):
        one = []
        one.append(data[i]['score'])
        for obj in data[i]['keypoints']:
            one.append(obj['score'])
            one.append(obj['position']['x'])
            one.append(obj['position']['y'])
        csv_data[i] = np.array(one)
    pd.DataFrame(csv_data, columns=columns).to_csv(/home/ubuntu/VaishDir/Testing Data/ + 'key_points.csv', index_label='Frames#')
import sys
testing_data = sys(argv[1])
convert_to_csv(testing_data)
test_data = makeMatrix('/home/ubuntu/VaishDir/Testing Data/' + 'key_points.csv')

# In[5]:


def makeMatrix(input):
    with open(input, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        columns = ['rightWrist_x', 'rightWrist_y']
        dataMatrix = np.zeros((len(data)-1, len(columns)))
        for i in range(dataMatrix.shape[0] + 1):
            dataRow = []
            if(data[i][33] != 'rightWrist_x'):
                dataRow.append(data[i][33])
            if(data[i][34] != 'rightWrist_y'):
                dataRow.append(data[i][34])
            if(i > 0):
                dataMatrix[i-1] = np.array(dataRow)
        return dataMatrix

# In[25]:


BOOK_1 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/book_1_narvekar.csv')
BOOK_2 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_(1)_JONNALAGADDA.csv')
BOOK_3 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_(1)_KARANJKAR.csv')
BOOK_4 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_DAVE.csv')
BOOK_5 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/Book_PRACTICE_1_Ge.csv')
BOOK_6 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_GUPTA.csv')
BOOK_7 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_kardale.csv')
BOOK_8 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/Book_PRACTICE_1_Li.csv')
BOOK_9 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_PATEL.csv')
BOOK_10 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_SARDHARA.csv')
BOOK_11 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_seal.csv')
BOOK_12 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_SHAH.csv')
BOOK_13 = makeMatrix('/home/ubuntu/VaishDir/Training Data/book/BOOK_PRACTICE_1_singh.csv')


CAR_1 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/car_1_narvekar.csv')
CAR_2 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_(1)_JONNALAGADDA.csv')
CAR_3 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_(1)_KARANJKAR.csv')
CAR_4 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_DAVE.csv')
CAR_5 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/Car_PRACTICE_1_Ge.csv')
CAR_6 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_GUPTA.csv')
CAR_7 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_kardale.csv')
CAR_8 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/Car_PRACTICE_1_Li.csv')
CAR_9 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_PATEL.csv')
CAR_10 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_SARDHARA.csv')
CAR_11 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_seal.csv')
CAR_12 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_SHAH.csv')
CAR_13 = makeMatrix('/home/ubuntu/VaishDir/Training Data/car/CAR_PRACTICE_1_singh.csv')



GIFT_1 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/gift_1_narvekar.csv')
GIFT_2 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_(1)_JONNALAGADDA.csv')
GIFT_3 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_(1)_KARANJKAR.csv')
GIFT_4 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_DAVE.csv')
GIFT_5 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/Gift_PRACTICE_1_Ge.csv')
GIFT_6 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_GUPTA.csv')
GIFT_7 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_kardale.csv')
GIFT_8 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/Gift_PRACTICE_1_Li.csv')
GIFT_9 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_PATEL.csv')
GIFT_10 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_SARDHARA.csv')
GIFT_11 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_seal.csv')
GIFT_12 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_SHAH.csv')
GIFT_13 = makeMatrix('/home/ubuntu/VaishDir/Training Data/gift/GIFT_PRACTICE_1_singh.csv')


MOVIE_1 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/movie_1_narvekar.csv')
MOVIE_2 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_(1)_JONNALAGADDA.csv')
MOVIE_3 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_(1)_KARANJKAR.csv')
MOVIE_4 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_DAVE.csv')
MOVIE_5 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_Ge.csv')
MOVIE_6 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_GUPTA.csv')
MOVIE_7 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_kardale.csv')
MOVIE_8 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_Li.csv')
MOVIE_9 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_PATEL.csv')
MOVIE_10 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_SARDHARA.csv')
MOVIE_11 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_seal.csv')
MOVIE_12 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_SHAH.csv')
MOVIE_13 = makeMatrix('/home/ubuntu/VaishDir/Training Data/movie/MOVIE_PRACTICE_1_singh.csv')

SELL_1 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/sell_1_narvekar.csv')
SELL_2 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_(1)_JONNALAGADDA.csv')
SELL_3 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_(1)_KARANJKAR.csv')
SELL_4 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_DAVE.csv')
SELL_5 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/Sell_PRACTICE_1_Ge.csv')
SELL_6 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_GUPTA.csv')
SELL_7 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_kardale.csv')
SELL_8 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/Sell_PRACTICE_1_Li.csv')
SELL_9 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_PATEL.csv')
SELL_10 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_SARDHARA.csv')
SELL_11 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_seal.csv')
SELL_12 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_SHAH.csv')
SELL_13 = makeMatrix('/home/ubuntu/VaishDir/Training Data/sell/SELL_PRACTICE_1_singh.csv')

TOTAL_1 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/total_1_narvekar.csv')
TOTAL_2 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_(1)_JONNALAGADDA.csv')
TOTAL_3 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_(1)_KARANJKAR.csv')
TOTAL_4 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_DAVE.csv')
TOTAL_5 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/Total_PRACTICE_1_Ge.csv')
TOTAL_6 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_GUPTA.csv')
TOTAL_7 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_kardale.csv')
TOTAL_8 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/Total_PRACTICE_1_Li.csv')
TOTAL_9 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_PATEL.csv')
TOTAL_10 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_SARDHARA.csv')
TOTAL_11 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_seal.csv')
TOTAL_12 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_SHAH.csv')
TOTAL_13 = makeMatrix('/home/ubuntu/VaishDir/Training Data/total/TOTAL_PRACTICE_1_singh.csv')


# In[12]:


# In[16]:


from numpy import sqrt
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance = distance + (row1[i] - row2[i])**2
    return sqrt(distance)
def sum(arr):
    sum = 0.0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum


# In[17]:


book = list()
book.append(euclidean_distance(test_data, BOOK_1)[0])
book.append(euclidean_distance(test_data, BOOK_2)[0])
book.append(euclidean_distance(test_data, BOOK_3)[0])
book.append(euclidean_distance(test_data, BOOK_4)[0])
book.append(euclidean_distance(test_data, BOOK_5)[0])
book.append(euclidean_distance(test_data, BOOK_6)[0])
book.append(euclidean_distance(test_data, BOOK_7)[0])
book.append(euclidean_distance(test_data, BOOK_8)[0])
book.append(euclidean_distance(test_data, BOOK_9)[0])
book.append(euclidean_distance(test_data, BOOK_10)[0])
book.append(euclidean_distance(test_data, BOOK_11)[0])
book.append(euclidean_distance(test_data, BOOK_12)[0])
book.append(euclidean_distance(test_data, BOOK_13)[0])

book_sum = sum(book)
car = list()

car.append(euclidean_distance(test_data, CAR_1)[0])
car.append(euclidean_distance(test_data, CAR_2)[0])
car.append(euclidean_distance(test_data, CAR_3)[0])
car.append(euclidean_distance(test_data, CAR_4)[0])
car.append(euclidean_distance(test_data, CAR_5)[0])
car.append(euclidean_distance(test_data, CAR_6)[0])
car.append(euclidean_distance(test_data, CAR_7)[0])
car.append(euclidean_distance(test_data, CAR_8)[0])
car.append(euclidean_distance(test_data, CAR_9)[0])
car.append(euclidean_distance(test_data, CAR_10)[0])
car.append(euclidean_distance(test_data, CAR_11)[0])
car.append(euclidean_distance(test_data, CAR_12)[0])
car_sum = sum(car)


gift = list()


gift.append(euclidean_distance(test_data, GIFT_1)[0])
gift.append(euclidean_distance(test_data, GIFT_2)[0])
gift.append(euclidean_distance(test_data, GIFT_3)[0])
gift.append(euclidean_distance(test_data, GIFT_4)[0])
gift.append(euclidean_distance(test_data, GIFT_5)[0])
gift.append(euclidean_distance(test_data, GIFT_6)[0])
gift.append(euclidean_distance(test_data, GIFT_7)[0])
gift.append(euclidean_distance(test_data, GIFT_8)[0])
gift.append(euclidean_distance(test_data, GIFT_9)[0])
gift.append(euclidean_distance(test_data, GIFT_10)[0])
gift.append(euclidean_distance(test_data, GIFT_11)[0])
gift.append(euclidean_distance(test_data, GIFT_12)[0])
gift.append(euclidean_distance(test_data, GIFT_13)[0])
gift_sum = sum(gift)


movie = list()

movie.append(euclidean_distance(test_data, MOVIE_1)[0])
movie.append(euclidean_distance(test_data, MOVIE_2)[0])
movie.append(euclidean_distance(test_data, MOVIE_3)[0])
movie.append(euclidean_distance(test_data, MOVIE_4)[0])
movie.append(euclidean_distance(test_data, MOVIE_5)[0])
movie.append(euclidean_distance(test_data, MOVIE_6)[0])
movie.append(euclidean_distance(test_data, MOVIE_7)[0])
movie.append(euclidean_distance(test_data, MOVIE_8)[0])
movie.append(euclidean_distance(test_data, MOVIE_9)[0])
movie.append(euclidean_distance(test_data, MOVIE_10)[0])
movie.append(euclidean_distance(test_data, MOVIE_11)[0])
movie.append(euclidean_distance(test_data, MOVIE_12)[0])
movie.append(euclidean_distance(test_data, MOVIE_13)[0])
movie_sum = sum(movie)

sell = list()

sell.append(euclidean_distance(test_data, SELL_1)[0])
sell.append(euclidean_distance(test_data, SELL_2)[0])
sell.append(euclidean_distance(test_data, SELL_3)[0])
sell.append(euclidean_distance(test_data, SELL_4)[0])
sell.append(euclidean_distance(test_data, SELL_5)[0])
sell.append(euclidean_distance(test_data, SELL_6)[0])
sell.append(euclidean_distance(test_data, SELL_7)[0])
sell.append(euclidean_distance(test_data, SELL_8)[0])
sell.append(euclidean_distance(test_data, SELL_9)[0])
sell.append(euclidean_distance(test_data, SELL_10)[0])
sell.append(euclidean_distance(test_data, SELL_11)[0])
sell.append(euclidean_distance(test_data, SELL_12)[0])
sell.append(euclidean_distance(test_data, SELL_13)[0])

sell_sum = sum(sell)


total = list()

total.append(euclidean_distance(test_data, TOTAL_1)[0])
total.append(euclidean_distance(test_data, TOTAL_2)[0])
total.append(euclidean_distance(test_data, TOTAL_3)[0])
total.append(euclidean_distance(test_data, TOTAL_4)[0])
total.append(euclidean_distance(test_data, TOTAL_5)[0])
total.append(euclidean_distance(test_data, TOTAL_6)[0])
total.append(euclidean_distance(test_data, TOTAL_7)[0])
total.append(euclidean_distance(test_data, TOTAL_8)[0])
total.append(euclidean_distance(test_data, TOTAL_9)[0])
total.append(euclidean_distance(test_data, TOTAL_10)[0])
total.append(euclidean_distance(test_data, TOTAL_11)[0])
total.append(euclidean_distance(test_data, TOTAL_12)[0])
total.append(euclidean_distance(test_data, TOTAL_13)[0])

total_sum = sum(total)


# In[18]:


min_dist = min(sell_sum, total_sum, movie_sum, gift_sum, car_sum, book_sum)


# In[19]:



def class_label(sell_sum, total_sum, movie_sum, gift_sum, car_sum, book_sum, min_dist):
    if(sell_sum == min_dist):
        return "sum"
    elif(total_sum == min_dist):
        return "total"
    elif(movie_sum == min_dist):
        return "movie"
    elif(gift_sum == min_dist):
        return "gift"
    elif(car_sum == min_dist):
        return "car"
    elif(book_sum == min_dist):
        "return book"

