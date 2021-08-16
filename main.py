
from os import RTLD_NODELETE
from flask import Flask, render_template, request, jsonify, Response,redirect
import threading
import time

from werkzeug import debug
from bot import answer,randomChat
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET KEY']= 'hw4WEB'
socketio = SocketIO(app)


autoMessage=[]
cntt=0
FLASK_CONNECT = {}

def autoChat():
    global autoMessage
    global cntt
    while 1:
        time.sleep(1)
        cntt+=1
        if(cntt %10 == 0):
            autoMessage.append(randomChat())

auto_bot = threading.Thread(target=autoChat)
auto_bot.start()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/chat",methods=['POST'])
def chat():
        global autoMessage
        global cntt
        cntt=0
        autoMessage.clear()
        mess = answer(request.form.get("message")) 
        return jsonify({'user':'Bot','message':mess})


@app.route("/shortPolling")
def short():
    return render_template('short.html')

@app.route("/shortPolling/chat", methods=['POST'])
def chat_short():
    global autoMessage 
    try:
        mess=autoMessage.pop()
        return jsonify({'user':'Auto chat','message' : mess})
    except:
        return Response('',status=404)

@app.route("/longPolling",methods=['GET','POST'])
def long():
    return render_template('long.html')

@app.route("/longPolling/chat", methods=['POST'])
def chat_long():
    global autoMessage 
    while(len(autoMessage)<1):
        pass
    mess=autoMessage.pop()
    return jsonify({'user':'Auto chat','message' : mess})


@app.route("/socket")
def socket():
    return render_template("socket.html")

@socketio.on('connect')
def on_connect():
    FLASK_CONNECT[request.sid] = True

@socketio.on('disconnect')
def on_disconnect ():
    FLASK_CONNECT[request.sid] = False
   
@socketio.on('message')
def on_message(data,methods=['POST','GET']):
    global cntt
    cntt =0
    mess = answer(data.get('message'))
    socketio.send({'user': 'Bot','message' : mess}, to = request.sid)


@socketio.on('sendAuto')
def on_sendAuto ():
    if (FLASK_CONNECT[request.sid]):
        if(len(autoMessage)>0):
            mess=autoMessage.pop()
            socketio.send({'user':'Auto chat','message' : mess}, to= request.sid)

if __name__ == '__main__':
    socketio.run(app, debug= True)