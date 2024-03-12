from models import *
from repositories import *

if __name__ == '__main__':
    org_repos = OrganizationRepository()
    skill_repos = SkillRepository()
    duty_repos = DutyRepository()
    vac_repos = VacancyRepository()
    cand_repos = CandidateRepository()
    dep_repos = DepartmentRepository()

    org_repos.save_item(Organization(name='org'))

    skill_repos.save_item(Skill(name='skl'))

    duty_repos.save_item(Duty(name='duty', skills=[Skill(name='test skill'), Skill(name='another skill')]))

    vac_repos.save_item(Vacancy(
        name='vac',
        salary=100000.00,
        experience=6,
        duties=[Duty(name='test duty', skills=[])],
        organization=Organization(name='test org')
    ))

    cand_repos.save_item(Candidate(
        name='test name',
        surname='test surname',
        vacancy=vac_repos.get_item(0),
        skills=skill_repos.get_item(0)
    ))

    dep_repos.save_item(Department(name='test dep', organization=org_repos.get_item(0)))

    print(cand_repos.get_item(0))