#!/home/itachi/miniconda3/bin/python3.9
from plistlib import UID
import re
from flask import *
import json
from collections import UserList, defaultdict
from numpy import result_type
import login
import otp
import note

o = otp.otp_handler()
otp_holder = []

app = Flask(__name__)

def create_msg(text,name = 'txt'):
    msg = {
        name : text 
    }
    msg = json.dumps(msg)
    return msg

def fetch_msg(result,name):
    result = json.loads(result)
    st = result[name]
    return st

def fetch_username(result):
    result = json.loads(result)
    username = result['username']
    return username

def fetch_password(result):
    result = json.loads(result)
    passw = result['password']
    return passw

def fetch_otp(result):
    result = json.loads(result)
    otp = result['otp']
    return otp


@app.route('/', methods = ['GET'])
def index():
    msg = {
    "txt" :   "This message is sent from python"
    }
    msg = json.dumps(msg)
    return msg

@app.route('/login',methods = ['POST'])
def pm():
    if request.method == "POST":
        result = request.data
        username = fetch_username(result)
        passw = fetch_password(result)
        l = login.credentials()
        status,uid = l.log(username,passw)
        # status = l.log(username,passw)
        print(status)
        msg = {
            'uid' : uid,
            'status' : status,
        }
        msg = json.dumps(msg)
        return msg

@app.before_request
def before_request():
    global l
    l = login.credentials()
    return None

        
@app.route('/forgotpassword',methods =['POST'])
def forgotpassword():
    if request.method == 'POST':
        result = request.data
        username = fetch_username(result)
        l = login.credentials()
        status =  l.forgot_password(username)
        status = json.dumps(status)
        return status
        
@app.route('/mainscreen',methods = ['POST'])
def main_screen():
    if request.method == 'POST':
        result = request.data
        result = json.loads(result)
        print(result)
        scale = fetch_msg(result,"scale")
        key = fetch_msg(result,'key')
        arp = fetch_msg(result,'arp')
        print(scale,key,arp)
        return create_msg('success')
     
@app.route('/generate_otp',methods = ['POST'])
def otp_handler():
    if request.method == 'POST':
        result = request.data
        username = fetch_username(result)
        l = login.credentials()
        status = l.check_existence(username)
        if status == False:
            otp = o.generator(username)
            l.send_mail(username,otp)
            print(otp)
            msg = otp
            msg = json.dumps(msg)
            return msg
        else:
            msg = "Account exists"
            msg = json.dumps(msg)
            return msg

@app.route('/register',methods =['POST'])
def register():
    if request.method == "POST":
        result = request.data
        username = fetch_username(result)
        passw = fetch_password(result)
        otp = fetch_otp(result)
        l = login.credentials()
        status = l.check_existence(username)
        if status == False:
            print("register",otp_holder)
            status = o.check_otp(username,otp)
            if status == True:
                status = l.check_existence(username)
                if status == False:
                    logid = l.create(username,passw)
                    msg = {
                        'logid' : logid,
                        'auth' : 'success',
                    }
                    msg = json.dumps(msg)
                    return msg
            else:
                return create_msg("Wrong")
        else:
            return create_msg("exists")
    

@app.route('/delete',methods =['POST'])
def delete_acc():
    print("hehe")
    if request.method == "POST":
        result = request.data
        login_id = fetch_msg(result,'uid')
        print(login_id)
        l = login.credentials()
        status = l.delete_acc(login_id)
        msg = create_msg("success")
        return msg

    
@app.route('/delete_fav',methods =['POST'])
def dlt_fav():
    if request.method == "POST":
        result =request.data
        wav_name = fetch_msg(result,'wav_name')
        wav_name = str(wav_name)
        l = login.credentials()
        status = l.delete_fav(wav_name)
        return create_msg("success")
    
@app.route('/edit_fav',methods =['POST'])
def edit_fav():
    if request.method == "POST":
        result =request.data
        wav_name = fetch_msg(result,'wav_name')
        new_name = fetch_msg(result,'new_name')
        uid = fetch_msg(result,'uid')
        wav_name = str(wav_name)
        new_name = str(new_name)
        uid = str(uid)
        new_name = new_name + "-" +  uid + ".wav"
        l = login.credentials()
        status = l.edit_fav(wav_name,new_name)
        return create_msg("success")
    
      
        
@app.route('/axios',methods =['POST'])
def getuid():
    if request.method == "POST":
        result = request.data
        username = fetch_username(result)
        msg = create_msg(username)
        return msg

@app.route('/prog_creator',methods = ['POST'])
def get_progression():
    if request.method == "POST":
        result = request.data
        scale = fetch_msg(result,'scale')
        arp = fetch_msg(result,'arp')
        key = fetch_msg(result,'key')
        uid = fetch_msg(result,'uid')
        n = note.scale_generator()
        progression,chords,wfn,mfn = n.create_progression(key,scale,arp,uid)
        print("p",progression)
        msg ={
            "prog": progression,
            "chords": chords,
            "wfn": wfn,
            "mfn": mfn
        }
        msg = json.dumps(msg)
        return msg
        
@app.route('/favourite',methods = ['POST'])
def add_favourite():
    if request.method == 'POST':
        result = request.data
        print("fetched")
        Login_id = fetch_msg(result,'uid')
        prog_name = fetch_msg(result,'prog_name')
        prog = fetch_msg(result,'prog')
        # print(Login_id, prog_name, prog)
        l = login.credentials()
        status = l.add_to_favourite(Login_id,prog_name,prog)
        if status == "success":
            txt = {
                'msg' : "success"
            }
            return json.dumps(txt)
        else:
            txt = {
                'msg' : "failure"
            }
            return json.dumps(txt)
        
@app.route('/saved',methods = ['POST'])
def access_saved():
    if request.method == 'POST':
        print("got it")
        result = request.data
        login_id = fetch_msg(result,'uid')
        print(login_id)
        l = login.credentials()
        status,name_list,prog_list = l.access_favourites(login_id)
        if status == "success":
            msg = {
                'status' : 'success',
                "name_list" : list(name_list),
                "prog_list" : list(prog_list) 
            }
            msg = json.dumps(msg)
            return msg
        elif status == "failure":
            print("hehe")
            msg = {
                'status' : 'failure'
            }
            msg = json.dumps(msg)
            return msg
    
@app.route('/wav',methods = ['POST'])
def get_wav():
    wav_file = "http://192.168.1.205/wav_files/excuses.wav"
    return wav_file

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000 ,  debug=True,threaded=True)
        
# @app.route('/test',methods =['POST'])
# def test():
#     if request.method == 'POST':
#         result = request.data
#         result = json.loads(result)
#         result = result['txt']
#         l = login.credentials()
#         st = l.test(result)
#         st = str(st)
#         txt = {
#             'str' : st
#         }
#         txt = json.dumps(txt)
#         return txt
