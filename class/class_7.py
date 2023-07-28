while True:
    a = input('방을 입력:')
    b = int(input('현재 인원을 입력:'))
    c = int(input('추가 인원을 입력:'))
    d = int(input('빠진 인원을 입력:'))


    class Room:
        def final(self, Room, b, c, d):
            print(f'{Room}호의 현재 인원은 {b}명, 최종 인원은 {b + c - d}명입니다.')


    r = Room()
    r.final(a, b, c, d)
# r14 = r1304('room1304', b, c, d)
# r15 = r1304('room1304', b, c, d)
#
# room = [r14, r15]
