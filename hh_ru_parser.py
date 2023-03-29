import requests

url = "https://api.hh.ru/vacancies"
payload_moskow = {"area": 1}
response_moskow_raw = requests.get(url, params=payload_moskow)
response_moskow_raw.raise_for_status()
response_moskow = response_moskow_raw.json()
print(f"Moskow all: {response_moskow['found']}")

payload_moskow_30 = {"area": 1, "period": 30}
response_moskow_30_raw = requests.get(url, params=payload_moskow_30)
response_moskow_30_raw.raise_for_status()
response_moskow_30 = response_moskow_30_raw.json()
print(f"Moskow last 30 days: {response_moskow_30['found']}")

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
    "Go",
    "Objective-C"
]

for language in programming_languages:
    payload = {"area": 1, "text": f"программист {language}", "search_field": "name"}
    response_raw = requests.get(url, params=payload)
    response_raw.raise_for_status()
    response = response_raw.json()
    print(f"{language}: {response['found']}")
