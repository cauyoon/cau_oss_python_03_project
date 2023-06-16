class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def __init__(self, name, city, district, ptype, longitude, latitude):
        #주차장 객체를 초기화하는 생성자
        #주어진 속성들을 이용해 __item 딕셔너리 생성
        self.__item = {'name': name, 'city': city, 'district': district, 'ptype': ptype, 'longitude': longitude, 'latitude': latitude}

    def get(self, keyword='name'):
        #주어진 키워드에 해당하는 속성값을 반환하는 메소드
        #기본값으로 'name' 속성값을 반환합니다
        return self.__item.get(keyword)
    
def str_list_to_class_list(str_list):
    #문자열로 구성된 리스트를 주차장 객체의 리스트로 변환
    list_park = []
    for num in str_list:
        mylist = num.split(",")
        data = parking_spot(mylist[1], mylist[2], mylist[3], mylist[4], mylist[5], mylist[6])
        list_park.append(data)
    return list_park
    
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for target in spots:
        print(target)

def filter_by_name(spots, name):
    # 주어진 이름에 해당하는 주차장 객체를 필터링하여 반환하는 함수
    return [target for target in spots if name in target.get('name')]

def filter_by_city(spots, city):
    # 주어진 도시에 해당하는 주차장 객체를 필터링하여 반환하는 함수
    return [target for target in spots if city in target.get('city')]

def filter_by_district(spots, district):
    # 주어진 구역에 해당하는 주차장 객체를 필터링하여 반환하는 함수
    return [target for target in spots if district in target.get('district')]

def filter_by_ptype(spots, ptype):
    # 주어진 주차장 유형에 해당하는 주차장 객체를 필터링하여 반환하는 함수
    return [target for target in spots if ptype in target.get('ptype')]

def filter_by_location(spots, location):
    # 주어진 위치 범위에 해당하는 주차장 객체를 필터링하여 반환하는 함수
    return [target for target in spots if location[0] < target.get('latitude') and location[1] > target.get('latitude') and \
            location[2] < target.get('longitude') and location[3] > target.get('longitude')]


def sort_by_keyword(spots, keyword):
    # 주어진 키워드에 따라 주차장 객체를 정렬하여 반환하는 함수
    return sorted(spots, key=lambda x: x.get(keyword))

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    #spots = filter_by_district(spots, '동작')
    #print_spots(spots)
    
    # version#4
    #spots = sort_by_keyword(spots, 'name')
    #print_spots(spots)