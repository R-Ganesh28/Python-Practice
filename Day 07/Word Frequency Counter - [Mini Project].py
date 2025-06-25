def word_count(filename):
    with open(filename, 'r') as f:
        words = f.read()
        words = words.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    print(count)
filename = "sample.txt"
word_count(filename)
