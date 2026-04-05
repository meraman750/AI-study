from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    return model.encode(text)


def search_similar(query, chunks):
    query_emb = create_embedding(query)

    scores = cosine_similarity([query_emb], chunks)[0]
    best_index = scores.argmax()

    return best_index