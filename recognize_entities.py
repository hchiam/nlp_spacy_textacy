# pip install spacy
# spacy download en_core_web_sm

import spacy

nlp_model = spacy.load('en_core_web_sm') # en_core_web_lg is better but bigger

text_to_examine = u"London is the capital and most populous city of England and the United Kingdom.  Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium."

parsed_version_of_text = nlp_model(text_to_examine)

named_entities_detected = parsed_version_of_text.ents

for entity in named_entities_detected:
    print(str(entity.text) + ' (' + str(entity.label_) + ')')
