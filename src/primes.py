import unittest

class PrimeTestCase(unittest.TestCase):
    
    def test_true_if_is_prime(self):
        # Test true for all valid primes between 1 and 20
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for prime in primes:
            self.assertTrue(is_prime(prime))
    

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    unittest.main()