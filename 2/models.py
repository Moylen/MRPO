from dataclasses import dataclass


@dataclass(frozen=True)
class Organization:
    name: str


@dataclass(frozen=True)
class Skill:
    name: str


@dataclass(frozen=True)
class Duty:
    name: str
    skills: list[Skill]


@dataclass(frozen=True)
class Vacancy:
    name: str
    salary: float
    experience: int
    duties: list[Duty]
    organization: Organization


@dataclass(frozen=True)
class Candidate:
    name: str
    surname: str
    vacancy: Vacancy
    skills: list[Skill]


@dataclass(frozen=True)
class Department:
    organization: Organization
    name: str
