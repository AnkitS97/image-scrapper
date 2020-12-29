import argparse
import os
import time
from selenium import webdriver
import requests


def download_images(search: str, web_driver_path: str, target_folder_path='./images', number_images=10):
    target_folder = os.path.join(target_folder_path, '_'.join(search.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=web_driver_path) as wd:
        res = get_image_urls(search=search, number_images=number_images, wd=wd, sleep_between_interactions=0.5)

    counter = 0
    for img in res:
        save_image(target_folder, img, counter)
        counter += 1


def save_image(target_folder: str, url: str, counter):
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f'Error in downloading image {url} - {e}')

    try:
        f = open(os.path.join(target_folder, 'jpg_' + str(counter) + '.jpg'), 'wb')
        f.write(image_content)
        f.close()
        print(f'Saved successfully {url}')
    except:
        print(f'Error in saving image {url} - {e}')


def get_image_urls(search: str, number_images: int, wd: webdriver, sleep_between_interactions: int = 1):

    def scroll_to_end(wd: webdriver):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    wd.get(search_url.format(q=search))

    image_urls = set()
    image_count = 0
    result_start = 0

    while image_count < number_images:
        scroll_to_end(wd)

        thumbnails = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_thumbnails = len(thumbnails)

        print("Found {} images. Now fetching urls".format(number_thumbnails))

        for img in thumbnails[result_start: number_thumbnails]:

            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            images = wd.find_elements_by_css_selector('img.n3VNCb')
            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))

            image_count = len(image_urls)

            if image_count >= number_images:
                print(f"Found: {image_count} image links.")
                break
        result_start = number_thumbnails

    return image_urls


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver")
    parser.add_argument("--search")
    parser.add_argument("--max_images")
    args = parser.parse_args()

    # driver_path = args.driver
    # search_term = args.search
    # max_images = int(args.max_images)

    driver_path = './chromedriver.exe'
    search_term = 'cat'
    max_images = 5

    download_images(search=search_term, web_driver_path=driver_path, number_images=max_images)
