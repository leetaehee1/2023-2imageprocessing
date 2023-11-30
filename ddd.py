import numpy as np
from google.cloud import vision
from PIL import Image, ImageDraw
import cv2

eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

class LeftEye:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class RightEye:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def detect_face(face_file, max_results=10):
    client = vision.ImageAnnotatorClient(
        client_options={"api_key": " "}
    )
    content = face_file.read()
    image = vision.Image(content=content)
    responses = client.face_detection(image=image, max_results=max_results)
    return responses.face_annotations

def detect_eyes(gray_image):
    left_eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)
    right_eyes = []  # Define how to detect right eyes or modify as needed
    return left_eyes, right_eyes

def show_face(imagefile, faces, output_filename):
    img = cv2.imread(imagefile)

    for face in faces:
        box = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
        cv2.polylines(img, [np.array(box)], True, (255, 0, 0), 2)
        cv2.putText(img, str(format(face.detection_confidence, ".2f")),
                    (face.fd_bounding_poly.vertices[0].x,
                     face.fd_bounding_poly.vertices[0].y - 20),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

    for face in faces:
        box = [(vertex.x, vertex.y) for vertex in face.fd_bounding_poly.vertices]
        cv2.polylines(img, [np.array(box)], True, (255, 255, 0), 2)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    left_eyes, right_eyes = detect_eyes(gray)

    for (ex, ey, ew, eh) in left_eyes:
        left_eye = LeftEye(ex, ey, ew, eh)
        # Do something with left eye, e.g., draw a rectangle
        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    for (ex, ey, ew, eh) in right_eyes:
        right_eye = RightEye(ex, ey, ew, eh)
        # Do something with right eye, e.g., draw a rectangle
        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_filename = "./img/children.jpg"
output_filename = "./googleoutp.jpg"

with open(input_filename, "rb") as image:
    faces = detect_face(image, 10)
    print(f'Found {len(faces)} face')
    show_face(input_filename, faces, output_filename)
