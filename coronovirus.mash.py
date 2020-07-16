import requests
from yandex_geocoder import Client


URL = 'https://coronavirus.mash.ru/data2.json'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
           'accept' : '*/*'}
API_KEY = 'dd9332fa-fe6a-4c4b-a373-081677c9f41c'


def input_coordinates(vvod_coord):
    # Преобразование адреса в координаты через API YANDEX
    client = Client(API_KEY)
    coord = []
    coordinates = client.coordinates(f'Москва {vvod_coord}')
    coord.append(str(coordinates[1]))
    coord.append(str(coordinates[0]))
    return coord


def purse_mash():
    # Получение с сайта https://coronavirus.mash.ru/ json файла и его парсинг
    r = requests.get(URL, headers=HEADERS )
    test = r.json()
    coordinates_json = []
    for coordinat in range(len(test['features'])):
        coordinates_json.append(test['features'][coordinat]['geometry']['coordinates'])

    return coordinates_json

def main():
    print('\n Эта программа для проверки зараженных по Москве\n Для этого введите улицу и номер дома\n')
    vvod_coord = input(" Введите улицу и номер дома: ").title()

    coord = input_coordinates(vvod_coord)
    coordinates_json = purse_mash()

    if coord in coordinates_json:
        print(f' По адресу: г.Москва,ул.{vvod_coord} - есть зараженные')
    else:
        print(f' По адресу: г.Москва,ул.{vvod_coord} - нет зараженных')

if __name__ == '__main__':
    main()