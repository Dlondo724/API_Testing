import random
import pytest
from data.test_data import RequestData
from utilities.api_wrapper import base_available, get_request, return_json, post_request, put_request, patch_request, \
    delete_request
from utilities.utility_functions import make_dict_objects, make_user_first_name, get_job, create_password

"""we can move all the variables to a common file (file or database) for ease of modification when needed"""


class TestClass:
    @pytest.mark.unit
    def test_list_users_status_code(self):
        """Tests the status code of the get pages API
        gets the total number of pages and uses the last page to ensure it picks a valid page to send as a parameter"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_pages = get_request(RequestData.base_url, RequestData.get_users_request)
            response = get_request(RequestData.base_url, RequestData.get_users_request,
                                   make_dict_objects(page=return_json(num_pages, ["total_pages"])[0]))
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.integration
    def test_list_users_total_pages(self):
        """asserts that the number of pages is calculated correctly ana asserts that when the request is for a page
        that that page is returned"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_pages = get_request(RequestData.base_url, RequestData.get_users_request)
            total_users = return_json(num_pages, ["total"])
            num_per_page = return_json(num_pages, ["per_page"])
            pages = return_json(num_pages, ["total_pages"])
            response = get_request(RequestData.base_url, RequestData.get_users_request,
                                   make_dict_objects(page=return_json(num_pages, ["total_pages"])[0]))
            returned_page = return_json(response, ["page"])
            assert round(int(total_users[0]) / int(num_per_page[0])) is pages[0]
            assert int(returned_page[0]) is int(pages[0])
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_users_status_code(self):
        """Tests the status code of the get single user API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            response = get_request(RequestData.base_url, RequestData.get_users_request)
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_single_user_status_code(self):
        """Tests the status code of the get single user API gets the total number of users and uses a list
        comprehension to create a list of user numbers and randomly picks one to send as a parameter this ensures
        that it will always pick a valid user number"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_users = get_request(RequestData.base_url, RequestData.get_users_request)
            total_users = return_json(num_users, ["total"])
            user_number = random.choice([x for x in range(1, int(total_users[0]) + 1)])
            response = get_request(RequestData.base_url, f"{RequestData.get_single_user_request}/{user_number}")
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_list_resources_status_code(self):
        """Tests the status code of the get single user API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            response = get_request(RequestData.base_url, RequestData.get_list_resources)
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_get_single_resource_status_code(self):
        """Tests the status code of the get single user API
        gets the total number of resources and uses a list comprehension to create a list of user numbers and randomly
        picks one to send as a parameter this ensures that it will always pick a valid resources number"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_resources = get_request(RequestData.base_url, RequestData.get_list_resources)
            total_resources = int(num_resources.json()["total"])
            resource_number = random.choice([x for x in range(1, total_resources + 1)])
            response = get_request(RequestData.base_url, f"{RequestData.get_single_resource}/{resource_number}")
            assert response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_create_status_code(self):
        """Tests the status code of the get create API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            response = post_request(RequestData.base_url, RequestData.post_create,
                                    json=make_dict_objects(name=make_user_first_name(), job=get_job()))
            assert response.status_code == 201
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_update_status_code(self):
        """Tests the status code of the update API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            user_first_name = make_user_first_name()
            user_job = get_job()
            new_job = get_job(user_job)
            create_response = post_request(RequestData.base_url, RequestData.post_create,
                                           json=make_dict_objects(name=user_first_name, job=user_job))
            user_id = return_json(create_response, ["id"])
            update_response = put_request(RequestData.base_url, f"{RequestData.post_create}/{user_id}",
                                          json=make_dict_objects(name=user_first_name, job=new_job))
            assert update_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_update_patch_status_code(self):
        """Tests the status code of the update API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            create_body = make_dict_objects(name=make_user_first_name(), job=get_job())
            new_job = get_job(get_job(create_body["job"]))
            create_response = post_request(RequestData.base_url, RequestData.post_create, json=create_body)
            user_id = return_json(create_response, ["id"])
            update_response = patch_request(RequestData.base_url, f"{RequestData.post_create}/{user_id}",
                                            json=make_dict_objects(name=create_body["name"], job=new_job))
            assert update_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_delete_status_code(self):
        """Tests the status code of the get create API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            response = post_request(RequestData.base_url, RequestData.post_create,
                                    json=make_dict_objects(name=make_user_first_name(), job=get_job()))
            user_id = response.json()["id"]
            delete_response = delete_request(RequestData.base_url, f"{RequestData.post_create}/{user_id}")
            assert delete_response.status_code == 204
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_register_status_code(self):
        """Tests the status code of the post  register API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_users = get_request(RequestData.base_url, RequestData.get_users_request)
            total_users = return_json(num_users, ["total"])
            user_number = random.choice([x for x in range(1, int(total_users[0]) + 1)])
            response = get_request(RequestData.base_url, f"{RequestData.get_single_user_request}/{user_number}")
            register_response = post_request(RequestData.base_url, RequestData.post_login,
                                             json=make_dict_objects(email=return_json(response, ["email"])[0],
                                                                    password=create_password()))
            assert register_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
        return

    @pytest.mark.unit
    def test_login_successful_status_code(self):
        """Tests the status code of the post  login API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_users = get_request(RequestData.base_url, RequestData.get_users_request)
            total_users = return_json(num_users, ["total"])
            user_number = random.choice([x for x in range(1, total_users[0] + 1)])
            response = get_request(RequestData.base_url, f"{RequestData.get_single_user_request}/{user_number}")
            register_response = post_request(RequestData.base_url, RequestData.post_login,
                                             json=make_dict_objects(email=return_json(response, ["email"])[0],
                                                                    password=create_password()))
            assert register_response.status_code == 200
        else:
            assert 200 == server_status, "exit test, server not available!"
        return

    @pytest.mark.unit
    def test_single_user_not_found(self):
        """Tests the status code of the single user not found API gets the total number of users and selects the
        total + 1 to ensure that it always picks an invalid user number"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            response = get_request(RequestData.base_url, RequestData.get_users_request)
            invalid_user = return_json(response, ["total"])
            invalid_response = get_request(RequestData.base_url, RequestData.get_single_user_request + f"/{str(invalid_user)}")
            assert invalid_response.status_code == 404
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    @pytest.mark.unit
    def test_single_resource_not_found(self):
        """Tests the status code of the single user not found API
        gets the total number of resources and selects the total + 1 to ensure that it always picks an invalid
        resource number"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            response = get_request(RequestData.base_url, RequestData.get_list_resources)
            json_content = return_json(response, ["total"])
            invalid_resource = int(json_content[0]) + 1
            invalid_response = get_request(RequestData.base_url, RequestData.get_single_resource + f"/{str(invalid_resource)}")
            assert invalid_response.status_code == 404
        else:
            assert 200 == server_status, "exit test, server not available!"
            return

    def test_register_unsuccessful_status_code(self):
        """Tests the status code of the get create API"""
        num_users = get_request(RequestData.base_url, RequestData.get_users_request)
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            total_users = int(num_users.json()["total"])
            user_number = random.choice([x for x in range(1, total_users + 1)])
            response = get_request(RequestData.base_url, f"{RequestData.get_single_user_request}/{user_number}")
            body = make_dict_objects(email=return_json(response, ["email"])[0])
            register_response = post_request(RequestData.base_url, RequestData.post_register, json=body)
            assert register_response.status_code == 400
        else:
            assert 200 == server_status, "exit test, server not available!"
        return

    @pytest.mark.unit
    def test_login_unsuccessful_status_code(self):
        """Tests the status code of the post  login API"""
        server_status = base_available(RequestData.base_url)
        if server_status == 200:
            num_users = get_request(RequestData.base_url, RequestData.get_users_request)
            total_users = return_json(num_users, ["total"])
            user_number = random.choice([x for x in range(1, int(total_users[0]) + 1)])
            response = get_request(RequestData.base_url, f"{RequestData.get_single_user_request}/{user_number}")
            register_response = post_request(RequestData.base_url, RequestData.post_login,
                                             json=make_dict_objects(email=return_json(response, ["email"])[0]))
            assert register_response.status_code == 400
        else:
            assert 200 == server_status, "exit test, server not available!"
        return
