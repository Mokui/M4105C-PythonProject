
from bottle import get, post, request, run, route, template, error, static_file
from Database import *


# route needed to acces css files in the index.tpl file
@route("/web/bootstrap/css/<filename>")
def style(filename):
    return static_file(filename, root='web/bootstrap/css')


# route needed to acces fonts files in the index.tpl file
@route("/web/bootstrap/fonts/<filename>")
def style(filename):
    return static_file(filename, root='web/bootstrap/fonts')


# route needed to acces images in the index.tpl file
@route("/img/<filename>")
def img(filename):
	return static_file(filename,root='web/img/')


# route needed to acces Javascript files in the index.tpl file
@route("/js/<filename>")
def script(filename):
    return static_file(filename, root='web/js/')


# route which handle the access to a non defined address in the server
@error(404)
def error404(error):
    return '''
        <h1>Erreur 404</h1>
        <img src=\"http://i2.kym-cdn.com/photos/images/newsfeed/001/042/619/4ea.jpg\"/>
    '''


# route to access to the main page
@get('/index')
def login():
    return template('web/index.tpl', dict_installation_equipments={})


# route to get datas from the user's request
@post('/index')
def do_login():
    # get a connection to send requests to the database
    conn = create_connection("database.db")

    # collect the informations given by the user
    activityRequest = request.forms.get('activity')
    city = request.forms.get('city')

    # getting all the installations linked with the given city
    installations = get_installations_by_city(conn, city)
    dict_installation_equipments = {}
    for installation in installations :
        # iterate over all installations to get its equipments
        equipments_initial = get_equipments_by_installation(conn, installation.id)

        # list that will store only the equipments linked with the desired activity
        equipments_final = []

        for equipment in equipments_initial :

            # getting all the activities whose name contains the value in activityRequest
            activities = get_activities_by_equipment_and_name(conn, equipment.id, activityRequest)
            equipment.addActivities(activities)

            # if the list of activities isn't empty
            # we append the equipment to equipments_final
            if(activities != []) :
                equipments_final.append(equipment)

        if(equipments_final != []) :            
            dict_installation_equipments[installation] = equipments_final
        

    # sending a dict (key : installation, values : list of equipments) to the index.tpl file
    return template('web/index.tpl', dict_installation_equipments = dict_installation_equipments)


run(host='localhost', port=8079)
