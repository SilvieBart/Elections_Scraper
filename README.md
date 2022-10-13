Třetí projekt na Python Akademii od Engeta.

POPIS PROJEKTU

Projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí zde.

INSTALACE KNIHOVEN

Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít
nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

$ pip3 --version					          # ověřím verzi manažeru
$ pip3 install -r requirements.txt	# nainstaluji knihovny


SPUŠTĚNÍ PROJEKTU

Spuštění souboru elections_scraper.py v rámci přík. řádku požaduje dva povinné argumenty.
python elections_scraper <odkaz_uzemniho_celku> <vysledny_soubor>
Následně se vám stáhnou výsledky jako soubor s příponou .csv. 

UKÁZKA PROJEKTU

Výsledky hlasování pro okres Prostějov:

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: vysledky_prostejov.csv

SPUŠTĚNÍ PROGRAMU:

Python Elections_Scraper.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 vysledky_prostejov.csv

PRŮBĚH STAHOVÁNÍ:

STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
UKLADAM DO SOUBORU: vysledky_prostejov.csv
ZAPSANO. UKONCUJI PROGRAM...

ČÁSTEČNÝ VÝSTUP:

Kod obce,Nazev obce,Volici,Vydane obalky,Platne hlasy,ANO 2011,...
506761,Alojzov,205,145,144,32,0,0,0,1,17,6,0,29,0,1,0,0,1,0,5,0,1,4,15,5,
589268,Bedihošť,834,527,524,140,1,0,0,0,123,26,0,51,0,2,1,0,0,0,13,1,14,
...
