#! /usr/bin/env python3

import sys
import io

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")

# htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
print(
   """
     <html>
    <head>
        <meta charset="UTF-8">
        <title>index</title>
        <link rel="stylesheet" href=".css">
    </head>
    <body>
    <p>hello.</p>
    <a href="result.py">次へ</a>
    """
    
)

import sqlite3

# Create database in memory
conn = sqlite3.connect('sample.db')

curs = conn.cursor()

# Create a table
curs.execute("CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")

# Insert a row of data
curs.execute("INSERT INTO data(name) values('tanaka')")
curs.execute("INSERT INTO data(name) values('saito')")

# Save (commit) the changes
conn.commit()


curs.close()
conn.close()

print(
    """
        </body>
</html>
    """
)


