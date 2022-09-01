input_string=input()
input_list=input_string.split()
l=len(input_list)
list_num=[]
sortedlist_1=[]
mode_list=[]
for i in input_list:
    list_num=list_num+[int(i)]

for i in range(l):
    l1=len(sortedlist_1)
    if i==0:
        sortedlist_1 += [list_num[i]]
    elif i>0:
        new_num=True
        for j in range(l1):
            if list_num[i] == sortedlist_1[j]:
                new_num=False
                break
        if new_num==True:
            sortedlist_1 += [list_num[i]]
l1=len(sortedlist_1)

for i in sortedlist_1:
    mode=0
    for j in list_num:
        if i==j:
            mode+=1
    mode_list+=[mode]

maxmode=0
index=-1
for i in mode_list:
    if i>maxmode:
        maxmode=i
maxmode_list=[]
for i in range(len(mode_list)):
    index=index+1
    if mode_list[i]==maxmode:
        maxmode_list+=[sortedlist_1[index]]
ans=""
for i in maxmode_list:
    ans=ans+str(i)+" ,"
print("Mode is "+ans[:-1])

            
        
    
    
