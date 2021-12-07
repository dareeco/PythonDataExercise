# imports go here
import re

from PycharmProjects.Praksa import parser

def main():
   pass

if __name__ == '__main__':
   f = open("example.txt", "r")
   data=f.read()
   total_sentences,total_characters=parser.counter(data)
   print(f"Found total of {total_sentences} sentences. With total of {total_characters} character in the file....")

