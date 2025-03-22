from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))

# SUB
connector = rti.Connector("MyParticipantLibrary::Subscribers",  filepath + "/DDS.xml")
input_sen1_DDS = connector.getInput("Actuator1_sub::MySensor1Reader")
input_button_DDS = connector.getInput("Actuator1_sub::MyButtonStatusReader")

# PUB
connector = rti.Connector("MyParticipantLibrary::Publishers", filepath + "/DDS.xml")
outputDDS = connector.getOutput("Actuator1_pub::MyActuator1Writer")

# default status
id1 = 206586315
outputDDS.instance.setNumber("actuator_id", id1)
status = 'Working'
outputDDS.instance.setString("actuator_status", status)
outputDDS.write()
print(f'Actuator {id1} Message: {status}')

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

    input_sen1_DDS.read()
    if input_sen1_DDS.samples.length > 0:
        # make sure the sample is valid
        if input_sen1_DDS.samples[0].valid_data:
            sen1_temp_reading = input_sen1_DDS.samples[0].get_number("temp_reading")
            # define the status of actuator 1
            if status == 'Working':
                # received extreme temperature
                if sen1_temp_reading < 18 or sen1_temp_reading > 45:
                    status = 'Degraded'
                    outputDDS.instance.setString("actuator_status", status)
                    outputDDS.write()
            elif status == 'Degraded':
                # received normal temperature
                if sen1_temp_reading > 18 and sen1_temp_reading < 45:
                    status = 'Working'
                    outputDDS.instance.setString("actuator_status", status)
                    outputDDS.write()

    # print the message to a console only if values are valid
    print(f'Actuator {id1} Message: {status}')

    # send current state every 1 second (1 Hz)
    sleep(1)