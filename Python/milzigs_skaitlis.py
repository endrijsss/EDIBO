#! /usr/bin/python3.6

print("Ievadiet Skaitli")
# a =2**200000

#te ir tris darbibas - vertibas sagaidīšana, vertibas parveidosana, pieskirs$
#argument = input()
#int(argumnet)
#a = int(argument)

#pildot  int(input()) "bez izmeginajuma" programma var vienkarsi izlidot...
#tapec, lai "nelidotu", mes izmantosim try ... except ... finally konstrukci$
paziime = False
while not paziime:
#while pazime==False:
#while paziime!=True:
    try:
        a =  int( input() )
        paziime=true
    except:
        print("Diemžel cienijamais lietotaj to kas ievadits nevar",\
        "parveidot pa veselo tipa skaitli :-( ")
        print("Ludzu ievadiet skaitli velreiz")

paziime = True
while paziime:
    try:
        a = int( input() )
        print("a**100")
        print("Lūdzu ievadiet SKAITLI")
print("Šis teksts atrodas ārpus darbību bloka - pierakstīts bez",\
"atstarpēm priekšā, tāpēc tas parādīsies jebkurā gadijumā")

#if (a == int): print("a**100)
#print ("Ievadāmai vērtibai jābūt skaitlim")
#b=a**100
