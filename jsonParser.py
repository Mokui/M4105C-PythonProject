import json
from Activity import Activity
from Equipment import Equipment
from Installation import Installation
from EquipActiv import EquipActiv
from pprint import pprint



def parse_activities():
    """
    Parsing datas from activities.json and creating Activity and EquipActiv
    objects from those datas
    """
    data_file = open('files/activities.json')
    datas = json.load(data_file)
    datas_list = datas["data"]

    activities = []
    equip_activities = []
    id_set = []

    for data in datas_list :
        code = data["ActCode"]
        name = data["ActLib"]
        equip_id = data["EquipementId"]

        if code == None :
            continue

        equip_activity = EquipActiv(code, equip_id)
        equip_activities.append(equip_activity)

        if code in id_set :
            continue

        activity = Activity(code,name)
        activities.append(activity)
        id_set.append(code)

    return activities, equip_activities

def parse_installations():
    """
    Parsing datas from installations.json and creating Installation objects
    from those datas
    """
    data_file = open('files/installations.json')
    datas = json.load(data_file)

    datas_list = datas["data"]

    installations = []
    for data in datas_list :
        code = data["InsNumeroInstall"]
        name = data["geo"]["name"]
        address =  None

        if code == None :
            continue

        if data["InsNoVoie"] is not None :
            if data["InsLibelleVoie"] is not None:
                address = data["InsNoVoie"] + " " + data["InsLibelleVoie"]
        else :
            if data["InsLibelleVoie"] is not None:
                address = data["InsLibelleVoie"]

        postal_code = data["InsCodePostal"]
        city = data["ComLib"]
        latitude = data["_l"][1]
        longitude = data["_l"][0]

        installation = Installation(code, name, address, postal_code, city, latitude, longitude)
        installations.append(installation)

    return installations


def parse_equipments():
    """
    Parsing datas from equipments.json and creating Equipment objects
    from those datas
    """
    data_file = open('files/equipments.json')
    datas = json.load(data_file)

    datas_list = datas["data"]
    equipments = []

    for data in datas_list :

        code = data["EquipementId"]
        name = data["EquNom"]
        familly = data["FamilleFicheLib"]
        installation_id = data["InsNumeroInstall"]

        if code == None :
            continue

        equipment = Equipment(code, name, familly, installation_id)
        equipments.append(equipment)

    return equipments

