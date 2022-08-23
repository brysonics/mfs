import requests
import jsonpath
import json

# create a booking

create_booking_url = "https://restful-booker.herokuapp.com/booking"

# read json_file
file = open('E:\\API\\test.json', 'r')
json_input = file.read()
# convert into json
request_json = json.loads(json_input)

# make post request with json
headers = {"Content-Type": "application/json"}
response = requests.post(create_booking_url, headers=headers, json=request_json)
print(response.content)


# parse response into json
response_json = json.loads(response.text)

# pick id from json
booking_id = jsonpath.jsonpath(response_json, 'bookingid')

# getting the first value of booking_id
first_booking_id = booking_id[0]

# get booking created
get_booking_url = f"https://restful-booker.herokuapp.com/booking/{first_booking_id}"
response1 = requests.get(get_booking_url)
print(response1.content)


# create_token

create_token_url = "https://restful-booker.herokuapp.com/auth"
# read json_file
file = open('E:\\API\\test3.json', 'r')
json_token = file.read()
# convert into json
request_json_token = json.loads(json_token)
# make post request to get token

response_token = requests.post(create_token_url, json=request_json_token)
# parse response into json
response_token_json = json.loads(response_token.text)
# pick token from json
token = jsonpath.jsonpath(response_token_json, 'token')
# get first token
first_token = token[0]
print(first_token)

# update created booking

update_booking_url = f"https://restful-booker.herokuapp.com/booking/{first_booking_id}"

# read json_file
file = open('E:\\API\\test2.json', 'r')
json_input_update = file.read()
# convert into json
request_json_update = json.loads(json_input_update)

# make post request with json
headers = {"Content-Type": "application/json", "Cookie": f"token={first_token}"}
response_update = requests.put(update_booking_url, headers=headers, json=request_json_update)
print(response_update.content)

