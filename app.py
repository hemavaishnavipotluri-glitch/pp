from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# -----------------------------
# DATABASE SETUP
# -----------------------------
DB_NAME = "projects.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# HOME ROUTE (DISPLAY PROJECTS)
# -----------------------------
@app.route("/")
def home():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()

    return render_template("index.html", projects=projects)

# -----------------------------
# ADD PROJECT ROUTE
# -----------------------------
@app.route("/add", methods=["POST"])
def add_project():
    title = request.form.get("title")
    description = request.form.get("description")

    if title and description:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO projects (title, description) VALUES (?, ?)",
            (title, description)
        )
        conn.commit()
        conn.close()

    return redirect(url_for("home"))

# -----------------------------
# DELETE PROJECT ROUTE (optional upgrade)
# -----------------------------
@app.route("/delete/<int:id>")
def delete_project(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

# -----------------------------
# RUN APP (IMPORTANT FOR DEPLOYMENT)
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)