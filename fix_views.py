import re

with open('development/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

header = """import sqlite3
import os
from django.shortcuts import render
import datetime

def get_db_path():
    if os.environ.get('VERCEL'):
        return '/tmp/db.sqlite3'
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3')

DB_PATH = get_db_path()
"""

# Replace the original imports with the new header
content = re.sub(r'import sqlite3\nfrom django.shortcuts import render\nimport datetime\n', header, content)

# Replace all hardcoded sqlite3 connections with DB_PATH
content = re.sub(r"sqlite3\.connect\(['\"]db\.sqlite3['\"]\)", "sqlite3.connect(DB_PATH)", content)
content = re.sub(r"sqlite3\.connect\(['\"]db\.sqlite3['\"]\s*;\s*\)", "sqlite3.connect(DB_PATH)", content)

# Also handle cases where there is a semicolon outside the parenthesis
content = re.sub(r"sqlite3\.connect\(['\"]db\.sqlite3['\"]\)\s*;", "sqlite3.connect(DB_PATH);", content)


with open('development/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed views.py database paths!")
