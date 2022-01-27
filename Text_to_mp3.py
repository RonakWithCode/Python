import os
from gtts import gTTS # pip install gTTS

# file_path = input("file name or path ") 
# "\\"
# z:\code\ This is not work in python
# z:\\code\\ This is work in python

file_path = "work.txt" 
with open(file_path ,"r")as f:
    Text = f.read()
Language = "en"

text_gtts = gTTS(text=Text,lang=Language,slow=False)
text_gtts.save("Sample.mp3")


f.close()
os.system("Sample.mp3")
