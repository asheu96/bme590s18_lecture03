import pandas as pd
import numpy as np
import json

def main():
    csvfilenames = collect_all_csv_filenames()
    everyone = cat_data(csvfilenames)
    read_csv(everyone)
    write_csv(everyone)
    write_data(csvfilenames)

def collect_all_csv_filenames():
    from glob import glob
    list = glob('*.csv')
    list.remove('mlp6.csv')
    if 'everyone.csv' in list:
    	list.remove('everyone.csv')
    return list

def cat_data(filenames):
    headers = ["First Name", "Last Name", 'NetID', 'Github Name', 'Team Name']

    cat_data = []
    for i in range(len(filenames)):
        temp = pd.read_csv(filenames[i], names = headers)
        cat_data.append(temp)
    cat_data = pd.concat(cat_data, axis=0)
    return cat_data

def write_csv(file):
    file.to_csv('everyone.csv')

def read_csv(everyone):
    check_no_spaces(everyone)
    check_camel_case(everyone)

def write_data(csv_filenames):
    for item in csv_filenames:
        print(item)
        csvName = item[0:len(item)-3]
        df = pd.read_csv(item)
        df.to_json(csvName+'json')

def check_no_spaces(everyone):
    isSpace = False
    for index, row in everyone.iterrows():
        teamname = row['Team Name']
        teamname = str(teamname)
        if teamname[0] == ' ':
            teamname = teamname[1::]
        if (" " in teamname) == True:
            isSpace = True

    if isSpace == True:
        print('There is at least one team with a space in their name')
    else:
        print('There are no spaces in team names')

def check_camel_case(everyone):
    camelcount = 0
    firstIndex = 0
    upperCount = 0
    for index, row in everyone.iterrows():
        teamname = row['Team Name']
        teamname = teamname.strip()
        for char in teamname:
            if firstIndex == 0 and char.isupper() == False:
                break
            if char.isupper():
                upperCount += 1
            firstIndex += 1

        if upperCount > 1:
            camelcount += 1

        firstIndex = 0
        upperCount = 0
    print('The number of teams that used camel count was:', camelcount)


if __name__ == "__main__":
    main()
















