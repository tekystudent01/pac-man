def danh_Sach():
    a = open('text','r+')
    b = a.readlines()
    for elememt in b:
        print(elememt)
    a.close()
#danh_Sach()
def themHS():
    c = open('text','r+')
    print('bạn muốn thêm học sinh nào')
    ten =  str(input('nhập tên: '))
    tuoi = int(input('nhập tuổi: '))
    lop = input('nhập lớp: ')
    que_quan = str(input('nhập quê quán: '))
    data = '{},{},{},{} \n'.format(ten,tuoi,lop,que_quan)
    c.close()
themHS()