# TIER protocol i tidy data

Oryginalny zestaw danych znajdziesz w folderze /OriginalData.

Kolejne operacje, które zostały przeprowadzone na oryginalnych danych:
-- zmiana nazw większości kolumn (zmiennych), tak aby lepiej opisywały rodzaj przechowywanych danych
-- uporządkowanie danych przy pomocy funkcji melt() (skrócenie tabeli na szerokość, czego następstwem 
   jest jej wydłużenie, poprawia to czytelność danych)
-- rozbicie kolumny 'sex/age_group' na dwie osobne kolumny 'sex' i 'age group'
-- usunięcie rekordów zawierających niezidentyfikowane dane (Nan)
-- posortowanie danych po kraju i roku przeprowadzenia badania

Cały skrypt o nazwie Laboratorium_2.ipynb z odpowiednimi komentarzami do kodu zlokalizowany jest w folderze /CommandFiles.

Uporządkowane dane processed_tb.csv znajdziesz w folderze /AnalysisData. 
Nagłówki kolumn danych po przetworzeniu są następujące:
* country - string, informacja na temat kraju, gdzie badanie zostało przeprowadzone
* year - int, informacja o roku, w którym przeprowadzono badanie
* sex - string, określa płeć osób
* age_group - string, określa przedział wiekowy badanych osób
* case_count - określa dokładną wartość zachorowań na gruźlicę 
		w danym kraju i roku, osób o danej płci, 
		w określonym przedziale wiekowym