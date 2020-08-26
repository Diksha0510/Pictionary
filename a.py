import cv2
import numpy as np
from matplotlib import pyplot as plt
from tensorflow import keras

class pictionary():



# function to predict the drawing using the model
    def predict(self,im1):
        pred_probab=self.model.predict(im1)[0]
        pred_class = list(pred_probab).index(max(pred_probab))
        if(max(pred_probab)>0.5):
            print(max(pred_probab), self.pred[pred_class-1])

# mouse callback function
    def pic_draw(self,event,former_x,former_y,flags,param):

        if event==cv2.EVENT_LBUTTONDOWN:
            self.drawing=True
            self.current_former_x,self.current_former_y=former_x,former_y

        elif event==cv2.EVENT_MOUSEMOVE:
            if self.drawing==True:
                if self.mode==True:
                    cv2.line(self.im,(self.current_former_x,self.current_former_y),(former_x,former_y),(0,0,255),1)
                    self.current_former_x = former_x
                    self.current_former_y = former_y


        elif event==cv2.EVENT_LBUTTONUP:
            self.drawing=False
            if self.mode==True:
                cv2.line(self.im,(self.current_former_x,self.current_former_y),(former_x,former_y),(0,0,255),1)
                self.current_former_x = former_x
                self.current_former_y = former_y
    # return former_x,former_y


# im=np.zeros((255,255), dtype='float32')

    def __init__(self):
        self.drawing=False # true if mouse is pressed
        self.mode=True # if True, draw rectangle.
        self.pred=["alarm clock","bicycle","bed","airplane","apple","belt","banana","cake"]
        self.model=keras.models.load_model('/home/diksha/pictionary/my_model2.h5')

        self.im=cv2.imread(r'/home/diksha/pictionary/White.jpg')
        self.img1=cv2.imread(r'/home/diksha/python/black.JPG')
        cv2.namedWindow("Pictionary")
        cv2.setMouseCallback('Pictionary',self.pic_draw)

    def run(self):
        while(1):
            cv2.imshow('Pictionary',self.im)
            img=cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
            th, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
            blur1 = cv2.GaussianBlur(img, (5, 5), 0)
            cnts, heir= cv2.findContours(blur1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            if(len(cnts)>1):
                cv2.drawContours(self.img1, cnts,-1, (255,255,255),5)

                cnt = max(cnts, key=cv2.contourArea)

                print(cv2.contourArea(cnt))
                if cv2.contourArea(cnt) > 2000:
                    x, y, w, h = cv2.boundingRect(cnt)
                    self.im1 = self.img1[y:y + h, x:x + w]

                    self.im1 = cv2.resize(self.im1, (28, 28))
                    self.im1 = np.array(self.im1, dtype=np.float32)
                    self.im1 = np.reshape(self.im1, (-1, 28, 28, 1))
                    self.predict(self.im1)
    

            k=cv2.waitKey(1)&0xFF
            if k==27:
                break

            elif k==97:
                self.im=cv2.imread(r'/home/diksha/python/White.jpg')
                self.img1=cv2.imread(r'/home/diksha/python/black.JPG')

        cv2.destroyAllWindows()

if __name__ == '__main__':
    pictionary().run()

# /kaggle/input/quick-draw/full_numpy_bitmap_alarm clock.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_bicycle.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_bed.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_airplane.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_apple.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_belt.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_banana.npy
# /kaggle/input/quick-draw/full_numpy_bitmap_birthday cake.npy
