import preprocessor as p
import remove_countries as rm
import warnings

warnings.filterwarnings('ignore')

pre = p.preprocessor()

df = pre.cleanDataset()