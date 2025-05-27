# slicing: used for creating substring by extracting elements from another string
#         indexing[] or slice()
#         [start:stop:step]

#starting index & stopping index
name="Alan Otieno"
first_name=name[0:4] # start index:end index or [:4]
last_name=name[5:11] #start index:end index or [5:]
print(first_name)
print(last_name)

#step : how much we are increasing index by between starting and stopping
funky_name=name[0:12:2] #displays every 2nd character of the name or [::3
print(funky_name)

# reverse string
reversed_name=name[::-1]
print(reversed_name)

# using slice function
website="http://google.com"
slice=slice(7,-4) #or slice(-10,-4)
print(website[slice])

url=website[7:13]
print(url)