# imports go here
from PycharmProjects.Praksa2 import parser


def main():
   dict=parser.parser()
   stats=dict["stats"]
   print(f'Found total of {stats["total_sentences"]} sentences. With total of {stats["total_characters"]} character in the file....')


   pass

if __name__ == '__main__':
   main()
   
