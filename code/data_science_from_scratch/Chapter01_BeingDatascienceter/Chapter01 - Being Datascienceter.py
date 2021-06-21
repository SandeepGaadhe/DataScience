import sys

# ----------------------------------------------------------------------------------------------------
# Section : Documentation
# ----------------------------------------------------------------------------------------------------

"""
Created on Wed Nov 27 12:39:23 2019

@author: Sandeep G

@description :  the script is to contain all the code that is present in the book.
                Before running this script, understand below first

                0. args_kwargs.py
                1. FunctionsAsObject.py
                2. Decorators.py
                x. DataScienceFromScratch.py

"""

print ("\n***** Script Execution Start *****\n")

# ----------------------------------------------------------------------------------------------------
# Section : Utility
# ----------------------------------------------------------------------------------------------------

def mLog4p(pFunc):
    def mClosure(*args, **kwargs):

        # first print the function that is called and what parameter is passed
        print(f'\nLogMessage : Called {pFunc.__name__}() with varargs as {args} and kwargs as {kwargs}')

        # let's execute the real function and store the result
        yourFuncRetValue = pFunc(*args, **kwargs)

        #let's print the returned value
        print(f'LogMessage : Function {pFunc.__name__}() returned {yourFuncRetValue}\n')
        return yourFuncRetValue
    return mClosure

# ----------------------------------------------------------------------------------------------------
# Section : Start of Book Exercise
# ----------------------------------------------------------------------------------------------------

users	=	[
                {	"id":	0,	"name":	"Person0"	},
                {	"id":	1,	"name":	"Person1"	},
                {	"id":	2,	"name":	"Person2"	},
                {	"id":	3,	"name":	"Person3"	},
                {	"id":	4,	"name":	"Person4"	},
                {	"id":	5,	"name":	"Person5"	},
                {	"id":	6,	"name":	"Person6"	},
                {	"id":	7,	"name":	"Person7"	},
                {	"id":	8,	"name":	"Person8"	},
                {	"id":	9,	"name":	"Person9"	}
            ]

#print(users[0].get('name'))

friendships	=	[  (0,1),	(0,	2),	(1,	2),	(1,	3),	(2,	3),	(3,	4),
                   (4,5),	(5,	6),	(5,	7),	(6,	8),	(7,	8),	(8,	9)]


#add a list to users (list of dictionary) containing info of who is friend of whom


#print (users)

# ----------------------------------------------------------------------------------------------------
# Section : Exercise 01 : Adding direct friends to the list of users
# ----------------------------------------------------------------------------------------------------

for	user in	users:
    user["friends"]	= []

for	i,	j	in	friendships:				#	this	works	because	users[i]	is	the	user	whose	id	is	i
    users[i]["friends"].append(users[j].get('name'))	#	add	i	as	a	friend	of	j
    users[j]["friends"].append(users[i].get('name'))	#	add	j	as	a	friend	of	i


# ----------------------------------------------------------------------------------------------------
# Section : Exercise 02 : Find total Connections, average connections, number of friends per user
# ----------------------------------------------------------------------------------------------------

# Create a function to print total number of connections


# below is a self defined function
def totalConnSelf(pUserList):
    totalConn = 0
    for user in pUserList:
        #clsprint(user)
        #print(len(user['friends']))
        totalConn = totalConn + len(user['friends'])
        #print("\n")
    return totalConn

#below is book defined fuction

def totalConnBook(pUserList):

    return sum(len(user["friends"]) for	user	in	users)

def numberOfFriends(dUser):
    return (len(dUser["friends"]))

#print(totalConnSelf(users))
#print(totalConnBook(users))
#print("Avg User Conn : " + str(totalConnBook(users)/len(users)))
#print(users)

#for user in users:
#    print(user)
#    print(numberOfFriends(user))

# create a list (user_id, number_of_friends)
LT_numberOfFriendById = [(user["id"], numberOfFriends(user)) for user in users]

#print(LT_numberOfFriendById)
#print(LT_numberOfFriendById)
#print(sorted(LT_numberOfFriendById))
#print(sorted(LT_numberOfFriendById,key=lambda (user_id,num_of_friends): num_friends,revers=True))

# ------------------------------------------------------------------------------------------------------------
# Section : Exercise 03 : Storing friend of friends - note that the User dict structure is different than book
# ------------------------------------------------------------------------------------------------------------

# ----------------------------------------
# Section : Exercise 3.1 : Functions Def
# ----------------------------------------

@mLog4p
def getDirectFriend(userName):
    print(userName)
    print(users)


def friends_of_friend_ids_book(user):
# "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"] # for each of user's friends
            for foaf in friend["friends"]] # get each of _their_ friends



def friends_of_friend_ids_bad(user):

    if user['id'] == 0:
        print(f"\nInside friends_of_friend_ids_bad {user}")
        print(f"directFriends : {user['friends']}")
        for directFriend in user['friends']:
            getDirectFriend(directFriend)

# ----------------------------------------
# Section : Exercise 3.2 : Code Execution
# ----------------------------------------

# create an empty list to store foaf (friend of a friend)
for	user in	users:
    # user["foaf"]	= [] # get rid of foaf - not needed as foafCount covers it
    user["foafCount"]	= {}
#    print(user)

#print(f"users : {users}")

for dUser in users: # read the first user directory
    # print(f"\nParent loop execution for dUser: {dUser}")
    for sfriend in dUser['friends']: # read the direct friends one by one
        # print(f"\nChild loop execution for sfriend : {sfriend}")
        for dUserFriend in users: # re-read the master list of directory for parsing
            # print(f"\nGrandChild loop execution for dUserFriend : {dUserFriend}")
            if dUserFriend.get('name') == sfriend: # compare
                for directFriend in dUserFriend.get('friends'): # read the direct friend of matching friend
                        # print(f"\nGreatGrandChild loop execution for directFriend : {directFriend}")
                        if (directFriend != dUser.get('name')) and (directFriend not in dUser['friends']): # append only if not self or already present as direct friend # and (directFriend not in users[dUser['id']]["foaf"])

                            # get rid of foaf - not needed as foafCount covers it
                            # users[dUser['id']]["foaf"].append(directFriend)
                            # print(f"users[dUser['id']]['foafCount'] {users[dUser['id']]['foafCount']}. directFriend : {directFriend}")

                            # populate foafCount
                            if (dUser["foafCount"].get(directFriend)) is None:
                                myTempDict = {directFriend : 1}
                            else:
                                myTempDict = {directFriend : int(dUser["foafCount"].get(directFriend)) + 1}
                            dUser["foafCount"].update(myTempDict)



    # print(f"After Parent loop execution for : {dUser}\n")

#print('\n')
#for	user in	users:
#    print(user)

# ----------------------------------------------------------------------
# Section : Exercise 3.3 : Connect users by interests : Not implemented
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Section : Exercise 3.4 : Salaries and Experiences : Not implemented
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Section : Exercise 3.5 : Paid Accounts : Not implemented
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Section : Exercise 3.6 : Topics of interest : Not implemented
# ----------------------------------------------------------------------


print ("\n***** Script Execution End *****")








































