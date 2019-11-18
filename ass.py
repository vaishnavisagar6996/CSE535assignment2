import json
import csv
import numpy as np
import pandas as pd
import os
import math
import sys
import json
import numpy as np
import pandas as pd
import os

path_to_videos = r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE"



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
    data = json.loads(open(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/key_points_12.json", 'r').read())
    csv_data = np.zeros((len(data), len(columns)))
    for i in range(csv_data.shape[0]):
        one = []
        one.append(data[i]['score'])
        for obj in data[i]['keypoints']:
            one.append(obj['score'])
            one.append(obj['position']['x'])
            one.append(obj['position']['y'])
        csv_data[i] = np.array(one)
    pd.DataFrame(csv_data, columns=columns).to_csv(path_to_videos + 'key_points_12.csv', index_label='Frames#')


if __name__ == '__main__':

    files = os.listdir()
    for file in files:
        if not os.path.isdir(path_to_videos + file + "/"):
            new_path = os.path.splitext(file)[0] + "/"
            convert_to_csv(new_path)
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

BOOK_1 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points.csv")
BOOK_2 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_1.csv")
BOOK_3 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_2.csv")
BOOK_4 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_3.csv")
BOOK_5 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_4.csv")
BOOK_6 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_5.csv")
BOOK_7 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_6.csv")
BOOK_8 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_7.csv")
BOOK_9 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_8.csv")
BOOK_10 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_9.csv")
BOOK_11= makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_10.csv")
BOOK_12 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_11.csv")
BOOK_13 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/BOOK/BOOKkey_points_12.csv")
CAR_1 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_1.csv")
CAR_2 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_2.csv")
CAR_3 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_3.csv")
CAR_4 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_4.csv")
CAR_5 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_5.csv")
CAR_6 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_6.csv")
CAR_7 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_7.csv")
CAR_8 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_8.csv")
CAR_9 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_9.csv")
CAR_10 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_10.csv")
CAR_11 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_11.csv")
CAR_12 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/CAR/CARkey_points_12.csv")
GIFT_1 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points.csv")
GIFT_2 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_1.csv")
GIFT_3 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_2.csv")
GIFT_4 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_3.csv")
GIFT_5 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_4.csv")
GIFT_6 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_5.csv")
GIFT_7 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_6.csv")
GIFT_8 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_7.csv")
GIFT_9 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_8.csv")
GIFT_10 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_9.csv")
GIFT_11 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_10.csv")
GIFT_12 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_11.csv")
GIFT_13 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/GIFT/GIFTkey_points_12.csv")
MOVIE_1 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points.csv")
MOVIE_2 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_1.csv")
MOVIE_3 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_2.csv")
MOVIE_4 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_3.csv")
MOVIE_5 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_4.csv")
MOVIE_6 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_5.csv")
MOVIE_7 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_6.csv")
MOVIE_8 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_7.csv")
MOVIE_9 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_8.csv")
MOVIE_10 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_9.csv")
MOVIE_11= makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_10.csv")
MOVIE_12 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_11.csv")
MOVIE_13 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/MOVIE/MOVIEkey_points_12.csv")
SELL_1 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_1.csv")
SELL_2 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_2.csv")
SELL_3 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_3.csv")
SELL_4 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_4.csv")
SELL_5 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_5.csv")
SELL_6 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_6.csv")
SELL_7 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_7.csv")
SELL_8 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_8.csv")
SELL_9 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_9.csv")
SELL_10 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_10.csv")
SELL_11 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_11.csv")
SELL_12 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_12.csv")
SELL_13 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/SELL/SELLkey_points_13.csv")
TOTAL_1 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_1.csv")
TOTAL_2 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_2.csv")
TOTAL_3 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_3.csv")
TOTAL_4 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_4.csv")
TOTAL_5 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_5.csv")
TOTAL_6 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_6.csv")
TOTAL_7 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_7.csv")
TOTAL_8 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_8.csv")
TOTAL_9 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_9.csv")
TOTAL_10 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_10.csv")
TOTAL_11 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_11.csv")
TOTAL_12 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_12.csv")
TOTAL_13 = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/key_points_json/TOTAL/TOTALkey_points_13.csv")
test_data = makeMatrix(r"C:/Users/pinkh/OneDrive/Desktop/mobile computing/assignment2/TestData/TestData.csv")def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance = distance + (row1[i] - row2[i])**2
    return sqrt(distance)
def sum(arr):
    sum = 0.0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum
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
min_dist = min(sell_sum, total_sum, movie_sum, gift_sum, car_sum, book_sum)
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
        return "book"
val = class_label(sell_sum, total_sum, movie_sum, gift_sum, car_sum, book_sum, min_dist)
