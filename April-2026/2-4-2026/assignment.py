'''
Assignment (03/04/2026)

Assignment Name : NLP Mini App
Description : Build a chatbot, fake news detector, or keyword extractor.
'''

import re
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def ensure_nltk_resources() -> None:
	
	resources = [
		("tokenizers/punkt", "punkt"),
		("corpora/stopwords", "stopwords"),
	]

	for resource_path, resource_name in resources:
		try:
			nltk.data.find(resource_path)
		except LookupError:
			nltk.download(resource_name, quiet=True)


def extract_keywords(text: str, top_n: int = 8) -> list[tuple[str, int]]:
	
	tokens = word_tokenize(text.lower())
	english_stopwords = set(stopwords.words("english"))

	cleaned_tokens = [
		token
		for token in tokens
		if re.fullmatch(r"[a-z]+", token)
		and token not in english_stopwords
		and len(token) > 2
	]

	keyword_freq = Counter(cleaned_tokens)
	return keyword_freq.most_common(top_n)


ensure_nltk_resources()

sample_text = """
Natural language processing helps computers understand human language.
Keyword extraction is useful for summarization, search, and document analysis.
This mini app identifies important words from a text by removing stopwords
and counting the most meaningful terms.
"""

keywords = extract_keywords(sample_text, top_n=8)

print("Input Text:\n")
print(sample_text.strip())
print("\nTop Keywords:\n")

for word, frequency in keywords:
	print(f"{word}: {frequency}")