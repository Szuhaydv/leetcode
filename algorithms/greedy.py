stations = { "kone": {"id", "nv", "ut"}, "ktwo": {"wa", "id", "mt"}, "kthree": {"or", "nv", "ca"}, "kfour": {"nv", "ut"}, "kfive": {"ca", "az"} }

final_stations = set()
states_needed = set()
for _, items in stations.items():
    states_needed.update(items)

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = states_for_station
    states_needed -= states_covered
    final_stations.add(best_station)

print("Final stations:", final_stations)
