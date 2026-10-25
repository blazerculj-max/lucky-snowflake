# Lucky Snowflake

Gecko simulator v spomin na Luckyja Snowflakea, leopardjega gekona barvne različice mack snow, ki je odšel 24. oktobra 2026. V tem terariju živi naprej.

## Kako odpreš igro

**Igraj na spletu: https://blazerculj-max.github.io/lucky-snowflake/**

Lahko pa odpreš `index.html` v brskalniku. Igra deluje tudi brez interneta, le pisave se takrat zamenjajo s sistemskimi.

Različica v Claudu (zasebna, deliš jo v meniju Share): https://claude.ai/artifact/QJgFoCrq2o9zoc2QFuJMNN

## Kako urejaš

- Vsa koda igre je v `src/lucky.html`. Fotografije so v njej označene z `__IMG1__`, `__IMG2__` in `__IMG3__`.
- Fotografije so v mapi `slike/`.
- Po vsaki spremembi zaženi `python3 build.py`. Skripta zgradi `index.html` (samostojna stran) in `dist/artifact.html` (za objavo kot Claude artifact).

## Kaj je v igri

- **Terarij od zgoraj:** topla stran z ogrevalno ploščo in hladna stran, oznaki s temperaturo, tri skrivališča, posoda z vodo, skodelica z mokarji in umetna lobanja.
- **Lucky:** proceduralno narisan po fotografijah, rumen s pegami in rahlimi vijoličnimi zaplatami. Odrašča od črno-belega mladiča (osem noči).
- **Njegove navade:** kuka skozi oko lobanje in praska po steklu, ko hoče ven.
- **Življenje v terariju:** lov na čričke, hranjenje s pinceto, mokarji, pitje, levitev, kakanje in lulanje v kotičku, dan in noč (po želji po resnični uri).
- **Drugi prizori:** sprehod po sivem kavču s skodelico in počitek v dlani, kjer ga lahko božaš.
- **Meni:** album s fotografijami in statistiko, samodejni dnevnik vsake noči, spominska knjiga, svečka in nastavitve.
- **Nočna lučka:** samo terarij čez cel zaslon, Lucky živi sam.

## Kje se kaj shrani

- Napredek igre in dnevnik: v brskalniku (`localStorage`).
- Spomini in svečke: v različici v Claudu v bazi artifacta, kjer jih vidijo vsi, s katerimi deliš igro; na spletni strani in v lokalni kopiji samo v brskalniku.
