class Commandice:
    cname = '이젠'
    icetype = '1'  # 엄마는외계인

    def __init__(self, companyname, icetype):
        self.companyname = companyname
        self.icetype = icetype
        print('init')

    # def icemake(self, *args):
    #     print(*args)

    def parentmethod(self):
        print('parentmethod')
