import preprocessor as p
import remove_countries as rm
import warnings
import ml_preprocessor as ml

warnings.filterwarnings('ignore')

pre = p.preprocessor()

df = pre.cleanDataset()
print(df.columns)