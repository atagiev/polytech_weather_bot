import sqlite3

# States
# 0 - новый пользователь, нет локации
# 1 - отправил команду /sethomeloc, ждем от него локации
# 2 - знаем его дом локацию

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("CREATE TABLE users (id text, lat text, lon text, state text)")
        except:
            pass

    def update_loc(self, id, lat, lon):
        try:
            self.cursor.execute("UPDATE users SET lat = ?, lon = ? WHERE id = ?", (lat, lon, id,))
            self.conn.commit()
        except:
            pass

    def update_state(self, id, state):
        try:
            self.cursor.execute("UPDATE users SET state = ? WHERE id = ?", (state, id))
            self.conn.commit()
        except:
            pass

    def get_loc(self, id):
        try:
            self.cursor.execute("SELECT lat, lon FROM users WHERE id = ?", (id,))
            loc = self.cursor.fetchone()
            return loc[0], loc[1]
        except:
            return "0", "0"

    def get_state(self, id):
        try:
            self.cursor.execute("SELECT state FROM users WHERE id = ?", (id,))
            state = self.cursor.fetchone()[0]
            return state
        except:
            self.cursor.execute("INSERT INTO users VALUES (?,?,?,?)", (id, "0", "0", "0"))
            self.conn.commit()
            return "0"


if __name__ == '__main__':
    db = Database()
    db.get_state("1")
    db.update_loc("1", "1", "1")
    print(db.get_loc("1"))