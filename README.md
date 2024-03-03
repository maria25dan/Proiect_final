# Proiect_final
Acesta este proiectul pentru finalizarea cursului de Testare Automata
Site-ul pe care s-au facut testele este: https://the-internet.herokuapp.com/login
  Am implementat clasa TestLoghin care moștenește unittest.Test Case
fromunittest importTestCase
  Pachetul unitest este un framework. Acestmodulconțineclaselecare formeazăbazaunorcazurișisuite de testarespecifice(TestCase, TestSuiteetc.), precum șio clasăde bazatăfolosită la rulareatestelorșiraportarearezultatelor.
. Ulterior amcreatdiferitefuncțiipentruatestaurmatoarele:
  Testul1-Verifică dacă noul url e corect
  Test 2 -Verifică dacă page title e corect
  Test 3 -Verifică textul de pe elementul xpath=//h2 e corect și verifică dacă butonul de login este displayed
  Test 4 -Verificădacăatributulhrefal linkului‘Elemental Selenium’ e corect
  Test 5 -Lasăgoalecâmpurile user șipass, verificădacăeroareae displayed
  Test 6 -Completeazăcu user șipass invalide, verificădacămesajulde pe eroaree correct
  Test 7 -Lasăgoaleuser șipass, verificădacăeroareaa dispărut
  Test 8 -În lista label, se verificătextulca textulde pe elesăfie celașteptat(Username șiPassword)
  Test 9 -Completeazăcu user șipass valide, verificăca noulurlCONTINE /secure, am folosit un explicit wait pentruelementulcu clasa’flash succes’, apoi am verificădacăelementulcu clasa=’flash succes’ estedisplayed, verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
  Test 10 -Completeazăcu user șipass valide, verificădacăaajunspe https://the-internet.herokuapp.com/login
