class TestStringMethods(unittest.TestCase):

    def test_patterns(self):
        test_data = { 'foobar':'(foobar)^1',
                  'foofoo':'(foo)^2',
                  'fofofofofo':'(fo)^5',
                  'bbbbbbbbbb':'(b)^10'
        }

        for string, pattern in test_data.items() :
            self.assertEqual(pattern_formula(string),pattern)    
            print ("testing : ", string," ==> ",pattern, "OK") 

if __name__ == '__main__':
    unittest.main()
