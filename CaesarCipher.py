class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def _format_text(self, text):
        # Приводим к верхнему регистру и оставляем только буквы A-Z
        return ''.join([c for c in text.upper() if c in self.alphabet])
    
    def encrypt(self, plaintext):
        plaintext = self._format_text(plaintext)
        ciphertext = []
        for c in plaintext:
            index = (self.alphabet.index(c) + self.shift) % 26
            ciphertext.append(self.alphabet[index])
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext):
        ciphertext = self._format_text(ciphertext)
        plaintext = []
        for c in ciphertext:
            index = (self.alphabet.index(c) - self.shift) % 26
            plaintext.append(self.alphabet[index])
        return ''.join(plaintext)