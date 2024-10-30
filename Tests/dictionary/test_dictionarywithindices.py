
import unittest
from dictionarywithindices import convert_list_to_dict_with_indices

class TestConvertListToDictWithIndices(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(convert_list_to_dict_with_indices(['a', 'b', 'c']), {'a': 0, 'b': 1, 'c': 2})
        self.assertEqual(convert_list_to_dict_with_indices([10, 20, 30]), {10: 0, 20: 1, 30: 2})
        self.assertEqual(convert_list_to_dict_with_indices([]), {})

if __name__ == '__main__':
    unittest.main()
