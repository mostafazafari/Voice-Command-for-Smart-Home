# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:31:53 2023

@author: Mostafa Zafari
"""

import speech_recognition as sr
import tkinter as tk
import threading
import pyttsx3




r = sr.Recognizer()


room = {
"patterns": ["اشپزخونه", "هال", "سرویس", "اتاق", "راهرو", "پارکینگ", "حیاط", "انباری", "راه رو", "حال", ""]
}
action = {
"patterns": ["خاموش", "کم", "زیاد", "روشن", "وضعیت", "باز", "بسته", "بیشتر", "کمتر", "",]
}
objects = {
"patterns": ["لامپ", "چراغ", "پلیر", "تلوزیون", "پرده", "کولر", "اسپیکر", "شیر برقی", "قفل", "", "",]
}

command = {
  "room" : room,
  "action" : action,
  "objects" : objects
}                       #This is a list of several possible Persian command 
                        # to control different objects in a smart house.




def V_input():
    
    '''
    This function tries to understand the command from voices and passes it to the 
    control center. To do that, a voice that contains a specific command is received
    via a mic or a WAV file. The voice is converted to text using the speech_recognition
    library. The algorithm seeks specific keywords and places them in their relevant
    variables. At the end, a string is generated that is understandable for the control
    center and activate some actions in different places.

    '''
    
    
    Input_Voice = 1 # 0 for importing from Mic and 1 for importing from file
    
    
    
    if Input_Voice == 0:
       with sr.Microphone() as source:
           print('--------------------------------------------------------------')
           print('Say Something')
           r.adjust_for_ambient_noise(source)
           audio_text = r.listen(source, timeout=3,)
           
           
       string = r.recognize_google(audio_text, show_all=True,language= "fa-IR")
       string = string["alternative"][0]["transcript"]
       string = string.split()
       
     
    elif Input_Voice == 1:
            with sr.AudioFile('testv2.4.wav') as s:
                audio_text = r.listen(s)
                
                
            string = r.recognize_google(audio_text, show_all=True,language= "fa-IR")
            string = string["alternative"][0]["transcript"]
            string = string.split()
          
    
         
        
    line = ['خطا','خطا','خطا']
    for i in range (len(string)):
        if string[i] in command['room']['patterns']:
            line[0] = string[i]
            #line[0] = 'room'
            
        elif string[i] in command['action']['patterns']:
            line[1] = string[i]
            #line[1] = 'action'
            
        elif string[i] in command['objects']['patterns']:
             line[2] = string[i]
            #line[2] = 'objects'
                
        elif 'خطا' in line :
            print()
            print(' Something went wrong. Try again.')
            print()
            # print (line[2]+" در "+line[0]+" باید "+line[1]+" شود ")
            # string = V_input()
            # V_input()
        
        
    Say = pyttsx3.init()
    Say.say("It's done")
    Say.runAndWait()
    #print (line[2]+" باید "+line[1]+" در "+line[0]+" شود ")
    #print (line[0]+" باید "+line[1]+" در "+line[2]+" شود ")
    print (line[2]+" در "+line[0]+" باید "+line[1]+" شود ")
    
  
        
    return 



def v_activator():
    
    '''
    This function actives the code when you call it by a predefined keyword such as
    "hey jake" and by changing the color of the robot icon, you can see 
    it is listening for your command.
    
    '''
    
    while True:
        try:

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio_text = r.listen(source, timeout=5,)
                string = r.recognize_google(audio_text)
                string = string.lower()
                
            # string = "hey jake"
            if "hey jake" in string:
                label.config(fg="red")
                V_input()
                label.config(fg='black')
                
                # audio_text = r.listen(source, timeout=5,)
                # string = r.recognize_google(audio_text)
                # string = string.lower()

                if string is None:

                    label.config(fg='black')


        except:
            label.config(fg='black')
            continue





#A simple user interface

root = tk.Tk()          
label = tk.Label(text="🤖", font=("Arial", 120, "bold"))
label.pack()

threading.Thread(target=v_activator).start()

root.mainloop()



    





  
    