from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
filepath = osPath.dirname(osPath.realpath(__file__))

# PUB
connector = rti.Connector("MyParticipantLibrary::Publishers", filepath + "/DDS.xml")
normalOutputDDS = connector.getOutput("Temp_sensor1_pub::MySensor1Writer")
extremeOutputDDS = connector.getOutput("Temp_sensor1_pub::MySensor1ExtremeWriter")

while True:
    # publish the temperature in degrees (integer)
    temp1 = random.randint(10, 60)
    normalOutputDDS.instance.setNumber("temp_reading", temp1)
    normalOutputDDS.write()

    # print the message to a console
    print(f'Temperature Sensor 1 Message: {temp1} degrees')

    # save extreme temperature for dashboard
    if temp1 < 18 or temp1 > 45:
        extremeOutputDDS.instance.setNumber("temp_reading", temp1)
        extremeOutputDDS.write()

    # send current state every 1 second (1 Hz)
    sleep(1)
