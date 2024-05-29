import matplotlib.pyplot as plt
import seaborn as sns

data.boxplot()
data.hist()

tips = sns.load_dataset('tips')
tips.plot()
