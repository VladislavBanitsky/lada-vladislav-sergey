from flask import Flask, render_template, request, redirect # из библиотеки импортировать класс Flask
from flask_sqlalchemy import SQLAlchemy
import os.path
import tempfile

app = Flask(__name__) # создание объекта на основе класса + передача в качестве параметра имя исполняемого файла
# после этого мы можем прописывать функции, которые будут отслеживать переходы на разные URL адреса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db1 = SQLAlchemy(app)

class Film(db1.Model):
    id_film = db1.Column(db1.Integer, primary_key=True) # primary_key - автоматичсекая нумерация
    title_film = db1.Column(db1.String(100), nullable=False) # nullable - нельзя оставить поле пустым, String(100) - максимум 100 символов
    country_of_production = db1.Column(db1.Text, nullable=False)
    year_of_production = db1.Column(db1.Integer, nullable=False)
    age_ratings = db1.Column(db1.Integer, nullable=False)
    text = db1.Column(db1.Text, nullable=False) # db.Text - string ограничиваниет 250 символами, а Text - сколько угодно символов
    genre = db1.Column(db1.Text, nullable=False)
    director = db1.Column(db1.String(100), nullable=False)
    starring = db1.Column(db1.Text, nullable=False)
    price = db1.Column(db1.Integer, nullable=False)
    new = db1.Column(db1.String(100), nullable=False)  # default=True - значение по умолчаниию

    def __repr__(self):
        return self.title_film

# with app.app_context():
#     db1.create_all()
#     print ("База создана")




# # использование sqlite и создание БД
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(tempfile.gettempdir(), 'shop.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# # созадание таблицы в БД
# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary_key - автоматичсекая нумерация
#     title = db.Column(db.String(100), nullable=False) # nullable - нельзя оставить поле пустым, String(100) - максимум 100 символов
#     price = db.Column(db.Integer, nullable=False)
#     isActive = db.Column(db.Boolean, default=True) # default=True - значение по умолчаниию
#     #text = db.Column(db.Text, nullable=False) # db.Text - string ограничиваниет 250 символами, а Text - сколько угодно символов
#
#     def __repr__(self):
#         return self.title
# # with app.app_context():
# #     db.create_all()
# #     # print ("База создана")



@app.route('/') #отслеживание главной страницы
def home():
    homes = Film.query.order_by(Film.price).all()
    # homes = Item.query.all()
    return render_template('index.html', data=homes)
    #return "Hello!"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
       title_film = request.form['title_film']
       country_of_production = request.form['country_of_production']
       year_of_production = request.form['year_of_production']
       age_ratings = request.form['age_ratings']
       text = request.form['text']
       genre = request.form['genre']
       director = request.form['director']
       starring = request.form['starring']
       price = request.form['price']
       new = request.form['new']

       item_films = Film(title_film=title_film, country_of_production=country_of_production,year_of_production=year_of_production,
                         age_ratings=age_ratings, text=text, genre=genre, director=director, starring=starring, price=price, new=new)
       try:
           db1.session.add(item_films)
           db1.session.commit()
           return redirect('/')
       except:
           return "Ошибка"
    else:
        return render_template('create.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/halls')
def halls():
    return render_template('halls.html')

@app.route('/discounts')
def discounts():
    return render_template('discounts.html')


# вывод ошибок в браузере debug=True
#                         debug=False - ошибки не видет пользователь
if __name__ == "__main__":
    app.run(debug=True)


