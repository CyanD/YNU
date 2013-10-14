"""this is a function，to save all the item in a list to a given path, every item
in a line
the_list: the list you want to display
indent: decide whether to intent
level: intent size
save_Path: where to save the items, if it is null, use sandard out(print())
"""
def print_lol(the_list,indent=False,level=0,save_Path=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,save_Path)
        else:
            if indent:
                print("\t"*level,end='',file=save_Path)
            print(each_item,file=save_Path)
