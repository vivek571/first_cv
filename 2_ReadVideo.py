import cv2

#Opening a live video from camera
cap = cv2.VideoCapture(0)
#When opening a video file
#cap = cv2.VideoCapture(<file name>)

#to save the cam video, use below code
fourcc = cv2.VideoWriter(*'XVID')
out=cv2.VideoWriter('out.avi', fourcc, 20.0, (640,480))

#when using a video file, use below code
while(cap.isOpened()):
#while(True):
    ret, frame = cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        #change video color to grayscale
        grey_color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('video', frame)
        cv2.imshow('video', grey_color)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()