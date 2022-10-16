from click import style
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

e = pd.read_csv("50ulke.csv")

print(e)

# sns.displot(e["KİŞİ BAŞINA"])

n = pd.read_csv("dunyam.csv")
n.dropna(how="any", inplace=True)

sns.set(style="dark", font_scale =1.5, palette="muted")
sns.distplot(n["Doğum oranı"], bins=20, kde=False, color="g")

plt.show()
