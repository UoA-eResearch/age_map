#!/usr/bin/env python3

import csv
import sys
import re
import json

files = sys.argv[1:]
o = {}

for fn in files:
  with open(fn) as f:
    reader = csv.DictReader(f)
    for row in reader:
      #"Year","Area_type","Area_code","Area_description","Age_group_5_year_groups_to_85_years_and_over_code","Age_group_5_year_groups_to_85_years_and_over_description","Sex_code","Sex_description","Maori_ethnic_group
#_indicator_summary_code","Maori_ethnic_group_indicator_summary_description","Census_usually_resident_population_count","Age_group_5_year_groups_to_85_years_and_over_by_Maori_ethnic_group_indicator_summary_perc
#ent","Age_group_5_year_groups_to_85_years_and_over_by_sex_percent"
      if row["Area_type"] == "Statistical Area 2":
        code = row["Area_code"]
        year = row["Year"]
        age_group = row["Age_group_5_year_groups_to_85_years_and_over_description"]
        sex = row["Sex_description"]
        maori = row["Maori_ethnic_group_indicator_summary_description"]
        if maori != "Total":
          continue
        count = row["Census_usually_resident_population_count"]
        if count == "C":
          count = None
        else:
          count = int(count)
        if code not in o:
          o[code] = {
            "Male": {},
            "Female": {},
            "Total": {}
          }
        o[code][sex][age_group] = count

print(json.dumps(o, sort_keys=True, indent=4))
