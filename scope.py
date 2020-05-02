# global scope
x = 'global x'

def function():#fonksiyonlar yeni bir tanımlama alanı tanımlar
    # local scope
    x = 'local x' # local x olmasaydı global x değerini basardı
    #print(x)

function()
#print(x)

###################################
name = 'aykut' # global name

def change_name(new_name):
    name = new_name # ocal name
    #print(name)

#change_name('ömer')
#print(name)

#####################################

name = 'global string'

def greeting():
    name = 'sibel'

    def hello():
        name = 'Ömer' #local name. global name i ezer
        print('hello '+name) # burası için global name sibel

    #hello()   

#greeting()

##########################################

x = 50

def test(x):
    print (f'x : {x}') # şu ana kadar locak x yok globalı baz alır

    x = 100
    print(f'changed x to {x}') # local x var local x i alır

#test(x)

# global x üzerinde işlem yapabilmek için 'global' keyword kullan

x = 100

def degis():
    global x
    x=15
    print(f'local x : {x}')

degis()
print(f'global x : {x}')