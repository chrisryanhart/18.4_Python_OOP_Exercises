"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    ...
    def __init__(self):
        self.text = None
        self.parse_file()
    def __repr__(self):
        words_read = len(self.text)
        return f"{words_read} words read"
    # def read_file(self):


        # return text
    def parse_file(self):
        file = open("word_test.txt", "r")
        self.text = file.read().split()
        # split_text = self.text.split()
        # print(self.text)
        file.close()

    def random(self):
        word_count = len(self.text)
        random_index = random.randint(0,word_count-1)
        return self.text[random_index]
    


        return self.text
    # must read in list of words 

    # print out number of word read

    # def random():
        # returns a random word from that list of words


words = WordFinder()

random.randint(1,3)


# special word finder 
# eliminate special characters 
# never return 
# if first character is #, remove item
# we don't know when we'll receive file with comments or not

class SpecialWordFinder(WordFinder):
    def __init__(self):
        super().__init__()
        self.removed_list = []
        self.remove_special()
        

    def print_list(self):
        print('in print list func: ', self.text)

    def remove_special(self):
        for ele in self.text:
            if ele[0] != '#':
                self.removed_list.append(ele)
                # print('comment')
        # print(self.removed_list)
        # loop through list
        # if spec char exists, delete
        # can push to new array


specialwords = SpecialWordFinder()
