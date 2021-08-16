import random
from datetime import datetime

from werkzeug.utils import invalidate_cached_property

def answer(ques):
    ques=ques.lower()

    if ques in ["hi", "hey", "hello", "good morning", "good afternoon"] :
        ans="hi"
    elif ques in ["who are you", "are you human", "are you bot", "are you human or bot"]:
        ans ="I am just a bot"
    elif ques == "what is your name?":
        ans = "I am nameless. I don't have a name"
    elif 'time' in ques:
        now = datetime.now()
        ans = now.strftime("%H : %M : %S")
    elif ques in ["bye", "good bye", "goodbye", "see you later"] :
        ans="Bye!"
    else:
         ans ="I don't understand"
    return ans

randomAns=["I'm always here.","I'm listening.","Ask me anything.","Are you there?"]

def randomChat():
    return random.choice(randomAns)