def mark_string(value:str, n:int = 48):
    """
    Wraps a given string between and n number of '-' characters.\n
    n defaults to 48 if value is not provided
    """
    marks = n - len(value)
    marker = "-" * int(marks / 2)
    return f"{marker} {value} {marker}"