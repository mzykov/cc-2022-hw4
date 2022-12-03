import unittest
from staff_management_system import StaffManagementSystem

StaffManagementSystem.is_production = False

class TestStaffManagementSystem(unittest.TestCase):

    def test_total(self):
        staffman = StaffManagementSystem()

        company = staffman.create_company('Best Python Coders Gmbh.')
        president = staffman.assign_president(company, 'Zykov Mikhail')
        self.assertFalse(company.position('President').is_vacant)

        position_names = ['Junior', 'Middle', 'Senior', 'Team Lead', 'Boss']
        departments = {
            'Admin': position_names,
            'Devel': position_names,
            'QA': position_names,
            'HR': position_names,
        }

        for name in departments:
            department = staffman.add_department(name)
            staffman.add_positions(departments[name], department)

        adhead = staffman.add_employee('Ad Head', 25, True)
        admin = staffman.department('Admin', boss=adhead, parent=company)
        staffman.employ(adhead, admin.position('Boss'), boss=president)
        adjune = staffman.add_employee('Ad June', 26, True)
        staffman.employ(adjune, admin.position('Junior'), boss=adhead)
        admidlet = staffman.add_employee('Ad Midlet', 27, True)
        staffman.employ(admidlet, admin.position('Middle'), boss=adhead)
        adrise = staffman.add_employee('Ad Roines', 28, True)
        staffman.employ(adrise, admin.position('Senior'), boss=adhead)

        devhead = staffman.add_employee('Dev Head', 29, True)
        devel = staffman.department('Devel', boss=devhead, parent=company)
        staffman.employ(devhead, devel.position('Boss'), boss=president)
        devjune = staffman.add_employee('Developer One', 30, True, email='developer-one@email.net')
        staffman.employ(devjune, devel.position('Junior'), boss=devhead)
        devmidlet = staffman.add_employee('Developer Two', 31, True, phone='+12345678901')
        staffman.employ(devmidlet, devel.position('Middle'), boss=devhead)
        devrise = staffman.add_employee('Dev Roines', 32, True)
        staffman.employ(devrise, devel.position('Senior'), boss=devhead)
        devteam = staffman.add_employee('Dev Team', 33, True)
        staffman.employ(devteam, devel.position('Team Lead'), boss=devhead)

        qahead = staffman.add_employee('Qwa Head', 34, True)
        qa = staffman.department('QA', boss=qahead, parent=company)
        staffman.employ(qahead, qa.position('Boss'), boss=president)
        qamidlet = staffman.add_employee('Qwa Midlet', 35, True)
        staffman.employ(qamidlet, qa.position('Middle'), boss=qahead)
        qarise = staffman.add_employee('Qwa Roines', 36, True)
        staffman.employ(qarise, qa.position('Senior'), boss=qahead)
        qateam = staffman.add_employee('Qwa Team', 37, True)
        staffman.employ(qateam, qa.position('Team Lead'), boss=qahead)

        hrhead = staffman.add_employee('Hr Head', 38, True)
        hr = staffman.department('HR', boss=hrhead, parent=company)
        staffman.employ(hrhead, hr.position('Boss'), boss=president)
        hrjune = staffman.add_employee('Hr June', 39, True)
        staffman.employ(hrjune, hr.position('Junior'), boss=hrhead)
        hrmidlet = staffman.add_employee('Hr Midlet', 40, True)
        staffman.employ(hrmidlet, hr.position('Middle'), boss=hrhead)
        hrrise = staffman.add_employee('Hr Roines', 41, True)
        staffman.employ(hrrise, hr.position('Senior'), boss=hrhead)
        hrteam = staffman.add_employee('Hr Leader', 42, True)
        staffman.employ(hrteam, hr.position('Team Lead'), boss=hrhead)

        vacancies = staffman.vacancies()
        self.assertEqual(vacancies, [ str('Team Lead / Admin / 4'), str('Junior / QA / 4') ])

        self.assertEqual(
            staffman.search_by_email('developer-one@email.net').name,
            'Developer One'
        )

        self.assertEqual(
            staffman.search_by_phone('+12345678901').name,
            'Developer Two'
        )

if __name__ == '__main__':
    unittest.main()
