import requests

payload = dict(first_name='serhii', last_name='semyonich', email='zaurus@i.ua', password='123456')
r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
data = r.json()
key_1 = input("Enter the key, to see its values:")
print('Requested data from {} key is:{}'.format(key_1, data.get(key_1, "Incorrect key!")))