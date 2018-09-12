"""
The Markov_Chain class is a sequence table of string sequence-keys
and frequency map-values where each string sequence's respective
frequency map is the likelihood of the character which proceeds
it.

Referenced from:
    CSCI 2101A Lab 2
    Author: McKenna Thomas-Franz, James Wang
    Version: 21st February, 2018
"""

import random as rand
from Chain_Link import *

class Markov_Chain():
    def __init__(self):
        """ Constructs a chain. """
        self.chain = {}
    
    
    def add_to_chain(self, string_sequence, proceeding_character):
        """ Adds or modifies a key:value pair if key is new
            or already in the sequence. """
        if string_sequence not in self.chain:
            new_link = Chain_Link()
            new_link.add_to_link(proceeding_character)
            self.chain[string_sequence] = new_link
        else:
            existing_link = self.chain[string_sequence]
            existing_link.add_to_link(proceeding_character)
            self.chain[string_sequence] = existing_link
    
    
    def generate_proceeding_character(self, string_sequence):
        """ Generates a proceeding character for string_sequence.
            If string_sequence is not in the chain, will generate
            a character from a pool randomly. Else, will generate a
            character based on the probabilities found in the
            string_sequence's frequency map. """
        if string_sequence not in self.chain:
            characters_list = "abcdefghijklmnopqrstuvwyxz"
            chosen_index = rand.randint(0, len(characters_list) - 1)
            return characters_list[chosen_index]
        else:
            appropriate_link = self.chain[string_sequence]
            chosen_character = appropriate_link.generate_probable_character()
            return chosen_character
    
    
    def test_chain(self):
        """ Test various functions. """
        self.add_to_chain("string1", 'a')
        self.add_to_chain("string2", 'b')
        self.add_to_chain("string1", 'a')
        self.add_to_chain("string1", 'b')
        generated_list = []
        a_val = 0
        b_val = 0
        for i in range(0, 100000):
            generated_character = self.generate_proceeding_character("string1")
            generated_list.append(generated_character)
            if generated_character == 'a':
                a_val += 1
            else:
                b_val += 1
        print("a:b ratio", float(a_val)/float(b_val))
        print(self.generate_proceeding_character("nosuchstring"))
    
    

if __name__ == "__main__":
    test = Markov_Chain()
    test.test_chain()
    for string_sequence in test.chain:
        print([string_sequence, test.chain[string_sequence].link])