# imports go here
from PycharmProjects.Praksa2 import parser


def main():
   sentences,stats=parser.Parser()
   total_sentences=stats["total_sentences"]
   total_characters=stats["total_characters"]
   print(f"Found total of {total_sentences} sentences. With total of {total_characters} character in the file....")


   pass

if __name__ == '__main__':
   main()
   
