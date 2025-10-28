# TASK9

Task 9:To analyze and visualize Time Oriented Data 
Analysis to identify systemic patterns in the data that help to form trends, cycles or seasonal variances and to forecast the data. - Line Graph, Trend Lines, Area Chart 
Tools : Tableau, Language :Python 

Part- 2 
1. Performance of sales representatives 
2. Performance of different company departments over year 
3. Company Sales Branches Comparison 
4. Call Time Analysis 
5. Earthquake and Geospatial Data Analysis 
6. Top10 startup Investment Analysis 
7. Health Care analysis for patient care and reducing costs 
8. Create an interactive dashboard, to convey the data that had been collected over the financial year. 
9. Creating a Dashboard using COVID-19 data 

H. Learning Resources 
i. Text Books: 
1. Matthew Ward, Georges Grinstein, Daniel Keim, “Interactive Data Visualization Foundations, Techniques, and Applications”, 2nd Edition, A K Peters Ltd.Natick, Massachusetts, 2015. 

ii. Reference Books: 
1. Donabel Santos, “Tableau 10 Business Intelligence Cookbook”, Packt Publishing, 1786465639, 9781786465634, 2016. 

iii. Online References: 
1. “Data Science for beginner”, Accessed on April.11.2021[Online]. Available: https://bookdown.org/BaktiSiregar/data-science-for-beginners/Visualization.html 
2. “Exploratory data analysis and Data visualization”, Accessed on April.11.2021 [Online]. Available: https://www.creative-wisdom.com/teaching/WBI/EDA.shtml. 
3. “Visualization of Multivariate Data”, Accessed on April.11.2021 [Online].https://people.stat.sc.edu/hansont/stat730/MultivariateDataVisualization.pdf 


Signature of : 
Course handling faculty							Course Coordinator	
 
RUBURICS:


Part- 1 
Task 1: Exploration of Data Visualization Tools like Tableau, Python libraries, D3.js  CO1,S2
• Connecting Dataset 
• Preparation of data 
1.a)Extent a dataset by list the attributes  in any one of the format (CSV,Excel) .
Import python libraries whatever needed.
Read and display the details of the dataset
Show the dimensionality of data, columns, types and missing values
Compute statistics on numerical features
Compute shape of the dataset

1.b) Consider any one of the dataset 	from kaggle
Read the dataset and display 5 lines of your dataframe.
Identify the display the count of null values(missing values) in each columns
Clean up the blank(null) column and display it
Identify the duplicate entries from data set
Remove the duplicate entries from data set

Algorithm:
pd.read_csv("/content/student.csv"): This reads the CSV file and returns a DataFrame object. The contents of the DataFrame are printed to the console using print(a).
a.shape: This returns a tuple containing the dimensions of the DataFrame. The shape of the DataFrame is (1000, 8).
a.info(): This prints a concise summary of the DataFrame, including the data types of each column and the number of non-null values.
a.describe(): This returns a statistical summary of the DataFrame, including count, mean, standard deviation, minimum, and maximum values for each column.
a.head(): This returns the first 5 rows of the DataFrame.
pd.isna(a).sum(): This returns the number of missing values in each column.
a.dropna(): This removes all rows with missing values.
a.duplicated(): This returns a boolean Series indicating which rows are duplicates.
a.drop_duplicates(): This removes all duplicate rows from the DataFrame.

Code:

import pandas as pd
import numpy as np

a=pd.read_csv("/content/student.csv")
print(a)

sh=a.shape
print(sh)
a.info()
a.describe()
print(a.head())
pd.isna(a).sum()
a.dropna()
a.duplicated()
a.drop_duplicates()

Output:

(6, 6)


Exploratory Data Analysis 
Task 2: To visualize and perform Univariate analysis using continuous and categorical data  CO2,S3
Categorical Data - Bar chart, Pie Chart 
Continuous data – Scatterplot, Line Plot, Strip Plot, Swarm Plot, Histogram, Density Plot, Rug Plot.                               
Tools: Tableau, Language :Python 

