from random import choice
import sys

sys.path.insert(0, "./..")
from champs import top, jungle, mid, adc, support

role_dict = {"top": top, "jungle": jungle, "mid": mid, "adc": adc, "ad": adc, "support" : support, "sup": support, "jung": jungle}
roles = ["top", "jungle", "mid", "adc", "support"]

def choose_champ(role):
    champ = choice(role)
    # if champ == "Jayce" and choice((0,1)):
        # champ = choice(role)
    return champ

def choose_role():
    return choice(roles)
    
def main(argv):
    if argv[0] == "-r":
        argv[0] = choose_role()
        print(argv[0])
    if not argv[0] in role_dict:
        raise Exception("Invalid Role {0}".format(argv[0]))
    print(choose_champ(role_dict[argv[0]]))
    
if __name__ == "__main__":
    main(sys.argv[1:])