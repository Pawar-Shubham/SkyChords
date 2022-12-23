#!/home/itachi/miniconda3/bin/python3.9
from collections import defaultdict
from os import openpty
from shelve import DbfilenameShelf
import threading
import random
import pickle

# from cairo import OPERATOR_ATOP
from numpy import empty, empty_like, printoptions

class otp_handler:
    otp_list = defaultdict(list)
    empty_list = []
    def generator(self,username):
        otp = random.randint(1000,9999)
        self.otp_list[username].append(otp)
        self.create_pickle_file(self.otp_list)
        # flusher = threading.Timer(300.0,self.flush_dict,args = (username,))
        # flusher.start()
        return otp

    def flush_dict(self,username):
        self.otp_list.pop(username)

    # def check_otp(self,username,u_otp):
    #     print(self.otp_list)
    #     if username in self.otp_list:
    #         otp = (self.otp_list[username])              
    #         if u_otp == str(otp[0]):
    #             return True
    #     else:
    #         return u_otp
    
    def check_otp(self, username,u_otp):
        otp = self.access_pickle_file(username)
        print("otp = ",otp)
        # if otp[0] != u_otp:
        #     print('failure')
        #     return False
        if int(otp[0]) == int(u_otp):
            print('success')
            return True
        else:
            return False
        
    def create_pickle_file(self,d):
        print(d)
        print("Create picke file")
        dbfile = open('otpholder','w').close()
        # pickle.dump(self.empty_list,dbfile)
        dbfile = open('otpholder','ab')
        pickle.dump(d,dbfile)
    
    
    def access_pickle_file(self,user):
        print("Access picke file")
        dbfile = open('otpholder','rb')
        data = pickle.load(dbfile)
        print(data)
        if user in data:
            dbfile = open('otpholder','ab')
            # dbfile = open('otpholder','w').close()
            return(data[user])
        else:
            return False    