class User:
    name=None
    email=None
    def send_email(self):
        if self.email is not None:
            print("sendingemail"+self.email)
        else:
            print("error")

    def _init_(self,name,email): # este es el llamado Constructor 
        self.name=name
        self.email=email
    def _str_(self):
        return "User: " + self.email

class Student(User):
    id =None
    def _init_(self,
       name=None,
       email=None,
       id= None,
       score = None
       ):
       super()._init_(name,email)
       self.id= id
       self.score = score
    def _str_(self):
        return "Student:"+str(self.id)+","+self.email
    def _repr_(self):
        return f"Student(name='{self.name}',email='{self.email}', id='{self.id}')"
    {}
