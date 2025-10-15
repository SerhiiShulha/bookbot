def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    result = {}

    for char in text:
        result_char = char.lower()
        if result_char in result:
            result[result_char] += 1
        else:
            result[result_char] = 1

    return result

def sort_chars_by(char):
    return char["num"]

def get_report_values(chars_dict: dict[str, int]):
    result_list = []

    for char in chars_dict:
        if char.isalpha():
            result_list.append({"char": char, "num": chars_dict[char]})

    result_list.sort(reverse=True, key=sort_chars_by)

    return result_list