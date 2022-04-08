import cv2                                                                #import the cv2 library
cap = cv2.VideoCapture(0)                                                 #setup the camera into video source
model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")      #Importing the HaarCascade Classifier
while True:
    ret, img = cap.read()
    face  = model.detectMultiScale(img)                                   #detectMultiScale() function to detect the faces of the video
    if len(face) == 0:
        print("NO FACES")
    else:
        x1 = face[0][0]
        y1 = face[0][1]
        x2 = face[0][2] + x1
        y2 = face[0][3] + y1 
        cimg = img[y1:y2 , x1:x2]
        blur_img = cv2.blur(cimg, (50,50))
        rect_img = cv2.rectangle(img, (x1,y1), (x2,y2), [0,255,0],2)
        img[y1:y2 , x1:x2] = blur_img
        
        cv2.imshow("Blurred Face",img)                                   #cv2.imshow()-To Show the window of that particular video
        cv2.imshow("Square_on_image",rect_img)
        if cv2.waitKey(100) == 13:                                       #waitkey() function permits to wait for a specific time in milliseconds until we press the “enter” on the keyword
            break
cv2.destroyAllWindows()                                                  #cv2.destroyAllWindows() This function is used to abolish all the windows we created
