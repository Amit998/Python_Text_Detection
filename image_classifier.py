

import tensorflow.keras
import numpy as np
import cv2


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


class Classifier:

    def __init__(self, modelPath, labelsPath=None):
        self.model_path = modelPath
        np.set_printoptions(suppress=True)
        self.model = tensorflow.keras.models.load_model(self.model_path)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    

    def getPrediction(self, img, draw= True, pos=(50, 50), scale=2, color = (0,255,0)):
        imgS = cv2.resize(img, (224, 224))
        image_array = np.asarray(imgS)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        self.data[0] = normalized_image_array
        prediction = self.model.predict(self.data)
        indexVal = np.argmax(prediction)
        return indexVal



def main():
    cap = cv2.VideoCapture(0)
    maskClassifier = Classifier('Model/keras_model.h5')
    while True:
        _, img = cap.read()
        predection = maskClassifier.getPrediction(img)
        print(predection)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
