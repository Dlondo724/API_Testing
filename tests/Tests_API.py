import datetime
import random

import pytest
import requests

"""we can move all the variables to a common file for ease of modification when needed"""

base_url = 'https://reqres.in/'
get_users_request = "api/users"
get_single_user_request = "api/users"  # needs a /# put in the test = might be worth creating a function
get_list_resources = "api/unknown"
get_single_resource = "api/unknown"  # needs a /# put in the test = might be worth creating a function
post_create = "api/users"
post_register = "api/register"
post_login = "api/login"


class TestClass:
    @pytest.mark.unit
    def test_get_pages_status_code(self):
        """Tests the status code of the get pages API
        gets the total number of pages and uses the last page to ensure it picks a valid page to send as a parameter"""
        server_status = base_available(base_url)
        if server_status == 200:
            num_pages = get_request(base_url, get_users_request)
            pages = num_pages.json()["total_pages"]
            page = make_dict_objects(page=pages)
            response = get_request(base_url, get_users_request, page)
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_users_status_code(self):
        """Tests the status code of the get single user API"""
        server_status = base_available(base_url)
        if server_status == 200:
            response = get_request(base_url, get_users_request)
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_single_user_status_code(self):
        """Tests the status code of the get single user API gets the total number of users and uses a list
        comprehension to create a list of user numbers and randomly picks one to send as a parameter this ensures
        that it will always pick a valid user number"""
        server_status = base_available(base_url)
        if server_status == 200:
            num_users = get_request(base_url, get_users_request)
            total_users = int(num_users.json()["total"])
            user_number = random.choice([x for x in range(1, total_users + 1)])
            response = get_request(base_url, f"{get_single_user_request}/{user_number}")
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_list_resources_status_code(self):
        """Tests the status code of the get single user API"""
        server_status = base_available(base_url)
        if server_status == 200:
            response = get_request(base_url, get_list_resources)
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_single_resource_status_code(self):
        """Tests the status code of the get single user API
        gets the total number of resources and uses a list comprehension to create a list of user numbers and randomly
        picks one to send as a parameter this ensures that it will always pick a valid resources number"""
        server_status = base_available(base_url)
        if server_status == 200:
            num_resources = get_request(base_url, get_list_resources)
            total_resources = int(num_resources.json()["total"])
            resource_number = random.choice([x for x in range(1, total_resources + 1)])
            response = get_request(base_url, f"{get_single_resource}/{resource_number}")
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_create_status_code(self):
        """Tests the status code of the get create API"""
        server_status = base_available(base_url)
        if server_status == 200:
            first_name = make_user_first_name()
            job = get_job()
            body = make_dict_objects(name=first_name, job=job)
            response = post_request(base_url, post_create, json=body)
            assert response.status_code == 201
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_update_status_code(self):
        """Tests the status code of the update API"""
        server_status = base_available(base_url)
        if server_status == 200:
            user_first_name = make_user_first_name()
            user_job = get_job()
            create_body = make_dict_objects(name=user_first_name, job=user_job)
            new_job = get_job(user_job)
            create_new_body = make_dict_objects(name=user_first_name, job=new_job)
            create_response = post_request(base_url, post_create, json=create_body)
            user_id = create_response.json()["id"]
            update_response = put_request(base_url, f"{post_create}/{user_id}", json=create_new_body)
            assert update_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_update_patch_status_code(self):
        """Tests the status code of the update API"""
        server_status = base_available(base_url)
        if server_status == 200:
            user_first_name = make_user_first_name()
            user_job = get_job()
            create_body = make_dict_objects(name=user_first_name, job=user_job)
            new_job = get_job(user_job)
            create_new_body = make_dict_objects(name=user_first_name, job=new_job)
            create_response = post_request(base_url, post_create, json=create_body)
            user_id = create_response.json()["id"]
            update_response = patch_request(base_url, f"{post_create}/{user_id}", json=create_new_body)
            assert update_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_delete_status_code(self):
        """Tests the status code of the get create API"""
        server_status = base_available(base_url)
        if server_status == 200:
            first_name = make_user_first_name()
            job = get_job()
            body = make_dict_objects(name=first_name, job=job)
            response = post_request(base_url, post_create, json=body)
            user_id = response.json()["id"]
            delete_response = delete_request(base_url, f"{post_create}/{user_id}")
            assert delete_response.status_code == 204
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_register_status_code(self):
        """Tests the status code of the post  register API"""
        server_status = base_available(base_url)
        if server_status == 200:
            num_users = get_request(base_url, get_users_request)
            total_users = int(num_users.json()["total"])
            user_number = random.choice([x for x in range(1, total_users + 1)])
            response = get_request(base_url, f"{get_single_user_request}/{user_number}")
            email_address = response.json()["data"]["email"]
            register_password = create_password()
            body = make_dict_objects(email=email_address, password=register_password)
            register_response = post_request(base_url, post_login,
                                             json=body)  # requests.post(base_url + post_login, json=body)
            assert register_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
        return

    @pytest.mark.unit
    def test_login_successful_status_code(self):
        """Tests the status code of the post  login API"""
        server_status = base_available(base_url)
        if server_status == 200:
            num_users = get_request(base_url, get_users_request)
            total_users = int(num_users.json()["total"])
            user_number = random.choice([x for x in range(1, total_users + 1)])
            response = get_request(base_url, f"{get_single_user_request}/{user_number}")
            email_address = response.json()["data"]["email"]
            register_password = create_password()
            body = make_dict_objects(email=email_address, password=register_password)
            register_response = post_request(base_url, post_login, json=body)
            assert register_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
        return

    @pytest.mark.unit
    def test_single_user_not_found(self):
        """Tests the status code of the single user not found API gets the total number of users and selects the
        total + 1 to ensure that it always picks an invalid user number"""
        server_status = base_available(base_url)
        if server_status == 200:
            response = get_request(base_url, get_users_request)
            json_content = response.json()
            invalid_user = int(json_content["total"]) + 1
            invalid_response = get_request(base_url, get_single_user_request + f"/{str(invalid_user)}")
            assert invalid_response.status_code == 404
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_single_resource_not_found(self):
        """Tests the status code of the single user not found API
        gets the total number of resources and selects the total + 1 to ensure that it always picks an invalid
        resource number"""
        server_status = base_available(base_url)
        if server_status == 200:
            response = get_request(base_url, get_list_resources)
            json_content = response.json()
            invalid_resource = int(json_content["total"]) + 1
            invalid_response = get_request(base_url, get_single_resource + f"/{str(invalid_resource)}")
            assert invalid_response.status_code == 404
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    def test_register_unsuccessful_status_code(self):
        """Tests the status code of the get create API"""
        num_users = get_request(base_url, get_users_request)
        server_status = base_available(base_url)
        if server_status == 200:
            total_users = int(num_users.json()["total"])
            user_number = random.choice([x for x in range(1, total_users + 1)])
            response = get_request(base_url, f"{get_single_user_request}/{user_number}")
            email_address = response.json()["data"]["email"]
            body = make_dict_objects(email=email_address)
            register_response = post_request(base_url, post_register, json=body)
            assert register_response.status_code == 400
        else:
            assert 200 == server_status, "exit test, server not available!"
        return

    @pytest.mark.unit
    def test_login_unsuccessful_status_code(self):
        """Tests the status code of the post  login API"""
        server_status = base_available(base_url)
        if server_status == 200:
            num_users = get_request(base_url, get_users_request)
            total_users = int(num_users.json()["total"])
            user_number = random.choice([x for x in range(1, total_users + 1)])
            response = get_request(base_url, f"{get_single_user_request}/{user_number}")
            email_address = response.json()["data"]["email"]
            body = make_dict_objects(email=email_address)
            register_response = post_request(base_url, post_login, json=body)
            assert register_response.status_code == 400
        else:
            assert 200 == server_status, "exit test, server not available!"
        return


