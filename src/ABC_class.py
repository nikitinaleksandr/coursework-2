from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass

#
# class search_vacation(Parser):
#     def vacation(self):
#         print("Поиск вакансий")