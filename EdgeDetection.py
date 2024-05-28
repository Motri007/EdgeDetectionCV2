import cv2


image = cv2.imread("C:\\Users\\Motri\\Pictures\\Wallpaper\\5-cm-centimeters-per-second-wallpaper-1080p-90069.jpg")
grayedImage =cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
Blurredimage = cv2.GaussianBlur(grayedImage , (3 ,3), 0)
Edges = cv2.Canny( Blurredimage ,15 , 35)
cv2.imshow('Image' ,image)
cv2.imshow('the edges' , Edges)
cv2.waitKey(0)