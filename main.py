from flask import Flask, render_template, request, redirect  # из библиотеки импортировать класс Flask
from flask_sqlalchemy import SQLAlchemy  # Flask-SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it-trener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

    def __repr__(self):   # вывод id вопроса
        return f"<profiles {self.id}>"

class Experienced(db.Model):
    __tablename__ = 'experienced'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    # Четыре переменные для вопросов с 4-мя вариантами ответа
    var1 = db.Column(db.Text, nullable=False)
    var2 = db.Column(db.Text, nullable=False)
    var3 = db.Column(db.Text, nullable=False)
    var4 = db.Column(db.Text, nullable=False)
    # Переменная с правильным ответом
    right_answer = db.Column(db.Text, nullable=False)

    def __repr__(self):  # вывод id вопроса
        return f"<profiles {self.id}>"

class Professional(db.Model):  # Таблица для вопросов уровня "Профессионал"
    __tablename__ = 'professional'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    # Одна переменная для вопроса с вводом ответа
    single_var = db.Column(db.Text, nullable=True)
    # Переменная с правильным ответом
    right_answer = db.Column(db.Text, nullable=False)

    def __repr__(self):  # вывод id вопроса
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

    def __repr__(self):  # вывод id участника
        return f"<profiles {self.id}>"


def Test(id_q, id_m):  # id_q - id вопроса
    a = request.form.getlist('mybox')
    b = (a[0])  # введённый ответ
    print(b)
    # Вопрос по id_q для уровня Beginner
    ans = Beginner.query.filter_by(id=id_q).first()
    print(ans)
    # Пользователь, который проходит тест
    user = Member.query.filter_by(id=id_m, level_test="beginner", status="нет").first()
    print(user)
    # В ответе №1 нет ничего (ещё не решён)
    if user.ans1 == 1:
        user.ans1 = b  # записываем его ответ
    # В ответе №2 нет ничего (ещё не решён)
    elif user.ans2 == 2:
        user.ans2 = b  # записываем его ответ и т.д.
    elif user.ans3 == 3:
        user.ans3 = b
    elif user.ans4 == 4:
        user.ans4 = b
    elif user.ans5 == 5:
        user.ans5 = b
    elif user.ans6 == 6:
        user.ans6 = b
    elif user.ans7 == 7:
        user.ans7 = b
    elif user.ans8 == 8:
        user.ans8 = b
    elif user.ans9 == 9:
        user.ans9 = b
    elif user.ans10 == 10:
        user.ans10 = b

    kol = user.kol_prav
    int(kol)
    # Введённый ответ совпадает с правильным?
    if ans.right_answer == b:
        # Да, увеличиваем счётчик и обновляем данные
        kol += 1
        user.kol_prav = kol
        print(user.kol_prav)
        print("Классно")
    else:
        # Нет
        print("Не правильно")
    db.session.commit()
    return 0

def Test2(id_q, id_m):
    a = request.form.getlist('mybox')
    b = (a[0])
    print(b)
    ans = Experienced.query.filter_by(id=id_q).first()
    answer = Member.query.filter_by(id=id_m, level_test="experienced", status="нет").first()
    if answer.ans1 == 1:
        answer.ans1 = b
    elif answer.ans2 == 2:
        answer.ans2 = b
    elif answer.ans3 == 3:
        answer.ans3 = b
    elif answer.ans4 == 4:
        answer.ans4 = b
    elif answer.ans5 == 5:
        answer.ans5 = b
    elif answer.ans6 == 6:
        answer.ans6 = b
    elif answer.ans7 == 7:
        answer.ans7 = b

    elif answer.ans8 == 8:
        answer.ans8 = b

    elif answer.ans9 == 9:
        answer.ans9 = b

    elif answer.ans10 == 10:
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

