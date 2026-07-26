# day3.rpy

# Подвал товары база данных
init python:
    # Список товаров в подвале: (Название, Системное_имя, Цена)
    basement_products = [
        ("Фонарик", "flashlight", 5),
        ("Батарейка", "battery", 8),
        ("Старая книга", "old_book", 500),
        ("Солёные огурчики", "pickled", 43),
        ("Отмычка", "lockpick", 34)
    ]

# Интерфейс магазина

screen basement_shop():
    tag menu
    modal True  # Блокирует интерфейс под меню

    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        vbox:
            spacing 20

            # Шапка магазина
            text "Подвальная лавка" size 30 xalign 0.5
            text "Ваши деньги: [flp] flp." size 20 xalign 0.5

            null height 10

            # Список товаров
            vbox:
                spacing 10
                for name, item_id, price in basement_products:
                    hbox:
                        spacing 30
                        text "[name] — [price] flp." yalign 0.5 minwidth 250

                        # Кнопка покупки: активна, только если хватает денег
                        textbutton "Купить":
                            yalign 0.5
                            action [
                                SetVariable("flp", flp - price),
                                Function(inventory.append, item_id)
                            ]
                            sensitive flp >= price  # Кнопка гаснет, если денег мало

            null height 20

            # Кнопка выхода из подвала
            textbutton "Выйти из подвала":
                xalign 0.5
                action Return() # Возвращает управление в игровой скрипт
# home3
label home3:
    scene home

    t "Доброе утро!"

    p "Доброе утро!"

    s "Доброе утро!"

    show t surp

    t "Сегодня мы пойдём к колодцу!"

    show v normal at left

    v "Зачем?"

    t "Мы так узнаем истину"

    scene basement

    show v normal at left

    show s normal at right

    show t surp at center

    t "Пойдём!"

    s "А как мы узнаем правду?"

    t "В колодце лежит старая запись"

    menu:
        "Поддержать Вику":
            v "Спасибо! Я тебе дам ключ от подвала!"
            $ inventory.append("Ключ от подвала")
            "Теперь в сумке: [inventory]"
        "Поддержать Сашу":
            $ strange += 1
            s "Спасибо!"
            s "Вот тебе 13 флоппакоина!"

            $ flp = 87

            s "И ещё 2000!"

            $ gold += 2000

            t "Хотите что то приобрети?"

    call screen basement_shop

    if "pickled" in inventory:
        $ strange += 1

    " У вас есть: [inventory] вы близки к [strange]"

    t "Пойдём к старому колодцу!"

    p "Как?"

    v "Всё очень просто!"

    t "Надо использовать ключ"

    v "Ключ!"

    "Вы использовали ключ"

    scene coll

    show t normal at left

    show s normal at right

    show v normal at center

    t "Но вот старый колодец"

    v "Саша набери воду из колодца"

    s "Хорошо"

    "Саша набирает воду из колодца"

    s "Я поднял ведро"

    s "Тут старый ключ"

    t "Видишь?"

    p "Дай мне!"

    $ inventory.append("Старый ключ")

    v "Этот ключ от чего?"

    t "От сарая"

    s "Предлагаю поехать в Ефремов!"

    t "Злое Вельяминово"

    p "Что?"

    t "Поедем"

    a "Надо кушать!"

    s "Обед"

    scene home

    "Вы покушали"

    menu:
        "Погладить кошку":
            $ strange += 1
        "Погладить оленя":
            jump home3
    scene volkswagen1

    show t normal at left

    show s normal at right

    show v normal at center

    "В путь"
    $ text = "Вечер"

    show text "{size=80}{color=#fff}[text]{/color}{/size}" at truecenter

    "Злое Вельяминово/ Новое Вельяминово"
    hide text "{size=80}{color=#fff}[text]{/color}{/size}" at truecenter

    s "Я проснулся"

    stop music

    play music "p.mp3" fadein 1.0

    t "Мы едим"

    p "Зачем?"

    t "В Злом Вельяминово есть речка"

    s "Речка?"

    t "Слушайте"

    t "В Злом Вельяминово есть речка"

    t "Там сейчас чёрная вода"

    t "Там плавал один мужик"

    t "Он пропал"

    p "Странно"

    s "И что делать?"

    t "Есть там сарай"

    t "Его надо открыть ключом"

    vpr "Мы скоро приедем! Закрывайте окна!"

    scene volkswagen2

    show t normal at left

    show s normal at right

    show v normal at center

    p "Тихо!"

    v "Почему мы так долго?"

    vpr "Остановка. Деревня золото и комары"

    "Вы вышли на остановку и пришли обратно"

    vpr "Продолжаем путь"

    menu:
        "Съесть огурцы":
            $ strange += 1
            if "pickled" in inventory:
                "У вас есть [inventory]"
                $ inventory.remove("pickled")
                "Вы вкусно поели"
            else:
                "У вас нету огурцов"
        "Не есть":
            "Почему?"

    "Теперь пора сделать финальный выбор"

    menu:
        "Всех спасти":
            $ persistent.game_over_forever = True
            "Все будут жить, а ты нет"
            $ renpy.save_persistent()
            a "Пока!"
            $ renpy.quit()
        "Никого не спасти, но узнать истину":
            $ strange += 1
            "Продолжай"
    "Выбор сделан"

    vpr "Остановка!"

    scene black

    s "Мы дома"

    v "Почему?"

    t "Я не знаю"

    show t normal at left

    show s normal at right

    show v normal at center
    
    t "Давайте поужинаем и ляжем спать"

    s "Давайте!"

    "Вы поужинали"

    "Проверим"

    label vika:
        scene black

        show v normal

        "Ну зачем?"

        jump vika

    if velyminovo == True:
        "Похоже ты выбрал Новое Вельяминово"
        jump velyminovoend
    else:
        "Вы ложитесь спать"
        jump day4
    return
