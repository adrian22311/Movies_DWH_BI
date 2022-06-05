# Movies DWH/BI

### `./ETL` - proces ETL
### `./DWH_Backup` - backup hurtowni
### `./countries` - folder ze słownikami kodów krajów/języków
#### `.env` - plik musi zawierać api key z TMDB (API_KEY=<api_key>)


Tworzenie bazy danych (w odpowiedniej kolejność):
1. Uruchomienie pliku - `Movies_DateDimensionSetup.sql`
2. Uruchomienie pliku - `Movies_dwh_setup.sql`

