from datetime import datetime
from registeration import *
class project:
    ids = []
    format = "%d-%m-%Y"
    res = True

    def __init__(self,title,details,startTime,endTime,usrID,total_target=250000):
        self.title=title
        self.details=details
        self.total_target=total_target
        res=self.check_data(startTime,endTime)
        # print("final=",res)
    
        if res == True:
            self.endTime=endTime
            self.startTime=startTime
            print('Success!!')
    
        else:
            print('Failed!!')

        self.usrID=usrID
        self.total_target=total_target


        users_file=open("users.txt",'r+')
        lines=users_file.readlines()
        for i in range(len(lines)):
            self.ids.append(int(lines[i].split(",")[2]))
        
        print(self.ids)
        users_file.close()
        if usrID not in project.ids:
            raise Exception("User ID Doesn't belong to a user")
        else:
            print('Success')

        print('================================================================')
        
        projects_file=open("projects.txt",'a')
    
        projects_file.write(self.title+","+self.details+","+str(self.startTime)+","+str(self.endTime)
                            +","+str(self.usrID)+","+str(self.total_target)+"\n")
        projects_file.close()
        
        print('-------------- project created successfully ---------------')
        print('================================================================')

            
    def check_data(self,startTime,endTime):
        try:
            self.res = bool(datetime.strptime(startTime, self.format)) 
            # print('Res1',self.res)
            self.res = self.res and bool(datetime.strptime(endTime, self.format))
            # print('Res2',self.res)
        except ValueError:
            self.res = False
        return self.res
    


# pp=project('xas','casca','04-04-1995','04-04-1995',1200,250000)