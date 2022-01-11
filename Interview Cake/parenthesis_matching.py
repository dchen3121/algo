# Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.

# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
# finds the corresponding closing parenthesis.


def parenthesis_matching(sentence: str, index: int) -> int:
    num_params_in_between = 0

    for i in range(index + 1, len(sentence)):
        if sentence[i] == '(':
            num_params_in_between += 1
        elif sentence[i] == ')':
            if num_params_in_between == 0:
                return i
            num_params_in_between -= 1

    raise Exception
