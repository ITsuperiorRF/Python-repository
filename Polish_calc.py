# Проверка правильности ввода отсутствует (нет проверки от дурака)

def calc(obj):
    # Общая функция для работы с другими функциями
    def DoingFuncOperation(func, x, y): return func(x, y)
    # Функции для посчета
    def plus(x, y): return x + y
    def minus(x, y): return x - y
    def mult(x, y): return x * y
    def div(x, y): return x / y
    def degree(x, y): return x**y
    # Обращение к функциям через словарь
    d = {"+": plus, "-": minus, "*": mult, "/": div, "^": degree}
    resp = []
    # Добавление элементов в список для посчета
    for i in obj:
        if i in "1234567890":
            resp.append(i)
        # Если в список добавляется знак, то начинается подсчет
        elif i in "+-*/^":
            resp.append(i)
            resp.append(DoingFuncOperation(d[i], int(resp[resp.index(i) - 2]), int(resp[resp.index(i) - 1])))
            # Удаление "старых элементов" с которыми уже был произведен подсчет
            del resp[resp.index(i) - 2]
            del resp[resp.index(i) - 1]
            del resp[resp.index(i)]
    # возвращение вещественного числа (во избежание ошибок с целыми числами при делении)
    print(float(*resp))

inputObj = list(input("Введите ваш пример:\n"))
calc(inputObj)