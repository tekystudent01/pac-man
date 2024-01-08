diem = 0
luaChon = str
def start():
    global luaChon
    print('chào mừng bạn đến với trò chơi đố vui có thưởng')
    print('trò  chơi có các bộ câu hỏi như sau')
    print('1.Câu hỏi toán học')
    print('2.Câu hỏi bất ngờ')
    print('3.Xem điểm')
    print('4. Thoát trương trình')
    while True:
        luaChon = int(input('lựa chọn của bạn là: '))
        if(luaChon == 1):
            toanHoc()
        elif(luaChon == 2):
            doVuiCoThuong()
        elif(luaChon == 3):
            print('số điểm bạn có được là: ',diem)
        elif(luaChon == 4):
            break
def toanHoc():
    global diem
    question_1 = str(input('1+3 \nA.4 \nB.5 \nC.6'))
    if(question_1 == 'A'):
        print('đáp án chính xác')
        diem += 1
    else:
        print('đáp án sai bét')
    question_2 = str(input('2+3 \nA.4 \nB.5 \nC.6'))
    if(question_2 == 'C'):
        print('đáp án chính xác')
        diem += 1
    else:
        print('đáp án sai bét')
def doVuiCoThuong():
    global diem
    question_1 = str(input("Bạn hãy tưởng tượng bạn đang lênh đênh cùng chiếc thuyền \nở giữa hồ chứa đầy cá ăn thịt người và bổng nhiên thuyền của bạn bị \nlũng một lổ làm sao bạn sống sốt? \nA.bạn hãy ngừng tưởng tượng lại \n B.bạn lấy thân mình che lổ thuyền \ncâu trả lời của bạn là"))
    if(question_1 == 'A'):
        print('đáp án chính xác')
        diem += 1
    else:
        print('đáp án sai bét')
    question_2 = str(input("Năm Titanic chìm ở Đại Tây Dương vào ngày 15 tháng *, trong chuyến đi đầu tiên từ Southampton? \nA.tháng 3 \nB.tháng 4 \ncâu trả lời của bạn là: "))
    if(question_2 == 'B'):
        print('đáp án chính xác')
        diem += 1
    else:
        print('đáp án sai bét')
start()