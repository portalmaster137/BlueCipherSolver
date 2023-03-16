import logging
import util

def vigenere_cipher(
    enecryted: str,
    tri_deciphered: str,
):
    encrypted_list = util.string_to_alpha_list(enecryted)
    tri_deciphered_list = util.string_to_alpha_list(tri_deciphered)
    processing_list:list[int] = []

    for i in range(len(encrypted_list)):
        #first, get the value of the encrypted letter and tridigital deciphered letter
        encrypted_value = encrypted_list[i]
        tri_deciphered_value = tri_deciphered_list[i]
        #enc - tri
        processing_value = encrypted_value - tri_deciphered_value
        #if the value is less than 1, add 26 to it
        while processing_value < 1:
            processing_value += 26
        #add the value to the processing list
        processing_list.append(processing_value)
        logging.debug(f"Vigenere | {enecryted[i]} - {tri_deciphered[i]} = {processing_value}")
    result = util.alpha_list_to_string(processing_list)
    logging.debug(f"Vigenere Deciphered: {result}")
    return result
