import basic
import os

while True:
    text = input('phlush > ')
    if text.lower() == 'cls':
        clear = lambda: os.system('cls')
        clear()
        continue
        
    elif text.lower() in ['exit', 'exit()', 'quit', 'quit()']:
        exit()

    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)