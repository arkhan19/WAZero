from django.test import SimpleTestCase
from django.core.exceptions import ValidationError
from WAZero.validators import DisallowedWordsPasswordValidator


class DisallowedWordsPasswordValidatorSimpleTestCase(SimpleTestCase):
    def test_valid_password_doesntraise(self):
        valid_passwprd = "mypass"
        validator = DisallowedWordsPasswordValidator()
        try:
            validator.validate(valid_passwprd)
        except ValidationError:
            self.fail("ValidationError Thrown when Validating valid Password")

    def test_invalid_password_raises(self):
        invalid_password = "mypass" + DisallowedWordsPasswordValidator.disallowed_words[0]
        validator = DisallowedWordsPasswordValidator()
        self.assertRaises(ValidationError, validator.validate, invalid_password)

    def test_invalid_password_gives_exact_message(self):
        invalid_password = "mypass" + DisallowedWordsPasswordValidator.disallowed_words[0]
        message = "Password may not contain the words: reminder, reminders, password, abcdefgh, pass1234"
        validator = DisallowedWordsPasswordValidator()

        with self.assertRaisesMessage(ValidationError, message):
            validator.validate(invalid_password)