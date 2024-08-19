import argparse
import csv
import shutil
import tempfile
import urllib.request
import re


def download_data(url):
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            return tmp_file.name


def process_data(file_contents):
    website_data = []
    with open(file_contents, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            website_data.append(row[0:3:1])
        return website_data


def search_hits(website_data):
    total_hits = len(website_data)
    img = 0
    for i in website_data[:]:
        current_row = website_data.pop(0)
        img_hits = current_row[0]
        website_data.extend([current_row[1:]])
        if re.findall(r'([^\s]+(?=\.(jpg|gif|png))\.\2)', img_hits.lower()):
            img += 1
        else:
            continue
    img_hits = 100 * float(img / total_hits)
    return img_hits


def get_browser(website_data):
    browser_ls = []
    chrome = re.compile(r'Chrome/')
    firefox = re.compile(r'Firefox/')
    safari = re.compile(r'Version/')
    ie = re.compile(r'Trident/')
    count_chr = 0
    count_ff = 0
    count_saf = 0
    count_ie = 0
    for i in website_data[:]:
        current_row = website_data.pop(0)
        browser_hits = current_row.pop()
        browser_ls.append(browser_hits)
        website_data.extend(current_row)
        if chrome.findall(browser_hits):
            count_chr += 1
        elif firefox.findall(browser_hits):
            count_ff += 1
        elif safari.findall(browser_hits):
            count_saf += 1
        elif ie.findall(browser_hits):
            count_ie += 1
        else:
            continue
    browser_count = {'Chrome': count_chr, 'Firefox': count_ff, 'Safari': count_saf, 'Internet Explorer': count_ie}
    browser_max = max(browser_count, key=browser_count.get)
    return browser_max


def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    # takes argument --url from command line and parses it for use in download_data function
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='url to download', type=str, required=True,)
    args = parser.parse_args()
    main(args.url)

    csv_file = download_data(args.url)
    process_output = process_data(csv_file)
    hits = search_hits(process_output)
    print(f"Image requests account for {hits}% of all requests.")
    browser = get_browser(process_output)
    print(f"{browser} was the most used browser for 1/27/14.")

