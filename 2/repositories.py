from abc import ABC, abstractmethod
from models import Organization, Skill, Duty, Vacancy, Candidate, Department


class AbstractRepository(ABC):

    @abstractmethod
    def save_item(self, item):
        pass

    @abstractmethod
    def get_item(self, index):
        pass


class OrganizationRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Organization):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class SkillRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Skill):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class DutyRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Duty):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class VacancyRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Vacancy):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class CandidateRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Candidate):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class DepartmentRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Department):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]
