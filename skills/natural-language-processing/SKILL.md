---
name: Natural Language Processing
description: Build NLP applications using transformers library, BERT, GPT, text classification, named entity recognition, and sentiment analysis
---

# Natural Language Processing

## Overview

This skill provides comprehensive tools for building NLP applications using modern transformers, BERT, GPT, and classical NLP techniques for text classification, named entity recognition, sentiment analysis, and more.

## When to Use

- Building text classification systems for sentiment analysis, topic categorization, or intent detection
- Extracting named entities (people, places, organizations) from unstructured text
- Implementing machine translation, text summarization, or question answering systems
- Processing and analyzing large volumes of textual data for insights
- Creating chatbots, virtual assistants, or conversational AI applications
- Fine-tuning pre-trained transformer models for domain-specific NLP tasks

## NLP Core Tasks

- **Text Classification**: Sentiment, topic, intent classification
- **Named Entity Recognition**: Identifying people, places, organizations
- **Machine Translation**: Text translation between languages
- **Text Summarization**: Extracting key information
- **Question Answering**: Finding answers in documents
- **Text Generation**: Generating coherent text

## Popular Models and Libraries

- **Transformers**: BERT, GPT, RoBERTa, T5
- **spaCy**: Industrial NLP pipeline
- **NLTK**: Classic NLP toolkit
- **Hugging Face**: Pre-trained models hub
- **PyTorch/TensorFlow**: Deep learning frameworks

## Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import torch
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                         AutoModelForTokenClassification, pipeline,
                         TextClassificationPipeline)
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

# Download required NLTK resources
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

print("=== 1. Text Preprocessing ===")

def preprocess_text(text, remove_stopwords=True, lemmatize=True):
    """Complete text preprocessing pipeline"""
    # Lowercase
    text = text.lower()

    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words]

    # Lemmatize
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return tokens, ' '.join(tokens)

sample_text = "The quick brown foxes are jumping over the lazy dogs! Amazing performance."
tokens, processed = preprocess_text(sample_text)
print(f"Original: {sample_text}")
print(f"Processed: {processed}")
print(f"Tokens: {tokens}\n")

# 2. Text Classification with sklearn
print("=== 2. Traditional Text Classification ===")

# Sample data
texts = [
    "I love this product, it's amazing!",
    "This movie is fantastic and entertaining.",
    "Best purchase ever, highly recommended.",
    "Terrible quality, very disappointed.",
    "Worst experience, waste of money.",
    "Horrible service and poor quality.",
    "The food was delicious and fresh.",
    "Great atmosphere and friendly staff.",
    "Bad weather today, very gloomy.",
    "The book was boring and uninteresting."
]

labels = [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]  # 1: positive, 0: negative

# TF-IDF vectorization
tfidf = TfidfVectorizer(max_features=100, ngram_range=(1, 2))
X_tfidf = tfidf.fit_transform(texts)

# Train classifier
clf = MultinomialNB()
clf.fit(X_tfidf, labels)

# Evaluate
predictions = clf.predict(X_tfidf)
print(f"Accuracy: {accuracy_score(labels, predictions):.4f}")
print(f"Precision: {precision_score(labels, predictions):.4f}")
print(f"Recall: {recall_score(labels, predictions):.4f}")
print(f"F1: {f1_score(labels, predictions):.4f}\n")

# 3. Transformer-based text classification
print("=== 3. Transformer-based Classification ===")

try:
    # Use Hugging Face transformers for sentiment analysis
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    test_sentences = [
        "This is a wonderful movie!",
        "I absolutely hate this product.",
        "It's okay, nothing special.",
        "Amazing quality and fast delivery!"
    ]

    print("Sentiment Analysis Results:")
    for sentence in test_sentences:
        result = sentiment_pipeline(sentence)
        print(f"  Text: {sentence}")
        print(f"  Sentiment: {result[0]['label']}, Score: {result[0]['score']:.4f}\n")

except Exception as e:
    print(f"Transformer model not available: {str(e)}\n")

# 4. Named Entity Recognition (NER)
print("=== 4. Named Entity Recognition ===")

try:
    ner_pipeline = pipeline(
        "ner",
        model="distilbert-base-uncased",
        aggregation_strategy="simple"
    )

    text = "Apple Inc. was founded by Steve Jobs in Cupertino, California."
    entities = ner_pipeline(text)

    print(f"Text: {text}")
    print("Entities:")
    for entity in entities:
        print(f"  {entity['word']}: {entity['entity_group']} (score: {entity['score']:.4f})")

except Exception as e:
    print(f"NER model not available: {str(e)}\n")

# 5. Word embeddings and similarity
print("\n=== 5. Word Embeddings and Similarity ===")

from sklearn.metrics.pairwise import cosine_similarity

# Simple bag-of-words embeddings
vectorizer = CountVectorizer(max_features=50)
docs = [
    "machine learning is great",
    "deep learning uses neural networks",
    "machine learning and deep learning"
]

embeddings = vectorizer.fit_transform(docs).toarray()

