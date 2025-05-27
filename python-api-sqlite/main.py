import requests
import sqlite3

# Configurar API (use sua própria API key do TMDB)
API_KEY = 'SUA_API_KEY_AQUI'
url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=pt-BR&page=1'

# Requisição dos dados
res = requests.get(url)
dados = res.json()['results']

# Conectar ao banco e criar tabela
conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        nota REAL,
        data_lancamento TEXT
    )
''')

# Inserir dados no banco
for filme in dados:
    cursor.execute('''
        INSERT OR REPLACE INTO filmes (id, titulo, nota, data_lancamento)
        VALUES (?, ?, ?, ?)
    ''', (
        filme['id'],
        filme['title'],
        filme['vote_average'],
        filme['release_date']
    ))

conn.commit()

# Consulta: filmes com nota acima de 7
print("Filmes com nota acima de 7:")
for row in cursor.execute('SELECT titulo, nota FROM filmes WHERE nota > 7 ORDER BY nota DESC'):
    print(row)

conn.close()
