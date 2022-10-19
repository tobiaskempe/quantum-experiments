
import numpy as np


def generate_problem_and_save(F, R, n_routes, suffix='', verbose=False):
  A = generate_problem(F, R, n_routes, verbose=verbose)
  np.save('problem.npy', A)

def generate_problem(F, R, n_routes, verbose=False):
  # F ~ number of flights
  # R ~ number of routes
  # n_routes ~ number of routes that should complete the task
  #F = 468
  #R = 30
  #F = 200
  #R = 15
  #n_routes = 6
  n_flights_per_route = int(F/n_routes)
  print(n_flights_per_route)

  flight_numbers = np.array(range(F))

  routes = []

  for i in range(n_routes):
    flights_in_route = np.random.choice(flight_numbers, n_flights_per_route, replace=False)
    flight_numbers = flight_numbers[np.logical_not(np.isin(flight_numbers, flights_in_route))]
    print(len(flights_in_route))
    routes.append(flights_in_route)

  flight_numbers = np.array(range(F))

  for _ in range(n_routes, R):
    flights_in_route = np.random.choice(flight_numbers, n_flights_per_route, replace=False)
    print(len(flights_in_route))
    routes.append(flights_in_route)

  A = np.zeros((R, F))
  for i, route in enumerate(routes):
    A[i, route] = 1

  if verbose:
    print(A[:10, :10])

  return A
