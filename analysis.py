import csv

def get_highest_gdp(data,year):
    hi_gdp_state=data[0]["GeoName"]
    max=float(data[0][year])
    for d in data:
        val=float(d[year])
        if val<max:
            continue
        if val>max:
            max=val
            hi_gdp_state=d["GeoName"]
    return hi_gdp_state

def get_lowest_gdp(data, year):
    lo_gdp_state=(data[0]["GeoName"])
    min=float(data[0][year])
    for d in data:
        val=float(d[year])
        if val>min:
            continue
        if val<min:
            min=val
            lo_gdp_state=d["GeoName"]
    return lo_gdp_state

def get_state_gdp(data, state, year):
     for row in data:
        if row['GeoName'] == state:
            return row[year]



# save each row into a list 
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data, '2020'))

#get get_state_gdp for state of choosing using "get_state_gdp(list_data,"state_name","year")""
print(get_state_gdp(list_data,'Virginia','2020'))

#get state YOY between 2019 and 2020
yr1 = float(get_state_gdp(list_data, "Virginia", "2019"))
yr2 = float(get_state_gdp(list_data, "Virginia", "2020"))

print(float(yr2 - yr1))