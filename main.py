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
    if len(a) == 0:
        return 0
    b = (a[0])  # введённый ответ
    print(b)
    # Вопрос по id_q для уровня Beginner
    ans = Beginner.query.filter_by(id=id_q).first()
    print(ans)
    # Пользователь, который проходит тест
    user = Member.query.filter_by(id=id_m, level_test="beginner", status="нет").first()
    print(user)

    # В ответе №1 нет ничего (ещё не решён)
    if id_q == 1:
        user.ans1 = b  # записываем его ответ
    # В ответе №2 нет ничего (ещё не решён)
    elif id_q == 2:
        user.ans2 = b  # записываем его ответ и т.д.
    elif id_q == 3:
        user.ans3 = b
    elif id_q == 4:
        user.ans4 = b
    elif id_q == 5:
        user.ans5 = b
    elif id_q == 6:
        user.ans6 = b
    elif id_q == 7:
        user.ans7 = b
    elif id_q == 8:
        user.ans8 = b
    elif id_q == 9:
        user.ans9 = b
    elif id_q == 10:
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
    if len(a) == 0:
        return 0
    b = (a[0])
    print(b)
    ans = Experienced.query.filter_by(id=id_q).first()
    answer = Member.query.filter_by(id=id_m, level_test="experienced", status="нет").first()
    if id_q == 1:
        answer.ans1 = b
    elif id_q == 2:
        answer.ans2 = b
    elif id_q == 3:
        answer.ans3 = b
    elif id_q == 4:
        answer.ans4 = b
    elif id_q == 5:
        answer.ans5 = b
    elif id_q == 6:
        answer.ans6 = b
    elif id_q == 7:
        answer.ans7 = b

    elif id_q == 8:
        answer.ans8 = b

    elif id_q == 9:
        answer.ans9 = b

    elif id_q == 10:
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
    if len(a) == 0:
        return 0
    b = (a[0])
    print(b)
    c = b.lower()
    ans = Professional.query.filter_by(id=id_q).first()
    answer = Member.query.filter_by(id=id_m, level_test="professional", status="нет").first()
    if id_q == 1:
        answer.ans1 = c
    elif id_q == 2:
        answer.ans2 = c
    elif id_q == 3:
        answer.ans3 = c
    elif id_q == 4:
        answer.ans4 = c
    elif id_q == 5:
        answer.ans5 = c
    elif id_q == 6:
        answer.ans6 = c
    elif id_q == 7:
        answer.ans7 = c
    elif id_q == 8:
        answer.ans8 = c
    elif id_q == 9:
        answer.ans9 = c
    elif id_q == 10:
        answer.ans10 = c

    kol = answer.kol_prav
    int(kol)
    if ans.right_answer == c:
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
    # раскомментировать эти 3 строки для создания базы и потом снова закомментировать
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
    # " с помощью pip:", right_answer="pip install Flask")
    # ticket2 = Professional(question="Какое ключевое слово в C++ служит для динамического"
    #     " выделения памяти?", right_answer="new")
    # ticket3 = Professional(question="Как в C++ выделить динамически память для"
    #     " целочисленного массива array на length элементов?",
    #     right_answer="int *array = new int[length]")
    # ticket4 = Professional(question="Какое ключевое слово в C++ служит для освобождения"
    #     " динамически выделенной памяти?",
    #     right_answer="delete")
    # ticket5 = Professional(question="Что выведет данный код (C++): "
    #     "std::cout << ((true || false) ? 4 : 5) << std::endl;",
    #     right_answer="4")
    # ticket6 = Professional(question="Что выведет данный код (C++): "
    #     "std::cout << ((1 / 3 + 1 - 1) * 3) << std::endl;",
    #     right_answer="0")
    # ticket7 = Professional(question="Как в Python называются неизменяемые списки?",
    #     single_var="", right_answer="Кортежи")
    # ticket8 = Professional(question="Напишите код на языке Python, который преобразует"
    #     " переменную num_string типа str в тип int.",
    #     right_answer="num_string=int(num_string)")
    # ticket9 = Professional(question="Какое ключевое слово в Python обозначает"
    #     " анонимную функцию?", right_answer="lambda")
    # ticket10 = Professional(question="Напишите на языке Python условие с if, которое"
    #     " будет выполняться только при запуске данного файла .py"
    #     " и не будет выполняться при импорте. Используйте двойные кавычки."
    #     " Ответ запишите в виде if <условие>:",
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
        # print(name)
        item = Member(name_member=name, level_test="beginner", kol_prav=0, status="нет")
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
    quest = Beginner.query.filter_by(id=id).all()  # записываем в список
    print(type(quest))
    for el in quest:
        print(el.right_answer)
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
        # answer.status = "да"
        # db.session.commit()
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


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/vvod_vopr_db_t1', methods=['POST', 'GET'])
def vvod_vopr_t1():
    PASSWORD = '11111'
    if request.method == "POST":
        # print("Прошел")
        type = request.form['type']
        vopros = request.form['vopros']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        right_ans = request.form['right_ans']
        password = request.form['password']
        if int(type) == 1:
            kol = db.session.query(db.func.max(Beginner.id)).first()[0]
            print(kol)
            if kol != None:
                if kol >= 10:
                    db.session.commit()
                    return "Количество вопросов в тесте максимально, для добавления нового вопроса нужно обновить другой вопрос."

        if int(type) == 2:
            kol = db.session.query(db.func.max(Experienced.id)).first()[0]
            print(kol)
            if kol != None:
                if kol >= 10:
                    db.session.commit()
                    return "Количество вопросов в тесте максимально, для добавления нового вопроса нужно обновить другой вопрос."

        if (int(type) != 1 and int(type) != 2):
            return "Не правильно введено номер теста хы"

        if (right_ans != ans1) and (right_ans != ans2) and (right_ans != ans3) and (right_ans != ans4):
            return "Ошибка, правильный ответ не сопадает ни с одним из вариаетов ответа"

        if (password == PASSWORD):
            if (int(type) == 1):
                item = Beginner(question=vopros, var1=ans1, var2=ans2, var3=ans3, var4=ans4,  right_answer=right_ans)
                try:
                    db.session.add(item)
                    db.session.commit()
                    return redirect('/vvod_vopr_db_t1')
                except:
                    return "Ошибка"
            if (int(type) == 2):
                item = Experienced(question=vopros, var1=ans1, var2=ans2, var3=ans3, var4=ans4,  right_answer=right_ans)
                try:
                    db.session.add(item)
                    db.session.commit()
                    return redirect('/vvod_vopr_db_t1')
                except:
                    return "Ошибка"
            if (int(type) != 1 or int(type) == 2):
                return "Не правильно введен номер теста"
        else:
            return "У вас нет прав для внесения изменений в БД"
    else:
        return render_template('vvod_vopr_test1.html')


