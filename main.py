# Account Creation
from pyscript import display, document


def account_authentication(e):
    document.getElementById('output').innerHTML = ""

    username = document.getElementById('input1').value
    password = document.getElementById('input2').value

    if len(username) < 7 and len(password) < 10:
        display("Username must be at least 7 characters and password must be at least 10 characters.", target="output")

    elif len(username) < 7:
        display("Username must be at least 7 characters.", target="output")

    elif len(password) < 10:
        display("Password must be at least 10 characters.", target="output")

    elif password.isalpha():
        display("Password must contain at least one number.", target="output")

    elif password.isdigit():
        display("Password must contain at least one letter.", target="output")

    else:
        display("Your username and password are valid.", target="output")
