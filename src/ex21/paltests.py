import palmodule
import unittest

class PalindromeTest(unittest.TestCase):

    def testBuildPalindrome(self):
        palindrome=palmodule.buildPalindrome(None)
        self.assertEqual(palindrome,'nolemonnomelon')

if __name__ == '__main__' :
    unittest.main()

