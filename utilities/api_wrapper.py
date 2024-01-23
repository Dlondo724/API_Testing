import requests

def post_request(url, query, **args):
    """function adds a wrapper to the post request from the requests module, enter the base url the """
    return requests.post(url + query, **args)


def patch_request(url, query, **args):
    return requests.patch(url + query, **args)


def put_request(url, query, **args):
    return requests.put(url + query, **args)


def delete_request(url, query):
    return requests.delete(url + query)


def get_request(url, query, parameters_to_send=None, **headers_to_send):
    """function to send the get requests call"""
    combined_url = f"{url}{query}"
    return requests.get(combined_url, params=parameters_to_send, headers=headers_to_send)


def return_json(request_response, json_location):
    """function returns a list of items from the specified keys in the json_location that are contained in the
    request response"""
    json_return = []
    new_json = request_response.json()
    for field in json_location:
        if field in new_json.keys():
            json_return.append(new_json[field])
        for item in new_json.items():
            for i in range(0, len(item)):
                if type(item[i]) is dict:
                    if field in item[i].keys():
                        json_return.append(item[i][field])
    return json_return


def base_available(url):
    """function to return the base url status code to be able to verify the base is available"""
    return requests.get(url).status_code
