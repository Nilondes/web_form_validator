from app import app


data = {}
while True:
    field_name = input('Enter field name or leave empty to post request: ').strip()
    if field_name == '':
        response = app.test_client().post('/get_form', data=data)
        print(response.data)
        break
    else:
        field_value = input('Enter field value: ')
        data[field_name] = field_value
