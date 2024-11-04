import unittest
import tests_12_1
import tests_12_2

TeSt=unittest.TestSuite()   #объект TestSuite()
TeSt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
TeSt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))


runner=unittest.TextTestRunner(verbosity=2)
runner.run(TeSt)