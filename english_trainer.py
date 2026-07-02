import random

words = {
"indeed": "действительно",
"sufficient": "достаточный",
"roll_out": "вставать",
"flair": "талант",
"sincere": "искренний",
"assure": "уверять",
"have_a_poke_around": "осмотреться",
"intimidating": "пугающий",
"malicious": "вредоносный",
"overstimulated": "перегруженный",
"drifting_apart": "отдаляться",
"banter": "шутка",
"knock_it_off": "прекратить",
"celestial": "небесный",
"strive": "стремиться",
"bestow_upon": "одарить",
"mischievous": "шаловливый",
"point_out": "показать",
"catch_up": "узнать_новости",
"hit_different": "ощущаться_иначе",
"go-to": "лучший",    
"low-key": "немного",
"enervate": "изнурять",
"spellbinding": "завораживающий",
"vibrant": "яркий",
"reciprocate": "отвечать_взаимно",
"jump_to_conclusions": "спешить_с_выводами",
"on_and_off": "время_от_времени",
"ballpark_figure": "приблизительная_цифра",
"level_playing_field": "равные_условия",    
"from_the_ground_up": "с_нуля",
"talk_turkey": "перейти_к_делу",
"beat_around_the_bush": "ходить_вокруг_да_около",
"inner_turmoil": "внутреннее_напряжение", 
"call_it_a_day": "закончить_на_сегодня",
"nevertheless": "тем_не_менее",
"whereas": "тогда_как",
"ultimately": "в_итоге",    
    
    
}

while True:
    english_word = random.choice(list(words.keys()))
    translate = input(f"Переведи слово: {english_word}\n")

    if translate.lower() == "exit":
        print("Выход из тренировки")
        break

    if translate.strip().lower() == words[english_word]:
        print("Молодец огурец")
    else:
        print(f"Неправильно. Правильный ответ: {words[english_word]}")
