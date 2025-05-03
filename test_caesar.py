import unittest
from CaesarCipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher(3)  # сдвиг на 3
    
    def test_encrypt(self):
        plaintext = "HELLO WORLD"
        expected_ciphertext = "KHOORZRUOG"
        self.assertEqual(self.cipher.encrypt(plaintext), expected_ciphertext)
    
    def test_decrypt(self):
        ciphertext = "KHOORZRUOG"
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(self.cipher.decrypt(ciphertext), expected_plaintext)
    
    def test_shift_wraparound(self):
        cipher = CaesarCipher(27)  # сдвиг на 1
        plaintext = "Z"
        self.assertEqual(cipher.encrypt(plaintext), "A")

    def test_ignore_non_alpha(self):
        plaintext = "Hello, World! 123"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "HELLOWORLD")

if __name__ == "__main__":
    unittest.main()