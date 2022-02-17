import sqlite3

def connection():
    connt=sqlite3.connect("name.db")
    return connt

def create1(connt):
    cur=connt.cursor()
    cur.execute("create table Students(id integer,name text,age integer,course text);")
    connt.close()


def insert(connt):
    cur=connt.cursor()
    cur.executescript("""
    insert into Students values(1001,"Raziq",23,"ECE");
    insert into Students values(1002,"Khan",22,"IT");
    insert into Students values(1003,"pallavi",21,"Trinee");
    insert into Students values(1001,"pasha",20,"CS");
    insert into Students values(1001,"ashok",19,"ECE");

    """)
    connt.commit()
    connt.close()

def read(connt):
    cur=con.cursor()
    cur.execute("select * from Students")
    data=cur.fetchall()
    for d in data:
        print(d)
    connt.close()

def update(connt):
    cur = connt.cursor()
    cur.execute("select * from Students")
    print("details before update")
    data = cur.fetchall()
    for i in data:
        print(i)
    id = int(input("enter id  :"))
    name=input("Enter name to Update : ")
    cur.execute('update Students set name=? where id = ?', (name,id))
    connt.commit()
    cur.execute("select * from Students")
    print("Details After update")
    data = cur.fetchall()
    for d in data:
        print(d)
    connt.close()

def delete(connt):
    cur=connt.cursor()
    cur.execute("select * from Students")
    print("Details Before delete")
    data=cur.fetchall()
    for i in data:
        print(i)
    id=int(input("enter id to delete :"))
    cur.execute('delete from Students where id = ?',(id,))
    connt.commit()
    cur.execute("select * from Students")
    print("details after delete")
    data=cur.fetchall()
    for d in data:
        print(d)
    connt.close()




connt=connection()
create1(connt)

connt=connection()
insert(connt)
print("---------------------------display------------------")
con=connection()
read(connt)
print("---------------------------delete-------------------")
connt=connection()
delete(connt)
print("---------------------------update-------------------")
connt=connection()
update(connt)
