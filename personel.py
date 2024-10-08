import abc
from abc import ABC,abstractmethod 
class person(ABC):
    name=""
    famili=""
    age=0
    jens=bool
    tel=''
    @abstractmethod
    def __init__(self,name,famili,age,jens,tel) -> None:
        self.name=name
        self.famili=famili
        self.age=age
        self.jens=jens
        self.tel=tel
        
class company():
    name=""
    place=""
    kala=''
    price=''
    email=""
    phone=""
    fax=""
    Moshtariyan=[]
    Taminkonandegan=[]   
    personels=[] 
    hesabdar=''
    boss_All=''
    def __init__(self,name,place,kala,price,phone) -> None:
        self.name=name
        self.place=place
        self.kala=kala
        self.price=price 
        self.phone=phone
        self.Moshtariyan=[]
        self.Taminkonandegan=[]
        self.personels=[]
    def Add_Moshtariyan(self,moshtari):
        self.Moshtariyan.append(moshtari)    
    def Show_Moshtari(self):
        for item in self.Moshtariyan:        
            print(f"list moshtariyan: {item.name} {item.famili} kalaye sefarshi shoma {item.kala} hast va tedad kala {item.number_kala} adad mibashad  ba ghimat {item.price}$")         
    def Add_taminkonande(self,taminkonande):
        self.Taminkonandegan.append(taminkonande) 
    def Show_taminkonande(self):
        for item in self.Taminkonandegan:
            print(f"list taminkonandegan {item.name} tahiye shode az {item.mavad_Avaliye} ba ghimate {item.price_mavad_avaliye}$ ba tahvil {item.tahvil}")     
    def Add_personel(self,personel):
        self.personels.append(personel) 
    def Show_personel(self):
        for item in self.personels:
            print(f"list karkonan {item.name} {item.famili} {item.takhasos}")                             
class personel(person):
    takhasos=''
    saatKar=0
    dastmozd=''
    history_job=0 
    hesabdar='' 
    boss_All=''  
    def __init__(self, name, famili,takhasos,saatKar,dastmozd) -> None:
        self.name=name
        self.famili=famili
        self.takhasos=takhasos
        self.saatKar=saatKar
        self.dastmozd=dastmozd
class moshtari(person):
    History_shopping=""
    addres=""
    kala=""
    price=""
    number_kala=0
    companys=[]
    hesabdari=''
    def __init__(self,name,famili,kala,price,number_kala) -> None:
        self.name=name
        self.famili=famili
        self.kala=kala
        self.price=price
        self.number_kala=number_kala
        self.companys=[]
    def Add_Company(self,company):
        self.companys.append(company)    
    def Show_company(self):
        for item in self.companys:
            print(f"{item.name} {item.place} {item.kala} {item.price}")    
class Tamin(person):
    mavad_Avaliye=''
    price_mavad_avaliye=0
    tahvil=0
    forshandegan=''
    companys=[]
    hesabdar=''
    def __init__(self,name,mavad_Avaliye,price_mavad_avaliye,tahvil) -> None:
        self.name=name
        self.mavad_Avaliye=mavad_Avaliye
        self.price_mavad_avaliye=price_mavad_avaliye
        self.tahvil=tahvil
        self.companys=[]
    def Add_Company(self,company):
        self.companys.append(company)    
    def Show_company(self):
        for item in self.companys:
            print(f"{item.name} {item.place} {item.kala} {item.price}")    
    
class Hesabdari(person):
    tasviye_Moshtari= bool   
    tasviye_personel= bool   
    tasviye_Ba_taminkonnde= bool   
    Moshtariyan=[]
    Taminkonandegan=[]    
    personels=[]
    boss_All='' 
    def __init__(self,name,famili) -> None:
        self.name=name
        self.famili=famili
        self.Moshtariyan=[]
        self.Taminkonandegan=[]
        self.personels=[]
    def Add_Moshtariyan(self,moshtari):
        self.Moshtariyan.append(moshtari)    
    def Show_Moshtari(self):
        for item in self.Moshtariyan:        
            print(f"{item.name} {item.famili} {item.kala} {item.number_kala} {item.price}")    
    def Add_taminkonande(self,taminkonande):
        self.Taminkonandegan.append(taminkonande) 
    def Show_taminkonande(self):
        for item in self.Taminkonandegan:
            print(f"{item.name} {item.mavad_Avaliye} {item.price_mavad_avaliye} {item.tahvil}")                       
    def Add_personel(self,personel):
        self.personels.append(personel) 
    def Show_personel(self):
        for item in self.personels:
            print(f"{item.name} {item.famili} {item.takhasos}")                             
    
class Boss_company(person):
    takhasos=""
    history_jobs=""
    jobs_reward=""
    Modiriyat=''
    Moshtariyan=[]    
    Taminkonandegan=[]  
    personels=[]       
    hesabdar=''
    def __init__(self,name,famili,takhasos,history_jobs) -> None:
        self.name=name
        self.famili=famili
        self.takhasos=takhasos
        self.history_jobs=history_jobs
        self.Moshtariyan=[]
        self.Taminkonandegan=[]
        self.personels=[]
    def Add_Moshtariyan(self,moshtari):
        self.Moshtariyan.append(moshtari)
    def Show_Moshtari(self):
        for item in self.Moshtariyan:        
            print(f"{item.name} {item.famili} {item.kala} {item.number_kala} {item.price}")    
    def Add_taminkonande(self,taminkonande):
        self.Taminkonandegan.append(taminkonande) 
    def Show_taminkonande(self):
        for item in self.Taminkonandegan:
            print(f"{item.name} {item.mavad_Avaliye} {item.price_mavad_avaliye} {item.tahvil}")         
    def Add_personel(self,personel):
        self.personels.append(personel) 
    def Show_personel(self):
        for item in self.personels:
            print(f"{item.name} {item.famili} {item.takhasos}")                             
