import matplotlib.pyplot as plt

categories = ['Веб-разработка', 'Мобильная разработка', 'Разработка игр',
              'Data Science', 'Системное программирование']
values = [35, 20, 15, 25, 5]

plt.figure(figsize=(10, 6))
plt.barh(categories, values, color='blue')

plt.xlabel('Популярность (%)')
plt.ylabel('Категории')
plt.title('Популярность направлений в программировании')
plt.grid(axis='x', linestyle='--')

plt.tight_layout()
plt.show()
