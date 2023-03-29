from flask import Flask, render_template, request, redirect  # из библиотеки импортировать класс Flask
from flask_sqlalchemy import SQLAlchemy  # Flask-SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it-trener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
js = {'Name': '', '1': '', '2': ''}
    # print(js['Name'])
class Beginner(db.Model):
    __tablename__ = 'beginner'
    id = db.Column(db.Integer, primary_key=True)  # primary_key - автоматичсекая нумерация
    question = db.Column(db.Text,
                            nullable=False)  # nullable - нельзя оставить поле пустым
    var1 = db.Column(db.Text, nullable=False)
    var2 = db.Column(db.Text, nullable=False)
    var3 = db.Column(db.Text, nullable=False)
    var4 = db.Column(db.Text,
                      nullable=False)  # db.Text - string ограничиваниет 250 символами, а Text - сколько угодно символов
    right_answer = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=True)

    def __repr__(self):   # вывод id участника
        return f"<profiles {self.id}>"

class Experienced(db.Model):
    __tablename__ = 'experienced'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    var1 = db.Column(db.Text, nullable=False)
    var2 = db.Column(db.Text, nullable=False)
    var3 = db.Column(db.Text, nullable=False)
    var4 = db.Column(db.Text, nullable=False)
    right_answer = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<profiles {self.id}>"

class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    name_member = db.Column(db.Text)
    status = db.Column(db.Text)
    level_test = db.Column(db.Text)
    ans1 = db.Column(db.Text)
    ans2 = db.Column(db.Text)
    ans3 = db.Column(db.Text)
    ans4 = db.Column(db.Text)
    ans5 = db.Column(db.Text)
    ans6 = db.Column(db.Text)
    ans7 = db.Column(db.Text)
    ans8 = db.Column(db.Text)
    ans9 = db.Column(db.Text)
    ans10 = db.Column(db.Text)
    kol_prav = db.Column(db.Integer)

    def __repr__(self):
        return f"<profiles {self.id}>"


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

def Test2(id_q):
    a = request.form.getlist('mybox')
    b = (a[0])
    print(b)
    ans = Experienced.query.filter_by(id=id_q).first()
    answer = Member.query.filter_by(level_test="experienced", status="нет").first()
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

# Отслеживание главной страницы
@app.route('/')
def home():
    # раскомментировать эти строки для создания базы и потом снова закомментировать
    # with app.app_context():
    #     db.create_all()
    #     db.session.commit()
    # answer = Beginner.query.filter_by(id=10).first()
    # answer.var4 = "Ме"
    # answer.right_answer = "Класс"
    # db.session.commit()
    # print(answer.ans1)
    # print(answer.kol_prav)



    # Тест 1
    # Раскомментировать этот код для создания вопросов,
    # обновить страницу в браузере и снова закомментировать
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
    # db.session.add(ticket1)
    # db.session.commit()
    #
    # db.session.add(ticket2)
    # db.session.commit()
    #
    # db.session.add(ticket3)
    # db.session.commit()
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

    # Тест2
    # ticket1 = Experienced(question="Выбери лишнее:", var1="Лес", var2="Озеро", var3="Гора", var4="Дом", right_answer="Дом")
    # ticket2 = Experienced(question="Выбери лишнее:", var1="Мышь", var2="Монитор", var3="Клавиатура", var4="Паскаль", right_answer="Паскаль")
    # ticket3 = Experienced(question="Что думаешь?", var1="Все хорошо", var2="Все нормально", var3="Устал", var4="Все скучно",
    #                    right_answer="Все хорошо")
    # ticket4 = Experienced(question="Любимое животное?", var1="Собака", var2="Кошка", var3="Рыба", var4="Попугай",
    #                    right_answer="Собака")
    # ticket5 = Experienced(question="Любимый школьный прдмет?", var1="Алгебра", var2="История", var3="Биология",
    #                    var4="Информатика", right_answer="Информатика")
    # ticket6 = Experienced(question="Найди общее:", var1="С++", var2="Python", var3="Программирование", var4="Basic",
    #                    right_answer="Программирование")
    # ticket7 = Experienced(question="О растениях", var1="Одуванчик", var2="Крапива", var3="Ландыш", var4="Береза",
    #                    right_answer="Береза")
    # ticket8 = Experienced(question="О планетах", var1="Нептун", var2="Марс", var3="Земля",
    #                    var4="Юпитер", right_answer="Земля")
    # ticket9 = Experienced(question="Устал?", var1="Да", var2="Нет", var3="Сомневаюсь", var4="Не знаю",
    #                    right_answer="Нет")
    # ticket10 = Experienced(question="Как тест", var1="Класс", var2="Хорошо", var3="Норм", var4="Не очень",
    #                    right_answer="Классно")
    #
    # db.session.add(ticket1)
    # db.session.commit()
    #
    # db.session.add(ticket2)
    # db.session.commit()
    #
    # db.session.add(ticket3)
    # db.session.commit()
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



    # Перед созданием базы закомментировать этот код и удалить файл с базой
    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    return render_template('index.html')

