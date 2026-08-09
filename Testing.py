from database import Database

a = {'a' : 1 , 'b' : 2}
b = {'b' : 3 , 'c' : 4}
c = {'c' : 3 , 'd' : 4}


Database.createTrunk(name= 'main1' , password='pass1')

main1 = Database.connectTrunk(name = 'main1' , password='pass1')

main1.createBranch('Branch1.1')

gg = main1.connectBranch('Branch1.1' , 'pass1')

main1.createBranch('Brach1.2' , 'changepass')
gg2 = main1.connectBranch('Brach1.2' , 'changepass')

gg.write(a , 'pass1')

gg.append(b , 'pass1')

print(gg.read('pass1'))

gg.changePassword('pass1' , 'pass2')

print(gg.getValue('b' , 'pass2'))

print(gg.read('pass2'))
gg.deleteKey('c' , 'pass2')
print(gg.read('pass2'))

gg2.deleteItSelf('changepass')