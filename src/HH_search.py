import requests
from src.ABC_class import Parser
from src.FailWorker import FileWorker


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """


    def __init__(self, file_worker):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        # self.file_worker = file_worker
        self.__vacancies = []
        # super().__init__(file_worker)

    def check_response_status(self, response):
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения: {response.status_code}")

    def get_data(self, params):
        response = requests.get(self.__url, headers=self.__headers, params=params)
        self.check_response_status(response)
        return response.json()

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
            for vacancy in hh_parser.__vacancies:
                print(vacancy)


if __name__ == '__main__':
    file_worker = FileWorker('info_vacation.txt')
    hh_parser = HH(file_worker)
    hh_parser.load_vacancies('Python')
    # print('Вывод информации с HH: ')

    # keyword = input('Введите строку поиска вакансии: ')
    # load_vacancies(self, keyword)



