def print_marked_string(value:str, n:int = 48):
    """
    Wraps a given string between and n number of '-' characters and prints it.\n
    n defaults to 48 if value is not provided.
    Example: ----- Example -----
    """
    marks = n - len(value)
    marker = "-" * int(marks / 2)
    print(f"{marker} {value} {marker}")