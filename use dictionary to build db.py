def login():
    while True:
        if len(db)==0:
            print 'no record found ,you can not login.\nplease register first'
            break
        name = raw_input('plesase input your name:')
        if name not in db:
            print 'name not exist,please try again'
            continue
        while True:
            psw = raw_input('please input your password:')
            if db[name]!=psw:
                print'wrong password, plese try again'
            else:
                print 'login success!'
                break
        break


def register():
    while True:
        name = raw_input('please input your name:')
        if name in db:
            print 'already taken,please change your name!'
            continue
        psw = raw_input('please input your password:')
        db[name] = psw
        print'new user register succcessful!'
        break

cmds={'r':register,'lg':login}
db={}
pr ='''register:r
login:lg
quit:q
please make your your choice:'''
while True:
    cmd=raw_input(pr).strip().lower()
    if cmd not in ('r','lg','q'):
        print 'wrong input, please try again'
        continue
    if cmd =='q':
        break
    else:
        print 'your choice is %s'  %cmd
    cmds[cmd]()
    


                        
