from datetime import datetime

#TheMoscowTimes-Wednesday,October2,2002
mt = 'Wednesday,October2,2002'
mt_datetime = datetime.strptime(mt, '%A,%B%d,%Y')
print(mt_datetime)
#TheGuardian-Friday,11.10.13
gf = 'Friday,11.10.13'
gf_datetime = datetime.strptime(gf, '%A,%d.%m.%y')
print(gf_datetime)
#DailyNews-Thursday,18August1977
dn = 'Thursday,18August1977'
dn_datetime = datetime.strptime(dn, '%A,%d%B%Y')
print(dn_datetime)