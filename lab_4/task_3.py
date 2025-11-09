import matplotlib.pyplot as plt

programming_languages = ['C++', 'Python', 'Java', 'Javascript', 'Go', 'C#']
values = [20, 10, 40, 15, 5, 10]
colors = ['yellow', 'blue', 'red', 'gold', 'pink', 'orange']

plt.figure(figsize = (10,6))
plt.pie(values, colors = colors, labels = programming_languages, autopct='%1.1f%%')

plt.title('Preferences in programming languages', fontsize = 14)
plt.show()