@app.route('/obnov_vopr_db_t1', methods=['POST', 'GET'])
def obnov_vopr_t1():
    PASSWORD = '11111'
    if request.method == "POST":
        # print("Прошел")
        type = request.form['type']
        n_vopros = request.form['n_vopros']
        vopros = request.form['vopros']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        right_ans = request.form['right_ans']
        password = request.form['password']
        # if int(type) == 1:
        #     N_v = db.session.query(db.func.max(Beginner.id)).first()[0]
        #     print(kol)
        #     if kol == 10:
        #         db.session.commit()
        #         return "Количество вопросов в тесте максимально, для добавления нового вопроса нужно обновить другой вопрос."
        #
        # if int(type) == 2:
        #     kol = db.session.query(db.func.max(Experienced.id)).first()[0]
        #     print(kol)
        #     if kol >= 11:
        #         db.session.commit()
        #         return "Количество вопросов в тесте максимально, для добавления нового вопроса нужно обновить другой вопрос."

        if (int(type) != 1 and int(type) != 2):
            return "Не правильно введено номер теста хы"

        if (right_ans != ans1) and (right_ans != ans2) and (right_ans != ans3) and (right_ans != ans4):
            return "Ошибка, правильный ответ не сопадает ни с одним из вариаетов ответа"

        if (password == PASSWORD):
            if (int(type) == 1):
                obnov_vop = Beginner.query.filter_by(id=n_vopros).first()
                print(obnov_vop)
                if obnov_vop == None:
                    return "Вопроса под таким номером не существует"
                try:
                    obnov_vop.question = vopros
                    obnov_vop.var1 = ans1
                    obnov_vop.var2 = ans2
                    obnov_vop.var3 = ans3
                    obnov_vop.var4 = ans4
                    obnov_vop.right_answer = right_ans
                    db.session.commit()
                    db.session.commit()
                    return redirect('/')
                except:
                    return "Ошибка"

            if (int(type) == 2):
                obnov_vop = Experienced.query.filter_by(id=n_vopros).first()
                if obnov_vop == None:
                    return "Вопроса под таким номером не существует"
                try:
                    obnov_vop.question = vopros
                    obnov_vop.var1 = ans1
                    obnov_vop.var2 = ans2
                    obnov_vop.var3 = ans3
                    obnov_vop.var4 = ans4
                    obnov_vop.right_answer = right_ans
                    db.session.commit()
                    db.session.commit()
                    return redirect('/')
                except:
                    return "Ошибка"

            if (int(type) != 1 or int(type) == 2):
                return "Не правильно введен номер теста"
        else:
            return "У вас нет прав для внесения изменений в БД"
    else:
        return render_template('obnov_vopr_test1.html')









