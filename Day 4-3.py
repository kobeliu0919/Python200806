import os.path

d={}
def menu():
    print('歡迎來到成績查詢系統')
    print('1新增成績')
    print('2列出所有成績')
    print('3成績查詢系統')
    print('4離開系統')
def grade():
    x=open('grade.txt','a')
    x.write(y)
    x.write(z)
    x.write('\n')
    return('成績新增成功')
while  True:
    menu()
    w=int(input('你的選擇是'))
    if w == 1:
        while True:
            y=input('請輸入名子')
            z=input('(按零退出)請輸入成績') 
            if z!='0':
                d[y]=z
                print(grade())
            else:
                break    
    elif w == 2:
            x=open('grade.txt','r')
            print(x.read())
    elif w == 3:
        t=input('請輸入名子')
        for key in d:
            if key == t:
                print(key,'考了',d[key],'分',)
            else:
                print('你的成績尚未填入')
    else:
        break
        
    