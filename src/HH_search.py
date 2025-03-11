import requests
from src.ABC_class import Parser
from src.FailWorker import FileWorker
class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """


    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        # self.file_worker = file_worker
        self.vacancies = []
        # super().__init__(file_worker)



    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


if __name__ == '__main__':
    file_worker = FileWorker('info_vacation.txt')
    hh_parser = HH(file_worker)
    hh_parser.load_vacancies('Python')
    print('Вывод информации с HH: ')
    for vacancy in hh_parser.vacancies:
        print(vacancy)
    # keyword = input('Введите строку поиска вакансии: ')
    # load_vacancies(self, keyword)