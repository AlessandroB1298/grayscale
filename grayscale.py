import cv2 as cv
import os
from tqdm import tqdm
import sys


##* This is a good example of a single file but we want to use an entire folder.

def imageToGray():
    image_folder = os.path.join('/Users/aidanbongiorno/Desktop/grayscale_alchemie/images')
    output_folder = "./gray_images"
    os.makedirs(output_folder, exist_ok=True)

    for (root, dirs, files) in os.walk(image_folder):
        for f in tqdm(files, desc="Changing to gray"):
           img_path = os.path.join(root, f)
           img = cv.imread(img_path)
           
           if img is None:
               sys.exit("Can't find file", img_path)
           else:
            gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            output_path = os.path.join(output_folder, f) # join to the output path
            cv.imwrite(output_path, gray_img)
            print(f"Conversion successful for {f}")


    

def main():
    
    
   imageToGray()
    
if __name__ == "__main__":
    main()