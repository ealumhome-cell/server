from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DB_NAME = "budget_manage.db"

def init_db():
    conn = sqlite3.connect(DB_NAME) # opens a connection to the database file named 'budget_manger.db'
    cursor = conn.cursor() # creates a cursor/tool that lets the us send commands(SELECT, INSERT)

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    
    conn.commit() # Save changes to the database
    conn.close() # Close the connection to the database

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"}), 200

@app.post("/api/register")
def register():
    data = request.get_json()
    print(data)
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect(DB_NAME) # lopens a connection to the database file named 'budget_manager.db'
    cursor = conn.cursor() # Creates a cursor/tool that lets us send commands(SELECT, INSERT,...) to the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password)) # Executes an SQL statement
    conn.commit()
    conn.close() # Close the connection to the database
    
    return "in progress...."


if __name__ == "__main__":
    init_db()
    app.run(debug=True)