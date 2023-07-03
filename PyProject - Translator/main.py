# python offline translator package

from translate import Translator

input_lang = input('What language you want to translate to enter codes: ')
translator_Obj = Translator(to_lang=input_lang)

# input_text = input('Enter the text to translate: ')
try:
  with open('tests.txt', mode='r') as my_file:
    text = my_file.read()
    translation_var = translator_Obj.translate(text)
    
    with open('text-coverted.txt', mode='w') as my_file:
      my_file.write(translation_var)
      
except (FileNotFoundError, FileExistsError):
  print("File is not found or doesn't exist!")
