from class2 import parent


class icefactory(parent):

    def __init__(self, companyname, icetype):
        self.companyname = companyname
        self.icetype = icetype
        print('init')

    # 오버라이딩 : 부모메소드 이름 파일 개수 가 같으면 자식이 부모파일 메소드를 재정의한다.
    # 오버로딩 : 메소드명은 같은데 리턴 타입, 아규먼트 타입, 아규먼트 개수 틀리는 경우가 오버로딩
    def parentmethod(self):
        print('icefactory method')
