import operator

full_text = input("Give me some text: ")

remove_these = [',','.','?','(',')','-']
for thing in remove_these:
  full_text = full_text.replace(thing,'')


word_list = full_text.lower().split()

word_count = {}

for word in word_list:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=False)
  


for word_tuple in sorted_count:
  print(f'{word_tuple[0].capitalize()} - {word_tuple[1]}')

print(f'\nThere are {len(sorted_count)} unique words!')