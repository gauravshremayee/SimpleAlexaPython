import speech_recognition as sr 
from gtts import gTTS
import os
import re
mytext = 'Ok Sir, Alisha aapke liye play kar rahi hai ye song! Jai Hind'

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")


#enter the name of usb microphone that you found 
#using lsusb 
#the following name is only used as an example 
mic_name = "USB PnP Sound Device: Audio (hw:2,0)"
#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 

  
#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 
  
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
        

  
#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 

global child_pid


def excel():
        print("Starting Demo...")
        proc = subprocess.Popen(["python3", "demo.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        child_pid=proc.pid
        
        try: 
          text = r.recognize_google(audio) 
          print ("your music demand is: " + text )
          os.system("omxplayer -o alsa welcome.mp3")
          os.system("vlc --fullscreen jaggjitteya.mp4")
          #error occurs when google could not understand what was said 
      
        except sr.UnknownValueError: 
          print("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
          print("Could not request results from Google   Speech Recognition service; {0}".format(e))
          
          
def internet(): 
        os.system("start chrome.exe")
        
def media(): 
        os.system("start wmplayer.exe")
        
        
def stop(): 
        print("Stopping the Task....")        
        os.kill(child_pid, signal.SIGTERM)
        
def mainfunction(source): 
        audio = r.listen(source) 
        user = r.recognize(audio) 
        print(user) 
        if user == "Excel": 
                excel() 
        elif user == "Internet": 
                        internet() 
        elif user == "music": 
                media()
                
                
                

if __name__ == "__main__": 
  r = sr.Recognizer() 
  with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
    r.adjust_for_ambient_noise(source) 
    print ("Say Something")
    #listens for the user's input 
    while 1: 
      mainfunction(source) 
      
    
