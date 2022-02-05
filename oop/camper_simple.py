from auto import auto

class camper(auto):
    pass



# inizia il programma chiamante

if __name__ == "__main__":

    pippo = camper("pippo","Ford","Transit",2500, 1600, "giallo")

    marco = auto("marco","fiat","Bravo",2500, 200, "verde")

    print(pippo.scheda())
    print(marco.scheda())
  