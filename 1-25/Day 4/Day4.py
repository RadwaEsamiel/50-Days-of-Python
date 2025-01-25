import random

random_int = random.randint(1,10)
print(random_int)

random_int = random.randint(0,1)
if random_int == 0 :
    print("Heads")
else:
    print("tail")

________________________________________________________________


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[10])
print(states_of_america[-1])

states_of_america[-1] = "Hawai"
print(states_of_america[-1])


states_of_america.append("New State")
print(states_of_america[-1])


states_of_america.extend(["new state1","new state 2"])
print(states_of_america[-2])

________________________________________________________________________________

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


random_number = random.randint(0,len(friends) -1)

print(friends[random_number])

_______________________________________________________
print(random.choice(friends))

__________________________________________________________

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
