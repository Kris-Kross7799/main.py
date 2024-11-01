import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        obj = runner.Runner('example')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = runner.Runner('example')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj = runner.Runner('example')
        obj_2 = runner.Runner('example_2')
        for i in range(10):
            obj.walk()
            obj_2.run()
        self.assertNotEqual(obj.distance, obj_2.distance)

        self.assertEqual(obj.distance, 50)
