import unittest
from app import db
from functions import is_date, is_email, is_phone, field_type, find_template
import test_templates


class TestValidators(unittest.TestCase):

    def test_is_date(self):
        correct_date_1 = '2024-12-8'
        correct_date_2 = '8.12.2024'
        incorrect_date_1 = '2024-13-8'
        incorrect_date_2 = '8.13.2024'
        incorrect_date_3 = 'date'
        self.assertTrue(is_date(correct_date_1))
        self.assertTrue(is_date(correct_date_2))
        self.assertFalse(is_date(incorrect_date_1))
        self.assertFalse(is_date(incorrect_date_2))
        self.assertFalse(is_date(incorrect_date_3))

    def test_is_phone(self):
        correct_phone = '+7 123 456 78 90'
        incorrect_phone_1 = '+71234567890'
        incorrect_phone_2 = '+8 123 456 78 90'
        self.assertTrue(is_phone(correct_phone))
        self.assertFalse(is_phone(incorrect_phone_1))
        self.assertFalse(is_phone(incorrect_phone_2))

    def test_is_email(self):
        correct_email = 'test@test.com'
        incorrect_email_1 = 'test@test.daaf'
        incorrect_email_2 = 'test.ru'
        self.assertTrue(is_email(correct_email))
        self.assertFalse(is_email(incorrect_email_1))
        self.assertFalse(is_email(incorrect_email_2))

    def test_field_type(self):
        email = 'test@test.com'
        phone = '+7 123 456 78 90'
        date = '2024-12-8'
        text = '2024-25-5'
        self.assertEqual(field_type(email), 'email')
        self.assertEqual(field_type(phone), 'phone')
        self.assertEqual(field_type(date), 'date')
        self.assertEqual(field_type(text), 'text')


class TestFindTemplate(unittest.TestCase):

    def setUp(self):
        test_templates.date_phone_email_text()
        test_templates.date_phone_email()
        test_templates.date_phone()

    def tearDown(self):
        test_templates.clear_db()

    def test_phone_field(self):
        form = {'phone': '+7 123 456 78 90'}
        response_1 = find_template(db, form)
        test_templates.only_phone()
        response_2 = find_template(db, form)
        self.assertEqual(response_1, {'phone': 'phone'})
        self.assertEqual(response_2, 'only phone')

    def test_date_field(self):
        form = {'date': '2024-12-8'}
        response_1 = find_template(db, form)
        test_templates.only_date()
        response_2 = find_template(db, form)
        self.assertEqual(response_1, {'date': 'date'})
        self.assertEqual(response_2, 'only date')

    def test_email_field(self):
        form = {'email': 'test@test.com'}
        response_1 = find_template(db, form)
        test_templates.only_email()
        response_2 = find_template(db, form)
        self.assertEqual(response_1, {'email': 'email'})
        self.assertEqual(response_2, 'only email')

    def test_date_phone(self):
        form = {'phone': '+7 123 456 78 90', 'date': '8.12.2024'}
        response_1 = find_template(db, form)
        self.assertEqual(response_1, 'date_phone')

    def test_various_fields(self):
        form = {'phone': '+7 123 456 78 90',
                'date': '8.12.2024',
                'email':'test@test.com',
                'text': 'test',
                'f_name1': 'something'}
        response_1 = find_template(db, form)
        self.assertEqual(response_1, 'date_phone_email_text')


if __name__ == '__main__':
    unittest.main()