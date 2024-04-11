import os
import pandas
import re

#dirx = "/Volumes/My Passport/IFCB_PLIMS/AR82_ifcb_data/AR82_ifcb206_all_data/D20240408T021656_IFCB206.roi"
dir = "/Users/sawyer/Desktop/AR82-Pioneer20/ifcb-test-dir"

#f = open(dir, 'r')


#file_parameters = ["triggerCount", "roiCount", "humidity", "temperature", "runTime", "inhibitTime", "PMTAhighVoltage", "PMTBhighVoltage", "FileComment"]
'''
underway samples -> NumberSyringesToAutoRun: 10000
discrete samples -> NumberSyringesToAutoRun: 3
'''


def find_value_after_string(content):
    #print(hdr_content)
    file_parameters = ["triggerCount", "roiCount", "humidity", "temperature", "runTime", "inhibitTime",
                       "PMTAhighVoltage", "PMTBhighVoltage", "FileComment"]
    #for param in file_parameters:
    pattern = re.compile(r'triggerCount:\s*(\d+)')
    #print(pattern)
    match = pattern.search(hdr_content)

    if match:
        value = match.group(1)
        #return match.group(1)
        print("value: ", value)
    else: #return None
        print("No match found.")


for filename in os.listdir(dir):
    if filename.endswith(".hdr"):
        filepath = os.path.join(dir, filename)
        with open(filepath, "r") as file:
            hdr_content = file.read()
            find_value_after_string(hdr_content)


#value = find_value_after_string(search_string)





