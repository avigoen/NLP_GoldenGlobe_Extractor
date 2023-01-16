import spacy, difflib, nltk, ssl, certifi
from collections import Counter
certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('punkt')
nltk.download('stopwords')
spacy.cli.download("en_core_web_lg")

from nltk.corpus import stopwords

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk.stem import	WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
wordnet_lemmatizer = WordNetLemmatizer()
  
from nltk.stem.porter import PorterStemmer
porter_stemmer  = PorterStemmer()


nlp = spacy.load("en_core_web_lg")
stop_words = set(stopwords.words('english'))

