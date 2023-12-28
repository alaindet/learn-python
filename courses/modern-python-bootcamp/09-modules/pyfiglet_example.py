from sys import exit

from pyfiglet import figlet_format

def shutdown():
    print('\nBye!')

def read_text(prompt_message: str) -> str:
    txt = input(f'{prompt_message} > ')
    match txt:
        case 'exit':
            exit()
        case '':
            raise ValueError('No text provided, try again')
        case _:
            return txt

def main():
    while True:
        try:
            txt = read_text('What do I have to write?')
            figlet = figlet_format(txt)
            print(figlet)
        except ValueError as err:
            print(err)
            continue
        except (SystemExit, KeyboardInterrupt):
            shutdown()
            return
        
if __name__ == '__main__':
    main()