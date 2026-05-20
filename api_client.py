import requests

TIMEOUT = 5


def get_json_response(url, params, headers={}):
    try:
        if headers:= headers:
            response = requests.get(
                url, params=params, timeout=TIMEOUT, headers=headers)
            print(response.status_code)
            print(response.text)
            response.raise_for_status()
            fetched_data = response.json()
            return fetched_data

    except requests.HTTPError as e:
        print(e)

    except requests.ConnectionError:
        print("Could not connect. Please check your internet!")

    except requests.Timeout:
        print("Request timed out. Try again. ")

    except requests.TooManyRedirects:
        print("Too many redirects at the same time.")

    except requests.JSONDecodeError:
        print("Response cannot be decoded as json.")

    return None
