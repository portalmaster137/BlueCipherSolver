def string_to_alpha_list(input:str):
    output:list[int] = []
    for i in input:
        output.append(ord(i) - 64)
    return output

def alpha_list_to_string(input:list[int]):
    output:str = ""
    for i in input:
        output += chr(i + 64)
    return output