"""this is a function，to save all the item in a list to a given path, every item
in a line
the_list: the list you want to display
indent: decide whether to intent
level: intent size
save_Path: where to save the items, if it is null, use sandard out(print())
"""
import sys
def print_lol(the_list,indent=False,level=0,save_Path=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,save_Path)
        else:
            if indent:
                print("\t"*level,end='',file=save_Path)
            print(each_item,file=save_Path)

import os
#data=['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you didn't!", "Oh no you didn't!", "Oh look, this isn't an argument!", "No it isn't!", "It's just contradiction!", 'It IS!', 'You just contradicted me!', 'You DID!', 'You did just then!', '(exasperated) Oh, this is futile!!', 'Yes it is!']


Path="man_File.txt"
try:
        with open('man_Data.txt') as man, open(Path,'w') as man_File:
                print_lol(man,save_Path=man_File)########i dont know why?????????????  Solve
                #solution: do not read data from file, but from memory
except ValueError as err:
        print(str(err))

"""
with open('fe.txt','w') as ff:
        print_lol(data,save_Path=ff)"""
