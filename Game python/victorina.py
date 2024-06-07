print(" Добро пожаловать на Викторину")
questions = [
    {
        "question": "Сколько планет в Солнечной системе?",
        "options": ["8", "9", "10", "11"],
        "answer": "8"
    },
    {
        "question": "Какая планета имеет кольца в Солнечной системе?",
        "options": ["Марс", "Юпитер", "Венера", "Сатурн"],
        "answer": "Сатурн"
    },
    {
        "question": "Как называется спутник Земли?",
        "options": ["Луна", "Марс", "Венера", "Юпитер"],
        "answer": "Луна"
    },
    {
        "question": "Какова продолжительность жизни стрекозы?",
        "options": ["24 часа", "12 лет", "6 минут", "1 год"],
        "answer": "24 часа"
    },
    {
        "question": "Сколько игроков в олимпийской команде по керлингу?",
        "options": ["3", "7", "4", "5"],
        "answer": "24 часа"
    },
    {
        "question": "Сколько сердец у Осьминога?",
        "options": ["7", "1", "5", "3"],
        "answer": "24 часа"
    },
    {
        "question": "Кто изобрел искусственные газированные напитки??",
        "options": ["Луи Пастер", "Джозеф Пристли", "Нильс Бор", "Генрих Рудольф"],
        "answer": "Джозеф Пристли"
    },
    {
        "question": "Сколько подсолнухов было в третьей версии картины Ван Гога «Подсолнухи»?",
        "options": ["12", "15", "6", "22"],
        "answer": "12"
    },
    {
        "question": "Конец Первой мировой войны?",
        "options": ["Конец Первой мировой войны - 1917 г.", "Конец Первой мировой войны - 1916 г.", "Конец Первой мировой войны - 1919 г.", "Конец Первой мировой войны - 1918 г."],
        "answer": "Конец Первой мировой войны - 1918 г."
    },
    {
        "question": "Самый лучший язык программирования?",
        "options": ["Python", "Ryby", "Java", "C++"],
        "answer": "Python"
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Введите номер правильного ответа: ")
    if question["options"][int(answer)-1] == question["answer"]:
        print("Правильно!")
        return True
    else:
        print("Неправильно!")
        return False

def play_quiz(questions):
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    print(f"Вы набрали {score} из {len(questions)} возможных баллов.")

play_quiz(questions)