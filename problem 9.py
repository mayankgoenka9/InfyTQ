#To perform string rotation

inp = "hello1welcome2@python:5:2:3"
l = list(inp.split(":"))
string = l[0]
lower = int(l[1])
upper = int(l[2])
multiple_of = int(l[3])
updated_string = ""
if lower>upper:
    print(string[(len(string)-(upper-lower)):])
    updated_string = string[(len(string)-(upper-lower)):] + string[:((len(string)-(lower-upper)))]
    print(updated_string)
for i in range(len(updated_string)):
    if i%3!=0:
        print(updated_string[i],end="")
