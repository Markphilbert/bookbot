frank = "books/frankenstein.txt"
with open(frank) as f:
    # ...
    file_contents = f.read()
    print(f"--- Begin report of {frank} ---")
    print(f"{len(file_contents.split())} words found in the document" )

    character_count_dict = {}
    character_count = 1
    for i in file_contents.lower():
        if i.isalpha():
            if i in character_count_dict:
                character_count_dict[i] += character_count
            else:
                character_count_dict[i] = character_count
    for key in sorted(character_count_dict):
        print(f"The '{key}' character was found {character_count_dict[key]} times")
    print("--- End report ---")
