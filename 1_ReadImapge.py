import cv2
# print(cv2.__version__)

img=cv2.imread(r"C:\Users\God\Downloads\PythonPrac\OpenCV\lena.jpg", 0)
print(img)
# cv2.imshow('image', img)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
# cv2.imwrite('lena_copy.png', img)

cv2.imshow('image', img)
wait_key = cv2.waitKey(0)
if wait_key==27:                #27 is Escape key
    cv2.destroyAllWindows()
elif wait_key==ord('s'):        #s is the key
    cv2.imwrite('lena_copy.png', img)


