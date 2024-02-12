import random
import string
import time

def generate_random_text(length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for _ in range(length))
    
def generate_hello_world(words):
    correct_word = ""
    for i in words:
      right_word = ""
      while right_word != i:
        time.sleep(0.01)
        right_word = generate_random_text(1)
        print(correct_word + right_word)
        if right_word == i:
          print(correct_word)
          correct_word += right_word
    return correct_word

def get_ascii_letter_input(prompt):
   while True:
      user_input = input(prompt)
      if is_ascii_letter(user_input):
         return user_input
      else:
         print("Please enter only ASCII letters.")

def is_ascii_letter(input_string):
    for char  in input_string:
        if not('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9' or is_special_character(char)):
           return False
    return True

def is_special_character(char):
   return not char.isalnum()

user_input = get_ascii_letter_input("Enter ASCII letters only: ")
print(generate_hello_world(user_input))