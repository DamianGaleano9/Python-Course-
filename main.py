"""
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]
"""

"""
def manual_incrementing_matrix(n):
  matrix = [[None for y in range(n)] for x in range(n)]

  counter = 0

  for idx, el in enumerate(matrix):
    for nested_idx, nested_el in enumerate(el):
      matrix[idx][nested_idx] = counter + nested_idx

      counter += 1

  return matrix


print(manual_incrementing_matrix(3))

"""

#Python String Basics

""""
starter_sentence = "The quick brown fox jumped"

first_word = starter_sentence[0]

print(first_word)

sentence = "HELLO THERE!"
lowercase_sentence = sentence.lower()
print(lowercase_sentence)

"""


#In the code below, assign the variable sub_sentence to be "pie" by selecting a range from "sentence".

"""sentence = "Some pie please!"
sub_sentence = sentence[5:8]
print(sub_sentence)

"""


"""
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.

"""

my_heredoc = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.

.strip()

print(my_heredoc)"""




