from class2 import icefactory


class oneicesell(icefactory):
    def __init__(self,companyname,icetype):

        self.companyname=companyname
        self.icetype=icetype
        print('init')

    def parentmethod(self):
        print('oneicesell method')


oneice = oneicesell('배스킨라빈스','엄마는외계인')
oneice.parentmethod()
