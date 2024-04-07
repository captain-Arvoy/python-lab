# 1.wap to print a matrix containing group of similar elements by giving the input randomly in another matrix.

from collections import Counter
text_list=[1,3,5,1,3,2,5,4,2,1]
print("the original list:"+str(text_list))
temp=Counter(text_list)
res=[[key]*val for key,val in temp.items()]
print("matrix after grouping:"+str(res))
