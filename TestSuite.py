import unittest
import HtmlTestRunner
from tests.Home import Home
from tests.Login import Login
from tests.Account import Account
from tests.SearchFlight import SearchFlight
from tests.SearchHotel import SearchHotel

class TestSuite(unittest.TestCase):
    # Facem o suita de teste
    testSuite = unittest.TestSuite()

    # Adaugam clasele de testare ce urmeaza a fi testate in suita de teste
    testSuite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(Home),
        unittest.defaultTestLoader.loadTestsFromTestCase(Login),
        unittest.defaultTestLoader.loadTestsFromTestCase(Account),
        unittest.defaultTestLoader.loadTestsFromTestCase(SearchFlight),
        unittest.defaultTestLoader.loadTestsFromTestCase(SearchHotel),
    ])

    # Generam un raport cu ajutorul librariei HTMLTestRunner
    HtmlTestRunner.HTMLTestRunner(
        combine_reports=True,
        report_title="Final Exam Report",
        report_name="final_exam_report"
    ).run(testSuite)
