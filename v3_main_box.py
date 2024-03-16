from AccelerometerController import AccelerometerController
from PigRandomForest import PigRandomForest
import time
import chatphone_new as chatphone
import cloud

rf = PigRandomForest().load_model('pig_earthquake.model')
ac = AccelerometerController()
input_ = "0"

#set display device ip
agent = chatphone.chatphoe()
agent.recv_start()
location = input("Enter Location>>")
cloud_agent = cloud.updater(location)
while True:
    xyz = ac.get_xyz_difference()
    p = rf.predict(xyz)
    if p > 5:
        print(p)
        agent.send('true')
    else:
        print("under 6")
        agent.send('false')
    message = agent.get_message()
    if message:
        cloud_agent.update(message)
    time.sleep(3)
 