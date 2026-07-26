# Инициализируем переменную блокировки (по умолчанию False)
default persistent.game_over_forever = False
default persistent.velyminovoend = False
default persistent.vika = False

# Проверка
init python:
    # persistent.velyminovoend = False
    # persistent.game_over_forever = False
    if persistent.game_over_forever:
        renpy.exports.quit()
    if persistent.velyminovoend:
        print("error")
        renpy.exports.quit()


# Вы можете расположить сценарий своей игры в этом файле.
default gold = 11500
default strange = 0
default inventory = []
default velyminovo = False
default flp = 0
default text = "Нету"
default fan = 0
default electricity = 100
default gaz_v = 100
default water = 35
default time = "6:00"
default temper = 0

# Определение персонажей игры.
define o = Character('ОП', color="#c8ffc8")
define s = Character('Sasha', color="#1e88e5")
define t = Character('ТП', color="#228B22")
define k = Character('Kатя', color="#FF0000")
define sh = Character('Шурик', color="#228B22")
define a = Character('Все', color="#228B22")
define v = Character('Vика', color="#ff591f")
define p = Character("[name]")
define c = Character("Продавец")
define sy = Character("Подвал")
define d = Character("Денис", color="#ff7f00")
define vpr = Character("?", color="#ff7f00")

# Определение товаров (Имя, Цена, Описание)
init python:
    class Item:
        def __init__(self, name, price, description):
            self.name = name
            self.price = price
            self.description = description

    # Создаем базу данных товаров
    item_sword = Item("Меч", 350, "Острый стальной меч.")
    item_potion = Item("Зелье", 239, "Зачем?.")
    item_potion = Item("Вода", 56, "Водичка для странности")
    item_shield = Item("Весёлая игра", 1000, "Жаль что Саша может сделать только весёлою игру, а психологичесий хоррор никому не нужен")
# Магазин
screen shop_screen():
    tag menu
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        padding (20, 20)

        vbox:
            spacing 15

            # Шапка магазина
            hbox:
                xfill True
                text "Магазин" size 30
                text "Золото: [gold]" size 25 xalign 1.0

            null height 10

            # Список товаров
            viewport:
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 10

                    use shop_item(item_sword)
                    use shop_item(item_potion)
                    use shop_item(item_shield)

            null height 20

            # Кнопка выхода (ИСКЛЮЧИТЕЛЬНО Return)
            textbutton "Выйти из магазина":
                xalign 0.5
                action Return()

screen shop_item(current_item):
    hbox:
        xfill True
        vbox:
            text "[current_item.name]" size 20
            text "[current_item.description]" size 14 color "#aaa"

        textbutton "[current_item.price] золота":
            xalign 1.0
            yalign 0.5
            sensitive gold >= current_item.price
            # Убран Show(), добавлен Hide() перед действием, если нужно,
            # но для обновления данных в Ren'Py достаточно просто изменить переменные
            action [
                SetVariable("gold", gold - current_item.price),
                Function(inventory.append, current_item.name)
            ]


# Вместо использования оператора image можете просто
image o normal = "images/op.png"
image o no = "images/opno.png"
image s normal = "images/sasha.png"
image s surp = "images/sashasurp.png"
image t normal = "images/tp.png"
image v normal = "images/v.png"
image p normal = "images/p.png"
image k normal = "images/k.png"
image c normal = "images/c.png"
image t surp = "images/tpsurp.png"
image c surp = "images/csurp.png"
image d normal = "images/d.png"
image sh normal = "images/sh.png"
image sh surp = "images/shsurp.png"
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene screen

    if persistent.vikas:
        v "Зачем?"
        jump vika

    s "Ну всё мы приехали"

    $ fan = renpy.random.randint(1, 10)

    show o normal

    o "Здравствуйте!"

    s "Привет!"

    o "Помнишь? В 2025 году в Лобанове была чёрная вода"

    s "Да"

    $ name = renpy.input("Введите ваше имя:", length=12)

    p "Ну что? Пойдём!"

    s "Куда?"

    p "В магазин"

    o "Идите! Вот тебе саша 500 рублей!"

    s "Спасибо!"

    jump shop1



    return
label shop1:
    scene auto

    p "Мы в магазине!"

    call screen shop_screen

    p "Я надеюсь ты купил что то полезное"

    "[inventory]"

    if "Вода" in inventory:
        $ strange += 1
    else:
        "Всё будет хорошо"

    p "[strange]"

    p "Пойдём"

    s "ТП говрит что в Лобанове начили люди пропадать"

    p "Я знаю"

    s "Капец визуальные как там"

    s "новеллы"

    s "очень скучные."

    p "Игроки не хотят книги читать"

    p "У тебя истина [strange]"

    s "Я уже в эти игры играл"

    p "Я всех спасу"

    s "Сколько?"

    p "Только себя"

    s "Понятно"

    scene yard

    show o normal at center

    show s normal at left

    p "Здравствуйте!"

    o "Здравствуйте!"

    p "В Лобанове люди начали пропадать!"

    s "Мы поедем в Лобаново"

    o "Я поехала на автобусе!"

    hide o normal

    s "Мы тоже давай поедем!"

    p "Нужны билеты"

    s "У меня есть"

    p "Ну ладно"

    scene volkswagen

    c "Вы тоже тут?"

    p "Да"

    s "Мы едем в Лобаново"

    show c surp
    jump velyminovo