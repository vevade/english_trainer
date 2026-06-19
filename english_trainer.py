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
"drifting_apart": "уверять",
"banter": "шутка",
"knock_it_off": "прекратить",
"celestial": "небесный",


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
