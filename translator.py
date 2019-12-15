map = {'sync_with_stdio':'synchronizuj_z_standardowymwejsciewyjscie', 'priority_queue':'kolejka_priorytetowa', 'lower_bound':'dolne_ograniczenie', 'upper_bound':'gorne_ograniczenie', 'push_front':'pchac_przod', 'namespace':'przestrzen_nazw', 'protected':'chroniony', 'push_back':'pchac_plecy', 'make_pair':'zrob_para', 'continue':'kontynuuj', 'pop_back':'wyciagnac_plecy', 'ios_base':'wejsciewyjsciestrumien_baza', 'private':'prywatny', 'printf':'drukujf', 'insert':'wstawic', 'return':'zwroc', 'second':'drugi', 'public':'publiczny', 'vector':'kontener', 'switch':'przelacznik', 'struct':'struktura', 'double':'podwojna_zmiennoprzecinkowa', 'length':'dlugosc', 'string':'ciag_znakow', 'using':'uzywajac', 'break':'zepsuj', 'scanf':'skanujf', 'false':'falsz', 'class':'klasa', 'first':'pierwszy', 'begin':'poczatek', 'const':'staly', 'qsort':'qsortuj', 'float':'zmiennoprzecinkowa', 'stack':'stos', 'while':'dopoki', 'deque':'kolejka_dwustronna', 'queue':'kolejka', 'void':'proznia', 'else':'w_przeciwnym_wypadku', 'size':'rozmiar', 'true':'prawda', 'long':'duza', 'NULL':'ZERO', 'char':'znak', 'pair':'para', 'sort':'sortuj', 'endl':'koniec_linii', 'case':'przypadek', 'list':'lista', 'cout':'cwyjscie', 'bool':'zerojedynkowy', 'find':'znajdz', 'heap':'kopiec', 'main':'glowna', 'end':'koniec', 'for':'dla', 'tie':'wezel', 'cin':'cwejscie', 'map':'mapa', 'std':'standardowe', 'set':'zestaw', 'int':'calkowita', 'pop':'wyciagnac', 'if':'jezeli'} 

plik = input()

val = open(plik, 'r').read()
out = open('translated.cpp', 'a')
out.write("#include <bits/stdc++.h>\n")
for o in map:
    out.write('#define ' + map[o] + ' ' + o +'\n')
    val = val.replace(o, map[o])

out.write(val)