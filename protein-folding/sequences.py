
import numpy as np

sequences = [
  'HPPH',
  'HPPHPH',
  'PHPPHPH',
  'HPHPHPPH',
  'HHPPHPPHP',
  'HPPHPPHPPH',
  'HHHPPPHPPHPPPH',
  #'HHHPPHPPHPHPPHPHPH',
  #'PHPHPHPPHPHPPHPPHHH',
  #'HPHPHPPHPHPPHPPPPHHH',
  #'PHHPPHPHPPHPHPPHPPHHH',
  #'HPPHPPHPHPPHPHPPHPPHHH',
  #'PPHHHHPPHPPHPHPPHPHPPHP',
  #'HPPPPHPPHPHPPHPHPPHPPHHH',
  #'PHPHPHPHPPHPHPHPPHPPHHHHH',
  #'HHHHPPHHPPHPHPPHPHPPHHPPHH',
  #'PHPHPHPHPPHPHPHPPHPPPPHHHHH',
  #'PPHHHPPHPPHPHPHPPHPHPPHPPHHH',
  #'PHPHPHPPHHPPHPHPPHPPHHHHPPHHH',
  #'PPHHHHPPHPPHPHPPHHPPHPHPHPPHHH',
  #'PPHPPHHPPHHPPPPPHHHHHHHHHHPPPPPPHHPPHHPPHPPHHHHH',
  #'HHHHHHHHHHHHPHPHPPHHPPHHPPHPPHHPPHHPPHPPHHPPHHPPHPHPHHHHHHHHHHHHH',
]

structures = [
  [2, 0, 1, 3],
  [3, 0, 1, 4, 7, 6],
  [7, 4, 5, 2, 1, 0, 3],
  [3, 0, 1, 2, 5, 8, 7, 4],
  [8, 4, 0, 1, 5, 6, 10, 9, 13],
  [9, 8, 4, 5, 1, 2, 6, 7, 11, 10],
  [11, 15, 14, 13, 9, 8, 4, 5, 1, 2, 3, 7, 6, 10],
  #[17, 12, 13, 14, 9, 8, 3, 2, 7, 6, 11, 10, 15, 16, 21, 22, 23, 18],
  #[13, 12, 17, 22, 21, 16, 15, 10, 11, 6, 7, 2, 3, 8, 9, 14, 19, 18, 23],
  #[14, 8, 9, 10, 16, 17, 23, 22, 28, 27, 33, 32, 26, 25, 24, 18, 19, 20, 21, 15],
]

def build_result(structure, L):
  N = len(structure)
  vars = np.zeros((N * L ** 2))
  for f, s in enumerate(structure):
    vars[s * N + f] = 1
  return vars

if __name__ == '__main__':
  for s in sequences:
    print(len(s), s)