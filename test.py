def solution(P, S):
    #number of people and the total number of seats
    people = sum (P)
    seats = sum (S)
    if seats < people:
        return -1
    total = sorted(zip(S, P), reverse=True)
  cars_used = 0
  people_left = people
  for seats, people in total:
    if seats >= people:
      people_left -= people
    else:
      people_left -= seats
  
    if people_left <= 0:
      return cars_used + 1

    cars_used += 1
    return -1
