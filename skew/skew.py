import numpy as np
from skimage.transform import hough_line, hough_line_peaks
from skimage.transform import rotate
from skimage.feature import canny
from skimage.io import imread
from skimage.color import rgb2gray
from scipy.stats import mode

def _skew_angle(image):
    '''
        returns the most common angle from hough transform as skew of document
    '''
    
    #1 get edges
    image = rgb2gray(image)
    edges = canny(image)
    #2 Hough transform .
    tested_angles = np.deg2rad(np.arange(0, 180.0))
    h, theta, d = hough_line(edges, theta=tested_angles)
    _, angles, dists = hough_line_peaks(h, theta, d)
    
    #3 find the most common angle.
    most_common_angle = mode(np.around(angles, decimals=1))[0]
    #print(most_common_angle)
    skew_angle = np.rad2deg(most_common_angle - np.pi/2)
    #print(skew_angle) 
    return skew_angle