2.a) Choose any one of the dataset from website. Identify and utilize the categorical data(attribute) and continuous data(attribute). Construct a Bar chart, Pie Chart using Univariate analysis of Categorical data using identified data. Construct a Scatter plot, Line Plot, Strip Plot, Swarm Plot using Univariate analysis of continuous data using identified data
Algorithm:
Choose Dataset: Select a dataset with categorical and continuous attributes.
Identify Data Types: Distinguish between categorical (non-numeric) and continuous (numeric) attributes.
Construct Bar and Pie Charts: Create frequency tables for categorical data, then plot bar and pie charts to visualize distribution.
Construct Scatter, Line, Strip, and Swarm Plots: Utilize appropriate plots for continuous data analysis, considering relationships, trends, and distributions.
Interpret Visualizations: Analyze insights gained from visualizations, identifying patterns, dominant categories, and correlations.
Consider Further Analysis: Reflect on implications for further exploration or decision-making based on the analysis.
Document Findings: Summarize findings and observations for reporting or presentation purposes.
Program:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/content/sentimentdataset.csv")
platform_likes_top5 = df.groupby('Platform')['Likes'].sum().sort_values(ascending=False).head(5)

# Create a pie chart
plt.figure(figsize=(4, 4))
platform_likes_top5.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'lightsteelblue'])
plt.title('Top 5 Platforms by Total Likes')
plt.ylabel('')  # Remove the 'Platform' label on the y-axis
plt.show()

top5_countries = df.nlargest(5, 'Likes')


# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top5_countries['Country'], top5_countries['Likes'], color=['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'lightsteelblue'])
plt.xlabel('Country')
plt.ylabel('Total Likes')
plt.title('Top 5 Countries by Total Likes')
plt.show()

data = {
    'Text': ['Enjoying a beautiful day at the park!', 'Traffic was terrible this morning.', 'Just finished an amazing workout!', 'Excited about the upcoming weekend getaway!', 'Trying out a new recipe for dinner tonight.'],
    'Retweets': [15, 5, 20, 8, 12],
    'Likes': [30, 10, 40, 15, 25]
}

df = pd.DataFrame(data)

# Set the Seaborn style
sns.set(style="whitegrid")

# Create a scatter plot using Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Retweets', y='Likes', data=df, color='blue', alpha=0.7)
plt.title('Scatter Plot of Retweets vs Likes')
plt.show()

2. b) Utilize a given source of dataset that contains employee details.
Identify the categorical data (attribute) and continuous data (attribute).
Construct a Bar chart, Pie Chart using Univariate analysis of Categorical Data
Construct a Histogram, Density Plot, and Rug Plot using Univariate analysis of Categorical Data. Dataset Source: 
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from a CSV file
file_path = 'Employee.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Extract the column with categorical data for plotting (e.g., 'Gender')
categorical_column = 'Gender'  # Replace with the actual categorical column name

# Count the occurrences of each category
category_counts = df[categorical_column].value_counts()

