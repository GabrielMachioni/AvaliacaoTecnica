import os
import json
from main import CheckText


def test_check_text():
    json_path = os.path.join("tests", "test_text.json")
    expressions_path = os.path.join("assets", "expressoes.txt")
    output_path = os.path.join("tests","output_test.json")

    check_text = CheckText(json_path, expressions_path, output_path)

    check_text.load_texts()
    check_text.tokenize_sentences()
    check_text.load_expressions()
    check_text.process_sentences()
    check_text.create_output()

    with open(output_path, 'r', encoding='utf-8') as file:
        output = json.load(file)

    assert isinstance(output, list)
    assert len(output) == 4
    assert isinstance(output[0], dict)
    assert isinstance(output[1], dict)
    assert len(output[0]['sentenças']) == 4
    assert len(output[1]['sentenças']) == 2
    assert isinstance(output[0]['sentenças'][0], dict)
    assert isinstance(output[1]['sentenças'][0], dict)
    assert output[0]['sentenças'][0]['expressão'] is None
    
