import requests


# code source: https://habr.com/ru/post/666062/

def getAreas():
    response = requests.get('https://api.hh.ru/areas').json()
    areas = []
    for k in response:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name']])
    return areas


areas = getAreas()

print(list(filter(lambda x: x[3] == 'Москва', areas)))
