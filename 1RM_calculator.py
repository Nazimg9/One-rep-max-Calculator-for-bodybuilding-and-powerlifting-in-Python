import math

def print_all(orm):
    print("95% of 1RM : " + str(0.95 * orm))
    print("90% of 1RM : " + str(0.9 * orm))
    print("85% of 1RM : " + str(0.85 * orm))
    print("80% of 1RM : " + str(0.80 * orm))
    print("75% of 1RM : " + str(0.75 * orm))
    print("70% of 1RM : " + str(0.70 * orm))

def epley(weight,reps):
    print("Epley Formula (1 rep max)")
    orm=float(weight*(1+reps/30))
    print("your One rep max : "+str(orm))
    print("-"*100)
    return orm

def Brzycki(weight,reps):
    print("Brzycki Formula (1 rep max)")
    if reps<2:
        print("***Note: For this formula reps should be more than ONE")
        orm=0
    else:
        orm=float(weight*(36/(37-reps)))
        print("your One rep max : "+str(orm))
        print("-" * 100)
    return orm

def Lander(weight,reps):
    print("Lander Formula (1 rep max)")
    orm=float(100*(weight/(101.3-2.67123*reps)))
    print("your One rep max : "+str(orm))
    print("-" * 100)
    return orm
def Mayhew(weight,reps):
    print("Mayhew Formula (1 rep max)")
    if reps<2:
        print("***Note: For this formula reps should be more than ONE")
        orm=0
    else:
        orm=float(100*weight/(52.2+41.9*math.exp(-0.055*reps)))
        print("your One rep max : "+str(orm))
        print("-" * 100)
    return orm

def Lombardi(weight,reps):
    print("Lombardi Formula (1 rep max)")
    orm=float(weight*reps**0.10)
    print("your One rep max : "+str(orm))
    print("-" * 100)
    return orm

def Wathen(weight,reps):
    print("Wathen Formula (1 rep max)")
    orm=float(100*weight/(48.8+53.8*math.exp(-0.075*reps)))
    print("your One rep max : "+str(orm))
    print("-" * 100)
    return orm

def OConner(weight,reps):
    print("OConner Formula (1 rep max)")
    if reps<2:
        print("***Note: For this formula reps should be more than ONE")
        orm=0
    else:
        orm=float(weight*(1+0.025*reps))
        print("your One rep max : "+str(orm))
        print("-" * 100)
    return orm


weight= float(input("Enter weight lifted : "))
reps=float(input("Enter total reps performed : "))

epley_orm=epley(weight,reps)
Brzycki_orm=Brzycki(weight,reps)
Lander_orm=Lander(weight,reps)
Mayhew_orm=Mayhew(weight,reps)
Lombardi_orm=Lombardi(weight,reps)
Wathen_orm=Wathen(weight,reps)
OConner_orm=OConner(weight,reps)
if reps<2:
    avg_orm = ((epley_orm + Brzycki_orm + Lander_orm + Mayhew_orm + Lombardi_orm + Wathen_orm
               + OConner_orm) /4).__round__()
else:
    avg_orm=((epley_orm+Brzycki_orm+Lander_orm+Mayhew_orm+Lombardi_orm+Wathen_orm
         +OConner_orm)/7).__round__()
print("*"*100+"\nAverage possible One rep max By all formulas : "+str(avg_orm))
print_all(avg_orm)
