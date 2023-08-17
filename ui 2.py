import PySimpleGUI as sg

sg.theme('BlueMono')

layout = [[sg.Button('Upload Questions'), sg.Button('Generate Question Paper')],
          [sg.Text('No file selected', key='-FILE-')],
          [sg.Button('Submit', key='-SUBMIT-', disabled=True)],
          [sg.Text('Select an option from each dropdown list:', key='-INFO-', visible=False)],
          [sg.Combo(['All Years', '1st Year', '2nd Year', '3rd Year', '4th Year'], key='-DROPDOWN1-', visible=False),
           sg.Combo(['All Depts', 'CSE', 'ECE', 'EEE'], key='-DROPDOWN2-', visible=False),
           sg.Combo(['IAT-1', 'IAT-2', 'IAT-3'], key='-DROPDOWN3-', visible=False)]]

window = sg.Window('My App', layout, size=(500, 150), resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Upload Questions':
        filepath = sg.popup_get_file('Select a file', file_types=(('Excel Files', '*.xlsx'),))
        if filepath:
            window['-FILE-'].update(f'File selected: {filepath}')
            window['-SUBMIT-'].update(disabled=False)
    if event == '-SUBMIT-':
        window['-INFO-'].update(visible=True)
        window['-DROPDOWN1-'].update(visible=True)
        window['-DROPDOWN2-'].update(visible=True)
        window['-DROPDOWN3-'].update(visible=True)

window.close()
