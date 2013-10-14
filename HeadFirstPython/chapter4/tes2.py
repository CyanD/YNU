import pickle
man=['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you didn't!", "Oh no you didn't!", "Oh look, this isn't an argument!", "No it isn't!", "It's just contradiction!", 'It IS!', 'You just contradicted me!', 'You DID!', 'You did just then!', '(exasperated) Oh, this is futile!!', 'Yes it is!']
try:
        with open("man1.txt","wb") as man1:
                pickle.dump(man,man1)
except pickle.PickleError as picErr:
        print("Error:"+str(picErr))

try:
        with open("man1.txt",'rb') as man1:
                man2=pickle.load(man1)
except IOError as err:
        print("IOError:"+str(err))
except pickle.PickleError as picE:
        print("PE:"+picE)
print(man2)        
print(isinstance(man2,list))
print(isinstance(man1,list))
