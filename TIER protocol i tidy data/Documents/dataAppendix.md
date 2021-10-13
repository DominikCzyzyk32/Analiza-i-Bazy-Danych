# Data appendix

Oryginalny zestaw danych znajdziesz w folderze /OriginalData.

Uporządkowane dane processed_tb.csv znajdziesz w folderze /AnalysisData. 
Rekordy z wybrakowanymi danymi (zawierającymi Nan-y) zostały usunięte.
Nagłówki kolumn danych po przetworzeniu są następujące:
* country - string, informacja na temat kraju, gdzie badanie zostało przeprowadzone
* year - int, informacja o roku, w którym przeprowadzono badanie
* sex - string, określa płeć osób
* age_group - string, określa przedział wiekowy badanych osób
* case_count - określa dokładną wartość zachorowań na gruźlicę 
		w danym kraju i roku, osób o danej płci, 
		w określonym przedziale wiekowym

Dodatkowe informacje na temat wyżej wymienionych zmiennych (opisy danych, wykresy słupkowe
prezentujące dane) znajdziesz w skrypcie Laboratorium_2_data_appendix.ipynb w folderze
/CommandFiles.