# Create a pie chart
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title(f'Pie Chart of {categorical_column}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from a CSV file
file_path = 'Employee.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Extract the column with categorical data for plotting (e.g., 'City')
categorical_column = 'City'  # Replace with the actual categorical column name

# Count the occurrences of each category
category_counts = df[categorical_column].value_counts()

# Create a bar chart
plt.bar(category_counts.index, category_counts, color=['skyblue', 'lightcoral', 'lightgreen', 'orange'])
plt.title(f'Bar Chart of {categorical_column}')
plt.xlabel(categorical_column)
plt.ylabel('Count')

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from a CSV file
file_path = '/content/Employee.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Extract the column with continuous data for plotting (e.g., 'Age' column)
continuous_column = 'Age'  # Replace 'Age' with the actual column name
# Create a histogram
plt.hist(df[continuous_column], bins=10, edgecolor='black')  # You can adjust the number of bins as needed, bins=blue bars
plt.title(f'{continuous_column} Distribution')
plt.xlabel(continuous_column)
plt.ylabel('Frequency')
# Show the plot
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset from a CSV file
file_path = 'Employee.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Extract the column with continuous data for plotting (e.g., 'Age' column)
continuous_column = 'Age'  # Replace 'Age' with the actual column name

# Create a density plot
sns.kdeplot(df[continuous_column], fill=True)
plt.title(f'Density Plot of {continuous_column}')
plt.xlabel(continuous_column)
plt.ylabel('Density')

# Show the plot
plt.show()




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset from a CSV file
file_path = 'Employee.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Extract the column with continuous data for plotting (e.g., 'ExperienceInCurrentDomain')
continuous_column = 'JoiningYear'  # Replace with the desired column name

# Create a rug plot
sns.rugplot(df[continuous_column], height=0.5)
plt.title(f'Rug Plot of {continuous_column}')
plt.xlabel(continuous_column)
plt.yticks([])  # Remove y-axis ticks for better clarity (optional)

# Show the plot
plt.show()




Task 3: To visualize and perform Bivariate analysis using continuous and categorical data 
Categorical vs. Categorical: Stacked Bar Chart, Grouped Bar chart, Segmented Bar Chart, Mosaic Plots . 
Continuous vs. Continuous: Scatterplot Fit Lines 
Categorical vs. Continuous : Bar Chart (Summary statistics), Grouped Kernel Density Plots, Box Plots, Violin Plots, Ridgeline Plots, Beeswarm Plots.  CO2,S3
Tools: Tableau, Language :Python      

Link for dataset: 

Identify Columns holding categorical data  
and Columns holding continuous data.

Construct a Stacked Bar Chart, Grouped Bar chart, Segmented Bar Chart using Bivariate analysis of categorical vs categorical data  for the attributes of approved and gender in above data set.
Construct a Scatterplot Fit Lines using bivariate analysis of   Continuous vs. Continuous data.
Identify the categorical vs Continuous data to plot the Bar Chart,Grouped Kernel Density Plots, Box Plots, Violin Plots, Ridgeline Plots, Beeswarm Plots. 

Algorithm:
1. Select Dataset: Choose a dataset containing both categorical and continuous variables.
2. Differentiate Variables: Identify categorical and continuous variables.
3.Categorical vs. Categorical: Create stacked, grouped, or segmented bar charts, along with mosaic plots, to visualize relationships between categorical variables.
4. Continuous vs. Continuous: Generate scatterplots with fit lines to explore relationships between two continuous variables.
5. Categorical vs. Continuous: Construct bar charts for summary statistics and use grouped kernel density plots, box plots, violin plots, ridgeline plots, or beeswarm plots to visualize distributions across categories.
6. Interpretation: Analyze visualizations for insights into relationships, distributions, and patterns, drawing conclusions for further analysis or decision-making.
Program:
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('/content/clean_dataset.csv')

# Extract the two columns
industry = df['Industry']
income = df['Income']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(industry, income, color='skyblue')
plt.xlabel('Industry')
plt.ylabel('Income')
plt.title('Income by Industry')
plt.xticks(rotation=45)
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read data from CSV file
df = pd.read_csv('/content/clean_dataset.csv')
# Extract the two columns
categorical_column = 'Ethnicity'
continuous_column = 'Income'
# Create grouped kernel density plots
plt.figure(figsize=(12, 8))
sns.kdeplot(data=df, x=continuous_column, hue=categorical_column, fill=True, common_norm=False)
plt.xlabel(continuous_column)
plt.title(f'Grouped Kernel Density Plot for {continuous_column} by {categorical_column}')
plt.legend(title=categorical_column)
plt.show()



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read data from CSV file
df = pd.read_csv('/content/clean_dataset.csv', nrows=50)
# Extract the two columns
categorical_column = 'Citizen'
continuous_column = 'Income'
# Create grouped box plots
plt.figure(figsize=(16, 12))
sns.boxplot(data=df, x=categorical_column, y=continuous_column)
plt.xlabel(categorical_column)
plt.ylabel(continuous_column)
plt.title(f'Grouped Box Plot for {continuous_column} by {categorical_column}')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read data from CSV file
df = pd.read_csv('/content/clean_dataset.csv')
# Extract the two columns
categorical_column = 'Ethnicity'
continuous_column = 'Income'
# Create violin plots
plt.figure(figsize=(12, 8))
sns.violinplot(data=df, x=categorical_column, y=continuous_column)
plt.xlabel(categorical_column)
plt.ylabel(continuous_column)
plt.title(f'Violin Plot for {continuous_column} by {categorical_column}')
plt.show()


import pandas as pd
from joypy import joyplot
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('/content/clean_dataset.csv')

# Extract the two columns
categorical_column = 'Industry'
continuous_column = 'Income'

# Create ridgeline plots
plt.figure(figsize=(12, 8))
joyplot(
    data=df,
    by=categorical_column,
    column=continuous_column,
    kind='kde',  # Use KDE (Kernel Density Estimation) for the ridgeline plot
    fill=True,
    linecolor="black",
    grid=True,
    linewidth=1,
    legend=True,
)

plt.xlabel(continuous_column)
plt.title(f'Ridgeline Plot for {continuous_column} by {categorical_column}')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('/content/DV task-4.csv')
# Assuming 'Age' is on the x-axis and 'Income' is on the y-axis
sns.lmplot(data=df, x='Age', y='Income', height=6, line_kws={'color': 'red'})
plt.title('Scatter Plot with Fit Line')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()


Task 4: To visualize and perform Multivariate analysis using Multiple variables involving Multiple measures                         
Scatterplot Matrix, Parallel Coordinates, Line Graph, Stacked Bar Chart                   CO2,S3
Tools: Tableau, Language :Python    
Link for dataset:https://www.kaggle.com/datasets/samuelcortinhas/credit-card-approval-clean-data.  This dataset contains a cleaned version of  on credit card approvals. Missing values have been filled and feature names and categorical names have been inferred, resulting in more context and it being easier to use.
Construct a Scatterplot Matrix, Parallel Coordinates, Line Graph, Stacked Bar Chart, using Multiple variables involving Multiple measures
Algorithm:
1. Import necessary libraries including NumPy, pandas, seaborn, matplotlib.pyplot, and plotly.express.
2. Load the dataset from a zip file using pandas `read_csv` function.
3. Print the loaded dataset to inspect its structure and contents.
4. Select numeric columns (Age, Debt, YearsEmployed), create a pairplot using seaborn to visualize pairwise relationships, and display the plot.
5. Use plotly.express to create a parallel coordinates plot, color-coded by the 'Approved' column, with dimensions as Age, Debt, and CreditScore, and show the plot.
6. Extract the first 20 entries of the dataset and plot the Age against Debt and CreditScore using a line plot with different colors for Debt and CreditScore, then display the plot.
7. Group the first 20 entries by Age, summing up Debt and CreditScore for each Age group, create a stacked bar chart representing Debt and CreditScore for each Age group, and display the chart.

Program:
import numpy as np
import pandas as pd
df= pd.read_csv("/content/archive (4).zip")
print(df)

import seaborn as sns
import matplotlib.pyplot as plt
numeric_subset = df[['Age', 'Debt', 'YearsEmployed']]
sns.pairplot(numeric_subset)
plt.show()

import pandas as pd
import plotly.express as px
attributes = ["Age", "Debt", "CreditScore"]
fig = px.parallel_coordinates(df, color="Approved", dimensions=attributes,color_continuous_scale=px.colors.diverging.Tealrose,color_continuous_midpoint=0.5)
fig.show()

first_20_entries = df.head(20)
age = first_20_entries['Age']
debt = first_20_entries['Debt']
credit_score = first_20_entries['CreditScore']
plt.figure(figsize=(10, 6))
plt.plot(age, debt, label='Debt', color='blue')
plt.plot(age, credit_score, label='Credit Score', color='green')
plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Line Graph: Age, Debt, and Credit Score')
plt.legend()
plt.grid(True)
plt.show()

grouped_data = first_20_entries.groupby('Age').sum()[['Debt', 'CreditScore']]
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Stacked Bar Chart: Debt and Credit Score by Age')
plt.legend(title='Attribute')
plt.show()

Task 5: To design and perform visualization for Trees                
• TreeMap, Sun Burst Display                                           CO3,S3
Tools: Tableau, Language :Python                   
5.a)  Construct a treeMap display on a real-world dataset. You can download the dataset in the given link. . US Cars'data was scraped from AUCTION EXPORT.com. This dataset included Information about 28 brands of clean and used vehicles for sale in US. Twelve features were assembled for each car in the dataset. In the data set you can take any attributes,Values and visualize it .

