class RequestData:
    # API variables
    base_url = 'https://reqres.in/'
    get_users_request = "api/users"
    get_single_user_request = "api/users"  # needs a /# put in the test = might be worth creating a function
    get_list_resources = "api/unknown"
    get_single_resource = "api/unknown"  # needs a /# put in the test = might be worth creating a function
    post_create = "api/users"
    post_register = "api/register"
    post_login = "api/login"
    # Database information
    test_db = r"c:\sqlite_databases\regres_data.db"
    test_db_users_table = "users"
    test_db_resources_table = "resources"
