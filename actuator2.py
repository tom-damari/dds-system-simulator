from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep

filepath = osPath.dirname(osPath.realpath(__file__))

# SUB
connector = rti.Connector("MyParticipantLibrary::Subscribers",  filepath + "/DDS.xml")
input_sen2_DDS = connector.getInput("Actuator2_sub::MySensor2Reader")
input_button_DDS = connector.getInput("Actuator2_sub::MyButtonStatusReader")

# PUB
connector = rti.Connector("MyParticipantLibrary::Publishers", filepath + "/DDS.xml")
outputDDS = connector.getOutput("Actuator2_pub::MyActuator2Writer")

# default status
id2 = 206556870
outputDDS.instance.setNumber("actuator_id", id2)
status = 'Working'
outputDDS.instance.setString("actuator_status", status)
outputDDS.write()
print(f'Actuator {id2} Message: {status}')

while True:

    input_button_DDS.read()
    if input_button_DDS.samples.length > 0:
        # make sure the sample is valid
        if input_button_DDS.samples[0].valid_data:
            button_command = input_button_DDS.samples[0].get_string("command")
            # define the status of actuator 1
            if status == 'Working' and button_command == "Stop":
                # received Stop command
                status = 'Stopped'
                outputDDS.instance.setString("actuator_status", status)
                outputDDS.write()
            elif status == 'Degraded' and button_command == "Stop":
                # received Stop command
                status = 'Stopped'
                outputDDS.instance.setString("actuator_status", status)
                outputDDS.write()
            elif status == 'Stopped' and button_command == "Start":
                # received Start command
                status = 'Working'
                outputDDS.instance.setString("actuator_status", status)
                outputDDS.write()

    input_sen2_DDS.read()
    if input_sen2_DDS.samples.length > 0:
        # make sure the sample is valid
        if input_sen2_DDS.samples[0].valid_data:
            sen2_temp_reading = input_sen2_DDS.samples[0].get_number("temp_reading")
            # define the status of actuator 2
            if status == 'Working':
                # received extreme temperature
                if sen2_temp_reading > 45:
                    status = 'Degraded'
                    outputDDS.instance.setString("actuator_status", status)
                    outputDDS.write()
            elif status == 'Degraded':
                # received normal temperature
                if sen2_temp_reading > 0 and sen2_temp_reading < 45:
                    status = 'Working'
                    outputDDS.instance.setString("actuator_status", status)
                    outputDDS.write()

    # print the message to a console
    print(f'Actuator {id2} Message: {status}')

    # send current state every 1 second (1 Hz)
    sleep(1)
