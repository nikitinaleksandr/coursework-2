from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, keyword):
        pass

class BaseClass:
    def __init__(self, arg):
        self.arg = arg

#
# class search_vacation(Parser):
#     def vacation(self):
#         print("Поиск вакансий")