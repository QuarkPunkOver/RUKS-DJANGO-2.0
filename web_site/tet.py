# Пример данных
country = ['United States']
movie_info = [
    'An ex-hitman comes out of retirement to track down the gangsters who killed his dog and stole his car.',
    "With the untimely death of his beloved wife still bitter in his mouth, John Wick, the expert former assassin, receives one final gift from her--a precious keepsake to help John find a new meaning in life now that she is gone. But when the arrogant Russian mob prince, Iosef Tarasov, and his men pay Wick a rather unwelcome visit to rob him of his prized 1969 Mustang and his wife's present, the legendary hitman will be forced to unearth his meticulously concealed identity. Blind with revenge, John will immediately unleash a carefully orchestrated maelstrom of destruction against the sophisticated kingpin, Viggo Tarasov, and his family, who are fully aware of his lethal capacity. Now, only blood can quench the boogeyman's thirst for retribution.—Nick Riganas",
    "John Wick is a retired hitman who returns to the criminal underworld to settle a debt. When his former employer's son, Santino, orders his men to take out John's beloved puppy, an unexpected and deadly altercation ensues, leaving his beloved pup dead. Fueled by vengeance and a drive for justice, John embarks on a brutal rampage to take down Santino and his gang, seeking vengeance for his beloved pup. Along the way, John discovers the shocking truth about the deaths of his wife and son and finds himself thrust into a final, epic showdown with Santino and his legion of hired guns.—FacebookPaginaMovies"
]

# Извлечение строк из списка и объединение их в одну строку
country_str = country[0]
movie_info_str = ' '.join(movie_info)

# Вывод результата без дополнительных символов
print("Страна:", country_str)
print("О фильме:", movie_info_str)