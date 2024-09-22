class WordsFinder:
    def __init__(self, *file_names: list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                puncts = [',', '.', '=', '!', '?', ';', ':', ' - ']
                words = []
                for line in file:
                    line = line.lower()
                    for p in puncts:
                        line = line.replace(p, "")
                    words.extend(line.split())
                    # print(line)
                    all_words[file_name] = words
            return all_words

    def find(self, word):
        dict1 = {}
        # all_words = self.get_all_words()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict1[name] = words.index(word.lower()) + 1
        return dict1

    def count(self, word):
        counts = 0
        dict2 = {}
        # all_words = self.get_all_words()
        for name, words in self.get_all_words().items():
            dict2[name] = words.count(word.lower())
        return dict2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('tExt'))  # 3 слово по счёту
print(finder2.count('teXt'))  # 4 слова teXT в тексте всего
