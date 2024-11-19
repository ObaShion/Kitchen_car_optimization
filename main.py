import numpy as np
import matplotlib.pyplot as plt

#座標の配列
locations = np.array([
    [5, 9],#ひいらぎ
    [8, 1],#あすなろ
    [8, 4],#図書館
    [5, 5],#かえで
    [8, 8] #さつき
])

#重みの配列
#[ひいらぎ、あすなろ、図書館、かえで、さつき]
weights = np.array([1, 23, 17, 12, 10])

x_coords = locations[:, 0]
y_coords = locations[:, 1]

#重みありの中央値を計算
x_median = np.median(np.repeat(x_coords, weights))
y_median = np.median(np.repeat(y_coords, weights))

optimal_location = (x_median, y_median)

print(optimal_location)