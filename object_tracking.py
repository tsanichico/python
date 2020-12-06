import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (218,165,32), 2)

    cv2.imshow('hahahproject', img)

    z = cv2.waitKey(30) & 0xff
    if z==27:
        break

cap.release()