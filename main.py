from stats import words_count, count_character,chars_dict_to_sorted_list
import sys




def get_book_test(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents



def printer_report(path: str,wordCount:int,sortCharacter: list[tuple[str,int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for character,count in sortCharacter:
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


def main(path:str):
    #Obtengo el contenido del libro incertando la direccion del libro en formato texto
    content = get_book_test(path)

    #Obtengo la cantidad de palabras que tiene el libro
    words = words_count(content)

    #Cuento cuantas veces se uso cada letra en el libro
    count = count_character(content)

    #Ordeno las letras de mayor a menor frecuencia
    sorted = chars_dict_to_sorted_list(count)

    #Le agrego estetica al momento de devolver el resultado
    printer_report(path,words,sorted)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
#main()
