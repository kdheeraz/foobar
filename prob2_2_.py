# def solution(pegs):
#     p=0
#     if(len(pegs)==2):
#         p =(2*pegs[1]+pegs[0])/3
#         if((2*pegs[1]+pegs[0])%3==0):
#             return [(2*pegs[1]+pegs[0])%3,1]
#         else:
#             return [(2*pegs[1]+pegs[0]),3]
#         return p
#     st=pegs[0]
#     end=pegs[-1]

#     new_pegs = pegs[1:][:-1]

#     sub_sum=0
#     odd=False

#     for i in range(len(new_pegs)):
#         if(i%2==0):
#             sub_sum+=2*new_pegs[i]
#             odd=True
#         else:
#             sub_sum-=2*new_pegs[i]
#             odd=False
#     if(not odd):
#         p = 2*(end-sub_sum)+st
#     else:
#         p = 2*(sub_sum-end)-st
#     r1= p-st
#     if(r1>0):
#         return [r1,1]
#     else:
#         return [-1,-1]



from fractions import Fraction  
def solution(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]

    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])

    if (arrLength > 2):
        for index in range(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()
    if FirstGearRadius < 2:
        return [-1,-1]

    currentRadius = FirstGearRadius
    for index in range(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]


print(solution([4,30,50]))

