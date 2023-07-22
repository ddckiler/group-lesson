def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char in '+-/*!"№;%:?*()=' for char in password):
        return False

    if ' ' in password:
        return False

    if not all(char.isascii() for char in password):
        return False

    return True
import unittest

class PasswordValidationTest(unittest.TestCase):
    def test_valid_password(self):
        password = "Abcdefg1!#"
        self.assertTrue(validate_password(password))

    def test_short_password(self):
        password = "Abc123!"
        self.assertFalse(validate_password(password))

    def test_no_digit(self):
        password = "Abcdefg!#"
        self.assertFalse(validate_password(password))

    def test_no_lowercase(self):
        password = "ABCDEFG1!#"
        self.assertFalse(validate_password(password))

    def test_no_uppercase(self):
        password = "abcdefg1!#"
        self.assertFalse(validate_password(password))

    def test_no_special_character(self):
        password = "Abcdefg123"
        self.assertFalse(validate_password(password))

    def test_contains_space(self):
        password = "Abcdefg1!# "
        self.assertFalse(validate_password(password))

    def test_non_ascii_characters(self):
        password = "Привіт123!#"
        self.assertFalse(validate_password(password))

if __name__ == '__main__':
    unittest.main()