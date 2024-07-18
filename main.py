import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_image",help="The file path of the image requires conversion.",type=str)
parser.add_argument("--out",help="Write the ascii to a txt file and save it. Specify the path to save.",type=str)
args = parser.parse_args()

image_input = args.input_image
image_data = cv2.imread(image_input,cv2.IMREAD_GRAYSCALE)
height = image_data.shape[0]
width = image_data.shape[1]
ascii_array = ["@","%","#","*","+","=","-",":",",","."," "] #["!","@","#","$","%","^","&","*","(",")",",","."] 
ratio =  height/width
new_width = 50
new_height = int( ratio * new_width )
dim = (new_width,new_height)

crop_image = cv2.resize(image_data,dim)

# We could just do this instead of ascii array by capping the intensity, but it provides more detail in the intentsity.
# cv2.imwrite("test.crop.png",crop_image)
# threshold,arr = cv2.threshold(crop_image,127,255,cv2.THRESH_BINARY) # Lower boundary 127 and higher is 255

ascii_generator = ""
row,col = crop_image.shape

for i in range(row):
    for j in range(col):
        try:
            k = crop_image[i,j]
            ascii_generator+= ascii_array[k//25]
            if j==col-1:
                ascii_generator+="\n"
        except Exception as e:
            print(e)

print(ascii_generator)

if args.out:
    with open(args.out,"w+") as f:
        f.write(ascii_generator)
        print("Wrote the ASCII to: ",args.out)
        f.close()
