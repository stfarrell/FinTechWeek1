favFruits = ["mango", "avocado", "pineapple", "grapes", "pomegranate"]

print(favFruits)

favFruits.append("orange")

print(favFruits)

enisFav = favFruits[2]
print(enisFav)

#favFruits.pop(2)
print(favFruits)

for fruit in favFruits:
    print("I like " + fruit + ".")
    
for i in range(0,len(favFruits)):
    print("I like " + favFruits[i])

#fruitCriteria = [True, 0.20, True, True, 100, "banana", True]
    
fruitCriteria = {"isFresh": True,
    "costPerPound": 0.20,
    "isRipe": True,
    "inSeason": True,
    "howMuchLike": 100,
    "whatIsIt": "banana",
    "isAllergic": True
}

print(fruitCriteria)

print(fruitCriteria["isAllergic"])

fruitCriteria["specialFeature"] = "GMO"

print(fruitCriteria)

for key in fruitCriteria:
    print("The answer to " + str(key) + " is " + str(fruitCriteria[key]) + ".")
    
print(fruitCriteria["specialFeature"])
    
  
    
    





