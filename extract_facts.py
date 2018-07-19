# INSTALL INSTRUCTIONS:
# pip install spacy
# pip install textacy
# spacy download en_core_web_sm

import spacy
import textacy.extract

nlp_model = spacy.load('en_core_web_sm') # en_core_web_lg is better but bigger

text_to_examine = u"London is the capital and most populous city of England and the United Kingdom.  Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia.  It was founded by the Romans, who named it Londinium."

parsed_version_of_text = nlp_model(text_to_examine)

statements = textacy.extract.semistructured_statements(parsed_version_of_text, "London")

print("Here's what I found about London:")

for statement in statements:
    subject, verb, fact = statement
    print(' - ' + str(subject) + ' ' + str(verb) + ' ' + str(fact))
