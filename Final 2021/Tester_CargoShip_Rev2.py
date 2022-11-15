
'''
Name       : Don't sink my Battle Ship
Author     : Torri Baptista
Version    : 2.0
Due Date   : 12/13/2021
Filename   : Tester_CargoShip_Rev2.py (Cargo_Ship_Class_Rev2.py)
Purpose    : User will play guess letters for a Hidden Word
'''


from Cargo_Ship_Class_Rev2 import CargoShip
import torri_Library1 as Lib1
# ======================================== #

def main():
 
    Lib1.printHeader(__doc__)
    
    myShip = CargoShip("Baptista_Torri_Final_Project_Words.txt")
    
    #myShip = CargoShip("three_Words.txt")

if __name__ == "__main__":
    main()