5b) Build a sunburst display using above program dataset.
Construct a treeMap display on a real-world dataset.
Alogrithm:
1. Install the `squa` package using pip.rify
2. Import necessary libraries such as `pandas`, `matplotlib.pyplot`, and `squarify`.
3. Read the dataset from '/content/USA_cars_datasets.csv' into a pandas DataFrame `df`.
4. Group the DataFrame `df` by the 'brand' column and calculate the total price for each brand.
5. Create a figure of size 18x12 inches for the tree map visualization.
6. Use `squarify.plot()` to create a tree map plot.
7. Pass the sizes of the rectangles as the total price of each brand (`brand_total_price['price']`) and labels as the brand names (`brand_total_price['brand']`).
8. Set transparency with alpha=0.4 for better visualization.
9. Turn off the axis.
10. Set the title of the plot as 'Tree Map of Total Price by Brand'.
11. Display the plot using plt.show()

Program
pip install squarify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
df=pd.read_csv('/content/USA_cars_datasets.csv')
print(df)
brand_total_price = df.groupby('brand')['price'].sum().reset_index()
plt.figure(figsize=(18, 12))
squarify.plot(sizes=brand_total_price['price'], label=brand_total_price['brand'], alpha=0.4)
plt.axis('off')
plt.title('Tree Map of Total Price by Brand')
plt.show()
Output:


