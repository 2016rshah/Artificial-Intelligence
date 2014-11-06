def nb(w1, w2):
  count = 0
  for index in range(len(w1)):
    if(w1[index]!=w2[index]):
      count+=1
  return count;

file = open("words.txt", "r")

lines = file.readlines()
for index in range(len(lines)):
  lines[index] = lines[index].strip()
while(True):
  word1 = input("What word do you want to test?")
  print(word1)
  array = []
  for word2 in lines:
    if(nb(word1, word2) == 1):
      array.append(word2)
  print(array)
  print("------------------")

