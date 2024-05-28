import pyttsx3


try :
    
    def speak_access(speech):
        voice  = speech 
        pyttsx3.speak(voice)
except ModuleNotFoundError :
    print("You Haven't install module pyttsx3 install it  ")
    