import time
from threading import Thread

from devices.io.gpio import GPIO
from devices.io.pca9685 import PCA9685

class Device:

    def __init__(self):
        self.gpio = GPIO()
        self.pca9685 = PCA9685()
    
    def start(self):
        self.gpio.start()
        self.pca9685.start()