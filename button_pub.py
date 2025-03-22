from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random

filepath = osPath.dirname(osPath.realpath(__file__))

# PUB
connector = rti.Connector("MyParticipantLibrary::Publishers", filepath + "/DDS.xml")
outputDDS = connector.getOutput("Button_pub::MyButtonWriter")

# start by sending the default command Start
command = "Start"
outputDDS.instance.setString("command", command)
outputDDS.write()
print(f'Button Command Message: {command}')
sleep(5)

while True:
    # send Stop command every 20 seconds
    sleep(15)
    command = "Stop"
    outputDDS.instance.setString("command", command)
    outputDDS.write()
    print(f'Button Command Message: {command}')

    # send Start command 5 seconds after Stop command
    sleep(5)
    command = "Start"
    outputDDS.instance.setString("command", command)
    outputDDS.write()
    print(f'Button Command Message: {command}')
