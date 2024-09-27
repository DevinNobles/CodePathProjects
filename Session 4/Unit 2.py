
def cast_vote(votes, candidate):
    #check if key exist in dict
    if candidate in votes:
        votes[candidate] += 1
    else: 
        votes[candidate] = 1


    
    
    
    #if votes.get(candidate) != None:
        #votes[candidate] = 1
    
    





votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)





