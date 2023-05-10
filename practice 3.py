#Візьміть файл, в якому є багато англійських слів у рядках. Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.


with open('your_file.txt', 'r') as f:
    words = f.read().split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, freq in sorted_word_freq:
    print(f'{word}: {freq}')
