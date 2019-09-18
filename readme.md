This is a project that uses Scrapy to crawl company websites.

Dragnet then receives the data scraped and extracts text.

Afterwards, Spacy is used to extract: people, locations, organizations, products and events.
DbPedia is also used to extract people, locations, organizations and products.

All the data is stored in one large JSON that travels trough the pipeline and then is saved to file so individual steps can be re-run.

To set up do:
- python3.6 -m pip install cython spacy
- python3.6 -m spacy download en_core_web_lg
- python3.6 -m pip install -r requirements.txt

To run use ./run_me.sh and results will be stored in the result folder (an example currently there).

Possible next steps:
- use a class instead of a JSON as it's more explicit
- store in a database the results
- do something with the extracted data :)
