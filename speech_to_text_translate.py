# import required module 
import speech_recognition as sr 
from textblob import TextBlob
#from speech_helpers import transcribe_audio
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
# explicit function to take input commands 
# and recognize them 
def takeCommandHindi(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        # seconds of non-speaking audio before 
        # a phrase is considered complete 
        print('Listening') 
        r.pause_threshold = 0.7
        audio = r.listen(source) 
        try: 
            print("Recognizing") 
            Query = r.recognize_google(audio, language='hi-In') 
            # for listening the command in indian english 
            print("the query is printed='", Query, "'") 
        # handling the exception, so that assistant can 
        # ask for telling again the command 
        except Exception as e: 
            print(e) 
            print("Say that again please") 
            return "None"
        return Query 
# Driver Code        
# call the function 
sentence=takeCommandHindi() 
hi_blob=TextBlob(sentence)
print(hi_blob.detect_language())
print(hi_blob.translate(to='en'))
t=hi_blob.translate(to='en')
#print(ss)
print(t.sentiment)