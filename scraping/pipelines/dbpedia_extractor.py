import requests


class DbPediaExtractor:
    server = 'https://api.dbpedia-spotlight.org/'
    accepted_entity_types = ['Person', 'Place', 'Organisation', 'Product']

    def process_item(self, item, _):
        text = item.get('text')

        dbpedia_result = self._make_request(
            text
        )

        if not dbpedia_result or not dbpedia_result.get('Resources'):
            return item

        spotlight_concepts = {
            t: [] for t in self.accepted_entity_types
        }

        for concept_mention in dbpedia_result.get("Resources"):
            the_types = concept_mention['@types']

            the_type = None
            for particular_type in self.accepted_entity_types:
                if particular_type.lower() in the_types.lower():
                    the_type = particular_type

            if not the_type:
                continue

            uri = concept_mention.get('@URI')

            name = uri.replace(
                'http://dbpedia.org/resource/', ''
            ).replace(
                '_', ' '
            )

            spotlight_concepts[the_type].append({
                'spotlight_entity': name,
                'spotlight_position_start': int(concept_mention.get('@offset')),
                'spotlight_position_end': int(
                    concept_mention.get('@offset')) +
                    len(concept_mention.get('@surfaceForm')
                ),
                'spotlight_id': uri,
            })

        item['spotlight_entities'] = spotlight_concepts

        return item

    def _make_request(self, text):
        clean_text = self.clean_text_symbols(text)
        response = requests.post(
            f'{self.server}/en/annotate',
            data={
                'text': clean_text,
                'confidence': 0.5
            },
            headers={'Accept': 'application/json'}
        )
        response.raise_for_status()
        return response.json()

    def clean_text_symbols(self, text):
        """
        Cleans:
            emoticons,
            symbols and pictographs,
            transport & map symbols
            flags
        :param text: Text you need to clean
        :return: Clean text
        """
        import string
        clean_text = ''.join(ch for ch in text if ch in string.printable)

        return clean_text