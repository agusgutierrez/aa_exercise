from bs4 import BeautifulSoup
import urllib.request
import re


def html_analyzer(html_file):
    response = urllib.request.urlopen(html_file)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    words = re.findall(r'\w+', text)
    words = [word.lower() for word in words]
    return words


def txt_analyzer(path_to_txt):
    with open(path_to_txt, 'r') as file:
        text = file.read()
    words = re.findall(r'\w+', text)
    words = [word.lower() for word in words]
    return words


def check_if_exist(magazine_words, letter):
    letter_words = txt_analyzer(letter)
    is_doable = False

    for word in magazine_words:
        if word in letter_words:
            letter_words.remove(word)
        if len(letter_words) == 0:
            is_doable = True
            break

    if is_doable:
        return True
    else:
        return False


if __name__ == "__main__":

    while True:
        in_1 = input("Welcome, please let me know what file do you want to read (html or txt): ")
        if in_1 in ["html", "txt"]:
            break
        print("Please, specify by writing `html` or `txt`")

    if in_1 == "html":
        in_2 = input("Please, insert the link to the HTML file: ")
        words = html_analyzer(in_2)
    elif in_1 == "txt":
        in_3 = input("Please, insert the name of the file (stored in ./magazine_article/): ")
        words = txt_analyzer("./magazine_article/" + in_3)

    if check_if_exist(words, "./letter/my_letter.txt"):
        print("We can do it")
    else:
        print("We can NOT do it")
