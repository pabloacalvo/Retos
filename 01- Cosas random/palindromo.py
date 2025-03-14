def detect_palindrome(txt:str):
    txt = txt.replace(' ','').lower()
    return txt == txt[::-1]


texto = "anita lava la tina"

print(detect_palindrome(texto))