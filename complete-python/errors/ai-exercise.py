# Below is the AI 1.0 code, which works but cannot handle invalid input
# if the user input something other than an integer at first, the program will break due to a ValueError,
# caused by calling int() function on an non-integer input result
#
# Your task is to use the try-except-else-finally workflow to improve the existing code
# which can detect an invalid input in the beginning, and prints our an error message: 'Please input integers only.'
# then proceed
# to ask the user 'Do you want to play again? (y/N):' like the original function does

class AI:

    ACTION: {
        'play_again': 'y',
        'quit': 'n'
    }

    MESSAGE: {
        'input': 'Please enter an integer number: ',
        'answer': '{} is {}.',
        'play_again': 'Do you want to play again? ({}/{}): ',
        'value_error': 'Please input integer numbers only.',
        'quit': 'Goodbye.'
    }

    def interact(cls):
        while True:
            try:
                user_input = int(input(cls.MESSAGE.input))
                parity = 'even' if user_input % 2 == 0 else 'odd'
                print(cls.MESSAGE.play_again.format(user_input, parity))
            except ValueError:
                print(cls.MESSAGE.value_error)
            finally:
                user_input = input(cls.MESSAGE.play_again)
                if user_input != cls.ACTION.play_again:
                    print(cls.MESSAGE.qui)
                    break


AI.interact()
