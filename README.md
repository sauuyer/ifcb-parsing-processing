# OOI CGSN IFCB Data Product Management

### HDR file processing(make_csv_from_hdr_parse)

From a dump of data outputs from the IFCB, find all of the hdr files, pull out relevant metadata and create a csv that can be used to populate the OOI CGSN IFCB log spreadsheet. 

gather_variables_from_hdr.py -> identify and pull metadata from the hdr files
* Pulled parameters = ["FileComment", "triggerCount", "roiCount", "runTime", "inhibitTime", "humidity", "temperature", "runTime", "PMTAhighVoltage", "PMTBhighVoltage", "humidity", "SyringeSampleVolume", "syringeSamplingSpeed", "temperature", "RunFastFactor", "sampleNumber", "runSampleFast"]
* Input: flat directory of all data files from IFCB
* Output: hdrFileSummary.csv

hdrSummaryProcessing.py -> adds calculated parameters to the hdrFileSummary.csv file
* Added parameters:
       * Datetime (pulled from filename)
    



### Classifier sandbox (not uploaded)

A basic classifier that allows for large category organism and object identification to allow for quick comparision between ROI bins. 

###