# Отслеживание страницы с вводом имени для уровня "Новичок"
@app.route('/beginner', methods=['POST', 'GET'])
def name1():

    level_name = "Новичок"

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
        return render_template('name.html', level_name=level_name)

# Отслеживание страниц с вопросами для уровня "Новичок"
@app.route('/beginner/<int:id>', methods=['POST', 'GET'])
def question1(id):

    quest = Beginner.query.filter_by(id=id).all()
    if request.method == 'POST':
        Test(id)
        if id == 10:  # заключительный вопрос, показываем страницу с результатом
            return redirect('/beginner/10/result')
        else:  # иначе, показываем следующий вопрос
            return redirect(f'/beginner/{id+1}')
    return render_template('question.html', quest=quest, id=id)

# Отслеживание страницы с результатами для уровня "Новичок"
@app.route('/beginner/10/result')
def result():
    answer = Member.query.filter_by(status="нет").first()
    if answer == None:
        return redirect('/')
    elif answer.kol_prav >= 0:
        data = answer.kol_prav
        # answer.status = "да"
        # db.session.commit()
        return render_template('result.html', data=data)
    # elif :
    # try:
    #     data = answer.kol_prav
    #     return render_template('result.html', data=data)
    # except:
    #     answer = Member.query.filter_by(status="нет").first()
    #     print(answer)
        # answer.status = "да"
        # db.session.commit()
        # return render_template('index.html')

# Отслеживание страницы с вводом имени для уровня "Опытный"
@app.route('/experienced', methods=['POST', 'GET'])
def name2():
    level_name = "Опытный"
    if request.method == "POST":
        name = request.form['name_mem']
        print(name)
        item = Member(name_member=name, level_test="experienced", kol_prav=0, status="нет")
        print("Прошел")
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/experienced/1')
        except:
            return "Ошибка"
    else:
        return render_template('name.html', level_name=level_name)

# Отслеживание страниц с вопросами для уровня "Опытный"
@app.route('/experienced/<int:id>', methods=['POST', 'GET'])
def question11(id):
    quest = Experienced.query.filter_by(id=id).all()
    if request.method == 'POST':
        Test2(id)
        if id == 10:  # заключительный вопрос, показываем страницу с результатом
            return redirect('/experienced/10/result')
        else:  # иначе, показываем следующий вопрос
            return redirect(f'/experienced/{id+1}')
    return render_template('question.html', quest=quest)

# Отслеживание страницы с результатами для уровня "Опытный"
@app.route('/experienced/10/result')
def result2():
    answer = Member.query.filter_by(status="нет").first()
    data = answer.kol_prav
    answer.status = "да"
    db.session.commit()
    return render_template('result.html', data=data)

# Отслеживание страницы с вводом имени для уровня "Профи"
@app.route('/professional', methods=['POST', 'GET'])
def name3():
    return render_template('name.html')

@app.route('/about')
def about():
    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)