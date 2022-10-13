"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Silvie Bartošíková
email: silviebartosikova@gmail.com
discord: Silvie B.#8828
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup


def validace_vstupnich_udaju():
    url_prefix = "https://volby.cz/pls/ps2017nss/ps32"
    if len(sys.argv) < 3:
        print("Nebyly zadany 2 argumenty. Ukoncuji program...")
        return False
    if not sys.argv[1].startswith(url_prefix):
        print(f"Argument obsahuje nespravny odkaz: {sys.argv[1]}",
              f"Ukoncuji program...",
              sep="\n")
        return False
    return True


def hlavni():
    if not validace_vstupnich_udaju():
        quit(1)
    url = sys.argv[1]
    nazev_souboru = sys.argv[2]
    print(f"STAHUJI DATA Z VYBRANEHO URL: {url}",
          f"UKLADAM DO SOUBORU: {nazev_souboru}",
          sep="\n")
    vysledky_obce = vysledky_voleb(url)
    vsechny_strany = najdi_vsechny_strany(vysledky_obce)
    vysledky_tab = []
    for obec in vysledky_obce:
        vysledky_tab.append(vypis_vysledky_pro_obec(obec, vsechny_strany))

    zapis_vysledky_do_souboru(nazev_souboru, vytvor_hlavicky(vsechny_strany),
                              vysledky_tab)


def zapis_vysledky_do_souboru(nazev_souboru: str, table_header: list,
                              table_body: list[list]):
    with open(nazev_souboru, mode="w", newline="", encoding='utf-8') as zapis_csv:
        zapis = csv.writer(zapis_csv, delimiter=",")
        zapis.writerow(table_header)
        zapis.writerows(table_body)
        print(f"ZAPSANO. UKONCUJI PROGRAM...")


def vytvor_hlavicky(vsechny_strany: list):
    hlavicky = ["Kod obce", "Nazev obce", "Volici", "Vydane obalky",
                "Platne hlasy"]
    for strana in vsechny_strany:
        hlavicky.append(strana)
    return hlavicky


def vypis_vysledky_pro_obec(obec: dict, vsechny_strany: list):
    vysledky = [obec["kod_obce"], obec["nazev_obce"], obec["volici"],
                obec["vydane_obalky"], obec["platne_hlasy"]]
    for strana in vsechny_strany:
        vysledky.append(obec["strany"].get(strana, "0"))
    return vysledky


def najdi_vsechny_strany(vysledky_obce: list):
    nazvy_stran = set()
    for obec in vysledky_obce:
        for strana in obec["strany"].keys():
            nazvy_stran.add(strana)
    return sorted(nazvy_stran)


def zpracuj_odpoved_serveru(url):
    odpoved_serveru = requests.get(url)
    return BeautifulSoup(odpoved_serveru.text, "html.parser")


def vysledky_voleb(url: str):
    soup = zpracuj_odpoved_serveru(url)
    obce = []

    for tab in soup.find_all("table", {"class": "table"}):
        for row in tab.find_all("tr"):
            kod_obce = row.find("td", {"class": "cislo"})
            if kod_obce is not None:
                nazev_obce = row.find("td", {"class": "overflow_name"}).get_text()
                href_detail_obce = row.find("a").get("href")
                url_detail_obce = create_url_from_href(url, href_detail_obce)

                soup_detail = zpracuj_odpoved_serveru(url_detail_obce)
                volici = soup_detail.find("td", {"headers": "sa2"}).get_text()
                vydane_obalky = soup_detail.find("td", {"headers": "sa3"}).get_text()
                platne_hlasy = soup_detail.find("td", {"headers": "sa6"}).get_text()
                obec = {
                    "kod_obce": kod_obce.get_text(),
                    "nazev_obce": nazev_obce,
                    "volici": volici,
                    "vydane_obalky": vydane_obalky,
                    "platne_hlasy": platne_hlasy,
                    "strany": vysledky_pro_strany(soup_detail)
                }
                obce.append(obec)
    return obce


def vysledky_pro_strany(soup_detail: BeautifulSoup):
    strany = {}
    for div in soup_detail.find_all("div", {"class": "t2_470"}):
        for tab in div.find_all("table", {"class": "table"}):
            for row in tab.find_all("tr"):
                nazev_strany = row.find("td", {"class": "overflow_name"})
                if nazev_strany is not None:
                    pocet_hlasu = nazev_strany.find_next_sibling("td", {"class": "cislo"}).get_text()
                    strany[nazev_strany.get_text()] = pocet_hlasu
    return strany


def create_url_from_href(original_url: str, href: str):
    return original_url[:original_url.rindex("/")+1] + href


if __name__ == "__main__":
    hlavni()
