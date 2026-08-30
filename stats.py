def words_count(word: str) -> int:
    nums_word = word.split()
    return len(nums_word)

def count_character(book: str) -> dict[str,int]:

    character: dict[str,int] = {}
    lower_book: str =  book.lower()

    for letter in lower_book:

        if letter in character:
            character[letter] += 1
        else:
            character[letter] = 1

    return character



def short_on(content:tuple[str,int]) -> int:
    return content[1]

def chars_dict_to_sorted_list(chars:dict[str,int]) -> list[tuple[str,int]]:
    chars_count: list[tuple[str,int]] = []

    for character in chars:
        chars_count.append((character, chars[character]))

    sorted_list = sorted(chars_count,reverse=True,key=short_on)

    return sorted_list
