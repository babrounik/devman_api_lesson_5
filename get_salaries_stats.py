import hh_ru_parser as hh
from terminaltables import AsciiTable


def main():
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
    hh_title = 'Headhunter Mosсow'
    hh_lang_stats = hh.get_mosсow_languages_stats(programming_languages)
    hh_table_lines = hh.prepare_data_for_visualisation(hh_lang_stats)
    hh_table_instance = AsciiTable(hh_table_lines, hh_title)
    hh_table_instance.justify_columns = {0: 'left', 1: 'right', 2: 'right', 3: 'right'}
    print(hh_table_instance.table)


if __name__ == '__main__':
    main()
