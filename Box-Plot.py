import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 


def load_housing_data():
    csv_path = os.path.join("Box-Plot.csv")
    return pd.read_csv(csv_path)
housing = load_housing_data()
housing.head()

plt.figure(figsize=(14, 7))

sns.set_style("white")

#Setting property of outliners of box-plot
flierprops = dict(marker='o', markerfacecolor='black', markersize=5, linestyle='none')

Box= sns.boxplot(y='PM-2.5', x='Day', 
                 data=housing, 
                # palette="Set3",
                 hue='Year',showmeans=True,meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                      "markersize":"5"}, linewidth=1.75, fliersize= 0,
                      flierprops=flierprops)

                     # whis=[0,100])
                      #showfliers=False)
# whis = Proportion of the IQR past the low and high quartiles to extend the plot whiskers. Points outside this range will be identified as outliers. 

#Font Size of Legend-Title
plt.setp(Box.get_legend().get_title(),fontsize='15')

#Font Size of Legend Content
plt.setp(Box.get_legend().get_texts(), fontsize='15')

#For the Axis of the plot
plt.tick_params(labelsize=16,width=1.5)

# To increase the graph size 
#plt.tight_layout()       

#Saving the plot 
#plt.savefig("simple_boxplot_with_Seaborn_boxplot_Python.png")

#Setting the y axis range
Box.set_ylim(0,900)

#Plotting Data

plt.xlabel("Diwali Week", fontsize=21,fontweight='bold')
plt.ylabel("PM-2.5 (µg/m³)", fontsize=21,fontweight='bold')

plt.show(Box)



