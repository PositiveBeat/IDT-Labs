#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# IMU exercise
# Copyright (c) 2015-2020 Kjeld Jensen kjen@mmmi.sdu.dk kj@kjen.dk

##### Insert initialize code below ###################

## Uncomment the file to read ##
# fileName = 'imu_razor_data_static.txt'
# fileName = 'imu_razor_data_pitch_55deg.txt'
# fileName = 'imu_razor_data_roll_65deg.txt'
fileName = 'imu_razor_data_yaw_90deg.txt'

## IMU type
#imuType = 'vectornav_vn100'
imuType = 'sparkfun_razor'

## Variables for plotting ##
showPlot = True
plotData = []

## Initialize your variables here ##
myValue = 0.0



######################################################

# import libraries
from math import pi, sqrt, atan2
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# open the imu data file
f = open (fileName, "r")

# initialize variables
count = 0
acc_x_array = []
gyro_array = []
time_dif_sum = 0
gyro = 0
gyro_prev = 0
ts_prev = 0

# looping through file

for line in f:
	count += 1

	# split the line into CSV formatted data
	line = line.replace ('*',',') # make the checkum another csv value
	csv = line.split(',')

	# keep track of the timestamps 
	ts_recv = float(csv[0])
	if count == 1: 
		ts_now = ts_recv # only the first time
	else:
		ts_prev = ts_now
		ts_now = ts_recv
		time_dif_sum += ts_now - ts_prev
		gyro_prev = gyro_z	# Save previous gyro value



	if imuType == 'sparkfun_razor':
		# import data from a SparkFun Razor IMU (SDU firmware)
		acc_x = int(csv[2]) / 1000.0 * 4 * 9.82;
		acc_y = int(csv[3]) / 1000.0 * 4 * 9.82;
		acc_z = int(csv[4]) / 1000.0 * 4 * 9.82;
		gyro_x = int(csv[5]) * 1/14.375 * pi/180.0;
		gyro_y = int(csv[6]) * 1/14.375 * pi/180.0;
		gyro_z = int(csv[7]) * 1/14.375 * pi/180.0;



	elif imuType == 'vectornav_vn100':
		# import data from a VectorNav VN-100 configured to output $VNQMR
		acc_x = float(csv[9])
		acc_y = float(csv[10])
		acc_z = float(csv[11])
		gyro_x = float(csv[12])
		gyro_y = float(csv[13])
		gyro_z = float(csv[14])
	 		

	##### Insert loop code below #########################

	# Variables available
	# ----------------------------------------------------
	# count		Current number of updates		
	# ts_prev	Time stamp at the previous update
	# ts_now	Time stamp at this update
	# acc_x		Acceleration measured along the x axis
	# acc_y		Acceleration measured along the y axis
	# acc_z		Acceleration measured along the z axis
	# gyro_x	Angular velocity measured about the x axis
	# gyro_y	Angular velocity measured about the y axis
	# gyro_z	Angular velocity measured about the z axis

	## Accelerometer ##
	roll = np.arctan2(-acc_x, acc_z)
	pitch = np.arctan2(acc_y, sqrt(acc_x**2 + acc_z**2))

	acc_x_array.append(roll * 180.0 / pi)	# To be used for filtering

	## Gyro ##
	# gyro = (gyro_z + gyro_prev) / (ts_now - ts_prev)
	# gyro += (gyro_x + gyro_prev)
	gyro += gyro_z * (ts_now - ts_prev)
	gyro_array.append(gyro)

	## Generic ##
	plotValue = gyro
	plotData.append (plotValue * 180.0 / pi)
	######################################################

## FILTER ##
T = time_dif_sum / count
# Sampling frequency
f_sample = 1 / T
print("Sampling time: ", f_sample)
# Cutoff frequency
f_cutoff = 50  

# Filtering
wn = f_cutoff / (f_sample * 2)
sos = signal.butter(1, wn, btype='low', analog=False, output='sos', fs=None)
filtered = signal.sosfilt(sos, acc_x_array)
# filtered = signal.sosfilt(sos, gyro_array)



## Gyro ##





# closing the file	
f.close()

# show the plot
if showPlot == True:
	# plt.plot(plotData)
	# plt.plot(filtered)
	plt.plot(gyro_array)
	plt.xlabel("Measurements")
	plt.ylabel("Degrees")
	# plt.title("Pitch")
	# plt.title("Roll")
	plt.savefig('imu_exercise_plot.png')
	plt.show()


