from random import choice
import sys

sys.path.insert(0, "./..")
from champs import top, jungle, mid, adc, support

role_dict = {"top": top, "jungle": jungle, "mid": mid, "adc": adc, "ad": adc, "support" : support, "sup": support, "jung": jungle}
roles = ["top", "jungle", "mid", "adc", "support"]

def choose_champ(role):
    """Returns a randomly chosen champion from the given
    role's champion pool.
    """
    champ = choice(role)
    # if champ == "Jayce" and choice((0,1)):
        # champ = choice(role)
    return champ

def choose_role():
    """Return a random role"""
    return choice(roles)
    
def main():
    role = input("Choose a role (-r for random):  ")
    if role == "-r":
        role = choose_role()
        print(role)
    if not role in role_dict:
        raise Exception("Invalid Role {0}".format(role))
    print(choose_champ(role_dict[role]))
    input("Press enter to exit...")
    
main()