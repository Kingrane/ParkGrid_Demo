def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    test_string = "А роза упала на лапу Азора"
    result = is_palindrome(test_string)
    print(f"Строка '{test_string}' - это палиндром? {result}")
