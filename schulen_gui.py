### Test of a simple python GUI ###

import PySimpleGUI as sg
import os.path
import orte


type_of_school_box = [[sg.Checkbox('Gymnasium', default=False, enable_events=True, key="-GYM-")], [sg.Checkbox('Realschule', default=False, enable_events=True, key="-RS-")], [sg.Checkbox('Gemeinschaftsschule', default=False, enable_events=True, key="-GMSSI-")], [sg.Checkbox('Freie Waldorfschule', default=False, enable_events=True, key="-FWS-")]]


def GeneralError():
    layout = [[sg.Text("Es ist ein Fehler aufgetreten")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Fehler", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()

def MissingWord():
    layout = [[sg.Text("Es wurde kein Suchwort angegeben, die Suche wird für ganz Baden-Württemberg durchgeführt")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Hinweis", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


def MissingSchoolType():
    layout = [[sg.Text("Es wurde kein einziger Schultyp angegeben!")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Hinweis", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


def ChooseParameters(ver):
    version = ver
    types_of_school = []

    search_word = [
        [sg.Text("Suche mit folgendem SUCHWORT:")],
        #[sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.In(size=(25, 1), enable_events=True, key="-SEARCHWORD-")]
    ]    

    
    layout = [
        [
            #sg.Column(welcome),
            #sg.VSeperator(),
            sg.Column(search_word),
            sg.VSeparator(),
            sg.Column(type_of_school_box)

        ],
        [
            sg.Button("OK")
        ]
    ]

    window = sg.Window(str("Schuldatenbankfinder (Version: " + version + ")"), layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button

        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        elif event == "OK":

            if not ((values["-SEARCHWORD-"] == "") or (values["-SEARCHWORD-"] == " ")):
                search = values["-SEARCHWORD-"]

            if values['-GYM-'] == True:
                types_of_school.append('GYM')

            if values['-RS-'] == True:
                types_of_school.append('RS')

            if values['-GMSSI-'] == True:
                types_of_school.append('GMSSI')

            if values['-FWS-'] == True:
                types_of_school.append('FWS')


            if types_of_school == []:
                MissingSchoolType()

            elif types_of_school != []:    

                try:
                    search_parameters = {'Search_Type': 'QUICKSEARCH', 'Search_Word': search, 'Location': "", 'Distance': "", 'Types_of_School': types_of_school}
                except:
                    MissingWord()
                    search = ""
                    
                try:
                    search_parameters = {'Search_Type': 'QUICKSEARCH', 'Search_Word': search, 'Location': "", 'Distance': "", 'Types_of_School': types_of_school}
                    return(search_parameters)
                except:
                    GeneralError()
                    exit

    window.close()


def MissingLocation():
    layout = [[sg.Text("Es wurde kein einziger Ort ausgewählt!")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Hinweis", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


def ChooseLocation(ver):
    version = ver

    location = [[sg.Listbox(values= orte.Orte_list, size=(30, 25), key='-LIST-', enable_events=True)]]

    distance = [
        [sg.Text("Suche im Umkreis (in km):")],
        #[sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.In(size=(25, 1), enable_events=True, key="-DISTANCE-")]
    ]    

    layout = [
        [
            sg.Column(location),
            sg.VSeperator(),
            sg.Column(distance),
            sg.VSeparator(),
            sg.Column(type_of_school_box)

        ],
        [
            sg.Button("OK")
        ]
    ]

    window = sg.Window(str("Schuldatenbankfinder (Version: " + version + ")"), layout)

    def loop():  # Create an event loop
        types_of_school = []
        dist = ""

        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "OK":

                if not (values['-LIST-'] == []):
                    location = values[['-LIST-'][0]]
                if (values['-LIST-'] == []):
                    MissingLocation()
                    types_of_school = []
                    loop()
                    break

                if not (values["-DISTANCE-"] == ""):
                    dist = values["-DISTANCE-"]


                if values['-GYM-'] == True:
                    types_of_school.append('GYM')

                if values['-RS-'] == True:
                    types_of_school.append('RS')

                if values['-GMSSI-'] == True:
                    types_of_school.append('GMSSI')

                if values['-FWS-'] == True:
                    types_of_school.append('FWS')


                if types_of_school == []:
                    MissingSchoolType()

                elif types_of_school != []:    

                    try:
                        search_parameters = {'Search_Type': 'SEARCH', 'Search_Word': "", 'Location': (location[0]), 'Types_of_School': types_of_school, 'Distance': dist}
                        #print(search_parameters)
                        return(search_parameters)
                    except:
                        GeneralError()
                        types_of_school = []
                        loop()

    search_parameters = loop()
    return(search_parameters)

    window.close()
    

def MissingPath():
    layout = [[sg.Text("Speicherort und/oder Dateiname wurden nicht ordnungsgemäß angegeben")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Fehler", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()



def ChooseFolder():
    # First the window layout in 2 columns

    folder_list_column= [
        [
            sg.Text("Wähle einen Speicherort"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ]
    ]

    # For now will only show the name of the file that was chosen

    file_name_column = [
        [sg.Text("Wähle einen Dateinamen (der nicht bereits existiert)")],
        #[sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.In(size=(25, 1), enable_events=True, key="-FILENAME-")]
    ]


    # ----- Full layout -----

    layout = [
        [
            sg.Column(folder_list_column),
            sg.VSeperator(),
            sg.Column(file_name_column),
        ],
        [
            sg.Button("OK")
        ]
    ]


    window = sg.Window("Ausgabedatei", layout)


    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        # Folder name was filled in, make a list of files in the folder
        elif event == "-FOLDER-":
            folder = values["-FOLDER-"]
        
        elif event == "-FILENAME-":
            filename = values["-FILENAME-"]        

        elif event == "OK":
            try:  
                return(str(folder + '/' + filename +'.csv'))
            except:
                MissingPath()
                            

    window.close()


def End(Speicherpfad):
    layout = [[sg.Text(("Suche abgeschlossen. Ausgabedatei gespeichert in %s"%(str(Speicherpfad))))], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Abgeschlossen", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()



def Ausgabepfad():
    directory = ChooseFolder()

    try:
        print(directory)
        return(directory)
    except:
        print("Es ist ein Fehler aufgetreten")
        exit





def ChooseSearchtype(ver):
    version = ver

    welcome = [
        [
            sg.Text("""
            *****************************************************
            * Herzlich willkommen im Schulenfinder BW *
            ******************* Version %s *******************
            *****************************************************
            """%(version))
        ]
    ]

    type_of_search = [
        [sg.Text("Wähle einen Suchtyp")],
        [sg.Radio('Stichwortsuche', "RADIO1", default=True, key = "-QS-"), sg.Radio('Orts- und Umkreissuche', "RADIO1", default=False, key = "-LS-")]
    ]
    
    layout = [
        [
            sg.Column(welcome),
            sg.VSeperator(),
            sg.Column(type_of_search)

        ],
        [
            sg.Button("OK")
        ]
    ]


    window = sg.Window(str("Schuldatenbankfinder (Version: " + version + ")"), layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        elif event == "OK":

            if values["-QS-"] == True:
                window.close()
                parameters = ChooseParameters(ver)
                break
            else:
                window.close()
                parameters = ChooseLocation(ver)
                break

    print(parameters)
    return parameters

    


#ChooseSearchtype("0.6")
