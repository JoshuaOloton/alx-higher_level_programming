#!/usr/bin/python3
"""  script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        html = resp.read()
print("Body response:")
print(f"\t-type: {type(html)}")
print(f"\t-content: {type(html)}")
print(f"\t-utf-8 content: {html.decode()}")
