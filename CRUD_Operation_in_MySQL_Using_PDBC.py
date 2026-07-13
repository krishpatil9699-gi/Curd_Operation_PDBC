import mysql.connector

def connect_db():
    con=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="@*#krish_",
        database="company"
    )
    print("connected successfully")
    return con


con=connect_db()
cursor=con.cursor()


#---------- DDL Command ----------

def create_table():
    query=(input("Enter Create Table query : \n"))
    cursor.execute(query)
    print("table created succesfully")

def drop_table():
    query=(input("Enter Drop table query"))
    cursor.execute(query)
    print("table Droped succesfully")

def alter_table():
    query=(input("Enter Alter table query"))
    cursor.execute(query)
    print("table Alterd succesfully")

def truncate_table():
    query=(input("Enter Trucate query"))
    cursor.execute(query)
    print("table Trucated succesfully")

def rename_table():
    query=(input("enter rename query"))
    cursor.execute(query)
    print("table renamed successfully ")

#---------- DQL Command ----------

def select():
    query=(input("enter select query \n"))
    cursor.execute(query)
    records=cursor.fetchall()
    for row in records:
        print(row)

def distint():
    query=(input("enter distint query"))
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
        print(row)

def order_by():
    query=(input("enter order by query"))
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
        print(row)

# def group_by():
#     query=(input("enter group by query"))
#     cursor.execute(query)

def where():
    name=(input("enter name"))
    query= "select *from employee where name=%s"
    cursor.execute(query,(name,))
    rows=cursor.fetchall()
    for row in rows:
        print(row)

# ------- DML command ---------

def insert():
    name=(input("enter name"))
    id=(input("enter id"))
    salary=(input("enter salary"))
    job=(input("enter job"))
    query=("insert into employee(name,id,salary,job)values(%s,%s,%s,%s)")
    cursor.execute(query,(name,id,salary,job))
    # commit_transaction()

def update():
    salary=(input("enter salary"))
    id=(input("enter id"))
    query=("update employee set salary=%s where id=%s")
    cursor.execute(query,(salary,id))
    # commit_transaction()

def delete():
    name=(input("enter the name :"))
    query=("delete from employee where name=%s")
    cursor.execute(query,(name,))
    print("row is deleted")
    # commit_transaction()

# def replace()


# ------- TCL command ---------

def commit_transaction():
    con.commit()
    print("changes has been saved")

def rollback_transaction():
    con.rollback()
    print(" changes has been usaved")

# ------- Utility Commands -------

def show_tables():
    cursor.execute("show tables")

    tables=cursor.fetchall()

    for table in tables:
        print(table)
def describe():
    name=input("enter table name")
    query=f"DESC {name}"
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
    

while True:
    print(" \n ===== Mysql Pdbc Menu =====\n")

    print(" ------------------ DDL Command ------------------")
    print(" 1. Create table")
    print(" 2. Drop table")
    print(" 3. Alter table")
    print(" 4. Truncate table")
    print(" 5. Rename table")
    print("")
    print(" ------------------ DQL Command ------------------")
    print(" 6. Select ")
    print(" 7. Distinct ")
    print(" 8. Order by ")
    # print(" 9. Group by ")
    print(" 10. Where ")
    # print(" 11. Having  ")
    # print(" 12. Limit ")
    # print(" 13. Offset ")
    # print(" 14. Join ")
    # print(" 15. Union ")
    # print(" 16. Subqueries")
    # print(" 17. Aggregate Functions")
    print("")
    print(" ------------------ DML Command ------------------")
    print(" 11. Insert")
    print(" 12. Update")
    print(" 13. Delete")
    print("")
    print(" ------------------ TCL Command ------------------")
    print(" 14. Commit Changes")
    print("")
    print(" ------------------ Utility Command ------------------")
    print(" 15. Show table")
    print(" 16. Describe table ")



    choice=int(input(" Enter Command Number "))

    if choice==1:
        create_table()
    elif choice == 2:
        drop_table()
    elif choice == 3:
        alter_table()
    elif choice == 4:
        truncate_table()
    elif choice == 5:
        rename_table()
    elif choice == 6:
        select()
    elif choice == 7:
        distint()
    elif choice == 8:
        order_by()
    # elif choice == 9:
        # group_by()
    elif choice == 10:
        where()
    elif choice == 11:
        insert()
    elif choice == 12:
        update()
    elif choice == 13:
        delete()
    elif choice == 14:
        commit_transaction()
    elif choice == 15:
        show_tables()
    elif choice == 16:
        describe()



    

        



