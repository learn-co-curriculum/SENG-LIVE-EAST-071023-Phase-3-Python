import sqlite3

CONN = sqlite3.connect('lib/dog_walker.db')
CURSOR = CONN.cursor()