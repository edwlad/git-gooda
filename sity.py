#! python3

import sys
# sys.stdin = open('test.txt', encoding='utf-8')

sity = {
    'а': ['абакан', 'азов', 'александров', 'алексин', 'альметьевск', 'анапа', 'ангарск', 'анжеро-судженск', 'апатиты',
          'арзамас', 'армавир', 'арсеньев', 'артем', 'архангельск', 'асбест', 'астрахань', 'ачинск'],
    'б': ['балаково', 'балахна', 'балашиха', 'балашов', 'барнаул', 'батайск', 'белгород', 'белебей', 'белово', 'белогорск',
          'белорецк', 'белореченск', 'бердск', 'березники', 'березовский', 'бийск', 'биробиджан', 'благовещенск', 'бор',
          'борисоглебск', 'боровичи', 'братск', 'брянск', 'бугульма', 'буденновск', 'бузулук', 'буйнакск'],
    'в': ['великие луки', 'великий новгород', 'верхняя пышма', 'видное', 'владивосток', 'владикавказ', 'владимир',
          'волгоград', 'волгодонск', 'волжск', 'волжский', 'вологда', 'вольск', 'воркута', 'воронеж', 'воскресенск',
          'воткинск', 'всеволожск', 'выборг', 'выкса', 'вязьма'],
    'г': ['гатчина', 'геленджик', 'георгиевск', 'глазов', 'горно-алтайск', 'грозный', 'губкин', 'гудермес', 'гуково',
          'гусь-хрустальный'],
    'д': ['дербент', 'дзержинск', 'димитровград', 'дмитров', 'долгопрудный', 'домодедово', 'донской', 'дубна'],
    'е': ['евпатория', 'егорьевск', 'ейск', 'екатеринбург', 'елабуга', 'елец', 'ессентуки'],
    'ж': ['железногорск', 'жигулевск', 'жуковский'],
    'з': ['заречный', 'зеленогорск', 'зеленодольск', 'златоуст'],
    'и': ['иваново', 'ивантеевка', 'ижевск', 'избербаш', 'иркутск', 'искитим', 'ишим', 'ишимбай'],
    'й': ['йошкар-ола'],
    'к': ['казань', 'калининград', 'калуга', 'каменск-уральский', 'каменск-шахтинский', 'камышин', 'канск', 'каспийск',
          'кемерово', 'керчь', 'кинешма', 'кириши', 'киров', 'кирово-чепецк', 'киселевск', 'кисловодск', 'клин', 'клинцы',
          'ковров', 'когалым', 'коломна', 'комсомольск-на-амуре', 'копейск', 'королев', 'кострома', 'котлас', 'красногорск',
          'краснодар', 'краснокаменск', 'краснокамск', 'краснотурьинск', 'красноярск', 'кропоткин', 'крымск', 'кстово',
          'кузнецк', 'кумертау', 'кунгур', 'курган', 'курск', 'кызыл'],
    'л': ['лабинск', 'лениногорск', 'ленинск-кузнецкий', 'лесосибирск', 'липецк', 'лиски', 'лобня', 'лысьва', 'лыткарино',
          'люберцы'],
    'м': ['магадан', 'магнитогорск', 'майкоп', 'махачкала', 'междуреченск', 'мелеуз', 'миасс', 'минеральные воды',
          'минусинск', 'михайловка', 'михайловск', 'мичуринск', 'москва', 'мурманск', 'муром', 'мытищи'],
    'н': ['набережные челны', 'назарово', 'назрань', 'нальчик', 'наро-фоминск', 'находка', 'невинномысск', 'нерюнгри',
          'нефтекамск', 'нефтеюганск', 'нижневартовск', 'нижнекамск', 'нижний новгород', 'нижний тагил', 'новоалтайск',
          'новокузнецк', 'новокуйбышевск', 'новомосковск', 'новороссийск', 'новосибирск', 'новотроицк', 'новоуральск',
          'новочебоксарск', 'новочеркасск', 'новошахтинск', 'новый уренгой', 'ногинск', 'норильск', 'ноябрьск', 'нягань'],
    'о': ['обнинск', 'одинцово', 'озерск', 'октябрьский', 'омск', 'орел', 'оренбург', 'орехово-зуево', 'орск'],
    'п': ['павлово', 'павловский посад', 'пенза', 'первоуральск', 'пермь', 'петрозаводск', 'петропавловск-камчатский',
          'подольск', 'полевской', 'прокопьевск', 'прохладный', 'псков', 'пушкино', 'пятигорск'],
    'р': ['раменское', 'ревда', 'реутов', 'ржев', 'рославль', 'россошь', 'ростов-на-дону', 'рубцовск', 'рыбинск', 'рязань'],
    'с': ['салават', 'сальск', 'самара', 'санкт-петербург', 'саранск', 'сарапул', 'саратов', 'саров', 'свободный',
          'севастополь', 'северодвинск', 'северск', 'сергиев посад', 'серов', 'серпухов', 'сертолово', 'сибай', 'симферополь',
          'славянск-на-кубани', 'смоленск', 'соликамск', 'солнечногорск', 'сосновый бор', 'сочи', 'ставрополь',
          'старый оскол', 'стерлитамак', 'ступино', 'сургут', 'сызрань', 'сыктывкар'],
    'т': ['таганрог', 'тамбов', 'тверь', 'тимашевск', 'тихвин', 'тихорецк', 'тобольск', 'тольятти', 'томск', 'троицк',
          'туапсе', 'туймазы', 'тула', 'тюмень'],
    'у': ['узловая', 'улан-удэ', 'ульяновск', 'урус-мартан', 'усолье-сибирское', 'уссурийск', 'усть-илимск', 'уфа', 'ухта'],
    'ф': ['феодосия', 'фрязино'],
    'х': ['хабаровск', 'ханты-мансийск', 'хасавюрт', 'химки'],
    'ч': ['чайковский', 'чапаевск', 'чебоксары', 'челябинск', 'черемхово', 'череповец', 'черкесск', 'черногорск', 'чехов',
          'чистополь', 'чита'],
    'ш': ['шадринск', 'шали', 'шахты', 'шуя'],
    'щ': ['щекино', 'щелково'],
    'э': ['электросталь', 'элиста', 'энгельс'],
    'ю': ['южно-сахалинск', 'юрга'],
    'я': ['якутск', 'ялта', 'ярославль']
}
if input('Как играем, с другом или с компьютером?\n') == 'С другом':
    gamer = [
        input('Введите имя первого игрока:\n'),
        input('Введите имя второго игрока:\n')
    ]
else:
    gamer = [input('Введите имя игрока:\n'), 'компьютер']
idx, err, last = 0, 0, ''
sity_ans = set()

while True:
    if gamer[idx] == '-компьютер':
        ans = sity[last][0]
    else:
        ans = sys.stdin.readline().strip().lower()

    if not ans:
        print(f'Победил {gamer[(idx + 1) % 2]}.')
        break
    elif last == '':
        if ans not in sity.get(ans[0], []):
            print('Неверный город')
            continue
        last = ans[0]

    if ans in sity_ans:
        print('Уже назвали')
        err += 1
    elif last != ans[0] or ans not in sity.get(last, []):
        print('Неверный город')
        err += 1
    else:
        sity_ans.add(ans)
        sity[last].remove(ans)
        err = 0
        last = (ans[-2] if ans[-1] in 'цыь' else ans[-1])

    if err > 3:
        print(f'Победил {gamer[(idx + 1) % 2]}.')
        break
    elif len(sity.get(last, [])) == 0:
        print(f'Победил {gamer[idx]}.')
        break
    elif err == 0:
        idx = (idx + 1) % 2
