hit=open(r'C:\Users\User\Desktop\hit.txt','w')
text_file=open(r'C:\Users\User\Desktop\Hint_passwords.txt','r')
data=text_file.readlines()
print(data,type(data))
st="123\n"
dat=[]
for i in data:
    dat.append(i)
    dat.append(st)
for i in dat:
    hit.write(str(i))
text_file.close()
print(dat,type(dat))
print(len(dat))

name=open(r'C:\Users\User\Desktop\name.txt','w')
names=[]

for i in range(220):
    if i%2==0:
        names.append("admin\n")
    else:
        names.append("think\n")
for i in names:
    name.write(i)
name.close()