Build a sunburst display using above program dataset.
Algorithm:
1. Install the required packages `squarify` and `plotly` using pip.
2. Import necessary libraries: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `squarify`, and `plotly.express`.
3. Read the dataset from '/content/USA_cars_datasets.csv' into a pandas DataFrame `df`.
4. Group the DataFrame `df` by the combination of 'brand' and 'model' columns and calculate the total price for each combination.
5. Create a sunburst plot using Plotly Express (`px.sunburst()`):
   - Specify the DataFrame `sunburst_data` as the data source.
   - Set the path for the sunburst plot to follow the hierarchy of 'brand' and 'model'.
   - Define 'price' as the values to be represented.
   - Set the title of the plot as 'Sunburst Display of Total Price by Brand and Model'.
6. Display the plot using `fig.show()`.
Program:
pip install squarify
pip install plotly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import plotly.express as px
df=pd.read_csv('/content/USA_cars_datasets.csv')
print(df)
sunburst_data = df.groupby(['brand', 'model']).sum().reset_index()
fig = px.sunburst(sunburst_data, path=['brand', 'model'], values='price', title='Sunburst Display of Total Price by Brand and Model')
fig.show()
Output:





Task 6: To design and perform visualization for Graphs and Networks            
• Force based Layout                                                          CO3,S3
Tools: Tableau, Language :Python                         
Data set link : 
Utilize a given dataset link it contains network links, source and target technical tags, and the link value between each pair. It also contains the nodes of the network, the name of each node, the group to which this node belongs and a node size based on the frequency of use of this technological beacon. How to visualize and analyze a network graph using the Python programming language:
Algorithm:
Import necessary libraries:

Import NetworkX as nx for creating and manipulating network graphs.
Import Matplotlib.pyplot as plt for data visualization.
Import Pandas as pd for data handling.
Create an empty graph object G and set an attribute 'day' to "Stackoverflow."

Read node and edge data from CSV files ('stack_network_nodes.csv' and 'stack_network_links.csv') into DataFramesdf_nodes and df_links, respectively.

Add nodes to the graph G:

Iterate through the rows in df_nodes.
For each row, add a node to the graph with a 'name,' 'group,' and 'nodesize' attributes.
Add weighted edges to the graph G:

Iterate through the rows in df_links.
For each row, add a weighted edge from the 'source' to the 'target' with the 'value' as the weight.
Set visualization parameters:

Create a figure with a specified size.
Define visualization options like edge color, width, node labels, and font weight.
Determine colors for nodes based on their 'group' attribute.
Adjust node sizes based on the 'nodesize' attribute.
Draw the network graph:

Use nx.draw to visualize the graph.
Customize the node colors and sizes based on the calculated values.
Define the layout of the nodes using spring layout with specified parameters.
Set the edge color to a specific color.
Show the graph using plt.show().
End of the algorithm.

Code:
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph(day="Stackoverflow")
df_nodes = pd.read_csv('stack_network_nodes.csv')
df_links = pd.read_csv('stack_network_links.csv')

for index, row in df_nodes.iterrows():
G.add_node(row['name'], group=row['group'], nodesize=row['nodesize'])
for index, row in df_links.iterrows():
G.add_weighted_edges_from([(row['source'], row['target'], row['value'])])

