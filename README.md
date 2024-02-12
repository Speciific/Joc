**Yams (Yahtzee)**

Se va concepe și realiza o pereche de aplicații client-server, care vor implementa o varianta simplificată a jocului Yams. Regulile jocului pe care se va baza aplicația sunt următoarele:
1. Jucătorul are la dispoziție 5 zaruri și tabel următor în care se va completa punctajul obținut

|Rând   |Explicație                                                                                                                            |Punctaj|
|-------|--------------------------------------------------------------------------------------------------------------------------------------|-------|
|N1     |Aduni cât mai mulți de 1 și scrii suma lor. De ex. [1,2,1,3,3] -> 2                                                                   |       |
|N2     |Aduni cât mai mulți de 2 și scrii suma lor                                                                                            |       |
|N3     |Aduni cât mai mulți de 3 și scrii suma lor                                                                                            |       |
|N4     |Aduni cât mai mulți de 4 și scrii suma lor                                                                                            |       |
|N5     |Aduni cât mai mulți de 5 și scrii suma lor                                                                                            |       |
|N6     |Aduni cât mai mulți de 6 și scrii suma lor                                                                                            |       |
|JOKER  |Se trece suma tuturor zarurilor                                                                                                       |       |
|TRIPLA |Trebuie să obții trei zaruri cu aceeași valoare. Se trece suma tuturor zarurilor. De ex. [5,5,5,2,3] -> 21                            |       |
|CHINTA |Zarurile trebuie să aibă valori consecutive. Se trec 20 de puncte. De ex. pentru [2,3,1,5,4] sau [6,2,3,5,4] -> 20                    |       |
|FULL   |Trebuie să obții o configurație formată dintr-o triplă și o pereche. Se trec 30 de puncte. De ex. [1,2,1,1,2] ->30 sau [6,4,4,4,6]->30|       |
|CAREU  |Trebuie să obții patru zaruri cu aceeași valoare. Se trec 40 de puncte. De ex. [1,2,1,1,1] ->40 sau [6,6,6,4,6]->40                   |       |
|YAMS   |Toate cele cinci zaruri trebuie sa aibă aceeași valoare. Se trec 50 de puncte. De ex. [1,1,1,1,1] ->50 sau [5,5,5,5,5]->50            |       |

Punctajul total se obține prin adunarea valorilor completate în coloana „Punctaj”. Dacă suma valorilor aferente N1, ..., N6 este de minim 63 atunci se adaugă la total un bonus de 50 de puncte. Scopul jocului este obținerea unui punctaj total cât mai mare

2. Jucătorul aruncă toate cele 5 zaruri și în funcție de ceea ce a ieșit, fie se oprește și notează punctajul în tabel, fie alege câteva zaruri din cele 5, iar pe restul le relansează. Se pot relansa zarurile de maxim două ori.

Exemplu: Jucătorul aruncă zarurile. Numerele apărute sunt [1,1,3,5,6]. Pune deoparte [1,1] și relansează [3,5,6]. Numerele apărute sunt [1,2,5]. Pune deoparte „1” (acum are trei de „1” puși deoparte) și relansează [2,5]. Numerele apărute sunt [1,4]. Rezultatul final este deci [1,1,1,1,4]. Jucătorul alege să scrie 40 pe linia CAREU. Acesta este cel mai convenabil punctaj, însă putea scrie și 4 în dreptul rubricii N1, 8 pe linia TRIPLET sau tot 8 pe linia JOKER.
3. Jocul se încheie când toate coloanele sunt pline
4. Dacă jucătorul ajunge în situația în care mai sunt de completat rânduri care presupun o anumită configurație a zarurilor și aceasta nu se poate obține din cele trei aruncări totale jucătorul va fi obligat sa treacă valoarea zero.

Din perspectiva implementării, jocul presupune că jucătorul se folosește de aplicația client și va avea următoarea desfășurare:
1. Jucătorul (prin intermediul aplicației client), în momentul în care dorește să înceapă un joc, trimite serverului (prin tastare) mesajul START
2. Serverul răspunde trimițând ca mesaj de răspuns tabelul cu punctajul jucătorului, care în această fază va fi necompletat:

N1 ----->
<br/>N2 ----->
<br/>N3 ----->
<br/>N4 ----->
<br/>N5 ----->
<br/>N6 ----->
<br/>BONUS -->
<br/>JOKER -->
<br/>TRIPLA ->
<br/>CHINTA ->
<br/>FULL --->
<br/>CAREU -->
<br/>YAMS --->
<br/>TOTAL -->

3. Jucătorul trimite comanda ARUNCA
4. Serverul răspunde printr-o listă cu 5 elemente, care conține în ordine crescătoare, valorile celor 5 zaruri (valori generate aleator de către server) și numărul de relansări posibile. De exemplu:

[1, 1, 3, 5, 6] R=2

5. Conform regulilor, jucătorul are următoarele opțiuni:
<br/>a. Se oprește, și decide să treacă punctajul pe un anumit rând din tabel
<br/>b. Alege și păstrează anumite zaruri iar pe restul le relansează
6. Dacă jucătorul decide să completeze punctajul (situația 5.a.), atunci trimite către server denumirea rândului pe care dorește să completeze punctajul. De exemplu, jucătorul trimite N1 pentru a indica faptul că dorește să treacă valoarea 2 pe rândul N1 din tabel. Serverul va răspunde prin transmiterea tabelului cu punctajul jucătorului. De exemplu:

N1 -----> 2
<br/>N2 ----->
<br/>N3 ----->
<br/>N4 ----->
<br/>N5 ----->
<br/>N6 ----->
<br/>BONUS --> 0
<br/>JOKER -->
<br/>TRIPLA ->
<br/>CHINTA ->
<br/>FULL --->
<br/>CAREU -->
<br/>YAMS --->
<br/>TOTAL --> 2

In funcție de rândul ales, serverul va face determinarea corectă a punctajului care trebuie completat pe rândul respectiv și va actualiza tabelul cu punctajul, calculând eventualul bonus și totalul.

7. Dacă jucătorul se află în situația 5.b. atunci va indica prin comanda KEEP lista cu valorile pe care le va păstra. Serverul va genera alte valori pentru zarurile care se vor relansa și va răspunde printr-o listă conținând noile valori și numărul de relansări posibile. De exemplu:

Jucătorul trimite KEEP [1,1]
Serverul generează noi valori în locul lui 3,5,6 (de la pasul 4) și retrimite noua listă, ordonată crescător, ca răspuns:
1,2,5] R=1

8. Jucătorul poate relansa zarurile de maxim două ori. De exemplu:

Jucătorul trimite KEEP [1]
Serverul generează noi valori în locul lui 2,5 (de la pasul 7) și retrimite noua listă, ordonată crescător, ca răspuns:
1,4] R=0

9. Daca numărul de relansări afișat este 0 atunci jucătorul este obligat să completeze punctajul realizat în tabel
10. Jucătorul poate solicita în orice moment serverului să-i trimită situația punctajului prin trimiterea comenzii PUNCTAJ, iar serverul va returna tabelul cu valorile completate până la momentul respectiv
11. Orice comandă tastată greșit și trimisă serverului trebuie sesizată de acesta și raportată jucătorului prin răspunsul COMANDA ERONATA
12. Jocul se încheie la completarea întregului tabel sau când jucătorul abandonează. Abandonul se poate cere oricând prin trimiterea comenzii ABANDON. Dacă jocul se încheie normal, după completarea ultimului rând din tabel serverul va afișa tabelul cu punctajul realizat, iar clientul își va înceta execuția. Serverul va rămâne activ pregătit pentru o nouă sesiune de Yams.
