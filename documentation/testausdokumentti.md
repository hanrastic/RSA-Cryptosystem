# Testausdokumentti

## Selostus
Ohjelmassa on testattu kaikkia salauksen kannalta tärkeimpiä toimintoja, kuten;
- Alkulukujen luominen
- Alkuluvun tarkistaminen
- Viestin salaaminen ja salatun viestin kääntyminen

## Testauskattavuusrapotti
Testauskattavuusraportti löytyy [![Codecovista](https://codecov.io/gh/hanrastic/RSA-Cryptosystem/branch/main/graph/badge.svg?token=38QC8NMU4G)](https://codecov.io/gh/hanrastic/RSA-Cryptosystem)

## Miten ajaa testit itse?
Kloonaa repositorio. Siirry juurikansioon, ja aja:

```bash
    poetry install;poetry shell
```

```bash
    cd src;coverage run --branch -m pytest; coverage report -m
```
