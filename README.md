# Friend Path Checker – Instrukcja uruchomienia

Program sprawdza, czy na ścieżce od korzenia (twój dom) do każdego ulubionego kolegi (wierzchołek z `isFavourite=1`) nie ma innego ulubionego kolegi. Wyniki są wyświetlane w konsoli oraz w oknie graficznym z kolorowym drzewem.

## Wymagania systemowe
- System Windows 11 (powinien działać również na Windows 10, 8)
- Zainstalowany **Python 3.8 lub nowszy** (jeśli uruchamiasz kod źródłowy)
- Połączenie z Internetem (tylko do pobrania bibliotek)

## Szybki start – uruchomienie bez instalacji (plik .exe)
Jeśli masz plik `FriendPathChecker.exe`:
1. Umieść plik wykonywalny w dowolnym folderze.
2. Przygotuj plik z danymi (np. `FriendsGraph.txt`) w tym samym folderze.
3. Otwórz wiersz poleceń (cmd) w tym folderze lub użyj dwukliku na `FriendPathChecker.exe` (wtedy program poprosi o wybór pliku).
   - **Z linii poleceń:**  
     `FriendPathChecker.exe sciezka\do\pliku.txt`
   - **Z dwukliku:** pojawi się okno wyboru pliku – wskaż plik `.txt`.

> **Uwaga:** Jeśli program nie widzi pliku, podaj pełną ścieżkę lub umieść plik w tym samym folderze co `.exe`.

## Uruchomienie z kodu źródłowego (Python)

### Krok 1: Zainstaluj Pythona
- Pobierz Python 3.8+ ze strony [python.org](https://www.python.org/downloads/)
- Podczas instalacji **zaznacz** opcję `Add Python to PATH`

### Krok 2: Pobierz kod źródłowy
Utwórz folder projektu, a w nim następującą strukturę:

Projekt/  
├── main.py  
├── src/  
│ ├── node.py  
│ ├── loader.py  
│ ├── DFS.py  
│ └── drawGraph.py  
├── Data/  
│ └── FriendsGraph.txt  
└── README.md

Skopiuj dostarczone pliki do odpowiednich lokalizacji.

### Krok 3: Zainstaluj wymagane biblioteki
Otwórz **wiersz poleceń** (cmd) i przejdź do folderu projektu:
```cmd
cd C:\ścieżka\do\projektu
```

Wpisz kolejno (lub utwórz plik `requirements.txt`):
```cmd
pip install networkx matplotlib
```
### Krok 4: Uruchom program

```cmd
python main.py dane\FriendsGraph.txt
```

Jeśli nie podasz ścieżki, program otworzy okno dialogowe wyboru pliku.

Przykładowy plik `FriendsGraph.txt`:

```csv
#name,isFavourite,parent
home,0,None
Alice,0,home
Matthew,1,Alice
Tom,1,Matthew
Jeb,1,home
```
### Krok 5: Interpretacja wyników

- W konsoli zobaczysz listę ulubionych kolegów z oznaczeniem `[OK]` (czysta ścieżka) lub `[KONFLIKT]` (inni ulubieńcy po drodze).

- Po naciśnięciu Enter otworzy się okno graficzne:
    - Czerwone węzły – ulubieni koledzy.
    - Zielona obwódka – ścieżka czysta.
    - Czerwona obwódka – konflikt (na ścieżce był inny ulubieniec).
    - Panel boczny zawiera szczegółowy status dla każdego ulubionego.

## Przygotowanie własnych danych wejściowych

Plik tekstowy w formacie CSV (przecinek jako separator, kodowanie UTF-8):
- **pierwsza linia** może być nagłówkiem zaczynającym się od `#` – jest ignorowana.
- Każda następna linia: `nazwa,czy_ulubiony,rodzic`
    - `nazwa` – dowolny tekst (bez przecinków)
    - `czy_ulubiony` – `0` (zwykły) lub `1` (ulubiony)
    - `rodzic` – `None` dla korzenia, lub nazwa istniejącego węzła (rodzic musi pojawić się wcześniej w pliku)

Przykład (drzewo o trzech poziomach):
```csv
#name,isFavourite,parent
home,0,None
Adam,0,home
Ewa,1,home
Kain,0,Adam
Abel,1,Adam
```

W tym przykładzie:
- `Ewa` – ulubiona, ścieżka `home → Ewa` – brak konfliktu (OK)
- `Abel` – ulubiony, ścieżka `home → Adam → Abel` – na ścieżce nie ma innych ulubieńców (OK), bo `Adam` nie jest ulubiony.

## Rozwiązywanie problemów

|Problem|Rozwiązanie|
|---|---|
|`ModuleNotFoundError: No module named 'networkx'`|Wykonaj `pip install networkx`|
|`ModuleNotFoundError: No module named 'matplotlib'`|Wykonaj `pip install matplotlib`|
|Okno graficzne nie pojawia się lub zamyka natychmiast|Uruchom program z konsoli (cmd), a nie przez dwuklik. Sprawdź, czy masz zainstalowany `tkinter` (domyślnie w Pythonie)|
|`AttributeError: 'NoneType' object has no attribute 'isFavouriteFriend'`|Plik danych nie zawiera korzenia (wiersza z `parent=None`) lub zawiera puste linie. Sprawdź format pliku.|
|Polski znaki w oknie wyglądają jak krzaczki|Zapisz plik danych w kodowaniu UTF-8 (Notatnik → Zapisz jako → kodowanie UTF-8)|
|Program nie reaguje po naciśnięciu Enter|Wciśnij Enter w oknie konsoli, które ma fokus. Jeśli uruchamiasz z dwukliku na `.exe` – konsola może być ukryta, wtedy użyj wiersza poleceń.|

## Kompilacja własnego pliku .exe 

Jeśli chcesz stworzyć samodzielny plik wykonywalny:
1. Zainstaluj PyInstaller: `pip install pyinstaller`
2. W katalogu z `main.py` wykonaj:
```cmd
pyinstaller --onefile --name FriendPathChecker main.py
```
1. Plik `FriendPathChecker.exe` znajdziesz w folderze `dist`.