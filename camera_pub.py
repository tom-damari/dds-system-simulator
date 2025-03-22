import datetime
from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
filepath = osPath.dirname(osPath.realpath(__file__))

# PUB
connector = rti.Connector("MyParticipantLibrary::Publishers", filepath + "/DDS.xml")
outputDDS = connector.getOutput("Camera_pub::MyCameraWriter")

while True:
    # send the message as a string with real time
    time_stamp = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S.%f")[:-3]
    outputDDS.instance.setString("time_stamp", time_stamp)
    outputDDS.write()

    # print the message to a console
    print(f'Camera Message: {time_stamp}')

    # send current state every 0.1 seconds (10 Hz)
    sleep(0.1)
