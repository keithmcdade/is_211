import argparse
import csv
import datetime
# from datetime import datetime, timedelta
from datetime import time
import logging
import shutil
import tempfile
import urllib.request
import re
import webbrowser
from pprint import pprint
import collections
from itertools import groupby


def download_data(url):
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            return tmp_file.name


class WebData:
    def __init__(self, path, time, uagent, status, size):
        self.path = path
        self.time = time
        self.uagent = uagent
        self.status = status
        self.size = size


def process_data(file_contents):
    website_data = []
    with open(file_contents, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # web = WebData(row[0], row[1], row[2], row[3], row[4])
            website_data.append(row[0:3:1])
        # pprint(website_data)
        # print(web.uagent)
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
    # browser_set = []
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
        # browser_set = set(browser_ls)
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
    # pprint(website_data[::-1])
    return browser_max


# def get_time(website_data):
#     dates_list = [datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in website_data]
#     start = datetime.datetime.fromisoformat('2014-01-27 00:00:00')
#     end = datetime.datetime.fromisoformat('2014-01-27 23:59:59')
#     res_time = start
#     for i in dates_list[:]:
#         hit = dates_list.pop(0)
#         while hit <= end:
#             hit += datetime.timedelta(seconds=1)


def assignment_2():
    logging.basicConfig(filename='error.log', filemode='w')
    # logging.error('“Error processing line {} for ID {}”'.format(id_err, name_err))


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
    # time = get_time(process_output)
    # pprint(time)
