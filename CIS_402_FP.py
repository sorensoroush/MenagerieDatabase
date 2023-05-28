import mysql.connector

c = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20"
)

mc = c.cursor()


def print_sql(columns=False, array=False):
    print(mc)
    if columns:
        print(mc.column_names)
    if array:
        for result in mc:
            print(result)


def show_databases():
    mc.execute("SHOW DATABASES")
    print_sql(columns=False, array=True)


def drop_database_if_exists():
    mc.execute("DROP DATABASE IF EXISTS menagerie")
    print_sql()


def create_use_database():
    mc.execute("CREATE DATABASE menagerie")
    print_sql()
    mc.execute("USE menagerie")
    print_sql()


def create_pet_table():
    mc.execute("""CREATE TABLE pet (
               name VARCHAR(20),
               owner VARCHAR(20),
               species VARCHAR(20),
               sex CHAR(1),
               birth DATE,
               death DATE)""")
    print_sql()


def describe_pet_table():
    mc.execute("DESCRIBE pet")
    print_sql(columns=True, array=True)


def populate_pet_table():
    sql = 'INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s)'
    val = [
        ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', None),
        ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', None),
        ('Buff', 'Harold', 'dog', 'f', '1989-05-13', None),
        ('Fang', 'Benny', 'dog', 'm', '1990-08-27', None),
        ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29'),
        ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', None),
        ('Whistler', 'Gwen', 'bird', None, '1997-12-09', None),
        ('Slim', 'Benny', 'snake', 'm', '1996-04-29', None)
        ]
    mc.executemany(sql, val)
    c.commit()
    print_sql()


def select_pet_table(sql):
    mc.execute(sql)
    print_sql(columns=True, array=True)


def main():
    #print(c)  # Step 2
    #show_databases()  # Step 4
    drop_database_if_exists()  # Step 7
    create_use_database()  # Step 10
    create_pet_table()  # Step 11
    #describe_pet_table()  # Step 11
    populate_pet_table()  # Step 14
    #select_pet_table('SELECT * FROM pet')  # Step 14
    #select_pet_table("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'")  # Step 17
    #select_pet_table('SELECT name, birth FROM pet') # Step 20
    #select_pet_table('SELECT owner, COUNT(owner) from PET GROUP BY owner')  # Step 23
    #select_pet_table('SELECT name, birth, MONTH(birth) FROM pet')  # Step 26
    c.close()


if __name__ == '__main__':
    main()
