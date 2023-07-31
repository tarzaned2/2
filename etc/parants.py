class parants:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def parantprint(self):
        print(self.name)
        print(self.age)
        print(self.address)


p = parants('현동윤', 22, '논현동')
p.parantprint()
