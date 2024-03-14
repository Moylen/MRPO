from dataclasses import dataclass


@dataclass(frozen=True)
class Department:
    name: str


@dataclass(frozen=True)
class Skill:
    name: str


@dataclass(frozen=True)
class Duty:
    name: str


@dataclass
class Candidate:
    name: str
    surname: str
    skills: list[Skill]


@dataclass
class Vacancy:
    name: str
    skills: list[Skill]
    duties: list[Duty]
    candidates: list[Candidate]
    salary: float = None
    experience: int = None


@dataclass
class Organization:
    name: str
    departments: list[Department]
    vacancies: list[Vacancy]
