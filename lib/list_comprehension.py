#!/usr/bin/env python3

def return_evens(num_list):
    
    even_numbers = [num for num in num_list if num % 2 == 0]
    if not even_numbers:
        return []
    else:
        return(even_numbers)
pass

print(return_evens([ 0,1, 3, 5, 7,8, 9]))

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    else:
        exclamations=[sentence +"!" for sentence in sentence_list]
        return exclamations
    pass
