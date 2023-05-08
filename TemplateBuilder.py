import api
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


def filledTemplate(keyWords, rawText, streetName,gui):
    #alertType = "Accident"
    '''
    for word in keyWords:
        if alertType == "Accident":
            template = "Attention drivers: There has been an accident on "+streetName+". Please use alternate routes if possible. Emergency services are on the scene."
        elif alertType == "Road Closure":
            template = "Attention drivers: "+streetName+" is closed due to "+PoliceCodeTranslator+". Please use alternate routes. Expect delays."
        elif alertType == 'Weather Alert':
            template = "Attention drivers: Heavy traffic is reported on "+streetName+". Please expect delays and plan your route accordingly."
    '''
    for x in keyWords:
        if x[1] == "closure" or x[1] == "accident":
            template = "Attention drivers: There has been an accident on " + streetName + ". Please use alternate routes if possible. Emergency services are on the scene."
            print(template)
            api.twitterPost(template)
            gui.post_update(template)
            break
    return
    #print(keyWords)

    

