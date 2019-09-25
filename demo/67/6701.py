import requests
from bs4 import BeautifulSoup

def listTag():
    send_url = 'http://127.0.0.1:8080/web/dataTable.html'
    resp = requests.get(send_url)

    soup = BeautifulSoup(resp.text, "lxml")

    print(soup)
    all_script = soup.find_all('script')

    for script in all_script:
        tag = script.b
        print(tag)
        # print(script.get('src'))


def single():
    soup = BeautifulSoup('<script class="boldest">Extremely bold</script>', 'lxml')
    print(soup)
    tag = soup.string
    print(tag)


def main():
    # listTag()
    single()


if __name__ == "__main__":
    main()