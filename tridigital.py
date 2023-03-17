import logging
import enchant

d = enchant.Dict("en_US")

def tridigital_decipher(
    second_keyword: str,
    first_numbers: str,
    second_numbers: str,
    number_indicators: int,
    option_bypass: bool,
):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #remove any letters that is shown in the keyword
    for letter in second_keyword:
        alphabet = alphabet.replace(letter, "")
    # If the number of indicators is even, place the alphabet at the end of the keyword. Otherwise, place the alphabet at the beginning of the keyword.
    if number_indicators % 2 == 0:
        second_keyword = second_keyword + alphabet
    else:
        second_keyword = alphabet + second_keyword
    logging.debug(f"Using key: {second_keyword}")

    #split the second_keyword in three rows, of 9, 9 and 8 characters
    first_row = second_keyword[:9]
    second_row = second_keyword[9:18]
    third_row = second_keyword[18:]
    logging.debug(f"Tridigital grid: {first_row}")
    logging.debug(f"Tridigital grid: {second_row}")
    logging.debug(f"Tridigital grid: {third_row}")
    result = ""
    #loop 6 times
    for i in range(6):
        x = int(first_numbers[i])
        y = int(second_numbers[i])
        #use x as the row number and y as the column number to find the letter in the tridigital grid
        if x == 1:
            result += first_row[y-1]
        elif x == 2:
            result += second_row[y-1]
        elif x == 3:
            result += third_row[y-1]
    logging.info(f"Tridigital Deciphered: {result}")
    if not d.check(result) and not option_bypass:
        logging.fatal(f"Tridigital Deciphered: {result} is not a valid word")
        raise Exception(f"Tridigital Deciphered: {result} is not a valid word, use --tbypass to bypass this check")

    return result

        
