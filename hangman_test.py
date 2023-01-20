# author: Larissa Munishkina
# date: Mar 27, 2022
# file: test_hangman.py tests a hangman.py
# input: file 'dictionary_short.txt'
# output: possible assertion errors

import hangman
import sys
import io

dictionary_file = 'dictionary_short.txt'

if __name__ == '__main__':
    # test import_dictionary(filename)
    dict_standard = {2: ['ad'],
                     3: ['bat'],
                     4: ['card'],
                     5: ['dress'],
                     6: ['engine'],
                     7: ['T-shirt'],
                     8: ['gasoline'],
                     9: ['gathering'],
                     10: ['evaluation'],
                     11: ['self-esteem'],
                     12: ['unemployment']}
    dictionary = hangman.import_dictionary(dictionary_file)
    assert dictionary == dict_standard


    # test get_game_options()
    output_standard = 'The word size is set to 4.\nYou have 4 lives.\n'
    hangman.input = lambda x: '4'  # redirect input
    stdout = sys.stdout
    sys.stdout = io.StringIO()  # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue()
    sys.stdout = stdout  # restore stdout
    assert size == 4
    assert lives == 4
    assert output == output_standard

    #test output of the main loop
    with open("ex1.out", "r") as b:
        big_old_output = b.readlines()
        chunky_string = ""
        for i in big_old_output:
            chunky_string += i
    list_of_inputs = iter([3,2,"a","c","b", "t"])
    hangman.input = lambda x : next(x)(list_of_inputs)
    #(lambda x: i for i in x)(list_of_inputs)
    #badckup of standard output for later
    stdout = sys.stdout
    #redirect standard output to a string
    sys.stdout = io.StringIO()
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    print(output)
    assert output == chunky_string

    #if we have multiple, both inputs will be substituted with the value of lambda in the example for game options.








    print('Everything looks good! No assertion errors!')