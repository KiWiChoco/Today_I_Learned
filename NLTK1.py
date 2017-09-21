import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown

print(gutenberg.fileids())

print(len(gutenberg.raw('austen-emma.txt')))

macbeth = gutenberg.sents('shakespeare-macbeth.txt')
print(macbeth[1:5])

print(brown.categories())

print(brown.words(categories='news'))

news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
print(fdist)

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories()
                                             for word in brown.words(categories = genre))
print(cfd)

genres = ['news','religion','hobbies','science_fiction','romance']
modals = ['can','could','may','might','must','will']

cfd.tabulate(conditions = genres, samples = modals)