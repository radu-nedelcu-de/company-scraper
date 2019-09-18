import en_core_web_lg


class SpacyEntityExtractor:
    nlp = en_core_web_lg.load()
    accepted_entity_types = ['PERSON', 'GPE', 'ORG', 'Product', 'Event']

    def process_item(self, item, _):
        text = item.get('text')

        doc = self.nlp(text)

        entities_in_doc = {
            t: [] for t in self.accepted_entity_types
        }
        for entity in doc.ents:
            label = entity.label_
            if label not in entities_in_doc.keys():
                continue
            else:
                entities_in_doc[label].append({
                    'spacy_entity': entity.orth_,
                    'spacy_position_start': entity.start_char,
                    'spacy_position_end': entity.end_char,
                })

        item['spacy_entities'] = entities_in_doc

        return item