# JSON EXAMPLE
# { "EquSanitaireSportif" : "Oui" , "EquErpPA" : "Oui" , "EquEclairage" : "Non" , "EquHauteurEvolution" :  null  , "EquNatSurfaceBassin" :  null  , "EquNatureAcPubRout" :  null  , "EquSurfaceEvolution" : "900.00" , "EquNatLongueurBassin" :  null  , "EquSono" : "Non" , "GestionTypeProprietaireSecLib" : "Commune" , "EquConfortSolarium" : "Non" , "EquNatTobog" :  null  , "EquNatNbT1" :  null  , "EquUtilAutre" :  null  , "EquTravauxRealVetuste" : "Non" , "EquNatNbT3" :  null  , "EquNatSurv" :  null  , "EquConfortAutre" : "Non" , "EquNatSonorisationSub" :  null  , "EquErpCategorie" : "5" , "EquAccesHandisAire" : "Non" , "EquAccueilReception" : "Non" , "EquAccueilBuvette" : "Non" , "GestionTypeProprietairePrincLib" : "Commune" , "NatureLibelle" : "D<E9>couvert" , "EquDateMaj" : "2015-11-02 00:00:00" , "EquAccueilAutre" : "Non" , "EquHauteurSurfaceEvo" :  null  , "EquNatFormeLib" :  null  , "EquAccesHandisAucun" : "Oui" , "EquErpOA" : "Non" , "EquDouche" : "Oui" , "EquAccesHandimVestiaire" : "Non" , "EquNatEclSub" :  null  , "EquNatureLocPed" :  null  , "EquVestiaireSpoChauffe" : "Oui" , "EquNatureSignal" :  null  , "EquNom" : "Pas de Tir <C0> l'Arc" , "EquChauffageAutre" : "Non" , "EquAccesHandisVestiaire" : "Non" , "EquAccueilAucun" : "Non" , "EquipementTirPlateau" : "Non" , "EquipementTir50" : "Oui" , "EquAthNBMarteauMixte" :  null  , "EquUtilIndividuel" :  null  , "ComInsee" : "44073" , "EquConfortBainBouillonant" : "Non" , "EquNatNbP10" :  null  , "EquOuvertSaison" : "Non" , "EquNatProfMax" :  null  , "EquNatureAcPubPed" :  null  , "EquTableauFixe" : "Non" , "InsNom" : "Complexe des Frenouelles" , "EquGestionDSP" : "Non" , "EquNbVestiaireSpo" : "4" , "EquNatureSKTotalRemontee" :  null  , "EquTravauxRealDegradation" : "Non" , "EquAthNbCouloirLigne" :  null  , "EquAccueilDopage" : "Non" , "EquAccesHandimAire" : "Non" , "EquChrono" : "Non" , "GestionTypeGestionnairePrincLib" : "Commune" , "EquUtilFormation" :  null  , "EquNatureAcSecPed" :  null  , "EquSaeNbCouloir" :  null  , "EquNatProfMini" :  null  , "EquAthDev" :  null  , "EquSaeHauteur" :  null  , "EquAccueilBureau" : "Oui" , "EquAthNbJavelot" :  null  , "InsNumeroInstall" : "440730006" , "EquAnneeService" : "1990" , "EquAthNbSautPerche" :  null  , "EquNatCouloir" :  null  , "EquipementTir300" : "Non" , "EquAccesHandimAucun" : "Oui" , "EquNatureAcSecRout" :  null  , "EquipementTir200" : "Non" , "EquGpsX" : -1.653876 , "EquNomBatiment" :  null  , "EquipementTir100" : "Non" , "EquGpsY" : 47.408949 , "EquLargeurEvolution" : "15.00" , "EquChauffageNon" : "Oui" , "GestionTypeGestionnaireSecLib" :  null  , "EquAthNbSautHauteur" :  null  , "EquDateDernierTravauxReal" :  null  , "EquipementId" : "269831" , "EquUtilScolaire" :  null  , "EquNatureAutorise" :  null  , "EquSanitairePublic" : "Oui" , "EquAccueilInfirmerie" : "Non" , "EquAccueilClub" : "Oui" , "EquChauffageSolaire" : "Non" , "EquAthNbSautTriple" :  null  , "EquNatNbTTotal" :  null  , "EquProximite" : "Non" , "EquipNatureSituationLib" :  null  , "EquChauffageFuel" : "Non" , "EquipementTypeLib" : "1" , "EquDateDernierTravauxAucun" : "Oui" , "EquErpREF" : "Non" , "EquipementTir25" : "Non" , "EquAthNbDisque" :  null  , "EquAmenagementAucun" : "Oui" , "AnneeTravauxRealLibelle" :  null  , "EquAccesHandimSaniSpo" : "Non" , "EquNbCouloirPiste" : "0" , "EquChauffageElectricite" : "Non" , "EquNatNbP3" :  null  , "EquNatureClassFedeMaxi" :  null  , "EquAccesHandimTribune" : "Non-concerne" , "FamilleFicheLib" : "Pas de tir <E0> l'arc" , "EquNatNbPTotal" :  null  , "EquTravauxRealNorme" : "Non" , "EquErpCTS" : "Non" , "EquAthRiviere" :  null  , "EquAccesHandisTribune" : "Non-concerne" , "EquipementFiche" : "1401" , "NatureSolLib" : "Gazon naturel" , "EquNatSurfacePlageBassin" :  null  , "EquNatureESTour" :  null  , "EquipementTir10" : "Non" , "ComLib" : "H<E9>ric" , "EquAccueilMedic" : "Non" , "AnneeServiceLib" : "1985-1994" , "EquNatAutre" :  null  , "EquNaturePDESI" :  null  , "EquNatRiviere" :  null  , "EquNatureAlert" :  null  , "EquNatNbP7" :  null  , "EquNatureAcPubMec" :  null  , "EquNatNbP5" :  null  , "EquNatLargeurBassin" :  null  , "EquErpSG" : "Non" , "EquNatureClassFedeMini" :  null  , "EquAccueilLocalRangement" : "Oui" , "EquNatureAcPubNau" :  null  , "EquConfortSauna" : "Non" , "EquLongueurEvolution" : "60.00" , "EquAccesHandisSaniSpo" : "Non" , "EquNbPlaceTribune" : "0" , "EquConfortBainVapeur" : "Non" , "EquAthNbSautTotal" :  null  , "EquNatureAcSecNau" :  null  , "EquTravauxRealUsager" : "Non" , "EquUtilRecreation" : "1" , "EquAthNbPoids" :  null  , "EquNatFM" :  null  , "EquAccueilSalle" : "Oui" , "EquNatImHandi" :  null  , "EquNatMaV" :  null  , "EquNatureAcSecMec" :  null  , "EquAthNbCouloirHorsLigne" :  null  , "EquipementTirAutre" : "Oui" , "EquDemarcheHQE" : "Non" , "EquTravauxRealConformite" : "Non" , "EquNatureAETreuil" :  null  , "EquNbVestiaireArbitre" : "1" , "EquAthNbSautLongueur" :  null  , "EquAthNbLancerTotal" :  null  , "EquNatureSEVoies" :  null  , "EquAccesHandisSaniPub" : "Non" , "EquErpRPE" : "Non" , "EquNatMM" :  null  , "EquAthLongLigneDroite" :  null  , "EquErpX" : "Non" , "EquConfortAucun" : "Oui" , "EquErpR" : "Non" , "EquChauffageGaz" : "Non" , "EquErpO" : "Non" , "EquSaeSurface" :  null  , "EquErpN" : "Non" , "EquPresencePataugeoir" :  null  , "EquNatPentaglisse" :  null  , "EquUtilPerformance" : "1" , "EquNatureLocTec" :  null  , "EquErpP" : "Non" , "EquAccesHandimSaniPub" : "Non" , "EquUtilClub" : "1" , "EquAthNbMarteau" :  null  , "EquErpL" : "Non"}