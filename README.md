# extract-ofgem-generator-licencees
Script to extract the Ofgem Electricity Generator Licence holders from the PDF published by Ofgem

## Pre-requisites
Python and appropriate IDE installed to run the script

## Documentation for running

Author/updater	Jo Gerulaitis
Date	23/09/2025
Version 	0.3


### Tasks for person with Python installed (EST updater):

#### Download the new Ofgem list (PDF) and extract users
* Download the latest Ofgem list (PDF) file available at List of all electricity licensees including suppliers | Ofgem) and save to directory Python scripts are stored in in the format electricity_licencees_YYYYMMDD.pdf where the date is the date in the PDF, not the date of download.
* Open extractOfgemLicenceesPDF.py in an IDE. Update the ofgem_pdf_filename variable to reflect the file name of the PDF saved above.
* Run the file. You should now see a comma separated value file of the form “electricity_licencees_YYYYMMDD.csv”
* Open the csv and check that column A contains “ELECTRICITY GENERATION” for all rows, column B contains the name of the company and column C has a company number for all rows and that there are no other columns/rows.
* Check that the name/number of the first and last generator in the PDF list are the first and last in the csv.
* Send CSV to home computer to run the Companies House API script, as PINS blocking at moment.
Send result back to PINS email and then reformat to be like previous “ofgem_list_summary_YYYYMMDD.xlsx”, investigating any that were not found / don’t match previous address information. 

