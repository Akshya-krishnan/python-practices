# List 

score = [12,34,89]
names=["Akshaya", "Kavya", "Bhavana", "Fadiya"]

print(score,names)

# Methods
# 1 Retrieve Values
print(score[2],names[3])

# 2 Assign values

score[0]=13
print(score)

# 3 Length

print(len(score))

# 4 Add new value

score.append(60)
print(score)

# 5 Insert

score.insert(2,89)
print(score)

# 6 Remove

score.remove(13)
print(score)

# 7 Pop(Remove)

score.pop(2)
print(score)

# 8 Reverse

score.reverse()
print(score)

# 9 Sorting

names.sort()
print(names)

score.sort()
print(score)

#10 Sort By Descending

names.sort(reverse=True)
print(names)

score.sort(reverse=True)
print(score)