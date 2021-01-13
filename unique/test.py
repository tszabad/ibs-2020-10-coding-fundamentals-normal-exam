import unittest

from unique import unique
class TestAnagram(unittest.TestCase):

    self.assertTrue(unique("anagram", ["n", "g", "r", "m"]), True)
    self.assertFalse(unique("anagram", ["a","n", "g", "r", "m"]), False)
        with self.assertRaises(TypeError):
            unique(1234, [4,3,2,1])

if __name__ == '__main__':
    unittest.main()