import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def plot_fresnel(a1, a2, f, n):
    a1 = np.array(a1)
    a2 = np.array(a2)
    
    # Calculate ellipse shape and orientation
    centre = ((a1[0] + a2[0])/2, (a1[1] + a2[1])/2) # Midpoint Formula
    width = np.linalg.norm(a1 - a2)
    fresnel_radius = np.sqrt((n * f * (width/2)**2) / (width))
    diff_vec = [a2[0] - a1[0], a2[1] - a1[1]]
    angle = np.rad2deg(np.arctan2(diff_vec[1], diff_vec[0]))
    ellipse = Ellipse(centre, width, fresnel_radius, angle, alpha=0.2, edgecolor='red', linestyle='--', linewidth=2)
    
    # Plot Ellipse
    ax = plt.gca()  # Init plot
    ax.add_patch(ellipse)
    plt.scatter(a1[0], a1[1], zorder=2, color='red')
    plt.scatter(a2[0], a2[1], zorder=2, color='red')
    plt.xlabel('Distance [m]')
    plt.ylabel('Height [m]')
    plt.legend(['Fresnel Zone', 'Antennas'])
    plt.title('Frequency: ' + str(f) + ' GHz')

    return fresnel_radius, angle


def ex2_3():
    antenna1 = [0, 20]
    antenna2 = [1000, 20]
    frequencies = [2.4, 433/1000, 5.8]  # GHz
    n = 1   # Fresnel zone number

    i = 1
    for freq in frequencies:
        plt.subplot(2, 2, i)
        
        plot_fresnel(antenna1, antenna2, freq, n)
        
        plt.xlim([-10, 1010])
        plt.ylim([-10, 50])

        plt.show(block=False)
        i += 1
    
    plt.show()  # Block new plots untill all windows are closed

def ex2_4_a():
    antenna1 = [0, 0.5]
    antenna2 = [np.sqrt(400**2 - 50**2), 50]
    freq = 2.4  # GHz
    n = 1   # Fresnel zone number

    fresnel_radius, angle = plot_fresnel(antenna1, antenna2, freq, n)

    rectangle = plt.Rectangle((antenna2[0]/3, 0), 50, 20, fc='grey')
    
    ax.add_patch(rectangle)
    plt.show()  # Block new plots untill all windows are closed

if __name__ == '__main__':
    ax = plt.gca()  # Init plot

    # ex2_3()
    ex2_4_a()




#TODO - FIX ANGLE ERROR