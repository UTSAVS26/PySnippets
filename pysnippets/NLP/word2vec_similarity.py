from gensim.models import KeyedVectors

def word2vec_similarity(word1: str, word2: str, model_path: str = "path/to/word2vec.bin") -> float:
    model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    return model.similarity(word1, word2) 