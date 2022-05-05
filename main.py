
l_akcji = int(input())

egzemplarze = {}
uzytkownicy = {}

class Ksiazka:
    def __init__(self,data):
        self.nazwa = data[0]
        self.autor = data[1]
        self.rok_produkcji = data[2]

    def dodaj_egzemplarz(self):
        
        if str((self.nazwa, self.autor)) in egzemplarze.keys():
            egzemplarze[str((self.nazwa, self.autor))]+=1
        else:
            egzemplarze[str((self.nazwa, self.autor))]=1

        return True



class Uzytkownik:
    def __init__(self,nazwa,ksiazka):
        self.nazwa = nazwa
        self.ksiazka = ksiazka

    def jest_w_bazie(self):
        if self.nazwa in uzytkownicy.keys():
            return True
        else:
            return False

    def czy_mozna_wypozyczyc(self):
        if (len(uzytkownicy[self.nazwa])<3) and (self.ksiazka not in uzytkownicy[self.nazwa]):
            return True
        return False
    
    def wypozycz(self):
        if self.ksiazka in [eval(x)[0] for x in egzemplarze.keys()]:
            for ee_key,ee_value in egzemplarze.items():
                if eval(ee_key)[0] == self.ksiazka:
                    if egzemplarze[ee_key]>0:
                        egzemplarze[ee_key]-=1
                        uzytkownicy[self.nazwa].append(self.ksiazka)
                        return True
        return False
    
    def odddaj(self):
        if self.ksiazka in uzytkownicy[self.nazwa]:
            uzytkownicy[self.nazwa].remove(self.ksiazka)
            for ee_key,ee_value in egzemplarze.items():
                if eval(ee_key)[0] == self.ksiazka:
                    egzemplarze[ee_key]+=1
            return True
        return False

for aa in range(l_akcji):
    akcja = eval(input())

    akcja = tuple([str(x).strip() for x in akcja])

    if akcja[0]=='dodaj':
        print(Ksiazka(akcja[1:]).dodaj_egzemplarz())

        
    elif akcja[0] == 'wypozycz':
        if akcja[1] not in uzytkownicy.keys():
            uzytkownicy[akcja[1]] = []
        if Uzytkownik(akcja[1],akcja[2]).czy_mozna_wypozyczyc() == False:
            print(Uzytkownik(akcja[1],akcja[2]).czy_mozna_wypozyczyc())
        else:
            print(Uzytkownik(akcja[1],akcja[2]).wypozycz())
    
    
    elif akcja[0] == 'oddaj':

        print(Uzytkownik(akcja[1],akcja[2]).odddaj())
        
    else:
        raise Exception('zły rodzaj akcji')




