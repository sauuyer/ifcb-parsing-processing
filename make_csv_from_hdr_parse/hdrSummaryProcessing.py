from datetime import datetime
import pandas as pd

file = "/Users/sawyer/Desktop/AR82-Pioneer20/ifcb-test-dir/ifcb-parsing-processing/make_csv_from_hdr_parse/hdrFileSummaryFULL.csv"

df = pd.read_csv(file)

df['Datetime'] = pd.to_datetime(df['Filename'].str[1:15], format='%Y%m%dT%H%M%S')

print(5/df['runTime'])
print(df['sampleTime']*df['sampleVol_per_second'])
print(df['roiCount']*df['sampledVolume'])

df['sampleTime'] = df['runTime'] - df['inhibitTime']
df['sampleVol_per_second'] = 5/df['runTime']
df['sampledVolume'] = df['sampleTime']*df['sampleVol_per_second']
df['ROIsperSampledVol'] = df['roiCount']*df['sampledVolume']

#calculated parameters from Taylor

#Volume Analyzed
### looktime = runTime - inhibitTime
### if runsamplefast = false then runsamplefast==1
### flow rate = sampledVolume / runTime # (check on the time units for these)
### what is flow rate - flowRate presents in ifcbAquire (20 mins per syringe)
#### flow rate relevant details ::: 20 mins per syringe | 5 ml per syringe
volumeAnalyzed = (runFastFactor * runSampleFast) * f

print(df)

df.to_csv("hdrFileSummaryFullwithCalcs.csv")
