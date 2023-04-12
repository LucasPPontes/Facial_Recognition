import cv2
from deepface import DeepFace

img = cv2.imread("./img/Hasbulla.jpg")

emotion = DeepFace.analyze(img, actions=("emotion"))

age = DeepFace.analyze(img, actions=("age"))

print(age)
print("=-" * 50)
print(emotion)