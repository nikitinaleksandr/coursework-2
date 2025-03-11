from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


#
# class search_vacation(Parser):
#     def vacation(self):
#         print("Поиск вакансий")