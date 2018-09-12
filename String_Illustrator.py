"""
The String_Illustrator class has drawing capabilities. Int-
erprets a text as drawing commands and then draws using turtle.
"""

from String_Builder import *
from turtle import *


class String_Illustrator():
    def __init__(self):
        """ Constructs a String_Illustrator. """
        myString_Builder = String_Builder()
        self.generated_text = myString_Builder.main_method()
        self.word_list = self.generated_text.split(" ") # replace("\n", " ").
        self.instructions_list = []
        self.average_instruction_word_length = 0
        self.total_instruction_word_length = 0
    
    
    def generate_instructions_list(self):
        """ Generate a list of drawing instructions from 
            word_list. """
        for word in self.word_list:
            if len(word) > 0:
                instruction_word = (word.lower().replace(
                    "eau", "o").replace("oe", "o").replace(
                    "ae", "e").replace("ue", "u").replace(
                    "oo", "u").replace("ea", "i").replace(
                    "ee", "i").replace("sh", "D").replace(
                    "ch", "D").replace("kh", "D").replace(
                    "b", "C").replace("d", "C").replace(
                    "p", "C").replace("h", "S").replace(
                    "f", "S").replace("w", "S").replace(
                    "v", "S").replace("k", "I").replace(
                    "q", "I").replace("c", "I").replace(
                    "x", "I").replace("m", "F").replace(
                    "n", "F").replace("r", "B").replace(
                    "y", "B").replace("l", "R").replace(
                    "t", "R").replace("g", "H").replace(
                    "j", "H").replace("z", "T").replace(
                    "s", "T").replace("-", " ").replace(
                    ",", " ").replace(".", "  ").replace(
                    "/t", "   ").replace("\n", "   "))
                self.total_instruction_word_length += len(instruction_word)
                self.instructions_list.append(instruction_word)
        self.average_instruction_word_length = self.total_instruction_word_length / len(self.instructions_list)
    
    
    def draw_from_instructions(self):
        """ Draws. """
        setup(width = 1.0, height = 1.0, startx = None, starty = None)
        speed(99999)
        
        pu()
        xmax = .5 * (window_width())
        ymax = .5 * (window_height())
        window_top_left = (-xmax, ymax)
        starting_point = (-xmax, ymax - 5)
        vertical_progression = (window_height() - 10) / (self.total_instruction_word_length /
                                                         (window_width() / 10))
        goto(starting_point)
        
        for instruction_word in self.instructions_list:
            color("black")
            for instruction in instruction_word:
                if xcor() > xmax - 10:
                    pu()
                    goto(-xmax, ycor() - vertical_progression)
                
                if instruction == "a":
                    color("red")
                    pd()
                    forward(10)
                elif instruction == "i":
                    color("cyan")
                    pd()
                    forward(10)
                elif instruction == "u":
                    color("brown")
                    pd()
                    forward(10)
                elif instruction == "e":
                    color("pink")
                    pd()
                    forward(10)
                elif instruction == "o":
                    color("purple")
                    pd()
                    forward(10)
                elif instruction == "T":
                    forward(2)
                    right(90)
                    forward(2)
                    left(90)
                    forward(6)
                    left(90)
                    forward(2)
                    right(90)
                    forward(2)
                elif instruction == "C":
                    forward(2)
                    pu()
                    forward(6)
                    left(90)
                    pd()
                    circle(3)
                    right(90)
                    forward(2)
                elif instruction == "S":
                    forward(2)
                    pu()
                    forward(6)
                    pd()
                    right(90)
                    forward(3)
                    right(90)
                    forward(6)
                    right(90)
                    forward(6)
                    right(90)
                    forward(6)
                    right(90)
                    forward(3)
                    left(90)
                    forward(2)
                elif instruction == "I":
                    forward(2)
                    pu()
                    forward(6)
                    pd()
                    goto(xcor(), ycor() + 3)
                    goto(xcor() - 6, ycor() - 3)
                    goto(xcor() + 6, ycor() -3)
                    goto(xcor(), ycor() + 3)
                    seth(0)
                    forward(2)
                elif instruction == "F":
                    forward(2)
                    pu()
                    forward(6)
                    pd()
                    goto(xcor() - 6, ycor() + 3)
                    goto(xcor(), ycor() - 6)
                    goto(xcor() + 6, ycor() + 3)
                    seth(0)
                    forward(2)
                elif instruction == "D":
                    forward(2)
                    pu()
                    forward(6)
                    pd()
                    goto(xcor() - 3, ycor() + 3)
                    goto(xcor() - 3, ycor() - 3)
                    goto(xcor() + 3, ycor() - 3)
                    goto(xcor() + 3, ycor() + 3)
                    seth(0)
                    forward(2)
                elif instruction == "B":
                    forward(2)
                    goto(xcor() + 2, ycor() + 3)
                    goto(xcor() + 2, ycor() - 6)
                    goto(xcor() + 2, ycor() + 3)
                    seth(0)
                    forward(2)
                elif instruction == "R":
                    forward(4)
                    left(90)
                    forward(3)
                    right(180)
                    forward(3)
                    left(90)
                    forward(2)
                    right(90)
                    forward(3)
                    left(180)
                    forward(3)
                    right(90)
                    forward(4)
                elif instruction == "H":
                    forward(2)
                    pu()
                    forward(6)
                    pd()
                    left(90)
                    circle(3, 180)
                    pu()
                    seth(0)
                    forward(6)
                    pd()
                    forward(2)
                elif instruction == " ":
                    pu()
                    forward(10)
        done()


if __name__ == "__main__":
    Kiaora = String_Illustrator()
    Kiaora.generate_instructions_list()
    print(Kiaora.generated_text)
    print(Kiaora.word_list)
    print(Kiaora.instructions_list)
    Kiaora.draw_from_instructions()
    