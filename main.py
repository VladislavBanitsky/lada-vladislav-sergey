from flask import Flask, render_template, request, redirect, url_for  # из библиотеки импортировать класс Flask
from flask_sqlalchemy import SQLAlchemy
import os.path
import tempfile
from datetime import datetime
# from cloudipsp import Api, Checkout

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it-trener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Beginner(db.Model):
    __tablename__ = 'beginner'
    id = db.Column(db.Integer, primary_key=True)  # primary_key - автоматичсекая нумерация
    question = db.Column(db.Text,
                            nullable=False)  # nullable - нельзя оставить поле пустым, String(100) - максимум 100 символов
    var1 = db.Column(db.Text, nullable=False)
    var2 = db.Column(db.Text, nullable=False)
    var3 = db.Column(db.Text, nullable=False)
    var4 = db.Column(db.Text,
                      nullable=False)  # db.Text - string ограничиваниет 250 символами, а Text - сколько угодно символов
    right_answer = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=True)
#
#     # ff = db.relationship('Seans', backref='film_seans', lazy='dynamic')
    def __repr__(self):
        return f"<profiles {self.id}>"
#
class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)  # primary_key - автоматичсекая нумерация
    name_member = db.Column(db.Text)  # nullable - нельзя оставить поле пустым, String(100) - максимум 100 символов
    status = db.Column(db.Text)
    level_test = db.Column(db.Text)
    ans1 = db.Column(db.Text)
    ans2 = db.Column(db.Text)
    ans3 = db.Column(db.Text)
    ans4 = db.Column(db.Text)  # db.Text - string ограничиваниет 250 символами, а Text - сколько угодно символов
    ans5 = db.Column(db.Text)
    ans6 = db.Column(db.Text)
    ans7 = db.Column(db.Text)
    ans8 = db.Column(db.Text)
    ans9 = db.Column(db.Text)
    ans10 = db.Column(db.Text)
    kol_prav = db.Column(db.Integer)
#
#     # ff = db.relationship('Seans', backref='film_seans', lazy='dynamic')
    def __repr__(self):
        return f"<profiles {self.id}>"



# class Seans(db.Model):
#     __tablename__ = 'seans'
#     id = db.Column(db.Integer, primary_key=True)
#     id_film = db.Column(db.Integer, db.ForeignKey('film.id'))
#     format = db.Column(db.String(3), nullable=False)
#     data_of_pokaz = db.Column(db.String(100), nullable=False)
#     time_of_pokaz = db.Column(db.String(100), nullable=False)
#     hall = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#
#     ss = db.relationship('Ticket', backref='seans_ticket', lazy='dynamic')
#     def __repr__(self):
#         return f"<profiles {self.id}>"
#

def Test(id_q):
    a = request.form.getlist('mybox')
    b = (a[0])
    print(b)
    ans = Beginner.query.filter_by(id=id_q).first()
    answer = Member.query.filter_by(level_test="beginner", status="нет").first()
    if answer.ans1 == None:
        answer.ans1 = b
    elif answer.ans2 == None:
        answer.ans2 = b
    elif answer.ans3 == None:
        answer.ans3 = b
    elif answer.ans4 == None:
        answer.ans4 = b
    elif answer.ans5 == None:
        answer.ans5 = b
    elif answer.ans6 == None:
        answer.ans6 = b
    elif answer.ans7 == None:
        answer.ans7 = b

    elif answer.ans8 == None:
        answer.ans8 = b

    elif answer.ans9 == None:
        answer.ans9 = b

    elif answer.ans10 == None:
        answer.ans10 = b

    kol = answer.kol_prav
    int(kol)
    if ans.right_answer == b:
        kol += 1
        answer.kol_prav = kol
        print(answer.kol_prav)
        print("Классно")
    else:
        print("Не правильно")
    db.session.commit()
    return 0


@app.route('/')  # отслеживание главной страницы
def home():
    # with app.app_context():
    #         # px = Ticket.query.filter_by(id_seans=1).all()
    #         #  print(px[0].id)
    #         # db.session.delete(px)
    #     db.create_all()
    #     db.session.commit()
    answer = Beginner.query.filter_by(id=10).first()
    answer.var4 = "Ме"
    answer.right_answer = "Класс"
    db.session.commit()
    # print(answer.ans1)
    # print(answer.kol_prav)




    # ticket1 = Beginner(question="О жизни", var1="Классна", var2="Хороша", var3="Грустна", var4="Ужасна", right_answer="Грустна")
    # ticket2 = Beginner(question="О книгах", var1="Интересные", var2="Скучные", var3="Увлекательные", var4="Не интересные", right_answer="Интересные")
    # ticket3 = Beginner(question="Все плохо?", var1="Да", var2="Нет", var3="Сомневаюсь", var4="Не знаю",
    #                    right_answer="Да")
    # ticket4 = Beginner(question="О вселенной", var1="Жиза", var2="Классика", var3="Вечность", var4="Норм",
    #                    right_answer="Вечность")
    # ticket5 = Beginner(question="О фильмах", var1="Экшен", var2="Хоррор", var3="Комедии",
    #                    var4="Драма", right_answer="Экшен")
    # ticket6 = Beginner(question="О животных", var1="Белка", var2="Зебра", var3="Заяц", var4="Волк",
    #                    right_answer="Волк")
    # ticket7 = Beginner(question="О растениях", var1="Одуванчик", var2="Крапива", var3="Ландыш", var4="Береза",
    #                    right_answer="Береза")
    # ticket8 = Beginner(question="О планетах", var1="Нептун", var2="Марс", var3="Земля",
    #                    var4="Юпитер", right_answer="Земля")
    # ticket9 = Beginner(question="Устал?", var1="Да", var2="Нет", var3="Сомневаюсь", var4="Не знаю",
    #                    right_answer="Нет")
    # ticket10 = Beginner(question="Как тест", var1="Класс", var2="Хорошо", var3="Норм", var4="Не очень",
    #                    right_answer="Классно")
    #
    # # db.session.add(ticket1)
    # # db.session.commit()
    # #
    # # db.session.add(ticket2)
    # # db.session.commit()
    # #
    # # db.session.add(ticket3)
    # # db.session.commit()
    #
    # db.session.add(ticket4)
    # db.session.commit()
    #
    # db.session.add(ticket5)
    # db.session.commit()
    #
    # db.session.add(ticket6)
    # db.session.commit()
    #
    # db.session.add(ticket7)
    # db.session.commit()
    #
    # db.session.add(ticket8)
    # db.session.commit()
    #
    # db.session.add(ticket9)
    # db.session.commit()
    #
    # db.session.add(ticket10)
    # db.session.commit()
    #
    # print("Билет добавлен 10")



    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    return render_template('index.html')

