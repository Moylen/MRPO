from repositories import *

if __name__ == '__main__':
    org_repos = OrganizationRepository()
    skill_repos = SkillRepository()
    duty_repos = DutyRepository()
    vac_repos = VacancyRepository()
    cand_repos = CandidateRepository()
    dep_repos = DepartmentRepository()

    skill_repos.save_item(Skill(name='skl'))

    duty_repos.save_item(Duty(name='duty'))

    vac_repos.save_item(Vacancy(
        name='vac',
        salary=100000.00,
        experience=6,
        duties=[Duty(name='test duty')],
        skills=[Skill(name='skill'), Skill(name='skill2')],
        candidates=[Candidate(name='cand name', surname='cand surname', skills=[Skill('skl')])]
    ))

    org_repos.save_item(Organization(name='org', departments=[Department('dep')], vacancies=[vac_repos.get_item(0)]))

    cand_repos.save_item(Candidate(
        name='test name',
        surname='test surname',
        skills=skill_repos.get_item(0)
    ))

    dep_repos.save_item(Department(name='test dep'))

    print(cand_repos.get_item(0))

    print(vac_repos.get_item(0))
