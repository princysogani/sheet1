x = input("Input words: ")

words_list = x.split(",")
words_list.sort()
print((', ').join(words_list))
