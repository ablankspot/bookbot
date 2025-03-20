from stats import count_words
from stats import count_letters
from stats import sort_letter_count

def get_book_text(path):
  contents = ""
  with open(path) as f:
    contents = f.read()
  return contents

def main():
  import sys

  if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

  path = sys.argv[1]
  book = get_book_text(path)
  num_words = count_words(book)
  letter_counts = count_letters(book)
  sorted_map = sort_letter_count(letter_counts)
  
  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {path}...')
  print('----------- Word Count ----------')
  print(f'Found {num_words} total words')
  print('--------- Character Count -------')
  for item in sorted_map:
    print('{}: {}'.format(item['letter'], item['count']))
  print('============= END ===============')
  

main()