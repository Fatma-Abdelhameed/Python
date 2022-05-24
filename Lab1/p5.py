vowels = ['a', 'i', 'o', 'u', 'e']
def delete_vowels_from_text(text):
    for vowel in vowels:
         text = text.replace(vowel, '')
    return text
print(delete_vowels_from_text("fatma")) #output=>ftm