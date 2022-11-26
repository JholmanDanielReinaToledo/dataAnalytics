import pymongo
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

client = pymongo.MongoClient("mongodb+srv://userAtlas:<password>@cluster0.j4ancsp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db_list = client.list_database_names()

collection = client['mercadeo'].get_collection(name="matriculas")


new_collection = collection.find(
    {
        '$or':
            [
                {'Código del departamento(IES)': '11'},
                {'Código del departamento(IES)': '5'},
                {'Código del departamento(IES)': '76'},
            ]
    }
)


data = pd.DataFrame(new_collection)
data['Total Matriculados'] = data['Total Matriculados'].astype(int)
print(data['Total Matriculados'])
new_data = data[['Año', 'Total Matriculados', 'Código del departamento(IES)']]
new_data.set_index(['Año', 'Código del departamento(IES)'], inplace=True)
print(new_data.index)

# columns=groups[groups.le(limit)],

pivot = pd.pivot_table(
    new_data,
    index='Año',
    values='Total Matriculados',
    aggfunc=np.sum,
    columns='Código del departamento(IES)'
)


ax = pivot.plot(kind='bar', figsize=(20,10), fontsize=18, width=0.8)
for container in ax.containers:
    ax.bar_label(container)
#cs = data.groupby('Año')['Total Matriculados']
#cs.plot(kind="bar", figsize=(20,10))
#data = data.convert_dtypes()
#data['Código del Municipio(IES)'].value_counts().plot(kind="bar", figsize=(20,10))
plt.grid(axis='y')
plt.ylabel('Total matriculados en millones', fontsize=15)

plt.xlabel('Año', fontsize=15)
plt.title('Total matriculas', fontsize=18)
plt.savefig('7imagen.png')



new_collection = collection.find(
    {
        '$or':
            [
                {'Código del departamento(IES)': '91'},
                {'Código del departamento(IES)': '88'},
                {'Código del departamento(IES)': '86'},
            ]
    }
)


data = pd.DataFrame(new_collection)
data['Total Matriculados'] = data['Total Matriculados'].astype(int)
print(data['Total Matriculados'])
new_data = data[['Año', 'Total Matriculados', 'Código del departamento(IES)']]
new_data.set_index(['Año', 'Código del departamento(IES)'], inplace=True)
print(new_data.index)

# columns=groups[groups.le(limit)],

pivot = pd.pivot_table(
    new_data,
    index='Año',
    values='Total Matriculados',
    aggfunc=np.sum,
    columns='Código del departamento(IES)'
)


ax = pivot.plot(kind='bar', figsize=(20,10), fontsize=18, width=0.8)
for container in ax.containers:
    ax.bar_label(container)
plt.grid(axis='y')
plt.ylabel('Total matriculados en millones', fontsize=15)

plt.xlabel('Año', fontsize=15)
plt.title('Total matriculas', fontsize=18)
plt.savefig('8imagen.png')



new_collection = collection.find(
    {
        '$or':
            [
                {'Código del Municipio(IES)': '11001'},
                {'Código del Municipio(IES)': '5001'},
                {'Código del Municipio(IES)': '76001'},
            ]
    }
)

data = pd.DataFrame(new_collection)
print(data.keys())
data['Total Matriculados'] = data['Total Matriculados'].astype(int)
print(data['Total Matriculados'])
new_data = data[['Año', 'Total Matriculados', 'Código del Municipio(IES)']]
new_data.set_index(['Año', 'Código del Municipio(IES)'], inplace=True)
print(new_data.index)

# columns=groups[groups.le(limit)],

pivot = pd.pivot_table(
    new_data,
    index='Año',
    values='Total Matriculados',
    aggfunc=np.sum,
    columns='Código del Municipio(IES)'
)


ax = pivot.plot(kind='bar', figsize=(20,10), fontsize=18, width=0.8)
for container in ax.containers:
    ax.bar_label(container)
plt.grid(axis='y')
plt.ylabel('Total matriculados en millones', fontsize=15)

plt.xlabel('Año', fontsize=15)
plt.title('Total matriculas', fontsize=18)
plt.savefig('9imagen.png')


new_collection = collection.find(
    {
        '$or':
            [
                {'Código del Municipio(IES)': '5440'},
                {'Código del Municipio(IES)': '91001'},
                {'Código del Municipio(IES)': '5579'},
            ]
    }
)

data = pd.DataFrame(new_collection)
print(data.keys())
data['Total Matriculados'] = data['Total Matriculados'].astype(int)
print(data['Total Matriculados'])
new_data = data[['Año', 'Total Matriculados', 'Código del Municipio(IES)']]
new_data.set_index(['Año', 'Código del Municipio(IES)'], inplace=True)
print(new_data.index)

# columns=groups[groups.le(limit)],

pivot = pd.pivot_table(
    new_data,
    index='Año',
    values='Total Matriculados',
    aggfunc=np.sum,
    columns='Código del Municipio(IES)'
)


ax = pivot.plot(kind='bar', figsize=(20,10), fontsize=18, width=0.8)
for container in ax.containers:
    ax.bar_label(container)
plt.grid(axis='y')
plt.ylabel('Total matriculados en millones', fontsize=15)

plt.xlabel('Año', fontsize=15)
plt.title('Total matriculas', fontsize=18)
plt.savefig('10imagen.png')