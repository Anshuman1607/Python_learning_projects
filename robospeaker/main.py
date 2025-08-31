import win32com.client
if __name__ == '__main__':
 print("Welcome to Robospeaker 1.1. Created by Anshuman Mishra")
 speaker = win32com.client.Dispatch("SAPI.SpVoice")
 while True:
     name = input("Enter what you want me to say:")
     if name == "exit":
         break
     speaker.Speak(name)