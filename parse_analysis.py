import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV
df = pd.read_csv('divanpars/divanpars/spiders/output.csv')

# Очистка и преобразование столбца "price" в числовой формат
# Удаляем любые символы валюты, пробелы, запятые, и преобразуем к float
df['price'] = df['price'].replace(r'[₽,\s]', '', regex=True).astype(float)

# Вычисление средней цены
average_price = df['price'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} рублей")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Цена (в рублях)')
plt.ylabel('Количество диванов')
plt.title('Гистограмма цен на диваны')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
