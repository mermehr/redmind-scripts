# xkcd_comics - Downloads comics by XKCD

import requests, os, bs4, time  # noqa: E401

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
num_downloads = 0
MAX_DOWNLOADS = 10
while not url.endswitch('#') and num_downloads < MAX_DOWNLOADS:
    # Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the url of the comic image
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_URL = 'http:' + comic_elem[0].get('src')
        # Download the image
        print(f'Downloading image {comic_URL}...')
        res = requests.get(comic_URL)
        res.raise_for_status()

    # Save the image file to ./xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_URL)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
            
    # Get the prev buttons url
    prev_link = soup.select = soup.select('a[rel="rev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')
    num_downloads += 1
    time.sleep(1)

    print('Done.')