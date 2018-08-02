# for multiplum in range(1,10):
#     print(multiplum, end="      ") 
#     for number in range(1,10):
#         print(multiplum*number, end="\t") 
#     print()

n = int(input("Enter number: "))
for multiplum in range(1,n+1):
    print(multiplum, end="      ") # First column
    for number in range(1,n+1):
        print(multiplum*number, end="\t") # Next 9 columns
    print()