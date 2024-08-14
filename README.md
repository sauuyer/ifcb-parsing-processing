# OOI CGSN IFCB Data Product Management

#### dashboard organization
- 1 dashboard for all ooi ifcb data
- each dataset in the public-facing dashboard represents 1 array (currently there will be 1 total dataset representing Pioneer MAB, this will contain moored, discrete, and underway data from all ooi ifcbs that operate at the pioneer mab site)

#### filters and tags

**filters** (these options are fixed in the dashboard)
- Dataset
- Instrument (instrument #)
- Cruise (cruise # by default, we might want to use/force ooi deployment number here instead?)
- Sample Type (discrete, underway, moored)

**tags**
- tags related to targeted sample depths (from water sampling strategy document): "surface", "chlorophyll max", "moored ifcb depth"
- tags related to nearby array site, within 2 km of a given site center (CNSM, etc.)

#### python processing file order

1. hdr_roi_compare.py 

      used to verify all corrisponding ROI and HDR files are in a directory. Outputs a csv files containing columns for general file name, ROI file name (including extension), and HDR file name (including extension)
      this is independant of the processing order technically; i.e., this doesn't create or cause any dependancies but it can be used as a pre-process qc step

   
3. gather_variables_from_hdr.py

      gathers file_parameters = ["FileComment", "triggerCount", "roiCount", "runTime", "inhibitTime", "humidity", "temperature", "runTime", "PMTAhighVoltage", "PMTBhighVoltage", "humidity", "SyringeSampleVolume", "syringeSamplingSpeed", "temperature", "RunFastFactor", "sampleNumber", "runSampleFast"]
      from hdr files

      outputs a csv where each gathered param is a column and each row represents one hdr file from the designated directory/ies of ifcb data (e.g., hdrFileSummary_2024-08-14.csv)

      this output is used in the hdrSummaryProcessing.py file

4. hdrSummaryProcessing.py

      outputs a csv containing
       - Datetime pulled from the file name
       - lookTime (lookTime = runTime - inhibitTime)
       - runSampleFast_Int
       - water_sample_type (in-lab testing, underway, discrete_sample, etc.; taken from file comment)
       - flowRate_mins (df['SyringeSampleVolume'] / df['syringeSamplingSpeed'])
       - volumeAnalyzed (df['RunFastFactor'] * df['runSampleFast_Int']) * df['flowRate_mins'] * (df['lookTime']/60)

       output csv filename example = hdrFileSummaryFULL_2024-08-14.csv

6. summaryHDR_and_underway.py

    merges hdrFileSummaryFULL csv with merged underway ship data.



### Classifier sandbox (not yet pushed to repo)

A basic classifier that allows for large category organism and object identification to allow for quick comparision between ROI bins. 


