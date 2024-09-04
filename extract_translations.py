
import json


with open('LINGUI_METADATA_FILE_PATH', 'r') as file:
    data = json.load(file)


text_origin = {}

for string in data.keys():
    text_origin.update({string: [data.get(string).get('origin')]})

del data


with open('TRANSLATIONS_FILE_PATH', 'r') as file:
    data = json.load(file)



translations = {}

for values in data.values():
    translations.update({values.get('message'):values.get('translation')})
    

del data    


for string in text_origin:
    text_origin.get(string).append(translations.get(string))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(text_origin, f, ensure_ascii=False, indent=4)
