from app import db


def only_email():
    db.insert({'name': 'only email', 'email': 'email'})

def only_phone():
    db.insert({'name': 'only phone', 'phone': 'phone'})


def only_date():
    db.insert({'name': 'only date', 'date': 'date'})


def only_text():
    db.insert({'name': 'only text', 'text': 'text'})


def phone_text():
    db.insert({'name': 'phone_text', 'phone': 'phone', 'text': 'text'})


def phone_email():
    db.insert({'name': 'phone_email', 'phone': 'phone', 'email': 'email'})


def date_email():
    db.insert({'name': 'date_email', 'date': 'date', 'email': 'email'})


def date_phone():
    db.insert({'name': 'date_phone', 'date': 'date', 'phone': 'phone'})


def date_text():
    db.insert({'name': 'date_text', 'date': 'date', 'text': 'text'})


def email_text():
    db.insert({'name': 'email_text', 'email': 'email', 'text': 'text'})


def date_phone_email():
    db.insert({'name': 'date_phone_email', 'email': 'email', 'date': 'date', 'phone': 'phone'})


def date_phone_text():
    db.insert({'name': 'date_phone_text', 'text': 'text', 'date': 'date', 'phone': 'phone'})


def date_email_text():
    db.insert({'name': 'date_email_text', 'text': 'text', 'date': 'date', 'email': 'email'})


def phone_email_text():
    db.insert({'name': 'phone_email_text', 'text': 'text', 'phone': 'phone', 'email': 'email'})


def date_phone_email_text():
    db.insert({'name': 'date_phone_email_text', 'date': 'date', 'text': 'text', 'phone': 'phone', 'email': 'email'})


def clear_db():
    db.truncate()


def show_all():
    return db.all()


if __name__ == '__main__':
    clear_db()
    only_phone()
    only_text()
    only_date()
    date_email()
    date_phone()
    date_phone_email_text()
    date_phone_email()
