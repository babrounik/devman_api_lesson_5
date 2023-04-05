# Receive info about salaries in mosсow

This script receives data about salaries in mosсow via API requests to [hh.ru](https://hh.ru/) website. Than it
processes it and format to
a good-looking table.

## How to set up environment

You do not need any specific keys.

```
cd ~/projects
git clone https://github.com/babrounik/devman_api_lesson_5.git
cd devman_api_lesson_5
pipenv shell $(which python3)
pipenv install -r requirements.txt
```

### Examples

#### How to run script:

```
python3 get_salaries_stats.py
```

![script started](https://github.com/babrounik/devman_api_lesson_5/blob/main/img/script%20work%20example.png?raw=true)