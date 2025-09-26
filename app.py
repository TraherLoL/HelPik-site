from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()

def ProductDB():
    ListDb = cursor.execute('SELECT * FROM product')
    return ListDb.fetchall()

@app.route('/')
def index(): 
    shop = ProductDB()
    return render_template('lol.html') #главная страница

@app.route('/ds')
def ds():
    return render_template('ds.html') #доставка

@app.route('/shmot') #калабы
def shmot():
    return render_template('shmot.html')

@app.route('/kr') #корзина
def kr():
    return render_template('kr.html')

@app.route('/lk') #личный кабинет
def lk():
    return render_template('lk.html')

@app.route('/shmot/aktn') #мерч артиста1
def aktn():
    return render_template('aktn.html')

@app.route('/shmot/akts') #мерч артиста2
def akts():
    return render_template('akts.html')

@app.route('/shmot/akta') #мерч артиста3
def akta():
    shop = ProductDB()
    return render_template('akta.html', shop=shop)

if __name__=='__main__':
    print("Bad aplle запуск")
    app.run(debug=True)