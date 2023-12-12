def most_common_words(filepath, number_of_words=3):  
    from collections import Counter
    f = open(filepath,"r", encoding='utf-8')
    filepath = f.read()
    for char in '-.,\n':
        filepath = filepath.replace(char,' ')
    filepath = filepath.lower().split()
    number_of_words = Counter(filepath).most_common(3)
    return number_of_words
print(most_common_words('lorem_ipsum.txt'))

