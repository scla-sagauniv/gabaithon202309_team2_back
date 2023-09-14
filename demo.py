#  model (https://github.com/singletongue/WikiEntVec/releases)

import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('models/demo2.txt', binary=False)
print(model.most_similar("日本"))
