frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás
que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear
realizar una búsqueda y reemplazo en un gran número DE archivos de
texto,o renombrar y reorganizar un montón de archivos con fotos de una
manera compleja. Tal vez quieras escribir alguna pequeña base de datos
personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'''

dict = {}

text = frase.replace(',', ' ').replace('.', ' ').replace('\n', ' ').replace('  ',' ').strip().split(' ')

for x in text:
    x = x.lower()
    if len(x) in dict:
        if x not in dict[len(x)]:
            dict[len(x)].append(x)
    else:
        dict[len(x)] = [x]


print(dict)
