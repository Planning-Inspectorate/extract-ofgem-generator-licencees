# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 11:38:56 2025

@author: Jo Gerulaitis
"""

# ==================================
# USER INPUTS
# ==================================

# set the name of the pdf containing Ofgem licence holders that you want extracted

update_date = "20260128"
ofgem_pdf_filename = "electricity_licencees_" + update_date + ".pdf"

# ==================================

# import packages
from pypdf import PdfReader
import pandas as pd
import re
import os 
from datetime import datetime

# set source_path to be location of this file
source_path = os.path.dirname(os.path.realpath(__file__))

# create pdf reader object
reader = PdfReader(source_path + "/" + ofgem_pdf_filename)

# initiate empty list to collect contents of pdf
text_split_all = []

# extract all pages of pdf
for page in reader.pages:
    
    # extract text from page
    text = page.extract_text()
    
    # split text into lines
    text_split = text.split("ELECTRICITY GENERATION ")
    
    # add to list of contents
    text_split_all.extend(text_split)
    
# trim leading/trailing whitespace
text_split_stripped_all = [t.strip() for t in text_split_all]

text_split_stripped_all = text_split_stripped_all[1:-1]

text_split_stripped_all[-1] = text_split_stripped_all[-1].split("ELECTRICITY INTERCONNECTOR")[0]

# remove unecessary list items (page numbers, headings etc)
regex_condition_1 = re.compile(r"Note:.*|please.*|(^[0-9]{1,3}$)|(^$)|OFFICIAL|(^All Electricity Licensees.*)|(^All Electricity Licencees.*)|queries.*|For any.*|[\r\n]+")
text_split_stripped_filtered_all = [i for i in text_split_stripped_all if not regex_condition_1.match(i)]

# remove other licence types and just keep ELECTRICITY GENERATION licence holders
text_split_stripped_filtered_all[-1] = re.sub(r"(ELECTRICI?T?TY\s+INTERCONNECTOR).*", "", text_split_stripped_filtered_all[-1], flags=re.IGNORECASE).rstrip()

# reassign to new variable name
elec_gen_list = text_split_stripped_filtered_all

# initiate empty dataframe to collect ofgem name and licnce number
elec_gen_df = pd.DataFrame(columns=["ofgem_name", "ofgem_licence_number"])

for j in elec_gen_list:
    
    # get the index of the last space in the list item, this will be where the licence number begins
    idx_start_licence_number = [i for i, word in enumerate(j) if word == " "][-1]
 
    # split item into name and licence number
    ofgem_name_tmp = j[0:idx_start_licence_number].strip()
    ofgem_licence_number_tmp = j[idx_start_licence_number:].strip().replace("(","").replace(")","")
    
    # convert to a dataframe
    df_tmp = pd.DataFrame({"ofgem_name": [ofgem_name_tmp], "ofgem_licence_number": [ofgem_licence_number_tmp]})
    
    # append to joint dataframe
    elec_gen_df = pd.concat([elec_gen_df, df_tmp])
    
    elec_gen_df["ofgem_licence_type"] = "ELECTRICITY GENERATION"

# reorder columns
elec_gen_df = elec_gen_df[["ofgem_licence_type", "ofgem_name", "ofgem_licence_number"]]

print(elec_gen_df)

# write to file
elec_gen_df.to_csv(source_path + "/electricity_licencees_" + update_date + ".csv", index = False)

