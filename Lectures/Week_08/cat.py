tail = True
legs = 4
name = 'Milo'

def walk():
    print('I am walking ' + getName() + '.')

def pet():
    if tail:
        print('When I pet ' + name + ', he purs.')
    else:
        print('When I pet ' + name + ', he hisses.')

def pedicure(legs=4):
    for leg in range(legs):
        print('I am clipping ' + getName() + "'s toenails on leg number " + str(leg+1) + '.')

def getName():
    return name

def getLegs():
    return legs
