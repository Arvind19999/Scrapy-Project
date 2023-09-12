import sqlite3


conn = sqlite3.connect("myQuotes.db")
curr = conn.cursor()

# curr.execute('''create table quote(
#                 title text,
#                 author text,
#                 tags text
#                 )''')
curr.execute('''
             insert into quote values('Python','Someone who has built python','python,numpy,pandas');
             ''')
conn.commit()
conn.close()
