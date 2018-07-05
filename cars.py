showroom = {"Tesla Model S", "1963 Chevrolet Corvette", "Datsun 240z", "Tesla Model 3"}
print(len(showroom))
showroom.add("Tesla Model S")
print(showroom)
showroom.update({"1966 Chevrolet Nova", "Toyota Camry"})
showroom.discard("Toyota Camry")
junkyard = {"Mazda Navajo", "Chrylser Crossfire", "1963 Chevrolet Corvette"}
print(junkyard.intersection(showroom))
showroom = showroom.union(junkyard, showroom)
print(showroom)
showroom.discard("Mazda Navajo")
print(showroom)