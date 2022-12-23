#!/usr/bin/python
import mysql.connector
class credentials:
    server = "localhost"
    username = "itachi"
    password = ""
    db = "skyChords"
    conn = mysql.connector.connect(host = server, user= username,password = password,database = db)
    cursor = conn.cursor()
    def __init__(self):
        print("class created")
    def log(self,username,password):
        sql = "select password,uid from user where email = '{}';".format(username)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result == []:
            print("Username or Password is wrong")
            return("failure")
        elif result[0][0] == password:
                print("Logged in")
                print("uid = ",result[0][1],"password = ",password)
                return('success',result[0][1])
        else:
            return("failure")


# c = credentials()

# s = c.log("shubham270902@gmail.com","1234")
# print(s)

# server = "localhost"
# username = "itachi"
# password = ""
# db = "skyChords"

# conn = mysql.connector.connect(host = server, user= username,password = password,database = db)
# cursor = conn.cursor()
# # sql = "create table user (uid int AUTO_INCREMENT UNIQUE, email varchar(30) PRIMARY KEY, password varchar(16));"
# sql = "insert into user (email,password) values('shubham270902@gmail.com','1234');"
# sql = "ALTER TABLE user uid  int  PRIMARY KEY"
# sql = "select password from user where email = 'shubham270902@gmail.com';"
# cursor.execute(sql)
# result = cursor.fetchall()
# if result == []:
#     print("Not present")
# # conn.commit()
# for x in result:
#     print(x)