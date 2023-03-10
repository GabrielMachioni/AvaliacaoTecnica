import json
import nltk


class CheckText:
    """
    Class responsible for checking the presence of expressions in a set of texts.
    """

    def __init__(self, json_path:str, expressions_path:str, output_path:str):
        self.json_path = json_path
        self.expressions_path = expressions_path
        self.output_path = output_path
        self.texts = {}
        self.sentences = {}
        self.expressions = []
        self.output = []

    def load_texts(self):
        """
        Loads the texts from the JSON file.
        """
        with open(self.json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            self.texts[item['id']] = item['texto']

    def tokenize_sentences(self):
        """
        Tokenizes text sentences using NLTK.
        """
        for id, text in self.texts.items():
            self.sentences[id] = nltk.sent_tokenize(text, language='portuguese')

    def load_expressions(self):
        """
        Loads the expressions from the text file.
        """
        with open(self.expressions_path, 'r', encoding='utf-8') as file:
            self.expressions = [line.strip().lower() for line in file]

    def process_sentences(self):
        """
        Checks the presence of expressions in each sentence.
        """
        for id, sentences in self.sentences.items():
            sentences_infos = []
            for sentence in sentences:
                dict_info = {"sentença": sentence, "expressão": None}
                start_of_sentence = nltk.word_tokenize(sentence)[:3]
                for expression in self.expressions:
                    if expression in sentence.lower():
                        for token in start_of_sentence:
                            if token in expression.split(' '):
                                dict_info['expressão'] = expression
                                break
                sentences_infos.append(dict_info)
            self.output.append({"id": id, "sentenças": sentences_infos})

    def create_output(self):
        """
        Create JSON output
        """
        with open(self.output_path, 'w', encoding='utf-8') as file:
            json.dump(self.output, file, ensure_ascii=False, indent=4)
            
        print('Arquivo output.json criado!')


if __name__ == "__main__":
    try:
        nltk.download('punkt')
    except Exception as ex:
        print(f'run requirements.txt or check your connection!\n{ex}')
        exit()

    json_path = "assets\\textos.json"
    expressions_path = "assets\expressoes.txt"
    output_path = "output.json"

    check_text = CheckText(json_path, expressions_path, output_path)

    check_text.load_texts()
    check_text.tokenize_sentences()
    check_text.load_expressions()
    check_text.process_sentences()
    check_text.create_output()
