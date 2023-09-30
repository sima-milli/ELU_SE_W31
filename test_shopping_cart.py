import unittest

# Import the functions you want to test
from shopping_cart import calculate_total, display_total

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        expected_total = 10.99 + 5.99 + 8.49
        self.assertEqual(calculate_total(cart), expected_total)

    def test_display_total(self):
        # Test if display_total returns the correct string
        total = 25.47
        expected_result = "Total price: 25.47"
        self.assertEqual(display_total(total), expected_result)

if __name__ == '__main__':
    unittest.main()
