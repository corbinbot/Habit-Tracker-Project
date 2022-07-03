import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "viveklawaniya"
TOKEN = "babugussakrtahai26"


user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)



# graph_config = {
#     "id": "graph1",
#     "name": "study graph",
#     "unit": "hrs",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()
date = today.strftime("%Y%m%d")

graphID = {
    "date": date,
    "quantity": input("how many hours did you study today?:"),
}


pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
# response = requests.delete(url=pixel_create_endpoint, headers=headers)
# print(response.text)
response_d = requests.post(url=pixel_create_endpoint, json=graphID, headers=headers)
print(response_d.text)
