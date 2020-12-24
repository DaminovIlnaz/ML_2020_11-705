import numpy as np
import matplotlib.pyplot as plt
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def resize(image, width, height, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    r = width / float(w)
    dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)


def find_face(img_path):
    img = cv2.imread(img_path)
    img = resize(img, 500, 500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
    print("Found {0} faces!".format(len(faces)))

    # Выделить лицо прямоугольником
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Faces found', img)
    cv2.waitKey(0)

find_face("img2.jpg")
find_face("img1.jpg")
