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

    return
