import sqlite3
import os.path


def check_tables(cursor, script):
    # if pets.db has no tables create them
    try:
        cursor.executescript("SELECT * FROM person; SELECT * FROM pet; SELECT * FROM person_pet;")
    except sqlite3.OperationalError:  
        cursor.executescript(script)
            
def main():
    
    path = "./pets.db"
    script = """CREATE TABLE person (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER
                );
                CREATE TABLE pet (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT,
                age INTEGER,
                dead INTEGER
                );
                CREATE TABLE person_pet (
                person_id INTEGER,
                pet_id INTEGER
                );"""
    
    # check to see if .db file already exists             
    checked = os.path.isfile(path)
    connection = sqlite3.connect("pets.db")
            #sqlite3.connect(":memory:") <-- use this for a temp sql database
    cursor = connection.cursor()    
    
    if not checked:
        # create tables in .db file if the file does not exist already
        cursor.executescript(script)
        print("new tables created")
    
    check_tables(cursor, script)
        
    # data to add to tables assigned to variable for easier refactoring
    insert_dict = {'Person': {1: (1, 'James', 'Smith', 41), 
                              2: (2, 'Diana', 'Greene', 23), 
                              3: (3, 'Sara', 'White', 27),
                              4: (4, 'William', 'Gibson', 23)
                              },
                   'Pet': {1: (1, 'Rusty', 'Dalmation', 4, 1),
                           2: (2, 'Bella', 'Alaskan Malamute', 3, 0),
                           3: (3, 'Max', 'Cocker Spaniel', 1, 0),
                           4: (4, 'Rocky', 'Beagle', 7, 0),
                           5: (5, 'Rufus', 'Cocker Spaniel', 1, 0),
                           6: (6, 'Spot', 'Bloodhound', 2, 1)   
                           },
                   'Person_Pet': {1: (1, 1),
                                  2: (1, 2),
                                  3: (2, 3),
                                  4: (2, 4),
                                  5: (3, 5),
                                  6: (4, 6)}
                   }
    
    # use insert_dict to create script for inserting data into tables
    for key in insert_dict:
        for val in insert_dict[key].values():
            cursor.executescript(f"INSERT INTO {key} VALUES {val}")
    
    print("data inserted into tables successfully")
                            
    
if __name__ == "__main__":
    main()

# use this terminal command to reset .db file before running load_pets.py
# rm pets.db | python3 load_pets.py
