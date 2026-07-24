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

    return
