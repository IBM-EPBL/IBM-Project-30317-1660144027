#import opencv librariy
import cv2
#import numpy
import numpy as np
#import image function from keras
from keras.preprocessing import image
#import load_model from keras
from keras.models import load_model
#import client from twilio API
from twilio.rest import Client
#imort playsound package
from playsound import playsound

#load the saved model
model = load_model(r'forest1.h5')
#define video
video = cv2.VideoCapture(0)
#define the features
name = ['forest','with forest']

account_sid = 'AC557b4c7a685d072baa73125f61031af3'
auth_token = 'a59cd5e5fdfddcc9ab008273557f8f78'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Forest fire is detected , stay alert',
         from_='+14247991869',
         to='+918940722793'
     )

print(message.sid)

#import opencv library
import cv2
#import numpy
import numpy as np
#import images and load_model function from keras
from keras_preprocessing import image
from keras.models import load_model
#import client from twilio API
from  twilio.rest import Client
#import playsound package
from playsound import playsound

#load the saved model
model = load_model(r'forest1.h5')
video = cv2.VideoCapture(0)
name = ['forest','with fire']

while(1):
    
    
    success, frame=video.read()
    cv2.imwrite("image.jpg",frame)
    img=image.load_img("image.jpg",target_size=(128,128,3))
    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    pred=model.predict(x)
    p=pred[0]
    print(pred)
    ##cv2.putText(frame,"predicted class= "+str(name[p]), (100,100),
      ##          cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
    pred=model.predict(x)
    
  
    if pred[0]==1:
       
       
       account_sid = 'AC557b4c7a685d072baa73125f61031af3'
       auth_token = 'a59cd5e5fdfddcc9ab008273557f8f78'
       client = Client(account_sid, auth_token)
       message=client.messages\
       .create(
       body='Forest Fire is Detected, stay alert',
       from_='+14247991869',to='+918940722793')
       
       print(message.sid)
       print('Fire Detected')
       print('SMS sent')
       playsound(r'C:\Users\My\Downloads\buzzer.mp3')
       
    else:
        print("No Danger")  
        
        cv2.imshow("image",frame)  
        
    if cv2.waitKey(1) & 0xFF ==ord('a'):
        break
video.release()
cv2.destroyAllWindows()

        