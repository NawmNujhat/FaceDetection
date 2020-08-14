import cv2
video = cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    check,frame=video.read()
    if check:
        faces = classifier.detectMultiScale(frame)
        for x, y, w, h in faces:
             frame= cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow("Window",frame)
    key = cv2.waitKey(30)
    if (key == ord('q')):
        break
video.release()
cv2.destroyAllWindows()