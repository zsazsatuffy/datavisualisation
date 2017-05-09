import json

with open('CO2IntesityEdit.json') as file1:
  dataSetA = json.load(file1)
with open('countrieslatlon.json') as file2:
  dataSetB = json.load(file2)

print "setA:", len(dataSetA)
print "setN:", len(dataSetB)

print

listOfCountrynames = [c["countryname"] for c in dataSetB]
print listOfCountrynames

for data in dataSetA:
    if not data["countryname"]in listOfCountrynames:
        print data["countryname"]
