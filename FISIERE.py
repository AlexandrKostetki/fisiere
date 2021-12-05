vocale='abeou'
x=0
with open('C:\Users\Admin\Desktop\litere.txt','r') as f:
    v=f.read()
with open('litere2.txt','w') as f:
    for i in v:
        f.write(i)
        x+=1
print('vocale=',x)