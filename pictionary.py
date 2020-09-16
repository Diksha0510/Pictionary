import cv2
import numpy as np
from matplotlib import pyplot as plt
from tensorflow import keras

drawing=False
mode=True
pred=["alarm clock","bicycle","bed","airplane","apple","belt","banana","cake"]
model=keras.models.load_model('./my_model2.h5')

# function to predict the drawing using the model
def predict(im1):
    pred_probab=model.predict(im1)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    if(max(pred_probab)>0.5):
        print(pred[pred_class-1])
    
# mouse callback function
def pic_draw(event,former_x,former_y,flags,param):
    global current_former_x,current_former_y,drawing, mode, im

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        current_former_x,current_former_y=former_x,former_y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(0,0,255),1)
                current_former_x = former_x
                current_former_y = former_y

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(0,0,255),1)
            current_former_x = former_x
            current_former_y = former_y
    return former_x,former_y


global im
im=cv2.imread(r'./white.jpg')
im=cv2.resize(im, (255,255))
img1=cv2.imread(r'./black.jpg')
cv2.namedWindow("Pictionary", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Pictionary", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback('Pictionary', pic_draw)
while(1):
    c=0
    cv2.imshow('Pictionary',im)
    img=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    th, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    blur1 = cv2.GaussianBlur(img, (5, 5), 0)
    cnts, heir= cv2.findContours(blur1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if(len(cnts)>1):
        cv2.drawContours(img1, cnts,-1, (255,255,255),5)

        cnt = max(cnts, key=cv2.contourArea)
        print(cv2.contourArea(cnt))
        if cv2.contourArea(cnt) > 2000:
            x, y, w, h = cv2.boundingRect(cnt)
            im1 = img1[y:y + h, x:x + w]
            im1 = cv2.resize(im1, (28, 28))
            im1 = np.array(im1, dtype=np.float32)
            im1 = np.reshape(im1, (-1, 28, 28, 1))
            predict(im1)

    k=cv2.waitKey(1)&0xFF
    if k==27:
        break

    elif k==97:
        im=cv2.imread(r'./white.jpg')
        im=cv2.resize(im, (255,255))
        img1=cv2.imread(r'./black.jpg')

cv2.destroyAllWindows()


# /kaggle/input/quick-draw/full_numpy_bitmap_alarm clock.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_bicycle.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_bed.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_airplane.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_apple.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_belt.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_banana.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_birthday cake.npy
