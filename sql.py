import sqlite3
import json
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("SELECT * FROM Dolg")
# print(cur.fetchall())


def db_profile_exist(uid, subject):
    with open("gigachad.json", "r") as fh:
        data = json.load(fh)
        for uid in data:
            if uid in data:
                print(True)
            else:
                print(False)
    # print(data)
db_profile_exist(3562356,"Ryma")




def db_profile_insertone(query):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO `Dolg` (id, grup_name, fio, phone, date_bith, passport, kem_vid, date_pas, kod_pod, reg_reg, subject) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (query['id'], query['grup_name'], query['fio'], query['phone'], query['date_bith'], query['passport'], query['kem_vid'], query['date_pas'], query['kod_pod'], query['reg_reg'], query['subject']))
    con.commit()
    con.close()

#Хранить в БД запись как в json


    b = {query['id']: query['subject']}
    with open("gigachad.json", "r") as fh:
        data = json.load(fh)
        data.update(b)
    with open("gigachad.json", "w") as fh:
        json.dump(data, fh, indent=4, ensure_ascii=False)







