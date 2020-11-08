def print_help():
    print (
        '',
        '-----------------',
        '교대근무 근무표',
        '0: 종료',
        '1: 근무패턴입력',
        '2: 근무스케줄표',
        '-----------------',
        '',
        sep='\n'
    )

def print_shift():
    print (
        '',
        '-----------------',
        '근무패턴',
        '1: 주야비휴',
        '2: 주주야야비휴',
        '3: 근무패턴입력',
        '-----------------',
        '',
        sep='\n'
    )

def print_shift_list():

    print ('추가예정') 

while True:
    print_help()

    choice = input("실행하고자 하는 번호를 입력해주세요 >> ")

    if choice == '0':
        print('프로그램을 종료합니다')
        break
    elif choice == '1':
        print_shift()
        choice_shift_num = input("본인의 근무패턴에 알맞은 번호를 입력해주세요 >> ")
        if choice_shift_num == '3':
            choice_shift = input("본인의 근무패턴을 입력해주세요 >> ")
        else :
            print ('잘못 입력했습니다.')
    elif choice == '2':
        print_shift_list()
        break
    else :
        print ('잘못 입력했습니다.') 

    

