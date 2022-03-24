def perm_lex(string):
    if string is None or len(string) == 0:
        """conditional statement for empty strings to return empty lists"""
        return []

    elif len(string) == 1:
        """conditional statement for returning a one character string"""
        return [string]

    else:
        lst = []

        for i in range(len(string)):
            """a loop is created that runs through each different character
               as the head of the string and is split from the body of the
               string """
            head = string[i]
            body = string[:i] + string[i + 1:]

            for j in perm_lex(body):
                """recursion is called here to run the new string that is the
                   body minus the head through the first function and continued
                   and appended to the final list"""
                lst.append(head + j)
    return lst
