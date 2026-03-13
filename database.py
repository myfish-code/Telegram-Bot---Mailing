import sqlite3

db = sqlite3.connect("mailing_bot.db", check_same_thread=False)

conn = db.cursor()

conn.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_number INTEGER,                   
            text TEXT                              
        )
    ''')
conn.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    app_name TEXT NOT NULL,    
    account_key TEXT NOT NULL, 
    account_value TEXT NOT NULL    
);

''')

#conn.execute("DELETE FROM accounts WHERE app_name=?", ("Telegram",))
#db.commit()

def get_mail():
    data = conn.execute("SELECT * FROM records").fetchall()

    return data

def add_mail(text):
    conn.execute('SELECT * FROM records ORDER BY user_number DESC LIMIT 1')
    max_user_number_record = conn.fetchone()

    if max_user_number_record:
        max_user_number_record = max_user_number_record[1]
    else:
        max_user_number_record = 0

    data = (max_user_number_record + 1, text)

    conn.execute("INSERT INTO records (user_number, text) VALUES (?, ?)", data)
    db.commit()

def remove_mail(number):

    conn.execute("DELETE FROM records WHERE user_number=?", (number,))
    
    conn.execute("UPDATE records SET user_number = user_number - 1 WHERE user_number > ?", (number,))
   
    db.commit()

    return True

def search_mail(number):
    data = conn.execute("SELECT * FROM records WHERE user_number=?", (number,)).fetchone()
    if not data:
        return False
    
    return data[2]

def get_account(app_name):
    data = conn.execute("SELECT * FROM accounts WHERE app_name=?", (app_name, )).fetchone()
    if not data:
        return False
    
    return (data[2], data[3])
def clear_account(app_name):
    conn.execute("DELETE FROM accounts WHERE app_name=?", (app_name,))
    db.commit()

def add_account(app_name, account_key, account_value):
    conn.execute("INSERT INTO accounts (app_name, account_key, account_value) VALUES (?, ?, ?)",
                  (app_name, account_key, account_value))
    db.commit()

