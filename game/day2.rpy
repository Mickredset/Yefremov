# day2.rpy

label day2:
    sh "Похоже мы приехали!"

    p "Саша! Пойдём"

    scene yard

    show v normal at center

    show t normal at left

    show s normal at right

    p "Привет! Вика"

    scene home1

    t "Было же светло!"

    v "Когда мы уже поедем?"

    p "Я и Саша приехали к вам на маршрутке"

    t "Перед всем этим у нас в колонке вода стала горячей"

    hide v normal

    show k normal

    k "Здравствуйте!"

    menu:
        "Пойти домой":
            "Моё тело моё дело"
        "Узнать про белочку":
            $ strange += 1
            k "Белочка!? Сама не знаю"
    scene dom

    show s normal

    if strange == 4:
        s "У меня нога болит"
    s "Как темно"

    # Показываем черный фон
    scene black

    show text "{size=80}{color=#fff}НОЧЬ{/color}{/size}" at truecenter

    with dissolve

    pause 3.0

    # Скрываем текст
    hide text
    with dissolve

    t "Наступила ночь!"
    k "Надо спать"

    "Вы ложитель спать"

    menu:
        "Истина":
            $ strange += 1
        "Спасение":
            "ХАахахахахаххахахахах"
    if strange == 5:
        "Нетутутутутуутутут"

    scene yard1

    s "Доброе утро!"

    p "Доброе!"

    v "Доброе утро Алина!"

    v "Не хочешли сыграть в крестики нолики?"

    p "Да!"

    "Ничья"

    p "Было классно!"

    v "Я приготовила еду"

    s "Я дошик съем"

    show t normal
    show v normal at center

    t "Утром светло, днём темно"

    "Вы поели"
    menu:
        "Выбрать странный путь":
            $ strange += 1
            "[strange]"
        "Выбрать путь Новое Вельяминово":
            $ velyminovo = True
        "Выбрать путь Лобаново":
            $ strange = 0
        "Выбрать путь Вики":
            "Это важно?"

    jump yefremov2
    return