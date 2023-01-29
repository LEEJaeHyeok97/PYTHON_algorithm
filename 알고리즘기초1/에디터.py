# import sys

# word = list(sys.stdin.readline().strip())
# n = int(sys.stdin.readline())

# cursor = len(word) + 1

# for i in range(n):
#     command = input()
#     if command == 'L':
#         if cursor == 0:
#             continue
#         else:
#             cursor-=1
#     elif command == 'D':
#         if cursor == len(word) + 1:
#             continue
#         else:
#             cursor+=1
#     elif command == 'B':
#         if cursor == 0:
#             continue
#         else:
#             del word[cursor-1]
#     else:
#         command = command.split()[1]
#         word.insert(cursor, command)

# for i in word:
#     print(i, end='')
