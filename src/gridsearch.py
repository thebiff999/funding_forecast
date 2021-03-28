from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import ml_preprocessor as mlp
import numpy as np

ml_p = mlp.ml_preprocessor()
df = ml_p.getDataFrame()
y = df['state'].values
df = df.drop(['state'], axis=1)
X = df.values

param_grid = {'n_neighbors': np.arange(14,30)}
knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, cv = 2)
knn_cv.fit(X, y)
print(knn_cv.best_params_)
print(knn_cv.best_score_)

# n = 1-15, cv = 4 -> n=14, precision = 0,62684
# n = 14-30, cv = 2 -> n=28, precision = 0,62895