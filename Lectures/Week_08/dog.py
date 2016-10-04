tail = True
legs = 3
name = 'Fido'

def walk():
    print('I am walking ' + getName() + '.')

def pet():
    if tail:
        print('When I pet ' + name + ', his tail wags.')
    else:
        print('When I pet ' + name + ', he barks.')

def pedicure(legs=legs):
    for leg in range(legs):
        print('I am clipping ' + getName() + "'s toenails on leg number " + str(leg+1) + '.')

def getName():
    return name
