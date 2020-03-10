string=input()

temp_list=[]

string1=string.lower()

for i in string1:

      if i not in temp_list:

          temp_list.append(i)

print(len(temp_list))

