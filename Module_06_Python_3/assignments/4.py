myTuple = (90, 41, 31, 47, 88, 75, 76, 31, 899)
evens = tuple()
odds = tuple()

# You can't directly append an element to a tuple, but you can create a new tuple by 
# combining the original tuple with the new element. This is done using tuple 
# concatenation

for num in myTuple:
    if num%2==0:
        evens += (num, ) # Comma indicates that the element to be concatenated is a Tuple !
    else:
        odds += (num, )
print(f"Evens = {evens}.\nOdds = {odds}.")
    
