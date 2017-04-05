from jsonParser import *

def main():
    list_activities, list_equip_activ = parse_activities()
    list_equipments = parse_equipments()
    list_installations = parse_installations()


if __name__ == '__main__':
    main()
