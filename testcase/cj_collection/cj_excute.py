import unittest
from unittest import TestCase,TestSuite,TextTestRunner
from api.cj_collection.cj_excute import CjExcute

class cjExcute(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        pass
    def test_create_success01(self):
        data = "taskId=402880df73a3b3f80173b316a8aa0052&type=log"
        result = CjExcute().cj_success(data)
        self.assertTrue(result)

    def test_create_faild01(self):
        pass
    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    # unittest.main()

    case = cjExcute("test_create_success01()")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)