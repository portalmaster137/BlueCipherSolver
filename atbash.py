import logging
def decrypt_atbash(keyword: str):
    #first, turn the keyword into a list of characters
    temp = list(keyword)
    for i in temp:
        #get the value of the character, A=1, B=2, etc.
        value = ord(i) - 64
        #subtract the value from 27 to get the new value
        new_value = 27 - value
        #convert the new value back to a character
        new_char = chr(new_value + 64)
        #replace the old character with the new character
        keyword = keyword.replace(i, new_char)
        logging.debug(f"Atbash |{i} -> {new_char}")
    logging.info(f"Atbash Deciphered: {keyword}")
    return keyword