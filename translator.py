

map = {'using':'uzywajac', 'namespace':'przestrzen_nazw', 'std':'standardowe', 'int':'calkowita', 'bool':'zerojedynkowy', 'return':'zwroc', 'main':'glowna', 'cout':'cwyjscie', 'cin':'cwejscie', 'for':'dla', 'while':'dopoki', 'switch':'przelacznik', 'case':'przypadek', 'if':'jezeli', 'else':'w_przeciwnym_wypadku', 'string':'ciag_znakow', 'float':'zmiennoprzecinkowa', 'double':'podwojna_zmiennoprzecinkowa', 'long':'duza', 'char':'znak', 'struct':'struktura', 'pair':'para', 'make_pair':'zrob_para', 'map':'mapa', 'set':'zestaw', 'vector':'kontener', 'list':'lista', 'queue':'kolejka', 'priority_queue':'kolejka_priorytetowa', 'deque':'kolejka_dwustronna', 'stack':'stos', 'heap':'kopiec', 'push_back':'pchac_plecy', 'insert':'wstawic', 'pop':'wyciagnac', 'pop_back':'wyciagnac_plecy', 'find':'znajdz', 'push_front':'pchac_przod', 'upper_bound':'gorne_ograniczenie', 'lower_bound':'dolne_ograniczenie', 'first':'pierwszy', 'second':'drugi', 'class':'klasa', 'public':'publiczny', 'private':'prywatny', 'protected':'chroniony', 'scanf':'skanujf', 'printf':'drukujf', 'tie':'wezel', 'ios_base':'wejsciewyjsciestrumien_baza', 'sync_with_stdio':'synchronizuj_z_standardowymwejsciewyjscie', 'NULL':'ZERO', 'false':'falsz', 'true':'prawda', 'size':'rozmiar', 'length':'dlugosc', 'begin':'poczatek', 'end':'koniec', 'sort':'sortuj', 'qsort':'qsortuj', 'endl':'koniec_linii', 'void':'proznia', 'break':'zepsuj', 'continue':'kontynuuj', 'const':'staly'} 

plik = input()

val = open(plik, 'r').read()
out = open('translated.cpp', 'a')
out.write("#include <bits/stdc++.h>\n")
for o in map:
    out.write('#define ' + map[o] + ' ' + o +'\n')
    val = val.replace(o, map[o])

out.write(val)