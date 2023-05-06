from validate_email_address import validate_email
class user:
    
    ids = [] # will be edited using id's inside the file
    
    def __init__(self,fname,lname,id,email,passwd,conf_passwd,phone):

        # 
        users_file=open("users.txt",'r+')
        lines=users_file.readlines()
        for i in range(len(lines)):
            self.ids.append(int(lines[i].split(",")[2]))
        print(self.ids)
        users_file.close()

        #
        print('======== Validating User first,last name . . . ')        
        if self.check_names(fname,lname)==False:
            raise Exception("Username must contain only alphapetical letters")
        else:
            self.fname=fname
            self.lname=lname
            print('name:Succeded')



        print('======== Validating User id . . . ')
        if id not in self.ids:
            self.ids.append(id)
            self.id=id 
            print('id:Succeded')
        else:
            raise Exception('id is already taken!!')


        print('======== Validating User mail . . . ')
        valid=validate_email(email)
        if valid == True:
            self.email=email 
            print('mail:Succeded')
        else:
            raise Exception('Email not valid!!')

        self.passwd=passwd
        print('======== Validating User passwd . . . ')
        if conf_passwd!=passwd:
            raise Exception("password doesn't match")
        else:
            self.conf_passwd=conf_passwd
            print('password:Succeded')


        
        print('======== Validating User phone . . . ')
        if self.check_phone(phone) == True:
            self.phone=phone
            print('phone:Succeded')
        else:
            raise Exception('phone must start with +20 and its length=13')

        print('================================================================')
        print('-------------- user created successfully ---------------')
        
        users_file=open("users.txt",'a')
        users_file.writelines(self.fname+","+self.lname+","+str(self.id)+","+self.email+","+self.passwd+","+
                         self.conf_passwd+","+self.phone+"\n")
        users_file.close()
        print('================================================================')

    def check_names(self,fname,lname):
        cnt = len(fname)
        for ch in fname:
            code = ord(ch)
            if 47 < code < 58:
                cnt = cnt -1
        return cnt == len(fname)  and fname!=""

    def check_phone(self,phone):
        if phone.startswith('+20') and len(phone)==13:
            return True
        else:
            return False

# user1=user('mostafa','essam',1200,'mustafaessam959@gmail.com','123','123','+201110991545')


