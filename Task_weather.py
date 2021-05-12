import requests
from datetime import datetime

link = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'lat': '59.92',
    'lon': '30.25',
    'appid': 'b9d0536abd43ef0819d3a46b4b658b38',
    'units': 'metric',
    'exclude': 'minutely,hourly'
}

res = requests.get(link, params=params)
weather = res.json()
weather_daily = weather['daily']


all_pressure = []
hPa_to_mmRtSt = 1.33322
date_and_temp_diff = dict()

for weather_day in weather_daily:
    pressure_hPa = weather_day['pressure']
    all_pressure.append(round(pressure_hPa/hPa_to_mmRtSt, 1))
    temp_morn = weather_day['temp']['morn']
    temp_night = weather_day['temp']['night']
    ts = int(weather_day['dt'])
    date = datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
    date_and_temp_diff[date] = abs(round(temp_night - temp_morn, 2))

max_pressure = max(all_pressure)
print(f'Максимальное давление за предстоящие 5 дней (включая текущий): {max_pressure} мм.рт.ст.')
day_min_diff = min(date_and_temp_diff.keys(), key=lambda x: date_and_temp_diff[x])
print(f'День с минимальной разницей между ночной и утренней температурой: {day_min_diff}')

