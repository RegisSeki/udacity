import os
import re

def rename():
  image_list = os.listdir("/Users/regisseki/Documents/Regis PVT/Projetos/Udacity/lesson5_image")


  for image_list_without_number in image_list:
    image_list = re.sub("\d+", "", file_name)