label velyminovoend:
    scene vhome

    "Выходи"


    "Новое Вельяминово?"

    $ main_menu = True
    $ persistent.velyminovoend = True

    "А теперь зайди в меню"

    "Зайди в меню! Нажми внизу кнопку меню! Или она мое называться опции"

    "Ты не можешь отступить"

# day4
screen resources_hud():
    layer "screens"

    # Используем фрейм в верхнем правом углу
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        background None

        # vbox (vertical box) расставит строки строго друг под другом
        vbox:
            spacing 10 # Расстояние между строкой электричества и газа

            # Строка электричества
            text "Электричество: [electricity]%" size 24 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]

            # Строка газа
            text "Газ: [gaz_v]%" size 24 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]

            # Строка воды

            text "Вода: [water] л" size 24 color "#ffffff" outlines [ (2, "#000000", 0, 0) ]

label day4:
    scene home

    t "Доброе утро!"

    t "У нас из под крана вода чёрная"

    t "Газа и электричества нету"

    show t normal at center

    show s normal at left

    show v normal at right

    s "И как мы жить будем?"

    t "У нас есть дизель"

    t "А также аккамулятор"


    "Теперь вверху видно оставшееся электричество и газ"

    show screen resources_hud

    v "Надо завтракать!"

    "Вы позавтракали"

    s "А у нас сколько воды?"

    $ water -= 1

    p "34 литров"

    v "Воду надо эконопить"

    t "Пойдёмте в подвал!"

    stop music

    scene black

    play sound "audio/footsteps.ogg"

    $ renpy.pause(6.0, hard=True)

    stop sound fadeout 1.0

    scene basement1

    s "Тут холодно"

    menu:
        "Уничтожить этот мир, но спасти Вику":
            "Выбор"
            python:
                # Получаем список кортежей всех сохранений
                for save_info in renpy.list_saved_games():
                    # Извлекаем имя слота (первый элемент кортежа)
                    slot_name = save_info[0]
                    # Удаляем сохранение по имени слота
                    renpy.unlink_save(slot_name)
            $ persistent.vikas = True
            $ renpy.save_persistent()
            $ renpy.quit()

        "Узнать истину":
            $ strange += 1
            "Истина близко"

    t "Вот подвал! Сейчас мы придём к Тёте Любе"

    s "Она нас в подвале заперла"

    p "Она сейчас вроде бы в автолавке"