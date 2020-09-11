import sqlite3

DB_PATH = './todo_restfull.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'
STATUS_LIST={NOTSTARTED,INPROGRESS,COMPLETED}


def start_db():
    conn = sqlite3.connect(DB_PATH)
    CREATE_SQL = '''CREATE TABLE IF NOT EXISTS "items"  (
            "id" INTEGER PRIMARY KEY,
            "item" TEXT NOT NULL,
            "status" TEXT NOT NULL
        );'''
    c = conn.cursor()
    c.execute(CREATE_SQL)
    conn.commit()

def add_to_list(item):
    try:       
        conn = sqlite3.connect(DB_PATH) 
        c = conn.cursor()
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

todo_list = {}

def get_all_items():
    try: 
        conn = sqlite3.connect(DB_PATH)       
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return rows
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(item_id):
    try:    
        conn = sqlite3.connect(DB_PATH)    
        c = conn.cursor()
        c.execute("select * from items where id='%s'" % item_id)
        item = c.fetchone()   
        if item:            
            return {'item':item}
        return None
    except Exception as e:
        print('Error: ', e)
        return None
    
def update_status(item_id, status):
    #Check if the passed status is a valid value
    if(status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif(status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif(status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print("Invalid Status - " + status)
        return None
    
    try:  
        conn = sqlite3.connect(DB_PATH)  
        c = conn.cursor()
        c.execute('update items set status=? where id=?', (status, item_id))
        conn.commit()
        return True
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(item_id):
    try:   
        conn = sqlite3.connect(DB_PATH)     
        c = conn.cursor()
        c.execute('delete from items where id=?', (item_id,))
        conn.commit()
        return {'delete': 1}
    except Exception as e:
        print('Error: ', e)
        return None