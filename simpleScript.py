import mysql.connector as connector
class DB:
    def __init__(self):
        print("\033c", end="")
        self.conn = connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pythondb")

        sql = "CREATE TABLE if not exists relics (name VARCHAR(225), expansion VARCHAR(20));"

        self.mycursor = self.conn.cursor()

        self.mycursor.execute(sql)


        self.choose_action()
        self.controller()

    def choose_action(self):
        print("What action would you like to take? (select/insert/drop)")
        self.action = input()
        print("What table?")
        self.table = input()

    def controller(self):
        if self.action == "select" or self.action == "SELECT":
            self.select_query()
        if self.action == "insert" or self.action == "INSERT":
            self.insert_query()
        if self.action == "drop" or self.action == "DROP":
            self.drop_query()


    def select_query(self):
        print("\033c", end="")
        sql = "SELECT * FROM {};".format(self.table)
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

    def insert_query(self):
        print("\033c", end="")
        print("What arguments do you want to use?")
        firstArgument = input()
        secondArgument = input()
        sql = "INSERT INTO {}(name, expansion) VALUES(%s, %s);".format(self.table)
        val = (firstArgument, secondArgument)
        self.mycursor.execute(sql, val)

        self.conn.commit()

    def drop_query(self):
        print("\033c", end="")
        sql = "DROP TABLE {};".format(self.table)
        self.mycursor.execute(sql)


p1 = DB()

#comman line program with class start asks for
#create if not exist