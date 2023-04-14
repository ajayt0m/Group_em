

import random

# read list of students from user input
students = input("Enter the names of students separated by commas: ").split(',')

# get number of members per group required from user
members_per_group = int(input("Enter the number of members per group required: "))

# shuffle the list of students randomly
random.shuffle(students)

# split the shuffled list into groups with the specified number of members per group
groups = [students[i:i+members_per_group] for i in range(0, len(students), members_per_group)]

# print the groups
print("The groups are:")
for i, group in enumerate(groups):
    print(f"Group {i+1}: {', '.join(group)}")
    


