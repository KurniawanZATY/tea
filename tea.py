# tea.py

import pyinputplus as pyip

def main():
    user_input = pyip.inputStr(prompt='Enter something: ')
    print(f'You entered: {user_input}')

if __name__ == "__main__":
    main()
