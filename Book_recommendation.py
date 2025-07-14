from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np

# 1. Chargement du dataset déjà fourni
# Ces lignes sont souvent déjà faites dans les 3 premières cellules :
# books = pd.read_csv("books.csv")
# ratings = pd.read_csv("ratings.csv")

# 2. Supprimer les utilisateurs avec < 200 notes et livres avec < 100 notes
ratings_filtered = ratings.groupby('User-ID').filter(lambda x: len(x) >= 200)
ratings_filtered = ratings_filtered.groupby('ISBN').filter(lambda x: len(x) >= 100)

# 3. Création d'une table pivot "livres x utilisateurs"
book_user_matrix = ratings_filtered.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating').fillna(0)

# 4. KNN (modèle basé sur la distance cosine)
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(book_user_matrix.values)

# 5. Fonction de recommandation
def get_recommends(book_title):
    if book_title not in book_user_matrix.index:
        return [book_title, []]
    
    book_vector = book_user_matrix.loc[book_title].values.reshape(1, -1)
    distances, indices = model_knn.kneighbors(book_vector, n_neighbors=6)
    
    # distances[0][0] = 0 (le livre lui-même), on l’ignore
    recommended = []
    for i in range(1, len(distances[0])):
        recommended_title = book_user_matrix.index[indices[0][i]]
        distance = distances[0][i]
        recommended.append([recommended_title, float(distance)])
    
    return [book_title, recommended]
