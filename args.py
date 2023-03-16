import argparse

def getArguments(args: list[str]):
    parser = argparse.ArgumentParser()
    #add a Encrypted word argument
    parser.add_argument("-e", "--encrypted", help="Encrypted word", required=True)
    #add a middle number argument
    parser.add_argument("-m", "--middle", help="Middle number", required=True)
    #add a bottom number argument
    parser.add_argument("-b", "--bottom", help="Bottom number", required=True)
    #add a second page word argument
    parser.add_argument("-s", "--second", help="Second page word", required=True)

    parser.add_argument("-i", "--indicators", help="Number of indicators", required=True)

    opt = parser.parse_args(args)
    return opt