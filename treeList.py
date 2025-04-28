import treeDirectory

count = 0

for item in treeDirectory.all_trees:
    print(item)
    count += 1

if count < 1:
    print(f'{count} is less than than 1.')
elif count % 3 == 0:
    print(f'{count} is divisible by three.')
elif count % 2 == 0:
    print(f'{count} is divisible by two.')
elif (count+1) % 3 == 0:
    print(f'{count}+1 is divisible by three.')
elif (count+1) % 2 == 0:
    print(f'{count}+1 is divisible by two.')
else:
    print(f'{count} is invalid.')

# print(count)