plt.figure(figsize=(15,15))
options = {
    'edge_color': '#FFDEA2',
    'width': 1.5,
    'with_labels': True,
    'font_weight': 'regular',
}
colors = [color_map[G.nodes[node]['group']] for node in G]
sizes = [G.nodes[node]['nodesize']*25 for node in G]

nx.draw(G, node_color=colors, node_size=sizes, pos=nx.spring_layout(G, k=1.5, iterations=15), **options)
ax = plt.gca()
ax.collections[0].set_edgecolor("#555555")
plt.show()

Output:



Task 7: To generate insight using Text Network Analysis and Visualization                    CO3,S3
Tools: Wordle, Tag Cloud, WordTree, InfraNodus 

7a) TagCrowd tool using Build a word cloud it contains your details.

7 b) Utilize wordtree package to generate the cloud of text and to plot graph using matplotlib library and visualize it.
Algorithm:
Import necessary libraries:

Import WordCloud from the WordCloud library for word cloud creation.
Import matplotlib.pyplot as plt for data visualization.
Define the text from which you want to create a word cloud. In this case, it's stored in the details variable.

Create a WordCloud object with specific parameters: Set the width and height of the word cloud image.
Specify the background color (white in this case).
Provide a list of stopwords to exclude common words (an empty list in this case).
Set the minimum font size for displayed words. Create a Matplotlib figure for displaying the word cloud:

Define the figure size (5x5 inches in this case) and specify the facecolor (None, which is transparent).
Generate the word cloud image using the generate method of the WordCloud object, passing in the text from step 2.

Display the word cloud image:

Use plt.imshow to display the word cloud. Turn off the axis to remove axis labels.Adjust the layout to minimize padding. Show the word cloud using plt.show().

End of the algorithm.

Code:
from wordcloud import WordCloud
import matplotlib.pyplot as plt

details = "Data visualization is the visual and interactive exploration and graphic representation of data of any type. This course covers data visualization concepts, practices, and tools particularly for analyzing and presenting business data. Students will evaluate, design, and develop effective visualizations and dashboards, using various development tools"

wordcloud = WordCloud(width = 800, height = 800,
background_color ='white',
stopwords = [],
min_font_size = 10).generate(details)

plt.figure(figsize = (5, 5), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()

Output:


Task 8: To analyze and visualize Spatial and Geospatial data         CO4,S3
Geographical Map, Map Projections 
Tools: Tableau, QGIS, Language :Python 

Data set Link: . 
This Dataset consist of population statistics by census years of cities and towns in Tamil Nadu obtained from various sources. Dataset consist of 6 columns - Name of city or town, Status of that city/town, District of that city/town and 3 columns of population statistics by census years(1991-03-01, 2001-03-01, 2011-03-01).Now the question is how can combine these pieces of information to generate insights such as Spatial and Geospatial data.
Task 9:To analyze and visualize Time Oriented Data                          CO5,S3
Analysis to identify systemic patterns in the data that help to form trends, cycles or seasonal variances and to forecast the data. - Line Graph, Trend Lines, Area Chart 
Tools : Tableau, Language :Python 

9a) The dataset set contains various features such as temperature, pressure, humidity, rain, precipitation,etc.

Data set Link: . This dataset contains weather data for New Delhi, India.This data was taken out from wunderground with the help of their easy to use api. It contains various features such as temperature, pressure, humidity, rain, precipitation,etc.To analyze and visualize Time Oriented Data using Line graph, trend lines, area chart.
Aim:To analyze and visualize Time Oriented Data using Line graph, trend lines, area chart.

