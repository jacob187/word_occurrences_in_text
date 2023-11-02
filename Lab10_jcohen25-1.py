import string, re
from collections import Counter


def main():
    # book_name = input(
    #     "Please enter the name of the text file, including the extension: "
    # )
    try:
        # Opens text file and stores in memory as file object
        with open("alice.txt") as f_obj:
            word_frequncy_in_text = wordFreq(f_obj.read())
            # print(word_frequncy_in_text.get("the"))
            output = printOut(word_frequncy_in_text)
            print(output)
    except FileNotFoundError:
        print("File does not exist")


def wordFreq(contents: str):
    # This commented code was my original soution
    # I found that the Counter makes the code more readable and consie
    # punctuation_list = list(string.punctuation)
    # characters_in_book = contents.split()
    # print(characters_in_book)

    # cleaned_words = [
    #     word for word in characters_in_book if word not in punctuation_list
    # ]

    # print(cleaned_words)
    # # cleaned_words = []
    # # for word in characters_in_book:
    # #     if word:
    # #         cleaned_word = "".join(
    # #             char for char in word if char not in punctuation_list
    # #         )
    # #         if cleaned_word:  # Check if the cleaned word is not empty
    # #             cleaned_words.append(cleaned_word)

    # # # Counts the occurences of every word and adds them to the dictionary
    # word_occurrence = {}
    # for word in cleaned_words:
    #     if word.lower() not in word_occurrence:
    #         word_occurrence[word.lower()] = 1
    #     elif word.lower() in word_occurrence:
    #         word_occurrence[word.lower()] += 1

    #############
    punctuation_list = list(string.punctuation)
    words = re.findall(r"\b[\w\']+\'?[\w]+\b", contents.lower())

    # Remove punctuation from each word
    cleaned_words = [word.strip("".join(punctuation_list)) for word in words]

    # Use Counter to count word frequencies
    word_occurrence = Counter(cleaned_words)

    return word_occurrence


def printOut(words_freq: object):
    output = ""
    for key, value in sorted(words_freq.items()):
        output += f"{key} :: {value}\n"

    return output


if __name__ == "__main__":
    main()


# def wordFreq(contents):
#     This commented code was my original soution
#     I found that the Counter makes the code more readable and consie
#     punctuation_list = list(string.punctuation)
#     characters_in_book = contents.split()

#     cleaned_words = []
#     for word in characters_in_book:
#         if word:
#             cleaned_word = "".join(
#                 char for char in word if char not in punctuation_list
#             )
#             if cleaned_word:  # Check if the cleaned word is not empty
#                 cleaned_words.append(cleaned_word)

#     # Counts the occurences of every word and adds them to the dictionary
#     word_occurrence = {}
#     for word in cleaned_words:
#         if word.lower() not in word_occurrence:
#             word_occurrence[word.lower()] = 1
#         elif word.lower() in word_occurrence:
#             word_occurrence[word.lower()] += 1
