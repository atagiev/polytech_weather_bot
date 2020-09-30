import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()        
        try:
            self.cursor.execute("CREATE TABLE users (id text, lat text, lon text)")
        except:
            pass

    def update_loc(self, id, lat, lon):
        try:
            self.cursor.execute("SELECT * FROM users WHERE id = ?",(id,))
            self.cursor.fetchone()[0]
            self.cursor.execute("UPDATE users SET lat = ?, lon = ? WHERE id = ?", (lat,lon,id,))
        except:
            self.cursor.execute("INSERT INTO users VALUES (?,?,?)",(id,lat,lon))
        self.conn.commit()

    def get_loc(self,id):
        try:
            self.cursor.execute("SELECT lat, lon FROM users WHERE id = ?",(id,))
            loc = self.cursor.fetchone()
            return 1, loc[0],loc[1]
        except:
            return 0, 0, 0

if __name__ == '__main__':
    db = Database()
    db.update_loc("1","1","1")
    print(db.get_loc("1"))