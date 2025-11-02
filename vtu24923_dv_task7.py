from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Data visualization helps in understanding patterns and insights from data effectively."
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
