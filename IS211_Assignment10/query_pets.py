import sqlite3
import re


def main():
    
    db_file = "pets.db"
    connection = sqlite3.connect(db_file)
        #sqlite3.connect(":memory:") <-- use this for a temp sql database
    cursor = connection.cursor()
       
    try:
        cursor.executescript("SELECT * FROM person; SELECT * FROM pet; SELECT * FROM person_pet;")
    except sqlite3.OperationalError:
        print(f"It appears there are no tables in {db_file}, you need to run load_pets.py to make them!")
        exit()
        
    while True:    
        get_id = input("Please enter an ID number: ")
        # exit program if user input is -1
        if int(get_id) == -1:
            print("Goodbye.")
            exit()
        # use regex to validate input, positive integers only    
        if not re.match("^[1-9]\\d*$", get_id):
            print("Invalid ID number.")
        # check if user input is valid id number in person table
        row = cursor.execute("SELECT * FROM person WHERE id = ?;", (get_id,)).fetchall()
        if not bool(row):
            print("That ID doesn't exist.")
        else:
            break
    
    # gets data from tables in pets.db based on id number
    owner = cursor.execute("""SELECT person.first_name, person.last_name, person.age
                          FROM person 
                          WHERE id = ?;""", (get_id,)).fetchone()
    pets = cursor.execute("""SELECT pet.name, pet.breed, pet.age, pet.dead
                          FROM person_pet
                          INNER JOIN pet ON person_pet.pet_id = pet.id
                          WHERE person_pet.person_id = ?;""", (get_id,)).fetchall()
    
    print("Owner:", owner)
    print("Pet(s):", pets)                     
    
    # more concise version 
    # row = cursor.execute("""SELECT person.first_name, person.last_name, person.age, 
                            #  pet.name, pet.breed, pet.age, pet.dead
                            #  FROM person_pet
                            #  INNER JOIN person ON person_pet.person_id = person.id
                            #  INNER JOIN pet ON person_pet.pet_id = pet.id
                            #  WHERE person_pet.person_id = ?;""", (get_id,)).fetchall()  
    
    
if __name__ == "__main__":
    main()
    