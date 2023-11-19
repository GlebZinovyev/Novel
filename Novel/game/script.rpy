# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Себастиан', color="#f54242", image='sebostian')
define so = Character('Соня', color="#6342f5", image='soniy')
define h = Character('Хиро', color="#f58d42", image='hiro')
define v = Character('Доктор', color="#ebdb34", image='doc')
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
init:
    define count_test1 = 0
    $ left2 = Position(xalign=0.1, yalign=1.1)
    $ left3 = Position(xalign=0.4, yalign=1.1)
    $ right2 = Position(xalign=0.8, yalign=1.1)
# Игра начинается здесь:
label start:
    # ПЕРВАЯ СЦЕНА
    scene bg close
    "Урок математики. Себастиан спит."
    so "Себастиан вставай, там тест раздают."
    scene bg math class
    with fade
    show soniy angry
    with dissolve
    so "Себастиан вставай, там тест раздают."
    hide soniy with dissolve
    show sebostian calm
    with dissolve
    s "Оооааа, спять хочется"
    hide sebostian with dissolve
    "Себастиан моргнул и перед ним появился тест"
    scene bg math2
    with fade
    ""
    menu:
        "Поставьте знак 1/25  ?  1/96"

        "<":
            "Себастиан кринжанул со знаний игрока"
        "=":
            "Себастиан кринжанул со знаний игрока"
        ">":
            $ count_test1 = count_test1 + 1
    menu:
        "Треугольник ABC  вписан  вокружность  с  центром .O Угол BAC  равен 32 .Найдите угол BOC. Ответ дайте в градусах."

        "64":
            call caunt
        "32":
            "Себастиан кринжанул со знаний игрока"
        "16":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Решите 2+2*2=?"

        "8":
            "Себастиан кринжанул со знаний игрока"
        "6":
            call caunt
        "2":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Площадь боковой поверхности треугольной призмы равна 24. Через среднюю линию основания призмы проведена плоскость, параллельная боковому ребру. Найдите площадь боковой поверхности отсечённой треугольной призмы."

        "6":
            "Себастиан кринжанул со знаний игрока"
        "12":
            call caunt
        "9":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "В сборнике билетов по биологии всего 25 билетов. Только в двух билетах встречается вопрос о грибах. На экзамене выпускнику достаётся один случайно выбранный билет из этого сборника. Найдите вероятность того, что в этом билете будет вопрос о грибах."

        "0,04":
            "Себастиан кринжанул со знаний игрока"
        "0,08":
            call caunt
        "0,02":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Решите (2+2)*2=?"

        "8":
            call caunt
        "6":
            "Себастиан кринжанул со знаний игрока"
        "2":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Найдите корень уравнения 3^(x-5)=81"

        "7":
            "Себастиан кринжанул со знаний игрока"
        "6":
            "Себастиан кринжанул со знаний игрока"
        "9":
            call caunt
    menu:
        "Найдите корень уравнения x^2+x+1=0"

        "-1 и 1":
            "Себастиан кринжанул со знаний игрока"
        "-1":
            "Себастиан кринжанул со знаний игрока"
        "Нет решения":
            call caunt
    menu:
        "Симметричную игральную кость бросили 3 раза. Известно, что в сумме выпало 6 очков. Какова вероятность события «хотя бы раз выпало 3 очка»?"

        "0,6":
            call caunt
        "0,3":
            "Себастиан кринжанул со знаний игрока"
        "0,4":
            "Себастиан кринжанул со знаний игрока"
        "Решите (2+2)*2=?"

    menu:
        "Ничего":
            call caunt
        "Мяу":
            "Себастиан начинает мяукать и в шоке осознаёт, что коровы не мяукают"
        "Муууу":
            "Себастиан смутно догадывается, что коровы вообще не говорят, но изменить ответ уже поздно"
    "Себастиан решил тест и опять заснул."
    #hide bg test
    #with fade
    # ВТОРАЯ СЦЕНА
    scene bg park1
    with fade
    show hiro calm at left2
    show sebostian calm at right2
    "Себастиан и Хиро гуляют."
    if count_test1 <= 4:
        h happy "Слабенько, Себастиан, слабенько! Какие планы на будущее после такой оценки?"
        s angry "Эх, да у меня еще есть время поднажать. Может быть, в Урфу повезет?"
    elif 5 <= count_test1 <= 6:
        h happy "Ну, ты справился, Себастиан, но можно и лучше. Куда решил направить свои таланты?"
        s calm "Нужно подтянуться, это точно. Может быть, попробую в Урфу?"
    elif 7 <= count_test1 <= 8:
        h happy "Ну неплохо сдал, Себастиан, но тут еще есть куда прыгать! Какие планы на учебу?"
        s calm "Да, неплохо, но есть к чему стремиться. Думаю, попробую в Урфу."
    elif 9 <= count_test1 <= 10:
        h happy "Эх, Себастиан, ты просто бог математики! Куда мечтаешь попасть?"
        s happy "Что поделаешь, я просто гений! Думаю, в Урфу, наверное."
    hide hiro with dissolve
    hide sebostian with dissolve
    scene bg park2
    with fade
    show hiro calm at left2
    show sebostian calm at right2
    h calm "Хмм, Урфу же в Екатеринбурге, далековато"
    menu:
        "Есть такое":
            h happy "Ну в Екб вроде не плохо"
        "Ничего страшного":
            h happy "Ну в Екб вроде не плохо"
        "Терпимо":
            h happy "Ну в Екб вроде не плохо"
    h calm "А куда конкретнее хочешь поступить?"
    s calm "Хочу на программиста, они зарабатывают многа деняк и это ближе к моим интересам. Да еще и профессия перспективная!"
    hide hiro with dissolve
    hide sebostian with dissolve
    scene bg park3
    with fade
    show hiro calm at left2
    show sebostian calm at right2
    h happy "Многа деняг? хых"
    h angry "А я еще совсем не определился...."
    h calm "Может на строителя или нефтяника.."
    s calm "Не парся так,"
    s calm "Посмотри что тебе интереснее"
    h calm "Ну мне интересно как строят здания"
    h happy "Хотелось бы небоскрёб свой построить"
    s happy "А на нефтяника хочешь потому что они много зарабатывают?"
    h happy "Ага, кто бы не хотел быть богатым?"
    s calm "В каждой сфере можно заработать нормально"
    s calm "Так что я бы посоветовал идти на строителя"
    h calm "Ну да, мне это интереснее будет"
    h calm "Может мне тоже тогда в Урфу поступить?"
    s happy "Давай, будем вместе учиться!"
    hide hiro with dissolve
    hide sebostian with dissolve
    ""

    # ТРЕТЬЯ СЦЕНА
    scene bg corridor
    with fade
    "Перед входом в кабинет"
    show sebostian calm at right2
    show hiro calm at left2
    show soniy happy at left3

    s "Ух... страшно сдавать егэ"
    so "Не бойся мы готовились весь год, мы точно сдадим"
    h "На этом жизнь не останавливается, не волнуйся"
    scene bg ege
    with fade
    "Заходят в кабинет и пишут экзамен"
    scene bg school
    with fade
    show sebostian calm at right2
    show hiro calm at left2
    show soniy calm at left3

    if count_test1 <= 4:
        s angry "Я точно плохо сдал"
        so "Ну не унывай, возможно проходной будет"
        h "Да, там же не так трудно было"
    elif 5 <= count_test1 <= 6:
        s "Ну вроде пойдёт, но много ошибок"
        so "Ну хотя бы сдал, уже хорошо"
        h happy "Хехе, а я вот думаю, что первую часть всю правильно написал"
    elif 7 <= count_test1 <= 8:
        s "Почти всё сделал, последнее задание не успел"
        so "А ты смог параметр сделать?"
        s angry "Не, думаю в нём допустил ошибку"
    elif 9 <= count_test1 <= 10:
        s happy "Вообще всё изи было. Спина только болит."
        so "По мне так сложно было"
        s angry "Непростой вариант, вторая часть все гробы"

    scene bg room
    with fade
    "Дом Себастиана, получение результатов"
    show sebostian calm at left2
    if count_test1 <= 2:
        scene bg ege11
        with fade
        "Себастиан видит 11 баллов  и  разочарован"
        "GAME OVER, остался на второй год"
        return
    elif 3 <= count_test1 <= 6:
        scene bg ege66
        with fade
        "Себастиан видит 66 баллов егэ по математике  и радуется"
        s happy "Дворником что ли буду"
    elif 7 <= count_test1 <= 8:
        scene bg ege74
        with fade
        "Себастиан видит 74 баллов егэ по математике, расстроен что не 81"
        s happy "Да я мегамозг, жалко что не 81"
    elif 9 <= count_test1 <= 10:
        scene bg ege100
        with fade
        "Себастиан видит 100 баллов егэ по математике, без эмоций смотрит на монитор"
        s calm "Пфф, как это можно не сдать"
    # СЦЕНА 4
    scene bg apartment
    with fade
    show sebostian calm at left2
    show soniy calm at right2
    s happy "Привет Соня, давай проходи"
    so happy "Приветик"
    so happy "Эй, Себастиан, это так здорово, что мы идем в университет! Куда ты собираешься поступать?"
    menu:
        "Ага, действительно здорово!":
            s happy ""
        "здорово, но немного грустно покидать школу.":
            s calm ""
    scene bg room
    with fade
    show sebostian calm at left3
    show soniy calm at right2
    s calm "Я думаю о поступлении в Урфу. Это же самый крутой вуз на урале!"
    so happy "О, Урфу звучит интересно!"
    s calm "А ты, Соня, куда решила поступать?"
    so calm "Я выбрала МГУ. Хочу пожить в Москве. МГУ - топ один вуз в стране, оттуда точно дураком не выпустишься."
    s happy "Москва, да там будет весело."
    so angry "Но, Себастиан, это означает, что мы долго не будем видеться"
    s calm "Да, я об этом подумал. Но мы всегда можем оставаться на связи и приезжать друг к другу в гости, верно?"
    so happy "Конечно! Ничто не может разрушить нашу дружбу. Мы всегда будем поддерживать связь и делиться новостями."
    s happy "Точно, ничто не сможет нас разлучить, даже если мы будем далеко друг от друга."
    scene bg apartment
    with fade
    show sebostian calm at left2
    show soniy calm at right2
    so calm "Ну я пошла, пока пока"
    s calm "Пока"
    hide soniy with dissolve
    "Соня уходит домой"
    # СЦЕНА 5
    scene bg black
    with fade
    "Хиро пишет в вк Себастиану."
    scene bg vk
    with fade
    h "Ты  когда планируешь ехать отдавать документы?"
    menu:
        "Вот 10 августа собрание будет, тогда и отдам":
            h  "Оо я туда тоже хотел поехать, давай вместе"
            s "Оо, давай"
        "До конца августа время ещё есть, успею":
            h  "Там 10 августа собрание будет, давай может вместе поедем?"
            menu:
                "Оо, давай":
                    call out
                "Почему бы и нет":
                    call out
        "Ещё не думал даже когда":
            h  "Там 10 августа собрание будет, давай может вместе поедем?"
            menu:
                "Оо, давай":
                    call out
                "Почему бы и нет":
                    call out
    h "Ну решили тогда"
    scene bg car
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    s "У нас ещё много времени до собрания, давай сходим медкомиссию для общежития пройдём"
    h "Да, давай"
    scene bg hostel9
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    h happy "Ооо та самая 9 общага"
    s happy "Вау, хотел бы там жить"
    h calm "Да она одна из самых новых, там до нас почти никто не жил"
    scene bg hoste11
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    s happy "Оо а это 11 общага, там удобная скамейка рядом"
    h sad "Ну она постарее выглядит,  коридорного типа"
    s calm "Ну я скорее всего там буду, что бы в 9 попасть надо высокие баллы по егэ"
    h calm "Ну главное что бы в общежитие заселили, а то тут можно за 15 минут до пары проснуться и не опоздать"
    s happy "Хаха"
    scene bg outmed
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    "Себастиан и Хиро заходят в медсанчасть"
    scene bg inmed
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    "Себастиан и Хиро расходятся по разным кабинетам"
    scene bg inmedroom
    with fade
    show sebostian calm at left2
    show doc calm at right2
    s "Можно войти?"
    v "Да, заходи"
    v "Так Себастиан вы с Сургута, из 5469160029166829 школы"
    v happy "хм длинное название школы"
    menu:
        "Мне много кто так говорил":
            v "Так очень трудно запомнить"
            s happy "да чего там 5469160029166829"
        "Промолчать":
            call out
    "Проходит некоторое время"
    scene bg inmedroom
    with fade
    show sebostian calm at left2
    show doc calm at right2
    v "Так всё можете идти"
    s "Спасибо до свидание."
    scene bg outmed
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    h "Как-то проще чем я думал"
    menu:
        "Ага, я думал труднее будет":
            hide sebostian calm
            show sebostian happy at left2
            h "Так  вроде уже на собрание надо идти"
        "Согласен":
            h "Так  вроде уже на собрание надо идти"
    scene bg guk
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    "Входят в ГУК"
    scene bg inguk
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    "Идут в актовый зал"
    scene bg gukhall
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    "Проходит плодотворное собрание"
    scene bg inguk
    with fade
    show sebostian happy at left2
    show hiro calm at right2
    h happy "Какой там зал большой был"
    menu:
        "Так и само здание универа большое":
            call out
        "Так оно просто гиганское.":
            call out
    h "Пойдём отнесём может оригиналы документов?"
    s calm "Пойдём"
    scene bg documents
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    "Себастиан и Хиро отдают документы"
    scene bg guk
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    h "Так а теперь можно поехать домой или пойти гулять."
    menu:
        "Пойдём гулять":
            scene bg e1
            with fade
            show sebostian calm at left2
            show hiro calm at right2
            "Топ-Топ-Топ"
            scene bg e2
            with fade
            show sebostian calm at left2
            show hiro calm at right2
            "Топ-Топ-Топ"
            scene bg e3
            with fade
            show sebostian calm at left2
            show hiro calm at right2
            "Топ-Топ-Топ"
            s happy "Так а теперь пора и домой"
        "Поехали домой":
            call out
    scene bg carout
    with fade
    show sebostian calm at left2
    show hiro calm at right2
    scene bg caraction
    with fade
    # АРКА 2
    # СЦЕНА 1

label out:
    return

label caunt:
    $ count_test1 = count_test1 + 1
    return

# git remote add origin https://github.com/GlebZinovyev/Novel.git ls -al
# git remote add origin https://github.com/GlebZinovyev/Novel.git    git push -f origin main
# rm -rf .git
# rmdir .git git commit -m "Novel" git add . git commit -m "first arc"