Algorithm:
Import necessary libraries: pandas, matplotlib.pyplot, seaborn, numpy, and LinearRegression from sklearn.
Read the CSV file containing the dataset into a DataFrame using pd.read_csv().
Preprocess the data by stripping column names, converting 'datetime_utc' column to datetime format, and setting it as the index.
Plot the temperature data over time using sns.lineplot(), specifying the x-axis as the index of the DataFrame and y-axis as the temperature column ('_tempm').
Customize the plot by adding a title, labels for the x and y axes, enabling grid lines, rotating x-axis labels for better readability, and displaying the plot using plt.show().
Program:
Line Graph
import pandas aspd
importmatplotlib.pyplotasplt
importseabornassns
importnumpyas np
fromsklearn.linear_modelimportLinearRegression
data = pd.read_csv('/content/testset.csv')
data.columns = data.columns.str.strip()
data['datetime_utc'] = pd.to_datetime(data['datetime_utc'])
data.set_index('datetime_utc', inplace=True)
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x=data.index, y='_tempm')  # Assuming '_tempm' is the column you want to plot
plt.title('Line Graph of Temperature over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


Output:

Trend Lines
import pandas aspd
importnumpyas np
importmatplotlib.pyplotasplt
fromsklearn.linear_modelimportLinearRegression
data = pd.read_csv('/content/testset.csv')
data.columns = data.columns.str.strip()
data['datetime_utc'] = pd.to_datetime(data['datetime_utc'])
data.set_index('datetime_utc', inplace=True)
data['_tempm'].fillna(data['_tempm'].mean(), inplace=True)
x = data.index.astype(int).values.reshape(-1, 1)  # Converting datetime to numerical
y = data['_tempm'].values  # Assuming '_tempm' is the column for temperature
model = LinearRegression()
model.fit(x, y)
slope = model.coef_[0]
intercept = model.intercept_
plt.figure(figsize=(10, 6))
plt.scatter(data.index, data['_tempm'], color='blue', label='Temperature Data')
plt.plot(data.index, slope * x + intercept, color='red', linestyle='-', linewidth=2, label='Trend Line')
plt.title('Temperature Trend with Trend Line')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

Area Chart:
import pandas aspd
importmatplotlib.pyplotasplt
data = pd.read_csv('/content/testset.csv')
data.columns = data.columns.str.strip()
data['datetime_utc'] = pd.to_datetime(data['datetime_utc'])
data.set_index('datetime_utc', inplace=True)
monthly_mean_temp = data['_tempm'].resample('M').mean()
plt.figure(figsize=(10, 6))
monthly_mean_temp.plot(kind='area', color='skyblue', alpha=0.7)  # Adjust alpha for transparency
plt.title('Monthly Mean Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

Result: Thus, we successfully implemented the Line graph, Trend lines, Area chart by Time Oriented Data and out is verified
Part- 2 

Performance of sales representatives
2. Performance of different company departments over year 
3. Company Sales Branches Comparison 
4. Call Time Analysis 
5. Earthquake and Geospatial Data Analysis 
6. Top10 startup Investment Analysis 
7. Health Care analysis for patient care and reducing costs 
8. Create an interactive dashboard, to convey the data that had been collected over the financial year. 
9. Creating a Dashboard using COVID-19 data 

1.Performance of sales representatives
Methodology, Code and, Results for evaluating the profitability
Percentage of customers who has outcome variable (dependent variable) as “1” (purchased the product) in both train and test datasets is ~11.2%
Calculating “Average profit per customer” by reaching out to all the customers in training data.

This shows that by reaching out to all the customers with a conversion rate of ~11.2% will lead to loss of $1,25,710. This warrants targeting selected audience who have higher odds of conversion.
3. Performing Logistic Regression on train data and using the predicted probability of the event happening to calculate the Cost, Revenue, Profit and Return on Investment (ROI) for each probability value at an interval of 0.01.
ROI= (Profit/Cost)*100

The above function takes “Actual outcome”, “Predicted probability of the event happening”, “Cost per individual”, “Revenue per individual”, “Range of probabilities to check” as input. The below snippet is a call for the above function with training data as input and using the estimated cost and revenue per individual as determined by the manager.

Below “Probability of event happening” is considered as cut off for segregating if the customer will buy a product or will not buy a product. We can observe that as the “Probability of event happening” increases,“% Target population” decreases, which means considering higher probability as a cut off leads to segregating less number of customers as the target population. But the interesting fact is as the “Probability of event happening” increases, the “ROI” increases which means though we are targeting less population we are getting good results as compared to targeting more population, which can also be seen in the below graph.


Graph of Revenue, Cost and Profit across different predicted probabilities of event happening:

This graph shows that as the “Probability of event happening” increases, metrics like cost, revenue, profit decreases and the ROI increases. Depending on the need of the hour like “Limitation of budget”, “High ROI” a specific probability can be selected as the cut-off, but it is also necessary to make sure that same results can be replicated using test data.
Graph of Return On Investment and Profit at different costs