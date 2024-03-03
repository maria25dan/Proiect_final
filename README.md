# Proiect_final

Acesta este proiectul pentru finalizarea cursului de Testare Automata

Site-ul pe care s-au facut testele este: https://the-internet.herokuapp.com/login
  Am implementat clasa TestLoghin care moștenește unittest.Test
  from unittest import TestCase

Ulterior am creat diferite funcții pentru a testa urmatoarele :

Testul 1 - Verifică dacă noul url e corect

Test 2 - Verifică dacă page title e corect

Test 3 - Verifică textul de pe elementul xpath=//h2 e corect și verifică dacă butonul de login este displayed

Test 4 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

Test 5 - Lasă goale câmpurile user și pass, verifică dacă eroarea e displayed

Test 6 - Completează cu user și pass invalide, verifică dacă mesajul de pe eroare e correct

Test 7 - Lasă goale user și pass, verifică dacă eroarea a dispărut

Test 8 - În lista label, se verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)

Test 9 - Completează cu user și pass valide, verifică ca noul url CONTINE /secure, am folosit un explicit wait pentru elementul cu clasa ’flash succes’, apoi am verifică dacă elementul cu clasa=’flash succes’ este displayed, verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

Test 10 - Completează cu user și pass valide, verifică dacă a ajuns pe https://the-internet.herokuapp.com/login


