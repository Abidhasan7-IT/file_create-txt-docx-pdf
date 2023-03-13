
names = ['Abid', 'Mamud', 'Abrar']

with open(r'F:\iubat.txt','w') as fp:
    for item in names:
        fp.write("%s\n" % item)
    print('Done')