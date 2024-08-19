import argparse
import csv
import datetime
import logging
import shutil
import tempfile
import urllib.request
from pprint import pprint


# this function will download a csv file and store it in a temp location
def download_data(url):
    # take url from argparse in main function and open it
    with urllib.request.urlopen(url) as response:
        # save file in temp location and return value to caller
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            return tmp_file.name


# this function processes the data in csv file from url
def process_data(file_contents):
    # initialize dictionary to store contents of csv file
    person_data = {}
    # open file and parse with DictReader function
    with open(file_contents, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # iterate through csv file to create a dictionary with ID# as key,
                # with name and birthday as value stored in tuple,
                # and with birthday converted to date object
                person_data[int(row["id"])] = (
                    row.get("name"), datetime.datetime.strptime(row.get("birthday"), '%d/%m/%Y').date())
            # catches entries with problems in the birthday column
            # and sends them to error.log via assignment2 function
            except ValueError:
                # ID# and row name are saved to variables here, so they can be passed
                # to assignment2 func and properly added to error log
                id_num = row["id"]
                name = row["name"]
                assignment_2(id_num, name)
                continue
        return person_data


# this function displays name and birthday associated with
# values from csv file from input from user_input function
# 1. catch input that is above 0 but is not associated with ID# in csv file
# 2. find name and birthday associated with ID# and print
# 3. exit program if and number <=0 is entered by user
def display_person(input_id, person_data):
    while True:
        if input_id > 0 and input_id not in person_data:
            print('ID number does not match database.')
            input_id = int(input('Please input an ID number: \n'))
        elif input_id in person_data:
            id_info = person_data[input_id]
            (name, birthday) = id_info
            # pprint(person_data) # uncomment to see full dictionary from csv file
            final_output = ('Person {} is {} with a birthday of {}.\n'.format(input_id, name, birthday))
            break
        elif input_id <= 0:
            print('ID number must be at least 1.\n')
            exit()
    return final_output


# this function logs errors from process_data function and logs it to error.log
def assignment_2(id_num, name):
    id_err = id_num
    name_err = name

    logging.basicConfig(filename='error.log', filemode='w')
    logging.error('“Error processing line {} for ID {}”'.format(id_err, name_err))


def user_input():
    # take user input
    input_id = input('Please input an ID number: \n')
    try:
        # check if input is valid data type, in this case int
        id_number = int(input_id)
    except ValueError:
        # directs user to attempt input again if an invalid value is entered
        id_number = int(input("Sorry, that didn't work.\nPlease input an ID number: \n"))
    return id_number


def main(url):
    print(f"Running main with URL = {url}...\n")


if __name__ == "__main__":
    # takes argument --url from command line and parses it for use in download_data function
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='url to download', type=str, required=True,)
    args = parser.parse_args()
    main(args.url)
    # program functions called here,
    # output from display_person function prints here
    user_input = user_input()
    csv_output = download_data(args.url)
    process_output = process_data(csv_output)
    display_output = display_person(user_input, process_output)
    print(display_output)
