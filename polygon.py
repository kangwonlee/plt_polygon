import numpy as np
import matplotlib.pyplot as plt


def polygon(sides:int=3, radius:float=1.0, x:float=0, y:float=0,):
    sides = int(sides)
    assert 3 <= sides
    interval_deg = 360 / sides
    offset_deg = 90
    angles_deg = np.arange(sides) * interval_deg
    angles_deg = np.append(angles_deg, [0])
    angles_deg += offset_deg
    
    angles_rad = np.deg2rad(angles_deg)
    x_array = radius * np.cos(angles_rad) + x
    y_array = radius * np.sin(angles_rad) + y
    
    plt.axis('equal')
    plt.plot(x_array, y_array)
    plt.grid(True)
    
    return x_array, y_array
