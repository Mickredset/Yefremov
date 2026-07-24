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

    return
