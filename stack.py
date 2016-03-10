# use list to build stack
stack= []

def push():
    stack.append(raw_input('please enter new string:').strip())

def popit():
    if len(stack)==0:
        print 'can not pop from an empty stack!'
    else:
        print 'remove[',`stack.pop()`,']successfully'

def viewstack():
    print 'the whole stack is:',stack

cmds={'u':push,'o':popit,'v':viewstack}

pr = '''
p[u]sh
p[o]p
[v]iew
[q]uit
enter your choice:'''
while True:
    while True:
        choice = raw_input(pr).strip()[0].lower()
        if choice not in 'uvoq':
            print '\nwrong input,please try again!\n'
        else:
            print '\nyour choice is %s\n'  %choice
            break
    if choice =='q':
        break
    else:
        cmds[choice]()


                                           
