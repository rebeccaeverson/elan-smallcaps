# elan-smallcaps
Parse an ELAN glossed tier into Latex with small caps

## How to run

```
python add_smallcaps.py <ELAN file> <tier name> <file with grammatical elements>
```

Example:

```
python add_smallcaps.py test.txt u-gl elements.txt
```

## Output

Given a file with this structure:

```
utterance   	mahta tei ihpurawe an ma'su wenu ni'kamarenin
u-mb        	ma-ta te-i ipura-we an ma'su wenu ni'kamaren-in
u-gl        	what-int say-hort.1ex.mn now-dsc2 an hesit manioc.beer word-ind.3mn
spa         	este para preparar el masato
TC          	00:00:23.896 - 00:00:27.508


utterance   	wenu yani'patera
u-mb        	wenu ya-ni'-pate-ra
u-gl        	manioc.beer des-make-seq.imprs-abl
spa         	cuando se quiere preparar el masato
TC          	00:00:28.093 - 00:00:29.888


utterance   	pa'ne ta'shirechin ki'sha wa'tere
u-mb        	pa'-ne ta'shire-chin ki'sha wa'te-re
u-gl        	go-ind.imprs morning-dsc3 cassava pull.from.root-ind.imprs
spa         	se va en la mañana ,a sacar yuca
TC          	00:00:30.008 - 00:00:33.058
```

And a grammatical elements file:

```
int
hort.1ex.mn
dsc2
ind.3mn
seq.imprs
abl
ind.imprs
dsc3
ind.imprs
prog
sub.imprs
loc
sub.3mn
```

The output will look like:

```
what-\textsc{int} say-\textsc{hort.1ex.mn} now-\textsc{dsc2} an hesit manioc.beer word-\textsc{ind.3mn}
manioc.beer des-make-\textsc{seq.imprs}-\textsc{abl}
go-\textsc{ind.imprs} morning-\textsc{dsc3} cassava pull.from.root-\textsc{ind.imprs}
```
