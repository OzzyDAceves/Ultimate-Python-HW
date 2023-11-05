def not_space(text):
    new_text = ""
    for spaces in text:
        if spaces != " ":
            new_text += spaces
    return new_text


def reverse(text):
    twist_text = ""
    for char in text:
        twist_text = char + twist_text
    return twist_text


def is_palindrome(text):
    text = not_space(text)
    twist_text = reverse(text)
    # print(twist_text)
    return text.lower() == twist_text.lower()


print(is_palindrome("level"))
print(is_palindrome("Madam in Eden I m Adam"))
print(is_palindrome("Petu Dogo"))
