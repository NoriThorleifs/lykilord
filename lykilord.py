import argparse
from islenska import Bin
from random import randint
from unidecode import unidecode

def orðaFabrikkan(b, dýpt):
    """
    BÍN er íslensk orðabók, við sækjum gögn með handahófsvöldum tölum.
    """
    if dýpt > 100:
        # Ef það mistekst 100 sinnum að sækja orð, þá hlýtur að vera villa í BÍn.
        raise TimeoutError("Eitthvað fór úrskeiðis við að sækja gögn frá BÍN.")
    dýpt += 1
    try:
        return unidecode(b.lookup_id(randint(0, 300000))[0].bmynd).capitalize()
    except:
        # Sumar tölur eru ekki með orð tengd þeim, þannig við reynum það til við fáum orð.
        return orðaFabrikkan(b, dýpt)
    
def afhöfða(strengur):
    """
    Fjarlægir fremsta stafinn í strengi. Skilar stafinum og afgangi strengsins.
    """
    höfuð = strengur[0]
    strengur = strengur[1:]
    return höfuð, strengur

def lykilorðaGerðin(snið:str = None):
    # Býr til nýtt tilvik af BÍN og hleður aðeins orð í nefnifalli.
    b = Bin(only_bin=True)
    parser = argparse.ArgumentParser(description="Býr til ný lykilorð af handahófi")
    parser.add_argument("-s", "--snið", help="Ræður sniði og röðun lykilorðsins, 'o' býr til orð sem eru með stóran staf í fyrsta.\n'n' býr til tölustaf frá 0 til 9.\n'.' bætir við punkti. Sniðið verður 'oo.nn' ef ekkert er valið.", default="oo.nn", type=str)
    args = parser.parse_args()

    # lo heldur um lykilorðið sjálft
    lo = ""
    if snið == None:
        snið = args.snið.lower()
    else:
        snið = snið.lower()
    try:
        while len(snið) >= 1:
            # Tekur fremsta stafinn úr sniðinu
            s, snið = afhöfða(snið)
            # Bætir við orði
            if s == "o":
                orð = orðaFabrikkan(b, 0)
                lo += orð 
            # Bætir við tölustafi
            elif s == "n":
                lo += str(randint(0,9))
            # Bætir við punkti
            elif s == ".":
                lo += "." 
            else:
                raise ValueError
    except ValueError:
        print("sniðið má aðeins innihalda o, n eða punkt með engum bilum")
        return None
    return lo

if __name__ == "__main__":
    print(lykilorðaGerðin())



