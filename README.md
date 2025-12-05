# Łatynkatar

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://github.com/latynkatar/latynkatar/blob/main/LICENSE)

Маленькая і простая бібліятэка для канвертацыі кірыліцы ў сучасную (з ž, č, š і v, т.зв. "чэшскую") і старую(з ż, cz, sz і w, т.зв. "пользскую") лацінку.

## Усталёўка

Latynkatar [ёсць у PyPI](https://pypi.org/project/latynkatar/).

```console
$ python -m pip install latynkatar
```

Не правяралася і не гарантуецца праца з **Python** да версіі **3.10**.

## Ужыванне

Усё досыць просталінейна:

```python
>>> import latynkatar
>>> # сучасная ("чэшская")
>>> latynkatar.convert("Але лёс склаўся так, што хрусць і папалам!")
'Ale los skłaŭsia tak, što chruść i papałam!'
>>> # сучасная без пазначэння транзітыўнай мяккасці
>>> latynkatar.convert("Але лёс склаўся так, што хрусць і папалам!", miakkasc=False)
'Ale los skłaŭsia tak, što chrusć i papałam!'
>>> # старая ("польская")
>>> latynkatar.convert_old("Але лёс склаўся так, што хрусць і папалам!")
'Ale los skłaŭsia tak, szto chruść i papałam!'
>>> # старая без пазначэння транзітыўнай мяккасці
>>> latynkatar.convert_old("Але лёс склаўся так, што хрусць і папалам!", miakkasc=False)
'Ale los skłaŭsia tak, szto chrusć i papałam!'
```
Прынцыпы працы бібліятэкі:
 - Ніякага выпраўлення памылак. 
 - Са зменаў правапісу толькі яўна пазначаецца транзітыўная мяккасць зычных, астатняе пры канвертацыі захоўваецца роўна з тымі ж асаблівасцямі правапісу і памылкамі, якія былі да канвертацыі. Прычым, пазначэнне мяккасці пры жаданні можна адключыць (гл. прыклад вышэй)
 - Кірылічныя сімвалы, якім адпавядае некалькі лацінскіх сімвалаў пры трансляцыі вялікіх літар маюць вялікай толькі першую літару ў пары (Chleb, Jan), што можа быць праблемай у выпадках, калі гэта не слова з вялікай літары ці абрэвіятура, а проста нешта напісанае КАПСАМ. Бо атрымаецца ChLEB, JaN.

## Анлайн канвертар
У якасці ўзору ўжывання бібліятэкі ці анлайн канвертара створанага на яе аснове магу прапанаваць паглядзець на сайт [latynkatar.org](https://latynkatar.org). Зыходнікі даступныя [тут](https://github.com/latynkatar/latynkatar_site).

## Ліцэнзія
Copyright група Łatynkatar, 2025

[![LGPL v3.0](https://www.gnu.org/graphics/lgplv3-with-text-154x68.png)](https://github.com/latynkatar/latynkatar/blob/main/LICENSE) ад [GNU](https://www.gnu.org/licenses/lgpl-3.0.html)