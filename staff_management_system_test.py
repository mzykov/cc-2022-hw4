import unittest
from staff_management_system import StaffManagementSystem

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

        adhead = staffman.add_employee('Ad Head')
        admin = staffman.department('Admin', boss=adhead, parent=company)
        staffman.employ(adhead, admin.position('Boss'), boss=president)
        adjune = staffman.add_employee('Ad June')
        staffman.employ(adjune, admin.position('Junior'), boss=adhead)
        admidlet = staffman.add_employee('Ad Midlet')
        staffman.employ(admidlet, admin.position('Middle'), boss=adhead)
        adrise = staffman.add_employee('Ad Roines')
        staffman.employ(adrise, admin.position('Senior'), boss=adhead)

        devhead = staffman.add_employee('Dev Head')
        devel = staffman.department('Devel', boss=devhead, parent=company)
        staffman.employ(devhead, devel.position('Boss'), boss=president)
        devjune = staffman.add_employee('Developer One', email='developer-one@email.net')
        staffman.employ(devjune, devel.position('Junior'), boss=devhead)
        devmidlet = staffman.add_employee('Developer Two', phone='+12345678901')
        staffman.employ(devmidlet, devel.position('Middle'), boss=devhead)
        devrise = staffman.add_employee('Dev Roines')
        staffman.employ(devrise, devel.position('Senior'), boss=devhead)
        devteam = staffman.add_employee('Dev Team')
        staffman.employ(devteam, devel.position('Team Lead'), boss=devhead)

        qahead = staffman.add_employee('Qwa Head')
        qa = staffman.department('QA', boss=qahead, parent=company)
        staffman.employ(qahead, qa.position('Boss'), boss=president)
        qamidlet = staffman.add_employee('Qwa Midlet')
        staffman.employ(qamidlet, qa.position('Middle'), boss=qahead)
        qarise = staffman.add_employee('Qwa Roines')
        staffman.employ(qarise, qa.position('Senior'), boss=qahead)
        qateam = staffman.add_employee('Qwa Team')
        staffman.employ(qateam, qa.position('Team Lead'), boss=qahead)

        hrhead = staffman.add_employee('Hr Head')
        hr = staffman.department('HR', boss=hrhead, parent=company)
        staffman.employ(hrhead, hr.position('Boss'), boss=president)
        hrjune = staffman.add_employee('Hr June')
        staffman.employ(hrjune, hr.position('Junior'), boss=hrhead)
        hrmidlet = staffman.add_employee('Hr Midlet')
        staffman.employ(hrmidlet, hr.position('Middle'), boss=hrhead)
        hrrise = staffman.add_employee('Hr Roines')
        staffman.employ(hrrise, hr.position('Senior'), boss=hrhead)
        hrteam = staffman.add_employee('Hr Team')
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
