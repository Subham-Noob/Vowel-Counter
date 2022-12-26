import string
from collections import Counter
from wordcloud import WordCloud


def text_analyzer(text):
    # Calculate word count
    words = text.split()
    word_count = len(words)

    # Calculate sentence count
    sentences = text.split(".")
    sentence_count = len(sentences)

    # Calculate character count
    character_count = len(text)

    # Calculate frequency of each word
    word_frequency = Counter(words)

    # Generate word cloud
    wordcloud = WordCloud().generate_from_frequencies(word_frequency)

    # Print results
    print("Number of words:", word_count)
    print("Number of sentences:", sentence_count)
    print("Number of characters:", character_count)
    print("Most frequent words:", word_frequency.most_common(5))
    wordcloud.to_image().show()


text = input("Enter some text:")
text_analyzer(text)
