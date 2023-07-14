import csv
import copy
import random


template = { "new_cases" : 0,
             "deaths" : 0,
             "recovered" : 0

            }

for key,value in template.items():
   print(f"{key} : {value}")
   print("===========")

date_list= []
value_list = []
with open('covid_data.csv','r') as fh:
   csv_reader = csv.reader(fh)
   next(csv_reader)
   for row in csv_reader:
      date_list.append(row[0])
      current_template = copy.deepcopy(template)
      current_template["new_cases"] = int(row[1])
      current_template["deaths"] = int(row[2])
      current_template["recovered"] = int(row[3])
      #print(current_template)
      value_list.append(current_template)

print(date_list)
print(value_list)
required_list = list(zip(date_list,value_list))
required_dict = dict(zip(date_list,value_list))
   #print(csv_reader)
   #line_count = 0
   #for row in csv_reader:
      #if linecount == 0:
      #   print(f"Colums are :{','.join(row)}")
       #  linecount += 1

print(required_list)
print("====================")
print(required_dict)
for key,value in required_dict.items():
   print(key)
   print("======")
   print(value)
   sum_cases = 0
   total_deaths = 0
   total_recoveries = 0
for key in required_dict:
   sum_cases = sum_cases + required_dict[key]["new_cases"]
   total_deaths = total_deaths + required_dict[key]["deaths"]
   total_recoveries = total_recoveries + required_dict[key]["recovered"]

print(f"Total cases are :{sum_cases}")
print(f"Total deaths are :{total_deaths}")
print(f"Total deaths are :{total_recoveries}")
print(f"Average no of new cases :{sum_cases/len(required_dict)}")

print(len(required_dict))

random_key = random.choice(list(required_dict.keys()))
print(random_key)
print(required_dict[random_key])
   
   
   
   
   


      