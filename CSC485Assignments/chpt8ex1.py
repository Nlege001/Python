# ch8/example1.py

import cv2

im = cv2.imread('input/ship.jpg') # takes a path of an image file and returns an image object
cv2.imshow('Test', im) # take a string and an iimage object and displays it in another window
                    # the string specifies the title of the string.
                    # this method should be followed by waitkey()
cv2.waitKey(0) # press any key to move forward here
               # takes a number and blocks thhe program for miliseconds

print(im)
print('Type:', type(im))
print('Shape:', im.shape)
print('Top-left pixel:', im[0, 0])
print('Done.')
