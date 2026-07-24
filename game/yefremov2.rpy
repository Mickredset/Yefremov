# yefremov2.rpy

label yefremov2:
    scene volkswagen
    show s normal at center
    show v normal at left
    v "Мы едем в город"

    s "Куда?"

    p "Тёте Любе!"

    menu:
        "Дать Саше 1000 рублей":
            s "Спасибо"
            $ gold -= 1000
        "Дать метафору":
            $ strange += 1
    if strange == 7:
        s "У меня нога прошла"
    else:
        "Хаахахахахахаахахахаххаа"

    scene yefremov2
    show c normal at center

    p "Мы у тёти Любы"

    c "Что вам нужно?"
    show s normal at left

    menu:
        "Чёрная вода":
            c "Злой дух девушки загрезняет воду"
        "Ночь в Лобанове":
            c "Лобаново это проклятое место. Там мог работать МТС, но волны не доходят"
        "Подвал":
            $ strange += 1
            c "Подвал! В подвале есть старый колодец! Я знаю. В том подваале находятся деньги!"
    menu:
        "Обмен рублей на FLP":
            c "Хорошо!"
            $ flp = gold/20
            $ gold = 15
            $ strange += 1
            "[strange]"
    "У тебя [gold] денег и [flp] денег"
    c "Идите в подвал!"
    s "Хорошо"
    jump basement
    return
label basement:
    show basement
    hide yefremov2
    hide c normal
    c "Пока!"

    c "Сидите в подвале!"

    s "Нет!"

    p "Саша разве ты не знал?"

    s "О чём?"

    p "Сейчас мы сделаем некоторые дейтсвия и поднимимся на верх"

    s "Вверху дверь заперта"

    p "Та дверь теперь будет от Лобаново"

    "У вас есть: [inventory]"

    s "Алина! Я даю тебе расширенный ключ для подвала"

    $ inventory.append("Расширенный ключ")

    menu:
        "Ефремов":
            jump start
        "Лобаново":
            $ strange += 1
            jump home2
        "Новое Вельяминово":
            jump velyminovo
label home2:
    show text "{size=80}{color=#fff}ВЕЧЕР{/color}{/size}" at truecenter
    scene home
    show t surp
    t "Здравствуйте!"

    play music "leto.mp3"

    t "Бесконечная ночь прошла!"

    t "Наступил вечер"

    t "Идите кушать домой"

    "Вы поели"

    v "Алина! Спокойного вечера!"

    p "Спасибо!"

    show s normal at left

    s "А что ночью будет?"

    t "Вылезут из под земли люди"

    s "Какие люди?"

    t "Которые выпили воды из скважины!"

    sy "Думать вы чёрный вода пить"

    t "Они уже вылезают"

    scene yard1

    show d at right

    d "Здравствуйте!"

    t "Ты слышал?"

    d "Я слыхал"

    d "Надо решать проблему"

    menu:
        "Я люблю Volkswagen":
            jump cat
        "Надо есть":
            $ strange += 1
            jump home3
label cat:
    scene black
    "Похоже тут никого нету"