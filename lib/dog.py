#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Frenchie", breed="Mastiff"):
        self.name = name
        self.breed = breed

    def getname(self):
        print("Retriving name")
        return self._name
    
    def setname(self, name):
        if type(name) is str and 0 < len(name) < 25 and name:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(getname, setname)
    
    def getbreed(self):
        print("Retriving breed")
        return self._breed

    def setbreed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    breed = property(getbreed, setbreed)

