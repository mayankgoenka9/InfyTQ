#To find a number such that it is concatenation of :
# 1 - sum of numbers before 5 and after 8
# 2 - string of numbers between 5 and 8 both included 

l = list(map(int, input().split()))
index_five = l.index(5)
index_eight = l.index(8)
sum_list = l[:index_five] + l[index_eight+1:]
total_sum_list = sum(sum_list)
string = ""
for i in range(index_five,index_eight+1):
    string+=str(l[i])
final = total_sum_list + int(string)
print(final)