def Test3(id_q, id_m):
    a = request.form.getlist('mybox')
    b = (a[0])
    print(b)
    ans = Professional.query.filter_by(id=id_q).first()
    answer = Member.query.filter_by(id=id_m, level_test="professional", status="нет").first()
    if answer.ans1 == 1:
        answer.ans1 = b
    elif answer.ans2 == 2:
        answer.ans2 = b
    elif answer.ans3 == 3:
        answer.ans3 = b
    elif answer.ans4 == 4:
        answer.ans4 = b
    elif answer.ans5 == 5:
        answer.ans5 = b
    elif answer.ans6 == 6:
        answer.ans6 = b
    elif answer.ans7 == 7:
        answer.ans7 = b
    elif answer.ans8 == 8:
        answer.ans8 = b
    elif answer.ans9 == 9:
        answer.ans9 = b
    elif answer.ans10 == 10:
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
    # # Добавление вопросов в базу
    # AddAndCommitData([ticket1, ticket2, ticket3, ticket4, ticket5,
    #                   ticket6, ticket7, ticket8, ticket9, ticket10])
    #
    # # Тест2
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
    # # Добавление вопросов в базу
    # AddAndCommitData([ticket1, ticket2, ticket3, ticket4, ticket5,
    #                   ticket6, ticket7, ticket8, ticket9, ticket10])
    #
    # # Тест3
    # ticket1 = Professional(question="Как в языке Python установить библиотеку flask"
    # " с помощью pip:", single_var="", right_answer="pip install Flask")
    # ticket2 = Professional(question="Какое ключевое слово в C++ служит для динамического"
    #     " выделения памяти?", single_var="", right_answer="new")
    # ticket3 = Professional(question="Как в C++ выделить динамически память для"
    #     " целочисленного массива array на length элементов?", single_var="",
    #     right_answer="int *array = new int[length]")
    # ticket4 = Professional(question="Какое ключевое слово в C++ служит для освобождения"
    #     " динамически выделенной памяти?", single_var="",
    #     right_answer="delete")
    # ticket5 = Professional(question="Что выведет данный код (C++): "
    #     "std::cout << ((true || false) ? 4 : 5) << std::endl;", single_var="",
    #     right_answer="4")
    # ticket6 = Professional(question="Что выведет данный код (C++): "
    #     "std::cout << ((1 / 3 + 1 - 1) * 3) << std::endl;", single_var="",
    #     right_answer="0")
    # ticket7 = Professional(question="Как в Python называются неизменяемые списки?",
    #     single_var="", right_answer="Кортежи")
    # ticket8 = Professional(question="Напишите код на языке Python, который преобразует"
    #     " переменную num_string типа str в тип int.", single_var="",
    #     right_answer="num_string=int(num_string)")
    # ticket9 = Professional(question="Какое ключевое слово в Python обозначает"
    #     " анонимную функцию?", single_var="", right_answer="lambda")
    # ticket10 = Professional(question="Напишите на языке Python условие с if, которое"
    #     " будет выполняться только при запуске данного файла .py"
    #     " и не будет выполняться при импорте. Используйте двойные кавычки."
    #     " Ответ запишите в виде if <условие>:", single_var="",
    #     right_answer='if __name__ == "__main__":')
    #
    # # Добавление вопросов в базу
    # AddAndCommitData([ticket1, ticket2, ticket3, ticket4, ticket5,
    #                   ticket6, ticket7, ticket8, ticket9, ticket10])

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
    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    if request.method == "POST":
        name = request.form['name_mem']
        print(name)
        item = Member(name_member=name, level_test="beginner", kol_prav=0, status="нет")

        print("Прошел")
        try:
            db.session.add(item)
            db.session.commit()
            id_m = item.id
            return redirect(f'/beginner/{id_m}/1')
        except:
            return "Ошибка"
    else:
        return render_template('name.html', level_name = level_name)

# Отслеживание страниц с вопросами для уровня "Новичок"
@app.route('/beginner/<int:id_m>/<int:id>', methods=['POST', 'GET'])
def question1(id_m, id):
    level_name = "Новичок"
    quest = Beginner.query.filter_by(id=id).all()
    print(quest)
    for el in quest:
        print(el)
    if request.method == 'POST':
        Test(id, id_m)
        if id == 10:  # заключительный вопрос, показываем страницу с результатом
            return redirect(f'/beginner/{id_m}/10/result')
        else:  # иначе, показываем следующий вопрос
            return redirect(f'/beginner/{id_m}/{id+1}')
    # quest - вопрос в БД, id - номер страницы вопроса в браузере
    return render_template('question.html', quest=quest, id=id, level_name=level_name)

