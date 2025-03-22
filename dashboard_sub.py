import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))

# SUB
connector = rti.Connector("MyParticipantLibrary::Subscribers",  filepath + "/DDS.xml")
input_camera_DDS = connector.getInput("Dashboard_sub::MyCameraReader")
input_Actuator1_DDS = connector.getInput("Dashboard_sub::MyActuator1StatusReader")
input_Actuator2_DDS = connector.getInput("Dashboard_sub::MyActuator2StatusReader")
input_sen1_DDS = connector.getInput("Dashboard_sub::MySensor1ExtremeReader")
input_sen2_DDS = connector.getInput("Dashboard_sub::MySensor2ExtremeReader")

while True:

    input_camera_DDS.read()
    if input_camera_DDS.samples.length > 0:
        if input_camera_DDS.samples[0].valid_data:
            time_stamp = input_camera_DDS.samples[0].get_string("time_stamp")
            print(f"Camera: < {time_stamp} >")
    else:
        print(f'Camera: <>')

    input_Actuator1_DDS.read()
    input_Actuator1_DDS_samples = []
    numOfSamples_actuator1 = input_Actuator1_DDS.samples.getLength()
    for j in range(0, numOfSamples_actuator1):
        if input_Actuator1_DDS.infos.isValid(j):
            actuator_status = input_Actuator1_DDS.samples.getString(j, "actuator_status")
            input_Actuator1_DDS_samples.append(actuator_status)
    if numOfSamples_actuator1 == 10: # wait for 10 readings and then print
        id1 = int(input_Actuator1_DDS.samples.getNumber(0, "actuator_id"))
        print(f'Actuator {id1}: {input_Actuator1_DDS_samples}')
    else:
        print(f'Actuator 206586315: []')

    input_Actuator2_DDS.read()
    input_Actuator2_DDS_samples = []
    numOfSamples_actuator2 = input_Actuator2_DDS.samples.getLength()
    for j in range(0, numOfSamples_actuator2):
        if input_Actuator2_DDS.infos.isValid(j):
            actuator_status = input_Actuator2_DDS.samples.getString(j, "actuator_status")
            input_Actuator2_DDS_samples.append(actuator_status)
    if numOfSamples_actuator2 == 10: # wait for 10 readings and then print
        id2 = int(input_Actuator2_DDS.samples.getNumber(0, "actuator_id"))
        print(f'Actuator {id2}: {input_Actuator2_DDS_samples}')
    else:
        print(f'Actuator 206556870: []')

    input_sen1_DDS.read()
    input_sen1_DDS_samples = []
    numOfSamples_sen1 = input_sen1_DDS.samples.getLength()
    for j in range(0, numOfSamples_sen1):
        if input_sen1_DDS.infos.isValid(j):
            temp_reading = input_sen1_DDS.samples.getNumber(j, "temp_reading")
            input_sen1_DDS_samples.append(temp_reading)
    if numOfSamples_sen1 == 10: # wait for 10 readings and then print
        print(f'Thermometer 1: {input_sen1_DDS_samples}')
    else:
        print(f'Thermometer 1: []')

    input_sen2_DDS.read()
    input_sen2_DDS_samples = []
    numOfSamples_sen2 = input_sen2_DDS.samples.getLength()
    for j in range(0, numOfSamples_sen2):
        if input_sen2_DDS.infos.isValid(j):
            temp_reading = input_sen2_DDS.samples.getNumber(j, "temp_reading")
            input_sen2_DDS_samples.append(temp_reading)
    if numOfSamples_sen1 == 10: # wait for 10 readings and then print
        print(f'Thermometer 2: {input_sen2_DDS_samples}')
    else:
        print(f'Thermometer 2: []')

    # print the status of the system to a console every 5 seconds
    sleep(5)
