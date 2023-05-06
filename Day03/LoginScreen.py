from registeration import *
from project import *

print('welcome to Crowd-Funding-App')
print('1] register\n2] login\n3] project menu')

ans=int(input('Enter ur choice: '))
if ans == 1:
    
    fname=input('enter fname: ')
    lname=input('enter lname: ')
    idd=int(input('enter id: '))
    mail=input('enter mail: ')
    passw=input('enter ur password: ')
    con_pass=input('confirm password: ')
    phone=input('enter ur phone: ')

    user1= user(fname,lname,idd,mail,passw,con_pass,phone)
    
    
    
    #print(len('+201110991545'),"  ,, ",'+201110991545'.startswith('+20'))

elif ans==2:
    mail=input('enter mail: ')
    passw=input('enter ur password: ')

    #check for user data---------
    
    users_file=open("users.txt",'r+') #3,4
    lines=users_file.readlines()
    flag=False
    for i in range(len(lines)):
        fileMail=lines[i].split(",")[3]
        filePass=lines[i].split(",")[4]
        if mail==fileMail and passw==filePass:
            flag=True
        
    if flag == True:
        print('logined successfully!!')
    else:
        print('user email or password not correct!!') 

    users_file.close()


elif ans==3:

    print('====== Opening Project Menu . .  .')
    print('1] Create\n2] View\n3] Edit\n4] Delete\n5] Search By Date ')
    ans=int(input('Enter ur choice: '))
    # create a project
    if ans == 1:

        title=input('Enter project title: ')
        
        details=input('Enter project details(... , ....): ')
        
        strtTime=input('Enter project start time(hint. 04-01-1997): ')
        
        endTime=input('Enter project end time(hint. 04-01-1997): ')
        

        usr_ID=int(input('Enter project owner id: '))

        total_target=input('Enter project total target (Enter 00 for default value 250,000): ')
        
        if isinstance(total_target,int):
            # print('newVal')
            project1= project(title, details, strtTime, endTime, usr_ID, total_target)
        else:
            # print('defaultVal')
            project1= project(title, details, strtTime, endTime,usr_ID)

    # view all projects
    elif ans == 2:

        projects_file=open("projects.txt",'r+')
        lines=projects_file.readlines()
        for i in range(len(lines)):
            print(lines[i],end="")
    
        projects_file.close()
        
    # edit his project
    elif ans == 3:
        
        user_idd=int(input('enter user id: '))
        
        flag=False
        
        projects_file=open("projects.txt",'r+') 
        
        lines=projects_file.readlines()
        
        
        # print(len(lines[0].split(",")))
        
        for i in range(len(lines)):
           
            if int(lines[i].split(",")[4])==user_idd: # keep other lines unchanged
                flag=True
                print('select fields to edit')
                field_name=['title','details','start time','end time','id','total target']
                emptyStr=""
                for j in range(6):

                    newVal=input(f"change attrib {field_name[j]}[.. for default value]")
                    if newVal!=".." and j!=4:
                        emptyStr = emptyStr+str(newVal)
                    if j==4: # id
                        emptyStr = emptyStr+ lines[i].split(",")[4]
                    if newVal==".." and j!=4:
                        emptyStr = emptyStr + lines[i].split(",")[j]

                    if j<5: emptyStr = emptyStr+","
                    else: emptyStr = emptyStr+"\n"

                #print("New Data=== ",emptyStr,end=" ")
                lines[i]=emptyStr

        with open('projects.txt','w',encoding='utf-8') as file:
            file.writelines(lines)

        if flag==False:
            print("user doesn't have any projects! !")    
        projects_file.close()
    #delete his project 
    elif ans ==4:
        user_idd=int(input('enter user id: '))
        flag=False
        projects_file=open("projects.txt",'r+') 
        lines=projects_file.readlines()
        for i in range(len(lines)):
             if int(lines[i].split(",")[4])==user_idd:
                 lines[i]=""
                 with open('projects.txt','w',encoding='utf-8') as file:
                    file.writelines(lines)
                 flag=True
                 break
        if flag==False:
            print("user doesn't have any projects! !")    
        projects_file.close()
    # search for a project by date
    elif ans ==5:
        st_date=input('Enter  (start date) of the project: ')
        en_date=input('Enter  (end date) of the project: ')
        flag=False
        
        projects_file=open("projects.txt",'r+') 
        
        lines=projects_file.readlines()
        for i in range(len(lines)):
            if lines[i].split(",")[2]==st_date and lines[i].split(",")[3]==en_date:
                print("-------------------- "+lines[i]+" --------------------")

        projects_file.close()


else:
    raise Exception('Choice not valid!!')







"""
Files will be created:
1- registered users
2- projects 
"""