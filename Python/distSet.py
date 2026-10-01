thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "fuel type": 'diesel'
}

thatdict = dict(brand = 'Audi', model = 'q9', fuel_type = 'Octen')

print(type(thisdict))
print(thisdict)
print(thisdict['brand'])
print(len(thisdict))
print(thatdict)

x = thisdict["fuel type"]
print(x)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

# Looping in Dist...
if 'model' in thisdict:
    print('Yes model is present');
else:
    print('Not a car');

for x in thisdict.values(): # to access items, keys use the same loop process..
    print(x)

# copy() mehtod in dist..

myNewDist = thisdict.copy();
print(myNewDist)

# diff btwn copy() method..

x = thisdict
print(thisdict)
print(id(thisdict))
print(x)
print(id(x))
x['model'] = 'q10'
print(thisdict)
print(x)

# now when use copy method

x = thisdict.copy()
x['model'] = 'q11'
print('Main dist:', thisdict)
print('Copy & update dist: ', x)

# nested dist...
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.popitem()) # remove last item from the dist...

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
y = car.setdefault("color", "white")
print(x)
print(y)
