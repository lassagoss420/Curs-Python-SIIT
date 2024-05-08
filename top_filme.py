name_list = [{
   'nume': 'George',
   'filme': ['Shrek', 'Bond', 'Fight Club']
},
{
 'nume': 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
},
{
 'nume': 'Stefan',
 'filme': ['Fight Club', 'Slumdog Milionare']
}]

# Care este cel mai vizionat film?
most_viewed_list = {}     #initiaza dictionarul ce va tine valorile numaratorii
top_utilizatori = {}      #initiaza dictionarul in care vor fi stocate valorile in format nume:nr de filme vizionate

for person in name_list:          #trece prin fiecare dictionar din lista
    top_utilizatori[person['nume']] = len(person['filme'])
    for movie in person['filme']: #trece prin fiecare cheie "filme" din fiecare dictionar din lista si sunt preluate de 'movie' la fiecare trecere
        # print(person['nume'])           #test, sa vad ce printeaza person
        if movie in most_viewed_list:
            most_viewed_list[movie] += 1 #daca filmul este si in movies si in most_viewed_list, adauga 1 la filmul respectiv
        else:
            most_viewed_list[movie] = 1
        # print(most_viewed_list) #test, sa vad ce printeaza most_viewed_list

sorted_top_utilizatori = sorted(top_utilizatori.items(), key=lambda x: x[1], reverse=True)
# top_utilizatori.items() returneaza o lista de tupluri cu numele si nr de filme iar functia lambda reprezinta criteriul
# de sortare, x[1] fiind al doilea element din tuplu, reverse inverseara rezultatul
most_viewed = max(most_viewed_list, key=most_viewed_list.get) #returneaza cheia cu cea mai mare valoare
most_viewed_name = most_viewed_list.get(most_viewed, 0) #returneaza valoarea cheii  returnate in most_viewed
viewed_sorted = sorted(most_viewed_list, key=most_viewed_list.get, reverse=True)  ## Sorteaza lista dupa vizualizari

print(sorted_top_utilizatori)
print('Sortand dupa numarul descrescator de vizualizari, lista este:', viewed_sorted)
print(f'{most_viewed} este cel mai vizionat film cu {most_viewed_name} vizionari.')


# Cine a vizionat cele mai multe filme?
max_filme = 0
max_nume = None

for filme in name_list:
    nr_filme = len(filme.get('filme'))
    if nr_filme > max_filme:
        max_filme = nr_filme
        max_nume = filme.get('nume')

print(f'{max_nume} a vizionat {max_filme} filme, cele mai multe.')





# Ciorna :))

# dictionar = name_list[:].get()
# max_filme = 0
# max_nume = None

# for i in name_list[].get():
#     for filme, nume in i.items():
#         nr_filme = len(filme)
#         if nr_filme > max_filme:
#             max_nume = nume
#             max_filme == nr_filme
#
# print(max_nume, max_filme)

# for filme, nume in name_list:
#     nr_filme = len(filme.get('filme'))
#     nume = nume.get('nume')
#     if nr_filme > max_filme:
#         max_nume = nume
#         max_filme = nr_filme
# print(max_nume, max_filme)