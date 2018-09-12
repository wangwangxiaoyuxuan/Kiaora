"""
The String_Builder class uses Markov Chains to build a string
sequence of a specified degree of similarity (S) to a user given
text file or string sequence.

If generating a sequence longer than the given original, the
program works better with very high user given material to degree of
similarity ratio. I.e., longer material and a shorter Markov Chain.

Fun input text example:
    "I find myself not nobody who would preferedly eat a ding dong nor am I the bringer of harbringer. I like, only sometimes, do I like to have hats. Neither can I, nor you, nor he, nor she. To do what. Why, I do not know. But here we shall launch into a soliloquay, mayhaps I spelt that wrongly. Hold on, are we not already engaged in a noninquisitive soliloquay."

Referenced from:
    CSCI 2101A Lab 2
    Author: McKenna Thomas-Franz, James Wang
    Version: 21st February, 2018
"""

from Markov_Chain import *

class String_Builder():
    def __init__(self):
        """ Constructs a String_Builder of a given degree
            of similarity. """
        self.S = input(
            "Your desired Markov_Chain length.\n\tRecommend a small chain (1-3).\n\tType int: ")
        self.sample_text = ""
        self.generated_chain = Markov_Chain()
        self.generated_text = ""
    
    
    def sample_from_file(self):
        """ Gets sample_text from a text file. """
        filename = input(
            "Your filename.\n\tRecommend a long text.\n\tRemember quotation marks and .txt.\n\tType str: ")
        with open(filename, 'r') as text_file:
            self.sample_text = text_file.read()
    
    
    def sample_from_input(self):
        """ Gets sample_text from a shell input. """
        self.sample_text = input(
            "Your text.\n\tRecommend to be over 100 words.\n\tRemember quotation marks.\n\tType str: ")
    
    
    def generate_Markov_Chain(self):
        """ Generate a Markov Chain of S degree of similarity
            to the sample_text. """
        i = 0
        while i < len(self.sample_text):
            if i + self.S >= len(self.sample_text):
                break
            else:
                self.generated_chain.add_to_chain(
                    self.sample_text[i : i + self.S],
                    self.sample_text[i + self.S])
                i += 1
    
    
    def generate_text_from_chain(self):
        """ Generate a text of text_length length using
            generated_chain as a probability guide towards
            similarity to sample_text. """
        text_length = input(
            "Your desired length of text.\n\tType int: ")
        self.generated_text = self.sample_text[0 : self.S]
        for i in range(text_length - self.S):
            self.generated_text += self.generated_chain.\
                generate_proceeding_character(
                self.generated_text[i : i + self.S])
    
    
    def print_generated_text(self):
        """ Print generated_text. """
        print(self.generated_text)
    
    
    def get_generated_text(self):
        """ Returns generated_text. """
        return self.generated_text
    
    
    def main_method(self):
        """ Operate the class from asking for a desired
            degree of similarity to printing generated_
            text. Will finally return generated_chain. """
        sample_option = input(
            "Your text input method. Either a local text file (\"file\")\nor a string sequence as input (\"input\").\n\tType str: ")
        if sample_option == "file":
            self.sample_from_file()
        elif sample_option == "input":
            self.sample_from_input()
        self.generate_Markov_Chain()
        self.generate_text_from_chain()
        #self.print_generated_text()
        return self.generated_text
            
        

if __name__ == "__main__":
    test_Builder = String_Builder()
    #test_Builder.sample_from_input()
    ##test_Builder.sample_from_file()
    ##print(len(test_Builder.sample_text))
    #test_Builder.generate_Markov_Chain()
    #test_Builder.generate_text_from_chain()
    #test_Builder.print_generated_text()
    test_text = test_Builder.main_method()
    print(test_text)