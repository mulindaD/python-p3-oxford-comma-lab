def oxford_comma(items):
    # items is a list of strings
    if len(items) == 2:
        str = ' and '.join(items)
        return str
    
    elif len(items) > 2:
        # If the length of the items of the list is more than 2
        # Join all the words before that str with ","
        # join the last word with that new str with "and" 
        str1 = ', '.join(items[:-1])
        print(f"{str1}, and {items[-1]}")
        return f"{str1}, and {items[-1]}"
    
    else:
        str = ''.join(items)
        return str

oxford_comma(["kiwi", "durian", "starfruit"])