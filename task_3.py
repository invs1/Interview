
words = "Hey there mate, it’s nice to finally meet you!"
maximum_width = 16

def justify(text, max_width: int) -> list[str]:
    """
    Function greedy justify paragraph of text.
    Max len of single word in the text = max_width.
    """

    lst_of_words = text.split()

    # temporary list
    lst = []
    # length of words
    n = 0
    # result list
    result = []

    for word in lst_of_words:

        while len(word) + n + len(lst) > max_width:
            gaps = (len(lst) - 1) or 1
            q, rem = divmod(max_width - n, gaps)

            for i in range(gaps):
                lst[i] += " " * q + (" " if i < rem else "")
            result.append("".join(lst))
            n, lst = 0, []

        lst.append(word)
        n += len(word)

    return result + [" ".join(lst).ljust(max_width)] if lst else []


print(justify(words, maximum_width))
