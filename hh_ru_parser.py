import requests

MOSCOW = 1
VACANCIES_PARSING_LIMIT = 2000
PER_PAGE = 100


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


def get_hh_vacancies(_language, _page, _per_page):
    _url = "https://api.hh.ru/vacancies"
    payload = {"area": MOSCOW,
               "text": f"программист {_language}",
               "search_field": "name",
               "page": _page,
               "per_page": _per_page}

    raw_response = requests.get(_url, params=payload)
    raw_response.raise_for_status()

    return raw_response.json()


def prepare_data_for_visualisation(lang_stats):
    columns_names = [("Язык программирования", "Найдено вакансий", "Обработано вакансий", "Средняя зарплата"), ]
    for lang, stats in lang_stats.items():
        columns_names.append((lang, stats['vacancies_found'], stats['vacancies_processed'], stats['average_salary']))
    return columns_names


def get_mosсow_languages_stats(programming_languages):
    lang_stats = {}

    for language in programming_languages:
        page = 0
        pages_limit = VACANCIES_PARSING_LIMIT // PER_PAGE

        response = get_hh_vacancies(language, page, PER_PAGE)

        all_vacancies = response['found']
        pages_without_limit = all_vacancies // PER_PAGE + 1
        max_page = pages_without_limit if pages_without_limit <= pages_limit else pages_limit

        salaries = []
        for vacancy in response["items"]:
            rub_salary = predict_rub_salary(vacancy)
            if rub_salary:
                salaries.append(rub_salary)
        for page_num in range(1, max_page):
            response = get_hh_vacancies(language, page_num, PER_PAGE)
            for vacancy in response["items"]:
                rub_salary = predict_rub_salary(vacancy)
                if rub_salary:
                    salaries.append(rub_salary)
        try:
            average_salary = int(sum(salaries) / len(salaries))
        except ZeroDivisionError:
            average_salary = 'NA'

        lang_stats[language] = {
            "vacancies_found": response['found'],
            "vacancies_processed": len(salaries),
            "average_salary": average_salary
        }
    return lang_stats
