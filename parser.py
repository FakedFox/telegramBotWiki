import requests
from bs4 import BeautifulSoup

def pars (urlAdd):
    url = 'https://ru.wikipedia.org/wiki/'
    longUrl = url + urlAdd
    html = requests.get(longUrl).text
    return BeautifulSoup(html, 'lxml')

def page (urlAdd):
    result = ''
    laststr = 0
    text = pars(urlAdd).findAll(['p', 'ul', 'h1', 'h2', 'h3'])
    for data in text:
        result += data.text
        laststr += len(result)
    with open("TXT\\file.txt", 'w', encoding='utf-8') as f:
        f.write(result)
    return laststr

def dellTxt (urlAdd):
    laststr = page(urlAdd)
    badLine = 0
    content = 0
    txtName = f'TXT\\{urlAdd}.txt'

    with open("TXT\\file.txt", 'r', encoding='utf-8') as f, open(txtName, 'w+', encoding='utf-8') as d:
        for num, line in enumerate(f, 0):
            if 'См. также[править | править код]' in line or 'Примечания[править | править код]' in line:
                badLine += num
                break
        f.seek(0)
        for num, line in enumerate(f, 0):
            if 'Содержание' in line:
                content += num
                break
        f.seek(0)

        if badLine > 0:
            for i in range(badLine):
                x = f.readline()
                d.write(x)
        else:
            for i in range(laststr):
                x = f.readline()
                d.write(x)
    return [badLine, content, laststr, txtName]

def img(urlAdd):
    foto = pars(urlAdd).find('img')
    foto = str(foto).split(' ')
    for i in foto:
        if 'src=' in i:
            foto = i
    foto = foto.replace('src=', 'http:')
    foto = foto.replace(f'"', '')
    foto = requests.get(foto)

    with open(f'TXT\\{urlAdd}.jpg', 'wb') as f:
        f.write(foto.content)
    return f'TXT\\{urlAdd}.jpg'



if __name__ == "__main__":
    urlAdd = 'водка'
    print(dellTxt(urlAdd))
    print(img(urlAdd))
