import datetime

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
    

def getMonthName(month):

    li=['January','February','March','April','May','June',

        'July','August','Setember','October','November','December']

    monthName=li[month-1]

    return monthName

def title(year,month):

    print()

    print('    ',getMonthName(month),' ',year)

    print('-'*26)

    print('일  월  화  수  목  금  토')

def getStartDay(year,month):

    d=datetime.date(year,month,1)

    return d.weekday()#월요일 0

def getLastDay(year,month):

    if month==12:

       year=year+1

       month=1

    else:

       month=month+1

    d=datetime.date(year,month,1)  

    t=datetime.timedelta(days=1)

    k=d-t

    return k.day


def body(year,month):

    startday=getStartDay(year,month)

    lastday=getLastDay(year,month)

    if startday==6:

        s=1

    else:

        s=startday+2

    c=0

    m=0

    for k in range(6):

        for i in range(7):

            c=c+1

            if c<s:

                print('{:>2}'.format(' '),end='  ')

            else:

                if lastday>m:

                    m=m+1

                    print('{:>2}'.format(m),'('+choice_shift_arr[m]+')',end='  ')
                    #print(choice_shift_arr[m])
                

        print()

    

def Dal(year,month):

    title(year,month)

    body(year,month)

def main():

    year=eval(input('연도를 입력하세요(ex. YYYY):'))
    
    month=eval(input('월을 입력하세요(1~12):'))

    Dal(year,month)
    # print_shift_list 에서 처리?

while True:
    print_help()

    choice = input("실행하고자 하는 번호를 입력해주세요 >> ")

    if choice == '0':
        print('프로그램을 종료합니다')
        break

    elif choice == '1':

        print_shift()

        choice_shift_num = input("본인의 근무패턴에 알맞은 번호를 입력해주세요 >> ")

        if choice_shift_num == '1':
            choice_shift_arr = ["주","야","비","휴"]

        elif choice_shift_num == '2':
            choice_shift_arr = ["주","주","야","야","비","휴"]

        elif choice_shift_num == '3':
            choice_shift = input("본인의 근무패턴을 입력해주세요 >> ")
            choice_shift_arr = list(choice_shift.strip())
            print(choice_shift_arr)
            for i in range(len(choice_shift_arr)) :
                print('('+choice_shift_arr[i]+')', end='  ')

        else :
            print ('잘못 입력했습니다.')

    elif choice == '2':
        main()

    else :
        print ('잘못 입력했습니다.') 


