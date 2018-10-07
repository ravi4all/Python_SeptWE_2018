dataset = [
    {
        "action" : ['baby', '300', 'avengers', 'dhoom', 'batman',
                    'thor','hulk','ironman','superman','MI',
                    'I am Legend','Robot'],
        "comedy" : ['pk','fukrey','stree'],
        "biopic" : ['gold','sanju'],
        "thriller" : ['saw']
        }
    ]

user_1 = {'pk', 'gold', 'baby', '300', 'saw', 'avengers',
          'thor','hulk','ironman','superman'}

user_2 = {'hulk','gold','ironman','saw','avengers','sanju',
          'stree','fukrey','dhoom','batman'}

sim = user_1.intersection(user_2)
union = user_1.union(user_2)

j = len(sim) / len(union)
dist = j * 100
print("Similarity is",round(dist,2))

action = 0
comedy = 0
biopic = 0
thriller = 0

for movie in sim:
    for data in dataset:
        if movie in data['action']:
            action += 1
        elif movie in data['comedy']:
            comedy += 1
        elif movie in data['thriller']:
            thriller += 1
        elif movie in data['biopic']:
            biopic += 1

print("Action : {}, Comedy : {}, Biopic : {}, Thriller : {}".format(action, comedy, biopic, thriller))

for movie_1 in dataset[0]['action']:
    if movie_1 not in user_2:
        print("Recommended",movie_1)
