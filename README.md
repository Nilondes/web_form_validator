# web_form_validator

This is a simple flask app which validates web forms

The database (tinyDB) contains form templates. Each template has name and fields with specified types: 

{
"name": "Form template name",
"field_name_1": "email",
"field_name_2": "phone"
}

The available types are:
- email;
- phone;
- date;
- text;

The API receives requests in format POST /get_form

with the data in form f_name1=value1&f_name2=value2

The response is the best template name which fields match the request or the form fields types if none has been found.


## Getting started
To start Docker from main directory:

```sh
$ docker build . -t dev
$ docker run -it -p 5000:5000 dev bash
$ cd web_form_validator
```

### Main app

```sh
$ python3 api.py
```

### Unit-tests

```sh
$ python3 test_functions.py
```

### Script for imitating test POST requests

```sh
$ python3 test_request.py
```

### Add test templates

```sh
$ python3 test_templates.py
```

Available commands in interactive mode:
- show_all() (Get all templates)
- clear_db() 
- only_phone (add template with only one phone field)
- date_phone_text (add template with date, phone and text fields)
- etc.