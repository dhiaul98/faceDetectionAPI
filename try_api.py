###### Using API Object Detection #######
''' 
    --------------------------
    Author  : Dhiaul Ma'ruf
    Date    : 15 Januari 2020
    --------------------------

    ++++++++++++++++++++++++++++++++++++++++++++++++
    |                   DESCRIPTION:               |
    ++++++++++++++++++++++++++++++++++++++++++++++++
    Berikut Merupakan Program untuk mengunakan API,
    yang kita buat untuk mendeteksi objek yang ada 
    pada suatu gambar dengan metode post html 

    ++++++++++++++++++++++++++++++++++++++++++++++++
    |                    HOW TO USE:               |
    ++++++++++++++++++++++++++++++++++++++++++++++++
    Open your terminal and type:

    cd [PATH FOR THIS FILE]
    python tryUsingAPI.py
'''

# import the necessary packages
import requests
import cv2

# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"

#define ipCam
ipCam = "http://10.122.1.62:4747/video/"#Ganti IP kamera dengan IP kamera yang akan di gunakan

cap = cv2.VideoCapture(ipCam)#Jika tidak menggunakan IP camera, tetapi menggunakan USB camera, ganti ipcam dengan index dari kamera (0,1,dll)
while True:
    ret, image = cap.read()
    ret, jpg = cv2.imencode('.jpg', image)
    payload = {"image": jpg}
    
    r = None
    #Try to request post method
    try:
        r = requests.post(url, files=payload).json()
    except:
        print("Link tidak ada")
    
    if r is not None:
        print ("{}".format(r))
        
        # loop over the faces and draw them on the image
        for (kelas,startX, startY, endX, endY) in r["faces"]:
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            print("kelas:{kelas}, ".format(kelas=kelas) + "pada kordinat " + str(startX) + " " + str(startY) + " "+ str(endX) + " " + str(endY))
    
    # show the output image
    cv2.imshow("stream", image)
    
    #break when 'esc' key pressed
    if cv2.waitKey(1)==27:
        break