"""Some functions can be moveto a file and imported to be common function file to be called by test files - possible 
way to utilize fixtures"""


def base_available(url):
    """function to return the base url status code to be able to verify the base is available"""
    return requests.get(url).status_code


"""Look into helper functions for the request to build parameters and headers
find places to refactor code to make simpler and look into ares where functions can be built if there is functionality
that is repeated or can be repeated"""


def post_request(url, query, **args):
    return requests.post(url + query, **args)


def patch_request(url, query, json=None, params=None, headers=None):
    return requests.patch(url + query, json=None, params=None, headers=None)


def put_request(url, query, json=None, params=None, headers=None):
    return requests.put(url + query, json=None, params=None, headers=None)


def delete_request(url, query, json=None, params=None, headers=None):
    return requests.delete(url + query, json=None, params=None, headers=None)


def get_request(url, query, parameters_to_send=None, **headers_to_send):
    """function to send the get requests call"""
    combined_url = f"{url}{query}"
    return requests.get(combined_url, params=parameters_to_send, headers=headers_to_send)


def make_user_first_name():
    """uses epoch timestamp based on date a time now to create a unique first name"""
    unique_timestamp = int(datetime.datetime.now().timestamp())
    return f"First{str(unique_timestamp)}"


def make_user_last_name():
    """uses epoch timestamp based on date a time now to create a unique last name"""
    unique_timestamp = int(datetime.datetime.now().timestamp())
    return f"Last{str(unique_timestamp)}"


def make_dict_objects(**dict_obs):
    """creates dictionary key value pairs for payloads, parameters, headers, etc."""
    new_dictionary = {}
    for arg in dict_obs.items():
        key_pair = (arg[0], arg[1])
        new_dictionary.update({key_pair})
    return new_dictionary


def get_job(current_job=None):
    """passing in a current job will exclude it from being selected again during the same test"""
    jobs = ["Software Engineer", "Quality Assurance Technician", "DevOps", "Business Analyst"]
    used_job = []
    if current_job is not None:
        used_job.append(current_job)
    remaining_jobs = [i for i in jobs if i not in used_job]
    """returns a random job"""
    return random.choice(remaining_jobs)


def create_email(first, last):
    email_domain = random.choice(["gmail.com", "comcast.net", "aol.com", "yahoo.com", "work.com"])
    return f"{first}.{last}@{email_domain}"


def create_password():
    pass_word = []
    number_of_symbols = 2
    number_of_numbers = 3
    number_of_upper = 1
    number_of_lower = 6

    symbols = ["!", "@", "#", "$", "&"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "X", "Y", "Z"]
    for i in range(0, number_of_symbols):
        pass_word.append(random.choice(symbols))
    for i in range(0, number_of_numbers):
        pass_word.append(random.choice(numbers))
    for i in range(0, number_of_upper):
        pass_word.append(random.choice(upper_letters))
    for i in range(0, number_of_lower):
        pass_word.append(random.choice(lower_letters))
    random.shuffle(pass_word)
    password_string = "".join([str(item) for item in pass_word])
    return password_string
