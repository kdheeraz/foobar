def getZeroes(string):
    last_idx=0
    last_idx_ones=0
    temp_cnt=0
    temp_cnt_ones=0
    max_cnt=0
    max_cnt_ones=0
    for i in range(len(string)):
        if(max_cnt<temp_cnt):
            max_cnt=temp_cnt
        if(string[i]=="0"):
            if i-1==last_idx:
                temp_cnt+=1
            else:
                temp_cnt=1
            last_idx=i   
        else:
            temp_cnt=0    
    print(max_cnt)       

getZeroes("110000001001100000111")     



