from PIL import Image
import numpy as np
import glob

image_list = [] 
rgb_mean = [] #to check the rgb score of individual images

#Idea is to calculate the  mean values of rgb, and find an overall mean which ranges between 0 and 255.

#glob library helps to find images with  similar extension in a folder. 
#So, this is a simple way to add images in a folder to the code
for image in glob.glob('*.jpg'):
    color = Image.open(image) #gives you the rgb values of images
    image_list.append(color)
        
    arr = np.asarray(color) #to convert into a numpy array  

    mn = arr.mean(0).mean(0) #find the mean across all elements
    value = np.mean(mn)
    rgb_mean.append(value)
        
#I have random chose random values. You can change the values to make it better
    if value >= 150:
        print('Bright')
        
    elif value > 100 and value < 150:
        print('Moderate')
            
    else:
        print('Dull')
        