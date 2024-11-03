import unittest
import Runner_2
from pprint import pprint


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.H = Runner_2.Runner('Huseyn', 10)
        self.A = Runner_2.Runner('Andrey', 9)
        self.N = Runner_2.Runner('Nic', 3)

    def test_run1(self):
        tour = Runner_2.Tournament(90, self.H, self.N)
        res = tour.start()
        last_number=max(res.keys())
        self.assertTrue(res[last_number] == 'Nic', "Ошибка!")
        self.all_results['test_run1'] = res

    def test_run2(self):
        tour = Runner_2.Tournament(90, self.A, self.N)
        res = tour.start()
        self.assertTrue(res[max(res.keys())] == 'Nic', "Ошибка-2")
        self.all_results['test_run2'] = res

    def test_run3(self):
        tour = Runner_2.Tournament(90, self.H, self.A, self.N)
        res = tour.start()
        lst = max(res.keys())
        self.assertTrue(res[lst] == 'Nic', "Ошибка-3")
        self.all_results['test_run3'] = res

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f"{i+1}, {cls.all_results[elem]}")





if __name__ == "__main__":
    unittest.main()
# class RunnerTest(unittest.TestCase):
#
#     def test_walk(self):
#         obj = runner.Runner('example')
#         for i in range(10):
#             obj.walk()
#         self.assertEqual(obj.distance, 50)
#
#     def test_run(self):
#         obj = runner.Runner('example')
#         for i in range(10):
#             obj.run()
#         self.assertEqual(obj.distance, 100)
#
#     def test_challenge(self):
#         obj = runner.Runner('example')
#         obj_2 = runner.Runner('example_2')
#         for i in range(10):
#             obj.walk()
#             obj_2.run()
#         self.assertNotEqual(obj.distance, obj_2.distance)
#
#         self.assertEqual(obj.distance, 50)
