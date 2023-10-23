import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data_dynamics.csv', delimiter='\t')
time = data['Time']
temperature = data['Temperature']

# Dopasowanie wielomianu do danych
coefficients = np.polyfit(time, temperature, deg=2)
polynomial = np.poly1d(coefficients)

# Określenie momentu, w którym temperatura osiągnie ekstremum wielomianu
extremum_time = -coefficients[1] / (2 * coefficients[0])
extremum_temperature = polynomial(extremum_time)

# Przewidywanie temperatury na czas 2600, 3000 i 4000
time_2600 = 2600
time_3000 = 3000
time_4000 = 4000

temperature_2600 = polynomial(time_2600)
temperature_3000 = polynomial(time_3000)
temperature_4000 = polynomial(time_4000)

# Generowanie punktów do ekstrapolacji przed ekstremum i po ekstremum
extrapolation_time = np.linspace(time.min(), time_4000, 100)
extrapolation_temperature = polynomial(extrapolation_time)

# Generowanie punktów przed i po ekstremum
time_before_extremum = extrapolation_time[extrapolation_time <= extremum_time]
temperature_before_extremum = polynomial(time_before_extremum)

time_after_extremum = extrapolation_time[extrapolation_time > extremum_time]
temperature_after_extremum = np.full(len(time_after_extremum), extremum_temperature)

# Wykres z ekstrapolacją i zaznaczeniem obszaru wypłaszczenia
plt.figure(figsize=(8, 6))
plt.plot(time, temperature, marker='o', linestyle='-', color='b', label='Dane eksperymentalne')
plt.plot(extremum_time, extremum_temperature, marker='x', color='r', label=f'Ekstrapolacja (t={extremum_time:.2f}, T={extremum_temperature:.2f})')
plt.fill_between(time_before_extremum, temperature_before_extremum, label='Ekstrapolacja przed ekstremum', alpha=0.3, color='g')
plt.fill_between(time_after_extremum, temperature_after_extremum, label='Wypłaszczenie', alpha=0.3, color='y')
plt.title('Przewidywana zależność temperatury od czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Temperatura [C]')
plt.grid(True)
plt.legend()
plt.show()

print(f'Przewidywana temperatura na czas 2600: {temperature_2600}')
print(f'Przewidywana temperatura na czas 3000: {temperature_3000}')
print(f'Przewidywana temperatura na czas 4000: {temperature_4000}')
