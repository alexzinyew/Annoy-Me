from flask import *
import json,time
from playsound import playsound
from plyer import notification

app = Flask(__name__)

Blacklist = ["alexzinyew"]

@app.route('/play/', methods=['POST'])
def post_page():
    data = request.get_json()

    User = data['User']
    Sound = data['Sound']
    Notif = data['Notif']

    if Notif:
        notification.notify(
                title = "From: {}".format(User),
                message = Sound,
                app_icon = None,
                timeout = 3,
            )
        print("{} said {}".format(User,Sound))
    else: 
        path = "{}.mp3".format(Sound)
        playsound(path)
        print("{} played {}".format(User,Sound))
    

    return "Sucess"
    
app.run(port=7777)
