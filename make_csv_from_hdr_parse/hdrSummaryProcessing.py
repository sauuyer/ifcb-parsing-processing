from datetime import datetime
import pandas as pd
import re

file = "/Users/sawyer/Desktop/AR82-Pioneer20/ifcb-test-dir/ifcb-parsing-processing/make_csv_from_hdr_parse/hdrFileSummaryFULL-TCadditions_2024-04-13.csv"


# read in processed file as a dataframe
df = pd.read_csv(file)
#drop rows where file names start with and underscore
#df = df.drop(df[df['Filename'].str.contains('._')])
df = df[~df['Filename'].str.startswith('._')]
#df = df.drop(df[df['Filename'].str.contains('_')])

print(df.head())

df['Datetime'] = pd.to_datetime(df['Filename'].str[1:15], format='%Y%m%dT%H%M%S')


#lookTime
df['lookTime'] = df['runTime'] - df['inhibitTime']

#Volume Analyzed
### if runsamplefast = false then runsamplefast==1 (correction from what is in original email)

def get_runSampleFast_Int(runSampleFast):
    if runSampleFast == False:
        return 1
    elif runSampleFast == True:
        return 0

### what is flow rate - flowRate presents in ifcbAquire (20 mins per syringe)
#### flow rate relevant details ::: 20 mins per syringe | 5 ml per syringe

df['runSampleFast_Int'] = df['runSampleFast'].apply(get_runSampleFast_Int)

#### syringeSamplingSpeed (usually 20 for 20 mins), SyringeSampleVolume (usually 5 ml)
df['flowRate_mins'] = df['SyringeSampleVolume'] / df['syringeSamplingSpeed']

#### volume analyzed calc
df['volumeAnalyzed'] = (df['RunFastFactor'] * df['runSampleFast_Int']) * df['flowRate_mins'] * (df['lookTime']/60)

print(df['volumeAnalyzed'])

df.to_csv("hdrFileSummaryFullwithCalcs_2024-04-13.csv", index = False)
