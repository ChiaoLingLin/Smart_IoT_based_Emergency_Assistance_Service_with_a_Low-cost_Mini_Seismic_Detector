from firebase import firebase

BOXL = 'boxLoaction'
LIST = 'List'

#產生資料
"""new_users = [
{'boxLoaction': 'A','List': '1,'},
{'boxLoaction': 'B','List': '1,2,3'},
{'boxLoaction': 'C','List': '1,2,3,4,5'},
{'boxLoaction': 'D','List': '1,2,3,4,5,6,7,8,9'},
{'boxLoaction': 'E','List': '1,2,3,4,5,6,7,8,9,10,11'},
{'boxLoaction': 'F','List': '1,2,3,4,5,6,7,8,9,10,11,12,13'},
]"""

db_url = 'https://bamboo-storm-392603-default-rtdb.firebaseio.com/'
fdb = firebase.FirebaseApplication(db_url, None)

def delete_location(location):
    url = '/'+location
    fdb.delete('/user',url)

def post_location(location,recv_dict):
    delete_location(location)
    url = '/user/'+location
    fdb.post(url, recv_dict)

class updater():
    def __init__(self,location):
        self.location = location
        self.username = 'Bob'
        self.state = 'safe'
        self.post()
    def post(self):
        assamble = {BOXL:self.location,LIST:self.username+":"+self.state+"\n"}
        post_location(self.location,assamble)
    def update(self,state):
        if state[1] == 'h':
            self.state = 'danger'
            self.post()
        elif state[1] == 's':
            self.state = 'safe'
            self.post()
        elif state[1] == 'i':
            self.username = state[2:]
            self.post()



#在user下查詢新增的資料(.get讀取)
"""users = fdb.get('/user', None)  #None全部讀取，1代表讀取第一筆，以此類推
for key in users:
    print(users[key])"""



