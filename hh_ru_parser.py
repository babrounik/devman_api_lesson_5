import requests

MOSCOW = 1


def getAreas():
    """
    Example:
        areas = getAreas()
        print(list(filter(lambda x: x[3] == 'Москва', areas)))
    # code source: https://habr.com/ru/post/666062/
    """
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


def predict_rub_salary(vacancy):
    salary = vacancy["salary"]
    if not salary:
        return
    currency = salary["currency"]
    if currency != 'RUR':
        return
    from_salary = salary["from"]
    to_salary = salary["to"]
    if from_salary and to_salary:
        return (from_salary + to_salary) / 2
    elif from_salary:
        return from_salary * 1.2
    elif to_salary:
        return to_salary * 0.8


def transform_dict_to_tuple(lang_stats):
    stats_tuples = [("Язык программирования", "Найдено вакансий", "Обработано вакансий", "Средняя зарплата"), ]
    for lang, stats in lang_stats.items():
        stats_tuples.append((lang, stats['vacancies_found'], stats['vacancies_processed'], stats['average_salary']))
    return stats_tuples


def get_mosсow_languages_stats(programming_languages):
    url = "https://api.hh.ru/vacancies"
    lang_stats = {}

    for language in programming_languages:
        payload = {"area": MOSCOW, "text": f"программист {language}", "search_field": "name"}
        raw_response = requests.get(url, params=payload)
        raw_response.raise_for_status()
        response = raw_response.json()

        salaries = []
        for vacancy in response["items"]:
            rub_salary = predict_rub_salary(vacancy)
            if rub_salary:
                salaries.append(rub_salary)
        lang_stats[language] = {
            "vacancies_found": response['found'],
            "vacancies_processed": len(salaries),
            "average_salary": int(sum(salaries) / len(salaries))
        }
    return lang_stats
