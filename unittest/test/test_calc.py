import unittest 
import calc

class TestCalc(unittest.TestCase):
    result1 = calc.add(2,4)
    result2 = calc.sub(5,3)
    def test_add(self):
        
        # self.assertEqual(result,5)
        assert calc.add(3,2) == 5, 'result should be 5'
        assert calc.add(3,-2) == 1, 'result should be 1'
        assert calc.add(1,4) == 4, 'result should be 5'

    def test_sub(self):
        
        self.assertEqual(calc.sub(5,2), 3)

if __name__ == '__main__':
    unittest.main()