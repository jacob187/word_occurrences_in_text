import string, re
from collections import Counter


def main():
    try:
        # Opens text file and stores in memory as file object
        with open("alice.txt") as f_obj:
            word_frequncy_in_text = word_freq(f_obj.read())
            my_list = dict_to_list(word_frequncy_in_text)
            sorted_list = sort_lists_by_occurrence(my_list)
            print(print_list(sorted_list))

    except FileNotFoundError:
        print("File does not exist")


def word_freq(contents: str):
    punctuation_list = list(string.punctuation)
    words = re.findall(r"\b[\w\']+\'?[\w]+\b", contents.lower())

    # Remove punctuation from each word
    cleaned_words = [word.strip("".join(punctuation_list)) for word in words]

    # Use Counter to count word frequencies
    word_occurrence = Counter(cleaned_words)

    return word_occurrence


def dict_to_list(word_freq: dict):
    occurrences = [[word, occurrence] for word, occurrence in word_freq.items()]
    return occurrences


def sort_lists_by_occurrence(input_list: list):
    sorted_list = sorted(input_list, key=lambda x: x[1])
    return sorted_list


def print_dict(words_freq: dict):
    output = ""
    for key, value in sorted(words_freq.items()):
        output += f"{key} :: {value}\n"

    return output


def print_list(word_freq: list):
    output = ""
    for i in word_freq:
        output += f"{i[0]} :: {i[1]}\n"
    return output


if __name__ == "__main__":
    main()
