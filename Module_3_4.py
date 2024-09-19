def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        b = root_word.lower()
        a = other_words[i].lower()
        if b in a or a in b:
            same_words.append(a)
    return (same_words)


rezult1 = single_root_words('лУг', 'лУга', 'луговОй', "пенный", "душистый", 'луГовый')
rezult2 = single_root_words('Шаг', 'ШагоМер', 'шаговой', "идущий", "Стремительный", 'Быстрый')
print(rezult1)
print(rezult2)