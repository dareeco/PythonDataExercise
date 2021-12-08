# imports go here
from PycharmProjects.Praksa2 import parser


def main():
   parse_result=parser.parser()
   stats=parse_result.__getitem__("stats")
   total_sentences=stats.get("total_sentences")
   print(f'Found total of {total_sentences} sentences. With total of {stats["total_characters"]} character in the file....')
   #It can be done with getting to avoid KeyError Exception




if __name__ == '__main__':
   main()
   
