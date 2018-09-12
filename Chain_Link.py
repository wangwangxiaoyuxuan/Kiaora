"""
The Chain_class is a frequency map of character-keys and
integer-values where each character's respective integer is
its frequency of occurance.

Referenced from:
    CSCI 2101A Lab 2
    Author: McKenna Thomas-Franz, James Wang
    Version: 21st February, 2018
"""

import random

class Chain_Link:
    def __init__(self):
        """ Construct a link. """
        self.link = {}
    
    
    def add_to_link(self, char_to_add):
        """ Adds or modifies a key:value pair if key is new
            or already in the frequency map. """
        if char_to_add not in self.link:
            self.link[char_to_add] = 1
            # print("modified +1 to " + char_to_add)
        else:
            self.link[char_to_add] += 1
            # print("added " + char_to_add)
    
    
    def generate_probable_character(self):
        """ Generates a character based on its frequency of
            occurance. Crude method of populating a list. """
        probable_possibilities_list = []
        for character, frequency in self.link.items():
            probable_possibilities_list += list(character * frequency)
        the_character = probable_possibilities_list[
            random.randint(0, len(probable_possibilities_list) - 1)]
        return(the_character)
    
    
    def test(self):
        """ Test various functions in the class. """
        self.add_to_link('b')
        self.add_to_link('z')
        self.add_to_link('b')
        self.add_to_link('a')
        self.generate_probable_character()
        
        
        
        
    

if __name__ == "__main__":
    test = Chain_Link()     # instantiate new Chain_Link
    test.test()             # shall: 1) print "I exist", 2) print list.
    print(test.link)        # frequency map is accessible outside of class
    if 'a' in list(test.link):  # understanding how to check keys
        print ("'a' is In")
    else:
        print ("Ney to 'a'")
    print("Wabbaba", test.link)
    test.generate_probable_character()