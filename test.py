from requests import get
print(get('http://127.0.0.1:5000/api/jobs').json())
print(get('http://127.0.0.1:5000/api/jobs/1').json())
print(get('http://127.0.0.1:5000/api/jobs/13123').json())
print(get('http://127.0.0.1:5000/api/jobs/errrr3rrororor').json())