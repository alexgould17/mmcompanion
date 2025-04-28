import html

def html_start(title):
    print('Content-type: text/html\n')
    print(f'<html>\n<head>\n<title>'
          f'{html.escape(title)}</title>\n</head>\n<body>')

def html_end():
    print('</body>\n</html>')

def html_list(items, ordered=False):
    print(f'<{'o' if ordered else 'u'}l>')
    for item in items:
        print(f'<li>{html.escape(item)}</li>')
    print(f'</{'o' if ordered else 'u'}l>')

def html_header(text, number):
    if number > 6:
        number = 6
    if number < 1:
        number = 1
    print(f'<h{number}>{html.escape(text)}</h{number}>')