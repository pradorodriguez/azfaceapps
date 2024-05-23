'''
Install the following python packages:

pip install azure-cognitiveservices-vision-face msrest opencv-python
'''

import os
from dotenv import load_dotenv
import cv2
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()
# This key will serve all examples in this document.
KEY = os.getenv("VISION_KEY")

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = os.getenv("VISION_ENDPOINT")

# Create a FaceClient
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Detect faces in an image
detected_faces = face_client.face.detect_with_url('https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/Face/images/Family1-Mom1.jpg?raw=true')

# Load the image using OpenCV
img = cv2.imread('pics/family1-mom1.jpg')

# Function to draw a rectangle on the image
def draw_rectangle(img, face_rectangle):
    # Calculate the coordinates of the rectangle
    left = face_rectangle.left
    top = face_rectangle.top
    right = left + face_rectangle.width
    bottom = top + face_rectangle.height

    # Draw the rectangle on the image
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

# Loop through each face
for face in detected_faces:
    # Get the face rectangle
    face_rectangle = face.face_rectangle

    # Draw the rectangle on the image
    draw_rectangle(img, face_rectangle)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
