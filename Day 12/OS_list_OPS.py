
import os
os.mkdir('test_folders')
os.rename('peoples.csv', 'renamed_people.csv')
os.remove('renamed_people.csv')
