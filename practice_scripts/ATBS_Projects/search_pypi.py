# search_pypi.py - Opens several search results on google.com
import requests, sys, webbrowser, bs4  # noqa: E401

# Grab the serach
print('Searching...')
res = requests.get('https://pypi.org/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Get top search links
soup = bs4.BeautifulSoup(res.text, 'parser.html')

# Open a browser tab for each result
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))

for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)