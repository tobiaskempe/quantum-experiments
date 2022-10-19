
import argparse
import os
import pickle
import dwave.inspector


parser = argparse.ArgumentParser()
parser.add_argument('run', type=str)
args = parser.parse_args()

with open(os.path.join('./runs', args.run), 'rb') as file:
  response = pickle.load(file)

print(response)
dwave.inspector.show(response)