@app.route('/vvod_vopr_db_t3', methods=['POST', 'GET'])
def vvod_vopr_t3():
    PASSWORD = '11111'
    if request.method == "POST":
        vopros = request.form['vopros']
        right_ans = request.form['right_ans']
        right_ans_nig = right_ans.lower()
        password = request.form['password']
        kol = db.session.query(db.func.max(Professional.id)).first()[0]
        if kol != None:
            if kol >= 10:
                db.session.commit()
                return "Количество вопросов в тесте максимально, для добавления нового вопроса нужно обновить другой вопрос."

        if (password == PASSWORD):
            item = Professional(question=vopros, right_answer=right_ans_nig)
            try:
                db.session.add(item)
                db.session.commit()
                return redirect('/vvod_vopr_db_t3')
            except:
                return "Ошибка"
        else:
            return "У вас нет прав для внесения изменений в БД"
    else:
        return render_template('vvod_vopr_test3.html')



@app.route('/obnov_vopr_db_t3', methods=['POST', 'GET'])
def obnov_vopr_t3():
    PASSWORD = '11111'
    if request.method == "POST":
        n_vopros = request.form['n_vopros']
        vopros = request.form['vopros']
        right_ans = request.form['right_ans']
        right_ans_nig = right_ans.lower()
        password = request.form['password']

        if (password == PASSWORD):
            obnov_vop = Professional.query.filter_by(id=n_vopros).first()
            if obnov_vop == None:
                return "Вопроса под таким номером не существует"
            try:
                obnov_vop.question = vopros
                obnov_vop.right_answer = right_ans_nig
                db.session.commit()
                db.session.commit()
                return redirect('/')
            except:
                return "Ошибка"
        else:
            return "У вас нет прав для внесения изменений в БД"
    else:
        return render_template('obnov_vopr_test3.html')


# Функция для добавления данных в базу
def AddAndCommitData(listTickets):
    for ticket in listTickets:
        db.session.add(ticket)
        db.session.commit()
    print("Билет добавлен 10")

if __name__ == "__main__":
    app.run(debug=True)
