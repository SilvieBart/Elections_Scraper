Třetí projekt na Python Akademii od Engeta.

POPIS PROJEKTU

Projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí zde.

INSTALACE KNIHOVEN

Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít
nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

pip3 --version				# ověřím verzi manažeru
pip3 install -r requirements.txt	# nainstaluji knihovny


SPUŠTĚNÍ PROJEKTU

Spučtění projektu election_scraper.py v rámci přík. řádku požaduje dva povinné argumenty.
python election_scraper <odkaz_uzemniho_celku> <vysledny_soubor>
Následně se vám stáhnou výsledky jako soubor s příponou .csv. 

UKÁZKA PROJEKTU

Výsledky hlasování pro okres Prostějov:

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: vysledky_prostejov.csv

Spuštění programu:

"C:\Program Files\Python310\python.exe" C:/Users/Silvie/PycharmProjects/pythonProject/venv/Elections_Scraper/Elections_Scraper.py

Průběh stahování:

STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
UKLADAM DO SOUBORU: vysledky_prostejov.csv
UKONCUJI Election_Scraper...
ZAPSANO DO SOUBORU: vysledky_prostejov.csv

Částečný výstup

Kod obce,Nazev obce,Volici,Vydane obalky,Platne hlasy,ANO 2011,Blok proti islam.-Obran.domova...
506761,Alojzov,205,145,144,32,0,0,0,1,17,6,0,29,0,1,0,0,1,0,5,0,1,4,15,5,18,9,0,0
589268,Bedihošť,834,527,524,140,1,0,0,0,123,26,0,51,0,2,1,0,0,0,13,1,14,2,82,6,34,28,0,0
589276,Bílovice-Lutotín,431,279,275,83,0,0,0,1,40,22,0,13,0,0,0,0,0,0,8,0,4,1,38,3,30,32,0,0...