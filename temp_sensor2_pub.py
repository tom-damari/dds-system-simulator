from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
filepath = osPath.dirname(osPath.realpath(__file__))

# PUB
connector = rti.Connector("MyParticipantLibrary::Publishers", filepath + "/DDS.xml")
normalOutputDDS = connector.getOutput("Temp_sensor2_pub::MySensor2Writer")
extremeOutputDDS = connector.getOutput("Temp_sensor2_pub::MySensor2ExtremeWriter")

while True:
    # publish the temperature in degrees (integer)
    temp2 = random.randint(0, 50)
    normalOutputDDS.instance.setNumber("temp_reading", temp2)
    normalOutputDDS.write()

    # print the message to a console
    print(f'Temperature Sensor 2 Message: {temp2} degrees')

    # save extreme temperature for dashboard
    if temp2 > 45:
        extremeOutputDDS.instance.setNumber("temp_reading", temp2)
        extremeOutputDDS.write()

    # send current state every 0.1 second (10 Hz)
    sleep(0.1)
