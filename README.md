# web_form_validator

This is a simple web service which validates web forms

The database (tinyDB) contains form tamplates. Each template has name and fields with specified types: 

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

The API receives requests in format POST /get_form/f_name1=value1&f_name2=value2 

The response is the list of template names which fields match the request.

