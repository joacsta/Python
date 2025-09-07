import pandas as pd

# AULA 01 - INTRO DO PANDAS

df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

# df.head(10)

# print(df.describe())
# print(f'linhas: {df.shape[0]} colunas: {df.shape[1]}')
# df.info()

# Index(['work_year', 'experience_level', 'employment_type', 'job_title',
#        'salary', 'salary_currency', 'salary_in_usd', 'employee_residence',
#        'remote_ratio', 'company_location', 'company_size'],
#       dtype='object')

# palavra chave: pandas

renomear_colunas = {
    'work_year': 'ano'
    ,'experience_level': 'senioridade'
    ,'employment_type': 'contrato'
    ,'job_title': 'cargo'
    ,'salary': 'salario'
    ,'salary_currency': 'moeda'
    ,'salary_in_usd': 'usd'
    , 'employee_residence': 'residencia' 
    ,'remote_ratio': 'remoto'
    , 'company_location': 'localizacao'
    , 'company_size': 'tamanho_empresa'
}

df.rename(columns=renomear_colunas, inplace=True)

senioridade = {
    'SE': 'sênior'
    ,'MI': 'pleno'
    ,'EN': 'junior'
    ,'EX':'executivo'
}


remoto = {
    0 : 'presencial'
    ,50 : 'híbrido'
    ,100: 'remoto'
}

tamanho_empresa = {
    'M': 'média'
    ,'L': 'grande'
    ,'S': 'pequena'
}

contrato = {
    'FT': 'tempo integral'
    ,'CT': 'contrato temporário'
    ,'PT': 'meio período'
    ,'FL': 'freelancer'
}


df['remoto'] = df['remoto'].replace(remoto)
df['senioridade'] = df['senioridade'].replace(senioridade)
df['contrato'] = df['contrato'].replace(contrato)
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

# print(df.describe(include='object'))


# AULA 02 - LIMPEZA DE DADOS
# palavra chave: print
import numpy as np


df.isnull().sum()
df['ano'].unique()
coluna_nula = df[df.isnull().any(axis=1)]

df_salarios = pd.DataFrame({
    'nome': ['ana','bruno', 'carlos', 'henrique','val']
    ,'salario': [1000, np.nan, 2000, np.nan, 100000]
    })

# print(coluna_nula)

# calculo de média e subtituição de nulos
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
# print(df_salarios)

df_temperatura = pd.DataFrame({
    'dia': ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    ,'temperatura': [30, np.nan, np.nan, 27, 26, 28, 29]
})

df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill()
# print(df_temperatura)

df_temperatura2 = pd.DataFrame({
    'dia': ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    ,'temperatura': [30, np.nan, np.nan, 27, 26, 28, 29]
})

df_temperatura2['preenchido_bfill'] = df_temperatura2['temperatura'].bfill()
# print(df_temperatura2)

df_cidades = pd.DataFrame({
    'nome' : ['ana','bruno', 'carlos', 'henrique','val', 'lara', 'sandy']
    ,'cidade': ['sao paulo', 'rio de janeiro', 'curitiba', np.nan, 'belém', np.nan, np.nan]
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('não informado')

df_limpo = df.dropna()

# print(df_limpo.isnull().sum())


df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
# print(df_limpo.info())
# print(df_limpo.head())



# AULA 03 - CRIANDO GRÁFICOS
import matplotlib.pyplot as plt
import seaborn as sns

# df_limpo['senioridade'].value_counts().plot(
#     kind='bar', title = 'distribuicao de senioridade')

# plt.show()

ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending = True).index

# plt.figure(figsize =(8,5))
# sns.barplot(data = df_limpo, x = 'senioridade', y = 'usd', order = ordem)
# plt.title('salario medio por nivel de senioridade')
# plt.xlabel('senioridade')
# plt.ylabel('salario medio anual em usd')

plt.figure(figsize =(8,4))
sns.histplot(df_limpo['usd'], bins = 50, kde= True)
plt.title('distribuicao dos salarios anuais')
plt.xlabel('salario em usd')
plt.ylabel('frequencia')

plt.show()