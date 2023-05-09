import seaborn as sns
import matplotlib

df = sns.load_dataset("penguins")

sns.pairplot(df, hue="species")

matplotlib.pyplot.show()
