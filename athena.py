from gpiozero import MotionSensor, AngularServo
from picamera import PiCamera
import os
from twilio.rest import Client
from time import sleep
import keyboard 



pir = MotionSensor(4)
camera = PiCamera()
 
servo = AngularServo(14, min_pulse_width=0.0006, max_pulse_width=0.0023)



print("Welcome to Athena Security Sentry")
command = input(''' ''')

img = 0

def take_photo():
    global img
    img = img + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % img)
    print('A photo has been taken')
    sleep(2)

def stop_camera():
    camera.stop_preview()
    exit()

def send_message():   
    account_sid='AC2f3d6f77e5f97c2a97676f6dcb1e3749'
    auth_token='0d01619c6d481b0f0ae40421ce02f10a'
    client = Client(account_sid, auth_token)

    message = client.messages \
    .create(
         body='Patrolling the Mojave almost makes you wish for a nuclear winter',
         from_='+12283385083',
         to='+15106958564'
     )




if "activate" in command:
 camera.start_preview()
 sleep(10)
 camera.stop_preview

if "turn" in command:
    camera.start_preview() 
    servo.angle = -90
    sleep(5)
    servo.angle = 50
    sleep(5)
    servo.angle = 0
    camera.start_preview()



else:
    print("Invalid command! Try again!")


    while True:
        if pir.motion_detected:
            for i in range (2,4):
             i = i + 1
            take_photo()
            send_message() 
            print(pir.motion_detected)

if keyboard.read_key() == "a":
       while(keyboard.read_key() == "a"):
         servo.angle = -100
        
 
  
                    