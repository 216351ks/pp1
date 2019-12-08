import statistics

tablica = [21600, 4350, 3920, 5590, 3250, 4010]

print(f"Średnia arytmetyczna wynagrodzeń jest równa: {statistics.mean(tablica)}")

print(f"Mediana wynagrodzeń jest równa: {statistics.median(tablica)}")

print(f'Odchylenie standardowe jest równe: {statistics.stdev(tablica)}')