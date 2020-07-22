
import pyttsx3 
  
# init function to get an engine instance for the speech synthesis  
##engine = pyttsx3.init(sapi5)
##voices = engine.getProperty('voices')
##for voice in voices:
  ## engine.setProperty('voice', voice.id)
   ##engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()

engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()