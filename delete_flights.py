import requests
import time

def lambda_handler(event, context):
    skyscanner_clone_backend_url = event['skyscanner_clone_backend_url']
    departure_date_milliseconds = int(round(time.time() * 1000))

    response = requests.delete(skyscanner_clone_backend_url, data={'departureDate': departure_date_milliseconds})

    print(response.status_code, response.reason)