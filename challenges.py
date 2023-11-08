def double_letters(word):
    for i in range (len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

print(double_letters("eror"))

def add_dots(text):
  return  "." .join(text)

def remove_dots(text):
    return text.replace(".", "")