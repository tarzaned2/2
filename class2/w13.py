#
#
# interface , abstract class 부모 자식들 ______________
# b5층부터 15층까지 설정 방 랜덤 학생수 랜덤 한층에 6개
#
# 리스트 출력 b5~ 15층
# 검색 13층 1304 현재인원 검색 -> 현재인원은 몇명입니다
#
# ==============================================
# 1.리스트
# 2.검색
# 3.방 지우기
# 4.수정
# 5.나가기
# ==============================================


class Ezen13:

    # 1반부터 6반까지
    # 1301 HTML 1302 jquery 1303 css 1304 python 1305 java 1306 ai
    #
    # rnumber  (s)방번호 rtotal (int)인원수 check ncs,unncs(str) sunject

    def print(self):
        print('=' * 50)

    def __init__(self, rnumber, rtotal, checkncs, subject):
        self.rnumber = rnumber
        self.rtotal = rtotal
        self.checkncs = checkncs
        self.subject = subject

    def ezen13print(self):
        print(self.rnumber)
        print(self.rtotal)
        print(self.checkncs)
        print(self.subject)


ezen13 = Ezen13('1301', 5, 'ncs', 'html')
ezen14 = Ezen13('1302', 3, 'ncs', 'jquery')
ezen15 = Ezen13('1303', 7, '비ncs', 'css')
ezen16 = Ezen13('1304', 8, 'ncs', 'python')
ezen17 = Ezen13('1305', 3, '비ncs', 'java')
ezen18 = Ezen13('1306', 2, 'ncs', 'ai')

ezen13.ezen13print()
ezen13.print()
ezen14.ezen13print()
ezen14.print()
ezen15.ezen13print()
ezen15.print()
ezen16.ezen13print()
ezen16.print()
ezen17.ezen13print()
ezen17.print()
ezen18.ezen13print()
ezen18.print()

# class ezen14
#업무 각 방 인원수 체크 해서 인원이 빠지는 경우 임의의수 해당한느인원 현재인원체크를 해서 출력하시오
#roomezen14 총 5명; 2명 퇴실 현재인원 3명
#01,02,03반

class Ezen14:
    def __init__(self,rnumber,total,gone,now):
        self.rnumber=rnumber
        self.total=total
        self.gone=gone
        self.now=now

    def ezen14print(self):
        print(f'방:{self.rnumber}')
        print(f'총인원:{self.total}')
        print(f'빠진인원:{self.gone}')
        print(f'현재인원:{self.now}')

eze14=Ezen14('1401',5,2,3)
eze15=Ezen14('1402',8,4,4)
eze16=Ezen14('1403',7,4,3)

print('='*50)
eze14.ezen14print()
print('='*50)
eze15.ezen14print()
print('='*50)
eze16.ezen14print()
print('='*50)

print()




