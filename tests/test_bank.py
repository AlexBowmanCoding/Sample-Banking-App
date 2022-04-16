from bankingapp.Bank import scramble, check, rng_account_number, rng_routing_number
import unittest

class TestApp(unittest.TestCase):
    def test_scramble(self):
        self.assertTrue(scramble("Test") == "b591aebf178853563ebc65b082e572429513da6d76d48d7f1caac82b182ee74c69687954823dd7009ef008c2dcbed9e3f164c98a3327302451fba61254f80af6") 
    
    def test_check_invalid_email(self):
        self.assertFalse(check("Troll@@@@@@bridge"))

    def test_check_valid_email(self):
        self.assertTrue(check("buisnessemail@company.com"))

    def test_rng_account_number(self):
        self.assertEqual(len(str(rng_account_number())),8)

    def test_rng_routing_number(self):
        self.assertEqual(len(str(rng_routing_number())),9)

        
if __name__ == "__main__":
    unittest.main()