# companyنمونه گیری از کلاس         
company1=company("samsung","south korea","mobile & pc ",8500,123456)    
company2=company("xiaomi","china","mobile & pc ",7500,123456)    
company3=company("appel","usa","mobile & pc ",10500,123456)    
company4=company("meta","usa","social network",145000,123456)    
company5=company("souni","south korea & china","mobile & Game console  ",9500,123456)    
company6=company("pixel","usa","mobile",9000,123456)    
# personelنمونه گیری از کلاس 
personel1=personel("mark","zakerberg","Boss",8,5000000000)
personel2=personel("emma","zilinski","secretary",10,4200)
personel3=personel("edmond","mikhtariyan","driver",12,4500)
personel4=personel("morad","onder","cook",12,3500)
personel5=personel("yorgen","ta","Data spiecialist",10,4800)
#moshtariنمونه گیری از 
moshtari1=moshtari("sadra","saidi","mobil",1500,1)
moshtari2=moshtari("yavar","toghrol","pc",1000,2)
moshtari3=moshtari("bijan","mortazavi","consol",1200,1)
moshtari4=moshtari("bayram","bagali","consol",1200,1)
moshtari5=moshtari("amirmansor","pashazade","pc",800,1)
# taminنمونه گیری از کلاس 
Tamin1=Tamin("app_Stor","game",15,"haman lahze")
Tamin2=Tamin("google play","game",15,"haman lahze")
Tamin3=Tamin("mayket","software",15,"haman lahze")
Tamin4=Tamin("netfilx","film",185,"haman lahze")
# hesabdarنمونه گیری از کلاس 
Hesabdar1=Hesabdari("khanom","shirzad")
Hesabdar2=Hesabdari("mr","gholami")
Hesabdar3=Hesabdari("mr","khrad")
Hesabdar4=Hesabdari("mr","hekmat yar")
# نمونه گیری از کلاس رییس 
boss1=Boss_company("elon","mask","shopping mobile",20)
boss2=Boss_company("jef","bizos","shopping kala",25)
boss3=Boss_company("bil","gets","shopping",30)
boss4=Boss_company("varen","bafet","shopping saham",30)
#صدا زدن و اجرای دستور پرینت
#اجرای دستورات شرکت
company1.Add_Moshtariyan(moshtari1)
company1.Add_Moshtariyan(moshtari2)
company1.Add_Moshtariyan(moshtari3)
company1.Show_Moshtari()
print(35*" * ")
company1.hesabdar=Hesabdar1
company2.Add_personel(personel1)
company2.Add_personel(personel2)
company2.Add_personel(personel3)
company2.Show_personel()
print(35*" * ")
company3.Add_taminkonande(Tamin1)
company3.Add_taminkonande(Tamin2)
company3.Add_taminkonande(Tamin3)
company3.Add_taminkonande(Tamin4)
company3.Show_taminkonande()
print("Hesabdar Company:",company1.hesabdar.name,company1.hesabdar.famili)
company1.boss_All=boss1
print("Boss:",company1.boss_All.name,company1.boss_All.famili)
# personelصدا زدن و اجرای دستورات کلاس 
personel1.hesabdar=Hesabdar1
print("Hesabdar for personel:",personel1.hesabdar.name,company1.hesabdar.famili)
# moshtariاجرای دستورات 
print(" * "*35)
moshtari1.Add_Company(company1)
moshtari1.Add_Company(company2)
moshtari1.Add_Company(company3)
moshtari1.Show_company()
print(" * "*35)
moshtari.hesabdari=Hesabdar2
print("hesabdar:",moshtari2.hesabdari.name,moshtari2.hesabdari.famili)
print(" $ "*35)
#اجرای دستورات حسابدار
Hesabdar1.Add_Moshtariyan(moshtari1)
Hesabdar1.Add_Moshtariyan(moshtari2)
Hesabdar1.Add_Moshtariyan(moshtari3)
Hesabdar1.Show_Moshtari()
print(35*" * ")
Hesabdar2.hesabdar=Hesabdar1
Hesabdar2.Add_personel(personel1)
Hesabdar2.Add_personel(personel2)
Hesabdar2.Add_personel(personel3)
Hesabdar2.Show_personel()
print(35*" * ")
Hesabdar2.Add_taminkonande(Tamin1)
Hesabdar2.Add_taminkonande(Tamin2)
Hesabdar2.Add_taminkonande(Tamin3)
Hesabdar2.Add_taminkonande(Tamin4)
Hesabdar2.Show_taminkonande()
Hesabdar4.boss_All=boss3
print("Boss All:",Hesabdar4.boss_All.name,Hesabdar4.boss_All.famili)
print(" * "*35)
#اجرای دستورات رییس
boss1.Add_Moshtariyan(moshtari1)
boss1.Add_Moshtariyan(moshtari2)
boss1.Add_Moshtariyan(moshtari3)
boss1.Show_Moshtari()
print(35*" * ")
boss2.hesabdar=Hesabdar1
boss2.Add_personel(personel1)
boss2.Add_personel(personel2)
boss2.Add_personel(personel3)
boss2.Show_personel()
print(35*" * ")
boss3.Add_taminkonande(Tamin1)
boss3.Add_taminkonande(Tamin2)
boss3.Add_taminkonande(Tamin3)
boss3.Add_taminkonande(Tamin4)
boss3.Show_taminkonande()
print(" * "*35)
boss4.hesabdari=Hesabdar3
print("hesabdar is :",boss4.hesabdari.name,boss4.hesabdari.famili)


