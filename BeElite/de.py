# Marketing_contact_list = [
#     'crazyunicorn42@gmail.com',  'wanderlust_adventurer@hotmail.com', 'techgeek88@yahoo.com', 'musiclover1234@outlook.com', 'fitnessfanatic57@gmail.com', 'bookworm321@protonmail.com'
# ]

# Sales_contact_list = emails = [
#     'fitnessfanatic57@gmail.com', 'bookworm321@protonmail.com', 'codingmaster99@gmail.com', 'travelbug2023@yahoo.com',  'gamerlife123@outlook.com'
# ]

# def jointContactList(list1, list2):
#     # using the python union method which creates unique elements from the 2 list
#     combinedSet = set(list1).union(list2)
#     return list(combinedSet)

# jointList = jointContactList(Marketing_contact_list, Sales_contact_list)
# print(jointList)


# '''
# DOCUMENTATION USED
# https://docs.python.org/3/library/stdtypes.html#set
# '''


# Enter your code here. Read input from STDIN. Print output to STDOUT
S = str(input())
N = len(S)
oddArr = []
evenArr = []
for i in range(0, N):
    if i % 2 > 0:
        oddArr.append(S[i])
    elif i == 0 or i % 2 == 0:
        evenArr.append(S[i])
        
print(str(''.join(evenArr)) + " " + str(''.join(oddArr)))