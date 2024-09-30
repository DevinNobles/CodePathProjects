"""""
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
"""

#Keys in Common

def common_keys(dict1, dict2):
    common_list = []
    for key1 in dict1:
        for key2 in dict2:
            if key1 == key2:
                 
        







