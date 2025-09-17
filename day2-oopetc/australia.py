import csv

headers = ['state', 'population']

data = [['VIC', 6649159], ['NSW', 8189266], ['SA', 1773243], ['WA', 2681633],
        ['Tasmania', 541479], ['Queensland',5221170], ['ACT', 432266], ['NT', 246338]]


with open('australiatask.csv', 'w', newline='') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=headers)

    writer.writeheader()
    for state in data:
        writer.writerow({'state': state[0], 'population': state[1]})



with open('australiatask.csv', 'w', newline='') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=headers)

    capital = 'capital'
    headers.append(capital)

    data = [['VIC', 6649159, 'Melbourne'], ['NSW', 8189266, 'Sydney'], ['SA', 1773243, 'Adelaide'], ['WA', 2681633, 'Perth'],
            ['Tasmania', 541479, 'Hobart'], ['Queensland', 5221170, 'Brisbane'], ['ACT', 432266, 'Canberra'], ['NT', 246338, 'idk']]

    writer.writeheader()
    for state in data:
        writer.writerow({'state': state[0], 'population': state[1], 'capital': state[2]})


        