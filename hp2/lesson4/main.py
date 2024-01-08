import number as num
import random as rd
import time
total_point = 0
challenge_point = 0
def toanHoc():
    global challenge_point
    global total_point
    question_1 = str(input('1+3 \nA.4 \nB.5 \nC.6'))
    if(question_1 == 'A'):
        print('đáp án chính xác')
        total_point += challenge_point
    else:
        print('đáp án sai bét')
    question_2 = str(input('2+3 \nA.4 \nB.5 \nC.6'))
    if(question_2 == 'C'):
        print('đáp án chính xác')
        total_point += challenge_point
    else:
        print('đáp án sai bét')
def doVuiCoThuong():
    global challenge_point
    global total_point
    question_1 = str(input("Bạn hãy tưởng tượng bạn đang lênh đênh cùng chiếc thuyền \nở giữa hồ chứa đầy cá ăn thịt người và bổng nhiên thuyền của bạn bị \nlũng một lổ làm sao bạn sống sốt? \nA.bạn hãy ngừng tưởng tượng lại \n B.bạn lấy thân mình che lổ thuyền \ncâu trả lời của bạn là"))
    if(question_1 == 'A'):
        print('đáp án chính xác')
        total_point += challenge_point
    else:
        print('đáp án sai bét')
    question_2 = str(input("Năm Titanic chìm ở Đại Tây Dương vào ngày 15 tháng *, trong chuyến đi đầu tiên từ Southampton? \nA.tháng 3 \nB.tháng 4 \ncâu trả lời của bạn là: "))
    if(question_2 == 'B'):
        print('đáp án chính xác')
        total_point += challenge_point
    else:
        print('đáp án sai bét')
def spinning_hat():
    global challenge_point
    challenge_point = rd.randrange(100,1000,100)
    print('bắt đầu quay nón.....')
    time.sleep(1)
    print('ting.....ting....ting...')
    num.shownumber(challenge_point)
def game_screen(seconds):
    print('*'*20)
    print('  CHIẾC NÓN KÌ DIỆU  ')
    print('*'*20)
    time.sleep(seconds)
def start():
    game_screen(2)
    print('-'*100)
    name = input('tên của bạn là: ')
    print('Xin chào {}, chào mừng bạn đến với trò chơi CHIẾC NÓN KÌ DIỆU'.format(name))
    print('-'*100)
    spinning_hat()
    toanHoc()
    print("Diem so cua ban la: {}".format(total_point))
start()