def text_analyzer(text):
    """
    Que miras bobo?
    """
    if text is None:
        text = input("What is the text to analyse?\n")
    if not isinstance(text, str):
        print("Error: Argument must be a string.")
        return
    uppers = sum(1 for c in text if c.isupper())
    lowers = sum(1 for c in text if c.islower())
    puncs = sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    spaces = sum(1 for c in text if c.isspace())
    print("The text contains:")
    print(f" - {uppers} upper letters")
    print(f" - {lowers} lower letters")
    print(f" - {puncs} punctuation marks")
    print(f" - {spaces} spaces")







