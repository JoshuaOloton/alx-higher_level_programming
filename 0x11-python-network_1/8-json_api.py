#!/usr/bin/python3
"""  takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as
a parameter. """

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
