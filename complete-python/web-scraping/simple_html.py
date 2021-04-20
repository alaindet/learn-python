from bs4 import BeautifulSoup

simple_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>This is a title</h1>
  <p class="subtitle">This is the subtitle</p>
  <p>This is just a paragraph</p>
  <ul>
    <li>Alice</li>
    <li>Bob</li>
    <li>Charlie</li>
  </ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(simple_html, 'html.parser')

def find_title() -> None:
    header1 = simple_soup.find('h1')
    header1_content = header1.string
    print(header1_content)

def find_list_items() -> None:
    list_items = simple_soup.find_all('li')
    list_contents = [list_item.string for list_item in list_items]
    print(list_contents)

def find_subtitle() -> None:
    subtitle = simple_soup.find('p', {'class': 'subtitle'})
    print(subtitle.string)

def find_other_paragraph() -> None:
    pars = simple_soup.find_all('p')
    get_css_classes = lambda element: element.attrs.get('class', '')
    other_paragraph = [p for p in pars if 'subtitle' not in get_css_classes(p)]
    print(other_paragraph[0].string)

find_other_paragraph()