import unittest
from logical_values import tubSonmi,numbers_compare,text_list,juft_sonlar,is_fibonacci
class LogicalValuesTest(unittest.TestCase):
    """Mantiqiy qiymatlarni tekshiruvchi klass"""
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))
    def test_max_number(self):
        self.assertEqual(numbers_compare(2,3,6),6)
    def test_text_list(self):
        self.assertEqual(text_list('salom dunyo','mehrobdan chayon'),['Salom dunyo','Mehrobdan chayon'])
    def test_sonlar(self):
        self.assertEqual(juft_sonlar(2,5,7,9,12,14),[2,12,14])
    def test_fibonacci(self):
        self.assertTrue(is_fibonacci(8))
        self.assertFalse(is_fibonacci(10))

unittest.main()
