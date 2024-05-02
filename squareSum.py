# import math
# count=0
# def square_sum(num):
#     global count
#     if(num==None):
#         return 0
#     if(num<1):
#         return 0
#     sqr = math.sqrt(num)
#     if(sqr==int(sqr)):
#         return 1
#     pos_sqs = [x**2 for x in range(1,int(sqr+1))]

#     print(pos_sqs)

#     count=([square_sum(num-j**2) for j in pos_sqs])

# square_sum(12)
# print(count)

    
import math

count = 0

def square_sum(num):
    global count
    
    if num is None:
        return 0
    if num < 1:
        return 0

    sqr = math.sqrt(num)
    if sqr == int(sqr):
        count += 1
        return 1

    pos_sqs = [x**2 for x in range(1, int(sqr) + 1)]
    
    for j in pos_sqs:
        count += square_sum(num - j**2)

    return count

result = square_sum(12)
print(result)

