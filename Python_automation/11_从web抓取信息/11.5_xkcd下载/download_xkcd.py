import os
import requests
import bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)  # If exist_ok is False (the default), an FileExistsError is raised if the target directory already exists
while not url.endswith('#'):

    # Download the page
    print(f"Downloading the {url}")
    ret = requests.get(url)
    ret.raise_for_status()
    soup = bs4.BeautifulSoup(ret.text, "html.parser")

    # Find the URL of the comic image
    comic_elem = soup.select('#comic img')
    if not comic_elem:
        print("Could not find comic image.")
    else:
        comic_url = comic_elem[0].get('src')

        # Download the image
        print(f"Downloading the image {comic_url}")
        ret = requests.get("https:"+ comic_url)
        ret.raise_for_status()

        # Save the image to ./xkcd
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
        for chunk in ret.iter_content(10000):
            image_file.write(chunk)
        image_file.close()

    # Get the Prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com/" + prev_link.get('href')



