# this app studies the join() string method
# syntax is 'separatorHere'.join(nameOfIterableToBeConvertedToString)
crew: list = ['Ripley', 'Dallas', 'Ash', 'MU/TH/ER', 'Xenomorph']
print('-'.join(crew))

# or an iterable can be declared directly inside of the join() method such that

print('/'.join(('Snake', 'Bandana')))
# .join returns keys as the string values if used on a dict
print(' '.join({'Warrant Officer': 'Ripley', 'Captain': 'Dallas'}))