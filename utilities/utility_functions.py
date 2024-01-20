import random
import datetime


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
