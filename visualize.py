#!/usr/bin/env python
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('NYC_taxi.csv', parse_dates=['pickup_datetime'], nrows=500000)

# nyc longitude
nyc_min_longitude = -74.05
nyc_max_longitude = -74.05

# nyc latitude
nyc_min_latitude = 40.63
nyc_max_latitude = 40.85

df2 = df.copy(deep=True)
for long in ['pickup_longitude', 'dropoff_longitude']:
  df2 = df2[(df2[long] > nyc_min_longitude) & (df2[long] < nyc_max_longitude)]

for lat in ['pickup_latitude', 'dropoff_latitude']:
  df2 = df2[(df2[lat] > nyc_min_latitude) & (df2[lat] < nyc_max_latitude)]
  


landmarks = {'JFK Airport': (-73.78,40.643),
             'Laguardia Airport': (-73.87, 40.77),
             'Midtown': (-73.98, 40.76),
             'Lower Manhattan': (-74.00, 40.72),
             'Upper Manhattan': (-73.94, 40.82),
             'Brooklyn': (-73.95, 40.66)}

def plot_lat_long(df, landmarks, points='Pickup'):
  plt.figure(figsize = (12,12))
  if points == 'pickup':
    plt.plot(list(df.pickup_longitude), list(df.pickup_latitude), '.', markersize=1)
  else:
    plt.plot(list(df.dropoff_longitude), list(df.dropoff_latitude), '.', markersize=1)

  for landmark in landmarks:
    plt.plot(landmarks[landmark][0], landmarks[landmark][1], '*', markersize=15, alpha=1, color='r')
    plt.annotate(landmark, (landmarks[landmark][0]+0.005, landmarks[landmark][1]+0.005), color='r', backgroundcolor='w')



  plt.title("{} Locations in NYC Illustrated".format(points))
  plt.grid(None)
  plt.xlabel("Latitude")
  plt.ylabel("Longitude")
  plt.show()

plot_lat_long(df2, landmarks, points='Pickup')
plot_lat_long(df2, landmarks, points='Drop Off')
