#! /usr/bin python
# -*- coding:utf-8 -*-

from PIL import Image
import pytesseract
import argparse
import cv2
import os

#argument parser
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("-r", "--resim", required=True, help="OCR yapilacak resmin yolu")
arg_parse.add_argument("-i", "--islem",  help="resim uzerinde ilave islem yapmak için")
args = vars(arg_parse.parse_args())

#uploading image and converting to gray scale

resim = cv2.imread(args["resim"])
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

#if entered -i parameter from commandline , this will work
if args["islem"] == "thresh" :
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# median blur filter for removing noises from image

elif args["islem"] == "blur" :
    gray = cv2.medianBlur(gray, 3)

dosya_Adi = "{}.png".format(os.getpid())
cv2.imwrite(dosya_Adi, gray)

#Uploading PIL image for OCR

metin = pytesseract.image_to_string(Image.open(dosya_Adi))
os.remove(dosya_Adi)

print(metin)

cv2.imshow("ilk hali", resim)
cv2.imshow("son hali", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

