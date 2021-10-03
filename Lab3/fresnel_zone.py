import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def plot_fresnel(a1, a2, f, n):
    a1 = np.array(a1)
    a2 = np.array(a2)
    
    # Calculate ellipse shape
    centre = ((a1[0] + a2[0])/2, (a1[1] + a2[1])/2) # Midpoint Formula
    width = np.linalg.norm(a1 - a2)
    fresnel_radius = np.sqrt((n * f * (width/2)**2) / (width))
    print(fresnel_radius)
    ellipse = Ellipse(centre, width, fresnel_radius, alpha=0.2, edgecolor='red', linestyle='--', linewidth=2)
    
    # Plot Ellipse
    ax = plt.gca()
    ax.add_patch(ellipse)
    plt.scatter(a1[0], a1[1], zorder=2, color='red')
    plt.scatter(a2[0], a2[1], zorder=2, color='red')
    marginx = width / 10
    plt.xlim([a1[0] - marginx, a2[0] + marginx])
    plt.ylim([-10, 50])
    plt.xlabel('Distance [m]')
    plt.ylabel('Height [m]')
    plt.legend(['Fresnel Zone', 'Antennas'])


if __name__ == '__main__':

    antenna1 = [0, 20]
    antenna2 = [1000, 20]
    frequencies = [2.4, 433/1000, 5.8]  # GHz
    n = 1   # Fresnel zone number

    i = 1
    for freq in frequencies:
        plt.subplot(2, 2, i)
        
        plot_fresnel(antenna1, antenna2, freq, n)
        
        plt.title('Frequency: ' + str(freq) + ' GHz')
        plt.show(block=False)
        i += 1
        
    plt.show()  # Block new plots untill all windows are closed

