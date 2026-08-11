import hashlib
from cryptography.fernet import Fernet 
import os
import json


class PASSWORD:
   def __init__(self):
    self.M_Token=None
    self.A_Token=None
    if(os.path.exists("key.txt")):
     with open("key.txt","rb") as f:
      key=f.read()
     self.F=Fernet(key)
    else:
     key=Fernet.generate_key()
     self.F=Fernet(key)
     with open("key.txt","wb") as f:
      f.write(key)
    db=self.database()
    if(db["admin"]["name"]=="" or db["admin"]["password"]==""):
     print("WELLCOME SIR LET'S START ")
     name=input("set username :")
     pin=input("set a pin ")
     self.save_admin(name ,pin)
     self.main()
    else:
     pas=input("enter password :")
     token =self.check_hash(pas)
     if(token):
      print("wellcome back sir ")
      self.main()
     else:
      print("wrong password")
     

   def database(self):
    if(os.path.exists("database.json")):
     with open("database.json","r") as f:
      database=json.load(f)
     return database
    else:
     database={"admin":{
                 "name":"",
                 "password":""},
               "passwords":{}
              }
     with open("database.json","w") as f:
      json.dump(database,f, indent=4)
     return database

   def save_database(self,data):
    with open("database.json","w") as f:
     json.dump(data,f,indent=4)

   def encry(self,text):
    return self.F.encrypt(text.encode()).decode("utf-8")
    return data

   def decry(self,en):
    d_d=self.F.decrypt(en)
    d_=d_d.decode()
    return d_
    return d_d

   def hash(self,text):
    hash =hashlib.sha256(text.encode()).hexdigest()
    return hash 

   def save_admin(self, name ,password):
    db=self.database()
    db["admin"]["name"]=name
    db["admin"]["password"]=self.hash(password)
    self.save_database(db)

   def save_password(self,name,pas):
    db=self.database()
    db["passwords"][name]={
      "name":name,
      "password":self.encry(pas)}
    self.save_database(db)

   def see_all(self):
    db=self.database()
    for i,user in enumerate(db["passwords"],start=1):
     print(i,".",user,"==",self.decry(db["passwords"][user]["password"]))

   def check_hash(self, text):
    db=self.database()
    hash=self.hash(text)
    if(hash==db["admin"]["password"]):
     return True
    else:
     return False
   def d_p(self,name):
    db=self.database()
    if(name in db["passwords"]):
     del db["passwords"][name]
     self.save_database(db)
    else:
     print("not exists")

   def main(self):
     while True:
      print("1.save password ")
      print("2.see all password")
      print("3.change password")
      print("4.delet all")
      print("5.exit")
      x=input("enter :")
      if(x=="5"):
       break
      elif(x=="1"):
       name=input("set name/site :")
       password=input("enter password :")
       self.save_password(name , password)
      elif(x=="2"):
       self.see_all()
      elif(x=="3"):
       pas=input("enter password :")
       Token=self.check_hash(pas)
       if(Token):
        name=input("set a name :")
        pasword=input("set a password ")
        self.save_admin(name , pasword)
        print("CHANGE PASSWORD ")
       else:
        print("wrong password")
      elif(x=="4"):
       pas=input("enter password !! :")
       Token=self.check_hash(pas)
       if(Token):
        os.system("rm database.json")
        return
        print("alll data clear !!")
       else:
        print("wrong password")
      else:
       print("wrong option")

if(__name__=="__main__"):
  main=PASSWORD()
