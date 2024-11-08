import unittest
import Runner_3
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8')
format('%(asctime)s/%(levelname)s/%(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            obj = Runner_3.Runner('example', speed=-2)
            for i in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info(f'test_walk выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            obj = Runner_3.Runner(True)
            for i in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info(f'test_run выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        obj = Runner_3.Runner('example')
        obj_2 = Runner_3.Runner('example_2')
        for i in range(10):
            obj.walk()
            obj_2.run()
        self.assertNotEqual(obj.distance, obj_2.distance)
        self.assertEqual(obj.distance, 50)



# r1=Runner_3.Runner('Nic',speed=-15)
# print(r1.speed)
# r1.test_walk()
