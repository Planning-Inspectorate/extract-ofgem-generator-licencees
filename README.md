# extract-ofgem-generator-licencees
Script to extract the Ofgem Electricity Generator Licence holders from the PDF published by Ofgem

## Pre-requisites
Python and appropriate IDE installed to run the script

## Documentation for running

* Author/updater: Jo Gerulaitis
* Date: 23/09/2025
* Version : 0.3


### Tasks for person with Python installed (EST updater):

#### Download the new Ofgem list (PDF) and extract users
* Clone or download this directory to your local machine
* Download the latest Ofgem list (PDF) file available at: https://www.ofgem.gov.uk/data/list-all-electricity-licensees-including-suppliers and save to your cloned/downloaded directory in the form electricity_licencees_YYYYMMDD.pdf where the date is the date in the PDF, not the date of download.
* Open extractOfgemLicenceesPDF.py in an IDE (Integrated Development Environment) such as Spyder or Visual Studio Code. Update the ofgem_pdf_filename variable to reflect the file name of the PDF saved above.
* Run the file. You should now see a comma separated value file of the form “electricity_licencees_YYYYMMDD.csv”
