#import API

'''
Template 1: Accident Alert
Attention drivers: There has been an accident on [Road Name/Number]. Please use alternate routes if possible. Emergency services are on the scene.

Template 2: Road Closure Alert
Attention drivers: [Road Name/Number] is closed due to [reason]. Please use alternate routes. Expect delays.

Template 3: Heavy Traffic Alert
Attention drivers: Heavy traffic is reported on [Road Name/Number]. Please expect delays and plan your route accordingly.

Template 4: Weather Alert
Attention drivers: [Rain/Snow/Wind/Storm] is causing poor driving conditions on [Road Name/Number]. Please drive with caution and reduce your speed.
'''


def filledTemplate(keyWords, rawText):

    road = "I-15"
    alertType = "Accident"
    PoliceCodeTranslator = "Minor/Moderate/Extreme Police activity"

    for word in keyWords:
        if alertType == "Accident":
            template = "Attention drivers: There has been an accident on "+road+". Please use alternate routes if possible. Emergency services are on the scene."
        elif alertType == "Road Closure":
            template = "Attention drivers: "+road+" is closed due to "+PoliceCodeTranslator+". Please use alternate routes. Expect delays."
        elif alertType == 'Weather Alert':
            template = "Attention drivers: Heavy traffic is reported on "+road+". Please expect delays and plan your route accordingly."

    #print(keyWords)

    

