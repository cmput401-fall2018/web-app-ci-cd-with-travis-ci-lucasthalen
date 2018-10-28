import unittest
from unittest.mock import *
from service import Service

class TestService(unittest.TestCase):
    def test_bad_random(self):
        mock_filedat = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
        with patch("service.open", mock_open(read_data=mock_filedat)):
            number = Service.bad_random()
            ln = mock_filedat.count('\n') + 1
            
            self.assertTrue(0 <= number <= ln)

    def test_divide(self):
        m = Service()

        # INTEGER #################
        # POSITIVE NUMERATOR AND...
        m.bad_random = Mock(return_value = 5)
        self.assertRaises(ZeroDivisionError, m.divide, 0) # 0 DIVISION
        self.assertEqual(m.divide(1), 5) # POSITIVE DIVISOR
        self.assertEqual(m.divide(-1), -5) # NEGATIVE DIVISOR
        
        # 0 NUMERATOR AND ...
        m.bad_random = Mock(return_value = 0)
        self.assertRaises(ZeroDivisionError, m.divide, 0) # 0 DIVISION
        self.assertEqual(m.divide(1), 0) # POSITIVE DIVISOR
        self.assertEqual(m.divide(-1), 0) # NEGATIVE DIVISOR

        # NEGATIVE NUMERATOR AND
        m.bad_random = Mock(return_value = -5)
        self.assertRaises(ZeroDivisionError, m.divide, 0) # 0 DIVISION
        self.assertEqual(m.divide(1), -5) # POSITIVE DIVISOR
        self.assertEqual(m.divide(-1), 5) # NEGATIVE DIVISOR

        # DECIMAL #################
        # POSITIVE NUMERATOR AND...
        m.bad_random = Mock(return_value = 5.5)
        self.assertRaises(ZeroDivisionError, m.divide, 0.0) # 0 DIVISION
        self.assertEqual(m.divide(0.25), 22.0) # POSITIVE DIVISOR
        self.assertEqual(m.divide(-0.25), -22.0) # NEGATIVE DIVISOR
        
        # 0 NUMERATOR AND ...
        m.bad_random = Mock(return_value = 0.0)
        self.assertRaises(ZeroDivisionError, m.divide, 0.0) # 0 DIVISION
        self.assertEqual(m.divide(0.25), 0.0) # POSITIVE DIVISOR
        self.assertEqual(m.divide(-0.25), 0.0) # NEGATIVE DIVISOR

        # NEGATIVE NUMERATOR AND
        m.bad_random = Mock(return_value = -5.5)
        self.assertRaises(ZeroDivisionError, m.divide, 0.0) # 0 DIVISION
        self.assertEqual(m.divide(0.25), -22.0) # POSITIVE DIVISOR
        self.assertEqual(m.divide(-0.25), 22.0) # NEGATIVE DIVISOR

        # OTHER ##################
        m.bad_random = Mock(return_value = 5)
        self.assertEqual(m.divide(2.0), 2.5)
        self.assertIsInstance(m.divide(2.0), float)
        self.assertIsInstance(m.divide(2), float)

    def test_abs_plus(self):
        m = Service()
        res = m.abs_plus(-1) # ADD NEGATIVE
        self.assertEqual(res, 2)

        res = m.abs_plus(0) # ADD 0
        self.assertEqual(res, 1)

        res = m.abs_plus(1) # ADD POSITIVE
        self.assertEqual(res, 2)

        self.assertRaises(TypeError, m.abs_plus, 'string') # TYPE REJECTION

    def test_complicated_function(self):
        m = Service()
        
        # both 0
        m.bad_random = Mock(return_value = 0)
        m.divide = Mock(return_value = 0)
        res = m.complicated_function(0)
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 0)

        # Odd number
        m.bad_random = Mock(return_value = 3)
        m.divide = Mock(return_value = 0)
        res = m.complicated_function(0)
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 1)

        # Negative number
        m.bad_random = Mock(return_value = -5)
        m.divide = Mock(return_value = 0)
        res = m.complicated_function(0)
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 1)

        # Divide has its own tests, and nothing is changed between this and a direct function call, so implicitly if those come back wrong this function has a problem

        # Bad random is largely tested, the only novelty really is to test that the % modulo returns correctly


if __name__ == '__main__':
    unittest.main()