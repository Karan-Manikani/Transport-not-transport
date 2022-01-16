from nltk.corpus import wordnet as wn

transport = wn.synset('transport.n.01')
transport_list = list(set([w for s in transport.closure(lambda s: s.hyponyms()) for w in s.lemma_names()]))

textfile = open('transport_list.txt', 'w')

for element in transport_list:
	textfile.write(element + '\n')

textfile.close()



