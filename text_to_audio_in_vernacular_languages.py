import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from googletrans import Translator
all_language_codes = [{"Hindi":"hi"}, {"Assamese":"as"},{"Bengali":"bn"},{"Bihari":"bh"},{"Dogri":"dgr"},{"	Kannada":"kn"},{"Kashmiri":"ks"},{"	Malayalam":"ml"},{"	Marathi":"mr"},{"Nepali":"ne"},{"Punjabi":"pa"},{"Sanskrit":"sa"},{"Sindhi":"sd"},{"Tamil":"ta"},{"	Telugu":"te"},]

 #Give Language code in whib'ch you want to translate the text:=>
lang_code = 'hi'
# Provide text that you want to translate:=>
input1 = 'temsen AM'
options = Options()
# this parameter tells Chrome that
# it should be run without UI (Headless)
#options.headless = True
# launch browser with selenium:=>
browser = webdriver.Chrome('C:\\Users\\Admin\\Desktop\\sunhackkk\\chromedriver.exe', options=options) #browser = webdriver.Chrome('path of chromedriver.exe file') if the chromedriver.exe is in different folder

# copy google Translator link here:=>
browser.get("https://translate.google.co.in/?sl=auto&tl="+lang_code+"&text="+input1+"&op=translate")

# just wait for some time for translating input text:=>
time.sleep(10)

# Given below x path contains the translated output that we are storing in output variable:=>
output1 = browser.find_element("xpath",'/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/di
                               v[1]/span[1]/span/span')
output1=output1.text
# Display the output:=>
print("Translated Paragraph:=> " + output1)
from gtts import gTTS
from playsound import  playsound

mytext= output1
language='en'
myobj=gTTS(text=mytext,lang=language,slow=True)
myobj.save("welcome1.mp3")
playsound("welcome1.mp3")