@app.route('/beginner', methods=['POST', 'GET'])  # отслеживание главной страницы
def name1():
    if request.method == "POST":
        name = request.form['name_mem']
        print(name)
        item = Member(name_member=name, level_test="beginner", kol_prav=0, status="нет")

        print("Прошел")
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/beginner/1')
        except:
            return "Ошибка"
    else:
        return render_template('name.html')

@app.route('/beginner/1', methods=['POST', 'GET'])  # отслеживание главной страницы
def question1():
    quest = Beginner.query.filter_by(id=1).all()
    if request.method == 'POST':
        Test(1)
        return redirect('/beginner/2')
    return render_template('question.html', quest=quest)

@app.route('/beginner/2', methods=['POST', 'GET'])  # отслеживание главной страницы
def question2():
    quest = Beginner.query.filter_by(id=2).all()
    if request.method == 'POST':
        Test(2)
        return redirect('/beginner/3')
    return render_template('question.html', quest=quest)

@app.route('/beginner/3', methods=['POST', 'GET'])  # отслеживание главной страницы
def question3():
    quest = Beginner.query.filter_by(id=3).all()
    if request.method == 'POST':
        Test(3)
        return redirect('/beginner/4')
    return render_template('question.html', quest=quest)


@app.route('/beginner/4', methods=['POST', 'GET'])  # отслеживание главной страницы
def question4():
    quest = Beginner.query.filter_by(id=4).all()
    if request.method == 'POST':
        Test(4)
        return redirect('/beginner/5')
    return render_template('question.html', quest=quest)


@app.route('/beginner/5', methods=['POST', 'GET'])  # отслеживание главной страницы
def question5():
    quest = Beginner.query.filter_by(id=5).all()
    if request.method == 'POST':
        Test(5)
        return redirect('/beginner/6')
    return render_template('question.html', quest=quest)


@app.route('/beginner/6', methods=['POST', 'GET'])  # отслеживание главной страницы
def question6():
    quest = Beginner.query.filter_by(id=6).all()
    if request.method == 'POST':
        Test(6)
        return redirect('/beginner/7')
    return render_template('question.html', quest=quest)


@app.route('/beginner/7', methods=['POST', 'GET'])  # отслеживание главной страницы
def question7():
    quest = Beginner.query.filter_by(id=7).all()
    if request.method == 'POST':
        Test(7)
        return redirect('/beginner/8')
    return render_template('question.html', quest=quest)


@app.route('/beginner/8', methods=['POST', 'GET'])  # отслеживание главной страницы
def question8():
    quest = Beginner.query.filter_by(id=8).all()
    if request.method == 'POST':
        Test(8)
        return redirect('/beginner/9')
    return render_template('question.html', quest=quest)


@app.route('/beginner/9', methods=['POST', 'GET'])  # отслеживание главной страницы
def question9():
    quest = Beginner.query.filter_by(id=9).all()
    if request.method == 'POST':
        Test(9)
        return redirect('/beginner/10')
    return render_template('question.html', quest=quest)


@app.route('/beginner/10', methods=['POST', 'GET'])  # отслеживание главной страницы
def question10():
    quest = Beginner.query.filter_by(id=10).all()
    if request.method == 'POST':
        Test(10)
        return redirect('/beginner/10/result')
    return render_template('question.html', quest=quest)

@app.route('/beginner/10/result')  # отслеживание главной страницы
def result():
    answer = Member.query.filter_by(status="нет").first()
    data = answer.kol_prav
    answer.status = "да"
    db.session.commit()
    return render_template('result.html', data=data)


@app.route('/experienced', methods=['POST', 'GET'])  # отслеживание главной страницы
def name2():
    # ticket1 = Beginner(question="О жизни", var1="Классна", var2="Хороша", var3="Грустна", var4="Ужасна", right_answer="Грустна")
    # ticket2 = Beginner(question="О книгах", var1="Интересные", var2="Скучные", var3="Увлекательные", var4="Не интересные", right_answer="Интересные")
    # ticket3 = Beginner(question="Все плохо?", var1="Да", var2="Нет", var3="Сомневаюсь", var4="Не знаю",
    #                    right_answer="Да")
    # db.session.add(ticket1)
    # db.session.commit()
    #
    # db.session.add(ticket2)
    # db.session.commit()
    #
    # db.session.add(ticket3)
    # db.session.commit()
    # print("Билет добавлен 3")
    # homes = Film.query.order_by(Film.year_of_production.desc()).all()
    return render_template('name.html')

@app.route('/professional', methods=['POST', 'GET'])  # отслеживание главной страницы
def name3():
    # homes = Film.query.order_by(Film.year_of_production.desc()).all()
    return render_template('name.html')


if __name__ == "__main__":
    app.run(debug=True)
