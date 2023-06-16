import file_manager as fm
import parking_spot_manager as psm

def start_process(path):
    #file_manager를 사용해 파일을 읽어옴
    str_list = fm.read_file(path) 
    #문자열 리스트를 주자장 객체 리스트로 변환
    spots = psm.str_list_to_class_list(str_list) 

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            #주차장 객체 리스트를 출력합니다
            psm.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                #입력 받은 이름으로 필터링
                spots = psm.filter_by_name(spots, keyword)
            elif select == 2:
                keyword = input('type city:')
                #입력 받은 도시로 필터링
                spots = psm.filter_by_city(spots, keyword)
            elif select == 3:
                keyword = input('type district:')
                #입력 받은 구역으로 필터링
                spots = psm.filter_by_district(spots, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                #입력 받은 타입으로 필터링
                spots = psm.filter_by_ptype(spots, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                keyword = (min_lat, max_lat, min_lon, max_lon)
                #입력된 제한된 뒤도와 경도의 범위로 필터링
                spots = psm.filter_by_location(spots, keyword)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                #주어진 키워드로 주차장 객체 리스트 정렬
                spots = psm.sort_by_keyword(spots, keyword)
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")