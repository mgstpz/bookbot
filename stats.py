def get_num_words(book_content):
    print("----------- Word Count ----------")
    return len(book_content.split())

def count_chars(book_content):
    print("--------- Character Count -------")
    list_of_chars = {}
    for i in range(0, len(book_content)):
        for c in range(0, len(book_content[i])):
            letter = book_content[i][c].lower()
            if (letter not in list_of_chars):
                list_of_chars[letter] = 1
            else:
                list_of_chars[letter] += 1
    return list_of_chars
def sort_on(items):
    return items["num"]

def sort_dict(dict):
    new_dict = []
    for key in dict:
        if key.isalpha():
            new_dict.append({"char": key, "num": dict[key]})
   
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict