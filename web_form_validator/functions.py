from tinydb import Query
from datetime import datetime
import re
from email_validator import validate_email


def is_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            return False


def is_phone(value: str) -> bool:
    pattern = r"\+7 \d{3} \d{3} \d{2} \d{2}"
    if re.fullmatch(pattern, value):
        return True

    return False


def is_email(value: str) -> bool:
    try:
        validate_email(value)
        return True
    except Exception:
        return False


def field_type(value: str) -> str:
    if is_date(value):
        return 'date'
    elif is_phone(value):
        return 'phone'
    elif is_email(value):
        return 'email'
    else:
        return 'text'

def sort_by_length(dictionary: dict):
    return len(dictionary)


def find_template(db, form: dict):
    Template = Query()
    typed_form = dict(map(lambda key_value: (key_value[0], field_type(key_value[1])), form.items()))

    for field in typed_form:
        matched_templates = db.search(Template[field] == typed_form[field])
        matched_templates.sort(key=sort_by_length, reverse=True)
        for matched_template in matched_templates:
            overlaps = sum(k in typed_form and typed_form[k] == matched_template[k] for k in matched_template)
            if overlaps  == len(matched_template) - 1:
                return matched_template['name']

    return typed_form
