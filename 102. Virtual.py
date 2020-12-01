import pyttsx3
assistant = pyttsx3.init()
assistant.say("Love yourself")
assistant.runAndWait()



#If you wants to take user input ther code be like

import pyttsx3
assistant = pyttsx3.init()
user = input(" Say something : ")
assistant.say(user)
assistant.runAndWait()
