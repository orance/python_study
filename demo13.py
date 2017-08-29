class MyClass:
    name = 'Jack'
    def sayHi(self):
        print 'Hello\n%s'%self.name

mc = MyClass()
print mc.name
mc.name = 'Lisa'
mc.sayHi()
