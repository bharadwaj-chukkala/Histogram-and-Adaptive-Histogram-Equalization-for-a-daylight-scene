'''
Author: Bharadwaj Chukkala
UID: 118341705
'''
##### Importing Libraries #####
#
#
import cv2 as cv
import numpy as np
import glob


'''
Cumulative Sum of the PIxel Intensities
'''
def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

'''
Normalizing the Cumulative Distributive Function
'''
def normalize(cdf):
    normalized_val = cdf/cdf.max()*255
    return normalized_val

'''
Function to perform Histogram Equalization
'''
def equalize(img):
    flat = img.flatten()
    hist, _ = np.histogram(flat, 256, [0, 256])
    cdf = cumsum(hist)
    normalize_cdf = normalize(cdf)
    cdf_normalized = np.uint8(normalize_cdf)
    hist_equalize = cdf_normalized[img]
    return hist_equalize

'''
Function to perform Adaptive Histogram Equalization
'''
def adaptive_equalize(img, n = 8):
    img = img.copy()
    h, w = img.shape
    sh, sw = h//n, w//n
    for i in range(0, h, sh):
        for j in range(0, w, sw):
            img[i:i+sh, j:j+sw] = equalize(img[i:i+sh, j:j+sw])
    return img


##### Reading the dataset #####
#
#
filename= glob.glob(r'hist_data/*.png')


for image in filename:

    #Reading every image in the dataset
    img = cv.imread(image)
    
    #Converting image to HSV color space
    img1 = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(img1)
    
    #Performing Histogram Equalization
    hist_equalize = equalize(v)
    
    #Performing Adaptive Histogram Equalization
    adaptive_hist_equalize = adaptive_equalize(v)

    #Merging the hue, saturation with equalized histogram on the value channel 
    hist_eq_img = cv.merge([h, s, hist_equalize])
    adp_hist_eq_img = cv.merge([h, s, adaptive_hist_equalize])
    
    #Converting the image from HSV to BGR color space
    hist_eq_img = cv.cvtColor(hist_eq_img, cv.COLOR_HSV2BGR)
    adp_hist_eq_img = cv.cvtColor(adp_hist_eq_img, cv.COLOR_HSV2BGR)
    
    height, width = 1080, 1920
    final_img=np.zeros((height,width,3), np.uint8)
    
    
    final_img[0:540,0:1920] = cv.resize(hist_eq_img, (1920,540), interpolation=cv.INTER_AREA)
    final_img[540:1080,0:1920] = cv.resize(adp_hist_eq_img, (1920,540), interpolation=cv.INTER_AREA)
    
    cv.putText(final_img,'[1] Histogram Equalization',(20,50), cv.FONT_HERSHEY_SIMPLEX, 2,(255,255,0), 2, 0)
    cv.putText(final_img,'[2] Adaptive Histogram Equalization',(20,600), cv.FONT_HERSHEY_SIMPLEX, 2,(255,255,0), 2, 0)

    cv.imshow('Output', final_img)
    cv.waitKey(300)

cv.destroyAllWindows()
