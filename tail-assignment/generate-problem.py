
import numpy as np

#F = 468
#R = 30
F = 200
R = 10
n_routes = 5
n_flights_per_route = int(F/n_routes)

flight_numbers = np.array(range(F))

routes = []

for i in range(n_routes):
  flights_in_route = np.random.choice(flight_numbers, n_flights_per_route, replace=False)
  flight_numbers = flight_numbers[np.logical_not(np.isin(flight_numbers, flights_in_route))]
  routes.append(flights_in_route)

flight_numbers = np.array(range(F))

for _ in range(n_routes, R):
  flights_in_route = np.random.choice(flight_numbers, n_flights_per_route, replace=False)
  routes.append(flights_in_route)

A = np.zeros((R, F))
for i, route in enumerate(routes):
  A[i, route] = 1

print(A[:10, :10])

np.save('problem.npy', A)
