# num = 25
#
# for i in range(2,num):
#     if num % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

min_range = 100
max_range = 200

for num in range(min_range, max_range):
    for i in range(2,num):
        if num % i == 0:
            # print("Not Prime number",num)
            break
    else:
        print("Prime number",num)