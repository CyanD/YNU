"""this is a function，to display all the item in a list
the_list: the list you want to display
indent: decide whether to intent
level: intent size
"""
def print_lol(the_list,indent=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            print('|',end='')
            if indent:
                print("\t"*level,end='')
            print(each_item)
