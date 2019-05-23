import csv
import os
import numpy as np
os. chdir("/home/etudiant/PycharmProjects/word6_to_32bitfloat-x-axis-g-")


def reorder(arr, index, n):
    '''

    :param arr: array to reorder
    :param index: reordering according to this index
    :param n: length of the array
    :return: the ordered array
    '''
    temp = [0] * n;

    # arr[i] should be
    # present at index[i] index
    for i in range(0, n):
        temp[index[i]] = arr[i]

        # Copy temp[] to arr[]
    for i in range(0, n):
        arr[i] = temp[i]
        index[i] = i
    return arr



with open ('bagfile-_os1_node_imu_packets.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    next(readCSV)  # skip header
    for row in readCSV:
        row = np.asarray(row)
        # print (row[25:29])
        temp = row[25:29]
        # print (temp)
        four_bytes = reorder(temp, [3, 2, 1, 0], 4)
        i =0
        for word in four_bytes:
            four_bytes[i] = bin(int(word))
            i += 1
        print (four_bytes)