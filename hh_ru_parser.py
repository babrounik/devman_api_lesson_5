import requests
from pprint import pprint


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
    if from_salary:
        return from_salary * 1.2
    if to_salary:
        return to_salary * 0.8


url = "https://api.hh.ru/vacancies"

programming_languages = [
    "JavaScript",
    "Java",
    "Python",
    "Ruby",
    "PHP",
    "C++",
    "C#",
    "C",
    "Go"
]

lang_stats = {}

for language in programming_languages:
    payload = {"area": 1, "text": f"программист {language}", "search_field": "name"}
    response_raw = requests.get(url, params=payload)
    response_raw.raise_for_status()
    response = response_raw.json()

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
pprint(lang_stats)
