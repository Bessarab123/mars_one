from requests import put, get, delete, post

print(get('http://127.0.0.1:5000/api/jobs').json())
print(get('http://127.0.0.1:5000/api/jobs/1').json())
print(get('http://127.0.0.1:5000/api/jobs/13123').json())
print(get('http://127.0.0.1:5000/api/jobs/errrr3rrororor').json())

print()
print(put('http://127.0.0.1:5000/api/v2/user/3', json={
    "user": {"address": "TARDIS", "age": 800, "email": "TARDIS@mars.org", "hashed_password": None,
             "modified_date": None, "name": "WHAT", "position": "solder", "speciality": None,
             "surname": "MISSY"}}).json())
print(delete('http://127.0.0.1:5000/api/v2/user/3'))
print(post('http://127.0.0.1:5000/api/v2/user', json={
    "user": {"address": "TARDIS", "age": 1821, "email": "TARDIS@mars.org", "hashed_password": None, "id": 3,
             "modified_date": None, "name": "WHO", "position": "solder", "speciality": None,
             "surname": "DOCTOR"}}).json())
print(get('http://127.0.0.1:5000/api/v2/user/3'))