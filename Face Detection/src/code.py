import cv2;
face_cascade = cv2.CascadeClassifier(r"C:\Users\user_name\AppData\Local\Programs\Python\Python38-32\haarcascade_frontalface_default.xml");
video = cv2.VideoCapture(0);
while True:
    check, frame = video.read();
    faces = face_cascade.detectMultiScale(frame,
                                          scaleFactor=2.1, minNeighbors=5);
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,455,0), 3);

    cv2.imshow('Face Detector', frame);

    key = cv2.waitKey(1);

    if key == ord('0'):
        break;
video.release();
cv2.destroyAllWindows();
