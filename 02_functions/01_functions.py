# deployment - prod A, B ... N
import subprocess


def checkout():
    """
        The function checks out the code in the given branch

        :returns    None
    """
    cmd = "git clone -b feature/... repo/name"
    subprocess.check_output(cmd, shell=True)


# # checkout
# def checkout(): # -> function
#     ...
#
# # clean and build
# def clean_and_build():
#     ...

# unit test
# functional test
# deployment


# Function definition
def is_even(number):
    if number % 2 == 0:
        return True
    return False


def square(number):
    return number * number


# Given a comma separated string, split them by comma and return
# json info


def introduce(user_info):  # name,25,city
    """
    splits by comma and returns json data (dictionary)


    :param user_info:   str
    :return:            dict
    """
    # split the string
    data = user_info.split(',')  # str -> split -> list

    # create dictionary
    json_data = {
        "name": data[0],
        "age": data[1],
        "city": data[2]
    }

    # return dictionary
    return json_data


# count odd numbers

# Variable scope
x = 10  # Global variable


def my_function():
    global x  # not recommended to use
    x = 5  # Local variable (different from the global x)
    x += 10
    print(f"Inside function: {x}")


if __name__ == '__main__':
    # print(is_even(10))
    # print(
    #     square(10)
    # )
    # print(introduce("Alice,25,New York"))

    my_function()
    print(f'Global x:', x)