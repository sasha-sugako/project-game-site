from flask import Flask
from data import db_session
from data import __all_models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
first = First_page()
first.kol_vo = 5
first.tema_vopr = 'Фильмы'
session = db_session.create_session()
session.add(first)
session.commit()
first = First_page()
first.kol_vo = 5
first.tema_vopr = 'Книги'
session = db_session.create_session()
session.add(first)
session.commit()
first = First_page()
first.kol_vo = 5
first.tema_vopr = 'Фауна'
session = db_session.create_session()
session.add(first)
session.commit()
first = First_page()
first.kol_vo = 5
first.tema_vopr = 'Еда'
session = db_session.create_session()
session.add(first)
session.commit()
first = First_page()
first.kol_vo = 5
first.tema_vopr = 'Солянка'
session = db_session.create_session()
session.add(first)
session.commit()
second = Second_page()
second.title = '''Какого ученого звания неожиданно для себя удостоился скромный
                  директор детского сада, он же «джентльмен удачи»?'''
second.otve = 'доцент'
second.kol_isp = 0
second.vopr_id = 1
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = 'В какой известной всему миру роли Шона Коннери сменил его молодой коллега Пирс Броснан?'
second.otve = 'бонд'
second.kol_isp = 0
second.vopr_id = 1
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = 'В каком городе Европы проводится самый престижный кинофестиваль?'
second.otve = 'канны'
second.kol_isp = 0
second.vopr_id = 1
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = 'Назовите имя и фамилию американского актера — исполнителя ролей Индианы Джонса в серии фильмов.'
second.otve = 'харрисон форд'
second.kol_isp = 0
second.vopr_id = 1
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = 'Кто сыграл знаменитого на весь мир боксера по имени Рокки?'
second.otve = 'сталоне'
second.kol_isp = 0
second.vopr_id = 1
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = 'Кто из героев русской литературы был хлебобулочным изделием?'
second.otve = 'колобок'
second.kol_isp = 0
second.vopr_id = 2
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Назовите героиню французской сказки, которая занималась 
                  неквалифицированным трудом, чистила печки, убиралась в доме.'''
second.otve = 'золушка'
second.kol_isp = 0
second.vopr_id = 2
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Какой вид энергии использовала баба яга, летая в ступе?'''
second.otve = 'нечистая сила'
second.kol_isp = 0
second.vopr_id = 2
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Назовите героя известной сказки русского поэта, который в конце получает 
                  черепно-мозговую травму,теряет дар речи и сходит с ума?'''
second.otve = 'поп'
second.kol_isp = 0
second.vopr_id = 2
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Кому Гамлет говорит следующую фразу: «Нет в Датском королевстве подлеца, который не был бы отпетым плутом»?'''
second.otve = 'горацио'
second.kol_isp = 0
second.vopr_id = 2
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = 'Эти животные, в отличие от других хищников, питаются не только мясом: они едят траву и ягоды.'
second.otve = 'медвед'
second.kol_isp = 0
second.vopr_id = 3
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Этих млекопитающих (не собак) приручили индийские магараджи, персидские шахи, турецкие султаны, арабские шейхи, эфиопские императоры к охоте на других животных.'''
second.otve = 'гепард'
second.kol_isp = 0
second.vopr_id = 3
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Какая птица является национальным символом США и изображен на гербе этой страны?'''
second.otve = 'орлан'
second.kol_isp = 0
second.vopr_id = 3
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Самый быстрый летун среди насекомых.'''
second.otve = 'стрекоз'
second.kol_isp = 0
second.vopr_id = 3
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''У этого крупного животного (до 2,5 метров ростом) детеныш рождается длиной всего три сантиметра.'''
second.otve = 'кенгуру'
second.kol_isp = 0
second.vopr_id = 3
session = db_session.create_session()
session.add(second)
session.commit()

second = Second_page()
second.title = 'Название какого фрукта с латинского языка буквально переводится «зернистый»?'
second.otve = 'гранат'
second.kol_isp = 0
second.vopr_id = 4
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Название какого овоща в греческом языке означает «неспелый, незрелый»? '''
second.otve = 'огурец'
second.kol_isp = 0
second.vopr_id = 4
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''ечина»?'''
second.otve = 'суфле'Название какого блюда из творога, в который вводят взбитые в густую пену яичные белки, во французском языке имеет еще и значение «пощ
second.kol_isp = 0
second.vopr_id = 4
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Название какого блюда образовано от удмуртских слов «ухо» и «хлеб»? '''
second.otve = 'пелмен'
second.kol_isp = 0
second.vopr_id = 4
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Название какого мясного блюда в переводе с немецкого означает как «обрезок бумаги, стружка»?'''
second.otve = 'шницел'
second.kol_isp = 0
second.vopr_id = 4
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''В 1994 году увидела свет «Энциклопедия экстремальных ситуаций». В статьи на букву «К» входят, например, 
                  «Кораблекрушение» и «Конец света», на букву «Ш» — «Шаровая молния». 
                  Назовите единственную статью на «Э».'''
second.otve = 'экзамен'
second.kol_isp = 0
second.vopr_id = 5
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''В 2011 году на спектакле в лондонском театре Barbican зрителям вместо кресел предлагались кровати, 
                  а завершалась программа утренним завтраком. Как назывался спектакль?'''
second.otve = 'колыбельная'
second.kol_isp = 0
second.vopr_id = 5
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''В карельской сказке волшебный жернов мог намолоть все, что захочешь. Оправляясь рыбачить, богач 
                  взял жернов и велел намолоть этого, да побольше. От тяжести лодка утонула, 
                  но жернов и на дне моря продолжал молоть. Что же?'''
second.otve = 'соль'
second.kol_isp = 0
second.vopr_id = 5
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''В литовском поселке Нида экспонируются эти предметы — символы Куршской косы. 
                  Некогда они могли поведать, сколько у хозяина домов, скота, детей.'''
second.otve = 'флюгер'
second.kol_isp = 0
second.vopr_id = 5
session = db_session.create_session()
session.add(second)
session.commit()
second = Second_page()
second.title = '''Рафаэль заломил за фреску 1 000 золотых; недовольный заказчик выбрал третейским судьей Микеланджело, 
                  зная о соперничестве художников. Микеланджело осмотрел работу и вынес этот вердикт.'''
second.otve = 'мало'
second.kol_isp = 0
second.vopr_id = 5
session = db_session.create_session()
session.add(second)
session.commit()


def main():
    db_session.global_init("db/game.sqlite")
    app.run()


if __name__ == '__main__':
    main()