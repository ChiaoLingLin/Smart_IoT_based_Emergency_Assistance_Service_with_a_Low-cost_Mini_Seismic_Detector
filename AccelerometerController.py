import busio
import board
import adafruit_adxl34x
import time
import numpy as np

class AccelerometerController:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.acc = adafruit_adxl34x.ADXL345(i2c)

    def set_last_xyz(self, data):
        self.last_xyz = data

    def get_xyz(self)->list[int,int,int]:
        self.set_last_xyz(self.acc.acceleration)
        time.sleep(0.1)
        [x,y,z] = self.acc.acceleration
        return [x,y,z]

    def get_xyz_difference(self)->list[int,int,int]:
        xyz = np.array(self.get_xyz())
        last_xyz = np.array(self.last_xyz)
        subtracted = np.subtract(last_xyz, xyz)
        return list(subtracted)
        