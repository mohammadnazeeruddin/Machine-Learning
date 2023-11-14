
import os

for root, dirs, files in os.walk('/home/nazeer/Desktop/main/main1/'):
     print(root)
     for file in files:
        print(file)
        