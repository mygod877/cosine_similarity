import argparse
import numpy as np
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main(args):
    data = get_data(args.datafile)
    cs = get_cs(args.query, data)

    max_index = np.argmax(cs)
    max_cs = cs[max_index][0]
    max_data = data[max_index]

    if max_cs > 1e-10:
        print(f"コサイン類似度: {max_cs}")
        print(f"アブストラクト: '{max_data}'")
    else:
        print("NotFound")

def get_data(datafile):
    abstract = np.loadtxt(f"{datafile}", encoding="utf-8", delimiter='|', dtype=str)
    data = []
    for s in abstract:
        text = s.replace(".", "")
        text = text.replace(",", "")
        text = text.replace("(", "")
        text = text.replace(")", "")
        text = text.replace("-", " ")
        data.append(text.lower())

    return data

def get_cs(query, data):
    tfidf = TfidfVectorizer()
    abstract_vector = tfidf.fit_transform(data).toarray()
    query_vector = tfidf.transform([query]).toarray()
    cs = cosine_similarity(abstract_vector, query_vector)
    
    return cs

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str)
    parser.add_argument("--datafile", type=str, default="./data/abstract.txt")
    args = parser.parse_args()
    main(args)