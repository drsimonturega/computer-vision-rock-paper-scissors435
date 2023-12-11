import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5', compile=False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
weapon_list = ["rock","paper","sissors","nothing"]
start_time = time.time()

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print((time.time() - start_time))
    if (time.time() - start_time) >= 6 or cv2.waitKey(1) & 0xFF == ord('c'):
        #print(type(prediction))
        prediction = np.ndarray.tolist(prediction)
        #print(prediction)
        prediction = prediction[0]
        rps_test = np.array(prediction)
        weapon_of_computer = weapon_list[np.argmax(rps_test)]
        print(f'You chose {weapon_of_computer}')
        break
            
# After the loop release the cap object
#print(f'check {prediction}')
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