# Compute similarity
similarity_matrix = cosine_similarity(embeddings)
print("Document Similarity Matrix:")
print(pd.DataFrame(similarity_matrix, columns=[f"Doc{i}" for i in range(len(docs))],
                  index=[f"Doc{i}" for i in range(len(docs))]).round(3))

# 6. Tokenization and vocabulary
print("\n=== 6. Tokenization Analysis ===")

corpus = " ".join(texts)
tokens, _ = preprocess_text(corpus)

# Vocabulary
vocab = Counter(tokens)
print(f"Vocabulary size: {len(vocab)}")
print("Top 10 most common words:")
for word, count in vocab.most_common(10):
    print(f"  {word}: {count}")

# 7. Advanced Transformer pipeline
print("\n=== 7. Advanced NLP Tasks ===")

try:
    # Zero-shot classification
    zero_shot_pipeline = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

    sequence = "Apple is discussing the possibility of acquiring startup for 1 billion dollars"
    candidate_labels = ["business", "sports", "technology", "politics"]

    result = zero_shot_pipeline(sequence, candidate_labels)
    print("Zero-shot Classification Results:")
    for label, score in zip(result['labels'], result['scores']):
        print(f"  {label}: {score:.4f}")

except Exception as e:
    print(f"Advanced pipeline not available: {str(e)}\n")

# 8. Text statistics and analysis
print("\n=== 8. Text Statistics ===")

sample_texts = [
    "Natural language processing is fascinating.",
    "Machine learning enables artificial intelligence.",
    "Deep learning revolutionizes computer vision."
]

stats_data = []
for text in sample_texts:
    words = text.split()
    chars = len(text)
    avg_word_len = np.mean([len(w) for w in words])

    stats_data.append({
        'Text': text[:40] + '...' if len(text) > 40 else text,
        'Words': len(words),
        'Characters': chars,
        'Avg Word Len': avg_word_len
    })

stats_df = pd.DataFrame(stats_data)
print(stats_df.to_string(index=False))

# 9. Visualization
print("\n=== 9. NLP Visualization ===")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Word frequency
word_freq = vocab.most_common(15)
words, freqs = zip(*word_freq)
axes[0, 0].barh(range(len(words)), freqs, color='steelblue')
axes[0, 0].set_yticks(range(len(words)))
axes[0, 0].set_yticklabels(words)
axes[0, 0].set_xlabel('Frequency')
axes[0, 0].set_title('Top 15 Most Frequent Words')
axes[0, 0].invert_yaxis()

# Sentiment distribution
sentiments = ['Positive', 'Negative', 'Positive', 'Negative', 'Positive']
sentiment_counts = Counter(sentiments)
axes[0, 1].pie(sentiment_counts.values(), labels=sentiment_counts.keys(),
              autopct='%1.1f%%', colors=['green', 'red'])
axes[0, 1].set_title('Sentiment Distribution')

# Document similarity heatmap
im = axes[1, 0].imshow(similarity_matrix, cmap='YlOrRd', aspect='auto')
axes[1, 0].set_xticks(range(len(docs)))
axes[1, 0].set_yticks(range(len(docs)))
axes[1, 0].set_xticklabels([f'Doc{i}' for i in range(len(docs))])
axes[1, 0].set_yticklabels([f'Doc{i}' for i in range(len(docs))])
axes[1, 0].set_title('Document Similarity Heatmap')
plt.colorbar(im, ax=axes[1, 0])

# Text length distribution
text_lengths = [len(t.split()) for t in texts]
axes[1, 1].hist(text_lengths, bins=5, color='coral', edgecolor='black')
axes[1, 1].set_xlabel('Number of Words')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Text Length Distribution')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('nlp_analysis.png', dpi=100, bbox_inches='tight')
print("\nNLP visualization saved as 'nlp_analysis.png'")

# 10. Summary
print("\n=== NLP Summary ===")
print(f"Texts processed: {len(texts)}")
print(f"Unique vocabulary: {len(vocab)} words")
print(f"Average text length: {np.mean([len(t.split()) for t in texts]):.2f} words")
print(f"Classification accuracy: {accuracy_score(labels, predictions):.4f}")

print("\nNatural language processing setup completed!")
```

## Common NLP Tasks and Models

- **Classification**: DistilBERT, RoBERTa, ELECTRA
- **NER**: BioBERT, SciBERT, spaCy models
- **Translation**: MarianMT, M2M-100
- **Summarization**: BART, Pegasus, T5
- **QA**: BERT, RoBERTa, DeBERTa

## Text Preprocessing Pipeline

1. Lowercasing and cleaning
2. Tokenization
3. Stopword removal
4. Lemmatization/Stemming
5. Vectorization

## Best Practices

- Use pre-trained models when available
- Fine-tune on task-specific data
- Handle out-of-vocabulary words
- Batch process for efficiency
- Monitor for bias in models

## Deliverables

- Trained NLP model
- Text classification results
- Named entities extracted
- Performance metrics
- Visualization dashboard
- Inference API
