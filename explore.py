# scoping

# statistics of charges
# total charges by region, sex, smoker
# average charges by smoker, region 

import csv
import locale

locale.setlocale(locale.LC_ALL, 'us_US')

csv_filepath = r"insurance.csv"


def csv_to_dict(filepath):
    """
    Opens CSV file and converts it to dictionary, enumerates it as well.
    """
    with open(csv_filepath, newline = '') as csv_file:
        header = csv_file.readline().split(',')
        header = [name.strip() for name in header]
        csv_data = csv.DictReader(csv_file, fieldnames = header,  delimiter = ',')
        
        new_dict = {}
        for row in enumerate(csv_data):
            new_dict[row[0]] = row[1]
        return new_dict

def curr(val):
    """
    Returns value in $US dollars with groupings of thousands
    """
    return locale.currency(val, grouping = True)

def print_dict(dictionary):
    """
    Iterates through dictionary and prints keys alongside values in currency format
    """
    for key, val in dictionary.items():
        print(f'The total for "{key}" is {curr(val)}.')


dict_data = csv_to_dict(csv_filepath)

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# create lists for each column for analysis
for val in dict_data.values():
    age.append(int(val['age']))
    sex.append(val['sex'])
    bmi.append(float(val['bmi']))
    children.append(val['children'])
    smoker.append(val['smoker'])
    region.append(val['region'])
    charges.append(round(float(val['charges']),2))

# calculate total charges across dataset
charges_total = 0.0
for charge in charges:
    charges_total += charge
print(f'The total charges for the record population is {curr(charges_total)}.')

# calculate average charges across all charges
charges_average = float(charges_total / len(charges))
print(f'The average charge across all records is {curr(charges_average)}.')

# sort charges 
charges_sorted = sorted(charges)

# calculate median charge across all charges
charges_median = 0
num_of_charges = int(len(charges))

if num_of_charges % 2 == 0:
    charges_median = charges_sorted[int(num_of_charges / 2)]
else:
    charges_median = int(charges_sorted[(num_of_charges / 2)] + charges_sorted[(num_of_charges / 2) - 1] / 2)

print(f'The median charge value is {curr(charges_median)}.')

# gather min and max values
max_charge = charges_sorted[-1]
min_charge = charges_sorted[0]

print(f'The max charge is {curr(max_charge)} and the min charge is {curr(min_charge)}.')
print('--')
#------------------------

# gather distinct regions
unique_regions = []
for elem in region:
    if elem not in unique_regions:
        unique_regions.append(elem)

# total charges per region
charges_by_region = {}
for region in unique_regions:
    charges_by_region[region] = 0.0

# iterate through dict values and unique regions to create totals by region
for val in dict_data.values():
    for region in charges_by_region.keys():
        if region == val['region']:
            charges_by_region[region] += float(val['charges'])

print('Total by regions:\n')
print_dict(charges_by_region)
print('--')

# ------------------------

# gather distinct sex values
unique_sex_values = []
for elem in sex:
    if elem not in unique_sex_values:
        unique_sex_values.append(elem)

# total charges by sex
charges_by_sex = {}
for elem in unique_sex_values:
    charges_by_sex[elem] = 0.0

# iterate through dict values and unique regions to create totals by sex
for val in dict_data.values():
    for elem in charges_by_sex.keys():
        if elem == val['sex']:
            charges_by_sex[elem] += float(val['charges'])

print('Totals by sex: \n')
print_dict(charges_by_sex)
print('--')
# ------------------------

# gather distinct smoker values
unique_smoker_values = []
for elem in smoker:
    if elem not in unique_smoker_values:
        unique_smoker_values.append(elem)

# total charges by smoker
charges_by_smoker = {}
for elem in unique_smoker_values:
    charges_by_smoker[elem] = 0.0

# iterate through dict values and unique regions to create totals by smoker
for val in dict_data.values():
    for elem in charges_by_smoker.keys():
        if elem == val['smoker']:
            charges_by_smoker[elem] += float(val['charges'])

print('Totals by smoker/non-smoker: \n')
print_dict(charges_by_smoker)
print('--')

# ------------------------

def find_total_average(category, uniques, dictionary):
    """
    Find total and average of a field
    """
    charges_all = {}
    for elem in uniques:
        if elem not in charges_all.keys():
            charges_all[elem] = []

    for val in dictionary.values():
        for elem in charges_all.keys():
            if val[category] == elem:
                charges_all[elem].append(val['charges'])

    print(f'Below are the results for the "{category}" category are:\n')
    # find total and average
    for type, lst in charges_all.items():
        total = 0.0
        average = 0.0
        for charge in lst:
            total += float(charge)
        average = total / len(lst)

        print(f'For value "{type}", the total is {curr(total)}, with an average charge of {curr(average)}.')
    print('--')

find_total_average('smoker', unique_smoker_values, dict_data)
find_total_average('sex', unique_sex_values, dict_data)
find_total_average('region', unique_regions, dict_data)
    
# ------------------------

        

