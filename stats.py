def count_words(contents):
  words = contents.split()
  return len(words)

def count_letters(contents):
  letter_counts = {}
  words = contents.split()

  for word in words:
    lower_case = word.lower()  
    for letter in lower_case:
      if letter in letter_counts:
        letter_counts[letter] += 1
      else:
        letter_counts[letter] = 1
  
  return letter_counts

def sort_letter_count(letter_counts):
  list_pairs = []

  for item in letter_counts:
    item = {'letter': item, 'count': letter_counts[item]}
    list_pairs.append(item)    

  list_pairs.sort(key=lambda k: k['count'], reverse=True)
  return list_pairs
  

