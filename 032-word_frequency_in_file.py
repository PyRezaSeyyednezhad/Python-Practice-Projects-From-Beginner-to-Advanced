# word_frequency_in_file
import matplotlib.pyplot as plt
from collections import Counter

def read_file(filePath):
    text = ""
    with open(filePath, "r") as File1:
        for line in File1:
            text += line
    return text

def word_frequency_in_file(filePath):
    text = read_file(filePath)
    all_words = text.split()
    cleaned_words = []
    for unclean_word in all_words:
        if "." in unclean_word:
            unclean_word = unclean_word.replace(".", "")
            cleaned_words.append(unclean_word)
        elif "," in unclean_word:
            unclean_word = unclean_word.replace(",", "")
            cleaned_words.append(unclean_word)
        elif "?" in unclean_word:
            unclean_word = unclean_word.replace("?", "")
            cleaned_words.append(unclean_word)
        elif "!" in unclean_word:
            unclean_word = unclean_word.replace("!", "")
            cleaned_words.append(unclean_word)
        elif "@" in unclean_word:
            unclean_word = unclean_word.replace("@", "")
            cleaned_words.append(unclean_word)
        elif "#" in unclean_word:
            unclean_word = unclean_word.replace("#", "")
            cleaned_words.append(unclean_word)
        else:
            cleaned_words.append(unclean_word)
    
    return Counter(cleaned_words)

def word_distribution(filePath):
    res_list = word_frequency_in_file(filePath)
    xy_list = []
    for key, value in res_list.items():
        xy_list.append((key, value))
    most_word_count = sorted(xy_list, key=lambda x: x[-1], reverse=True)[:10]
    x = [key for key,_ in most_word_count]
    y = [value for _,value in most_word_count]
    plt.figure(figsize=(9,6))
    plt.barh(x, y)
    plt.legend(["Counts"])
    plt.xlabel("Counts")
    plt.ylabel("Words")
    plt.show()

# print(read_file("./files/lorem.txt"))
# print(word_frequency_in_file("./files/lorem.txt"))
print(word_distribution("./files/lorem.txt"))
