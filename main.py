import os
from os import listdir
from skew.skew import _skew_angle
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd

folder_dir = "input_val"
result = []
verbose = True  # set verbose = False if you dont want to see the image

for images in os.listdir(folder_dir):
    if (images.endswith(".png")):
        inp_path = os.path.join(folder_dir,images)
        op_path =os.path.join('output_val',images)
        image = Image.open(os.path.join(folder_dir,images))
        skew_angle = _skew_angle(image)
        rotated_image = image.rotate(skew_angle)
        print(skew_angle)
        image.save(os.path.join('output_val',images))
        result.append([inp_path,op_path,skew_angle])
        if(verbose):
            fig, ax = plt.subplots(ncols=2, figsize=(12,20))
            ax[0].imshow(image)
            ax[0].set_title('Input image')
            ax[1].imshow(rotated_image, cmap="gray")
            ax[1].set_title('Kew corrected by '+str(skew_angle)+' degrees')
            plt.show()


df = pd.DataFrame(result, columns=['input', 'output', 'skew'])
df.to_csv('result.csv')