# Отслеживание страницы с результатами для уровня "Новичок"
@app.route('/beginner/<int:id_m>/10/result')
def result(id_m):
    answer = Member.query.filter_by(id=id_m, status="нет").first()
    if answer == None:
        return redirect('/')
    elif answer.kol_prav >= 0:
        data = answer.kol_prav
        answer.status = "да"
        db.session.commit()
        return render_template('result.html', data=data)

# Отслеживание страницы с вводом имени для уровня "Опытный"
@app.route('/experienced', methods=['POST', 'GET'])
def name2():
    level_name = "Опытный"
    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    if request.method == "POST":
        name = request.form['name_mem']
        print(name)
        item = Member(name_member=name, level_test="experienced", kol_prav=0, status="нет")
        print("Прошел")
        try:
            db.session.add(item)
            db.session.commit()
            id_m = item.id
            return redirect(f'/experienced/{id_m}/1')
        except:
            return "Ошибка"
    else:
        return render_template('name.html', level_name=level_name)

# Отслеживание страниц с вопросами для уровня "Опытный"
@app.route('/experienced/<int:id_m>/<int:id>', methods=['POST', 'GET'])
def question2(id_m, id):
    level_name = "Опытный"
    quest = Experienced.query.filter_by(id=id).all()
    if request.method == 'POST':
        Test2(id, id_m)
        if id == 10:  # заключительный вопрос, показываем страницу с результатом
            return redirect(f'/experienced/{id_m}/10/result')
        else:  # иначе, показываем следующий вопрос
            return redirect(f'/experienced/{id_m}/{id+1}')
    return render_template('question.html', quest=quest, id=id, level_name=level_name)

# Отслеживание страницы с результатами для уровня "Опытный"
@app.route('/experienced/<int:id_m>/10/result')
def result2(id_m): # переписать в соответствии с @app.route('/beginner/10/result')
    answer = Member.query.filter_by(id=id_m, status="нет").first()
    data = answer.kol_prav
    answer.status = "да"
    db.session.commit()
    return render_template('result.html', data=data)

# Отслеживание страницы с вводом имени для уровня "Профи"
@app.route('/professional', methods=['POST', 'GET'])
def name3():
    level_name = "Профи"
    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    if request.method == "POST":
        name = request.form['name_mem']
        print(name)
        item = Member(name_member=name, level_test="professional", kol_prav=0, status="нет")
        print("Прошел")
        try:
            db.session.add(item)
            db.session.commit()
            id_m = item.id
            return redirect(f'/professional/{id_m}/1')
        except:
            return "Ошибка"
    else:
        return render_template('name.html', level_name=level_name)

# Отслеживание страниц с вопросами для уровня "Профи"
@app.route('/professional/<int:id_m>/<int:id>', methods=['POST', 'GET'])
def question3(id_m, id):
    level_name = "Профи"
    quest = Professional.query.filter_by(id=id).all()
    if request.method == 'POST':
        Test3(id, id_m)
        if id == 10:  # заключительный вопрос, показываем страницу с результатом
            return redirect(f'/professional/{id_m}/10/result')
        else:  # иначе, показываем следующий вопрос
            return redirect(f'/professional/{id_m}/{id+1}')
    return render_template('question.html', quest=quest, id=id, level_name=level_name)

# Отслеживание страницы с результатами для уровня "Профи"
@app.route('/professional/<int:id_m>/10/result')
def result3(id_m):
    answer = Member.query.filter_by(id=id_m, status="нет").first()
    data = answer.kol_prav
    answer.status = "да"
    db.session.commit()
    return render_template('result.html', data=data)

# Отслеживание страницы "О сайте"
@app.route('/about')
def about():
    answer = Member.query.filter_by(status="нет").all()
    for i in range(len(answer)):
        if answer[i].status == "нет":
            answer[i].status = "да"
            db.session.commit()
    return render_template('about.html')

# Функция для добавления данных в базу
def AddAndCommitData(listTickets):
    for ticket in listTickets:
        db.session.add(ticket)
        db.session.commit()
    print("Билет добавлен 10")

if __name__ == "__main__":
    app.run(debug=True)
