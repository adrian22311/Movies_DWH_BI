Pliki związane z ETL

Opis:


### 1. `./Archive`
Folder w którym po wykonaniu któreś z dostępnych akcji w naszym ETL'u pojawią się wszystkie pliki csv użytę/wygenerowane poczas tego kroku (znajdują się one w zipie z datą kiedy zostały stworzone).

### 2. `./Data`.

Folder w którym zapisywane są tymczasowe pliki poczas kroku `Insert`. 

**UWAGA** 

Żeby krok `Insert` zadziałał musimy w tym folderze umieścić plik `newMovieID` (opis jak on ma wyglądać znajduję się w README w folderze `./Data`).

### 3. `./UpdateData`, `./UpdatePeopleData`

Foldery te przetrzymują tymczasowe pliki csv utworzone odpowiednio podczas kroków `Update Movies`, `UpdatePeople`.

### 4. `./MoviesETL`.

Folder ten zawiera nasz Integration Services Project (Visual Studio Code), czyli nasz ETL.

Utworzone zostały trzy SSIS Packages:
a. `Insert` - dodawanie nowych filmów (jeśli jest taka potrzeba dodawanie osób do tabeli People)
b. `UpdateMovies` - aktualizowanie tabeli Movie
c. `UpdatePeople` - aktualizowanie tabeli People

### 5. `./Errors*`

Zawiera pliki *.txt w których zapisywane są błędy napotkanie w trakcie naszego ETL'a. Nie są one zarchiwizowane, przy każdym wywołaniu naszego ETL'a są nadpisywane.

### 6. Pliki `*.bat` i `*.py`

Zgarnianie danych z api/web scraping, zapisywanie ich do plików CSV, które są następnie czytane w naszym procesie ETL.
Również pliki które archiwizują wygenerowane przez nas csv'ki.