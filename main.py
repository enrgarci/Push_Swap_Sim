import PySimpleGUI as sg

history = []


def sa(window, text_a):
    if (len(text_a) > 1):
        history.append('sa')
        temp = text_a[0]
        text_a[0] = text_a[1]
        text_a[1] = temp
        window['T_SA'].update(text_a)
        window['T_H'].update(" ".join(map(str, history)))


def sb(window, text_b):
    if (len(text_b) > 1):
        history.append('sb')
        temp = text_b[0]
        text_b[0] = text_b[1]
        text_b[1] = temp
        window['T_SB'].update(text_b)
        window['T_H'].update(" ".join(map(str, history)))


def pa(window, text_a, text_b):
    if (len(text_b) > 0):
        history.append('pa')
        window['T_H'].update(" ".join(map(str, history)))
        text_a.insert(0, text_b[0])
        text_b.pop(0)
        window['T_SA'].update(text_a)
        window['T_SB'].update(text_b)


def pb(window, text_a, text_b):
    if (len(text_a) > 0):
        history.append('pb')
        window['T_H'].update(" ".join(map(str, history)))
        text_b.insert(0, text_a[0])
        text_a.pop(0)
        window['T_SA'].update(text_a)
        window['T_SB'].update(text_b)


def ra(window, text_a):
    if (len(text_a) > 0):
        history.append('ra')
        window['T_H'].update(" ".join(map(str, history)))
        text_a.append(text_a[0])
        text_a.pop(0)
        window['T_SA'].update(text_a)


def rb(window, text_b):
    if (len(text_b) > 0):
        history.append('ra')
        window['T_H'].update(" ".join(map(str, history)))
        text_b.append(text_b[0])
        text_b.pop(0)
        window['T_SB'].update(text_b)


def rra(window, t):
    if (len(t) > 0):
        history.append('rra')
        window['T_H'].update(" ".join(map(str, history)))
        t.insert(0, t[-1:][0])
        t.pop()
        window['T_SA'].update(t)


def rrb(window, t):
    if (len(t) > 0):
        history.append('rrb')
        window['T_H'].update(" ".join(map(str, history)))
        t.insert(0, t[-1:][0])
        t.pop()
        window['T_SB'].update(t)

def rr(window, ta, tb):
    ra(window, ta)
    rb(window, tb)
    
    
def rrr(window, ta, tb):
    rra(window, ta)
    rrb(window, tb)
    

def DrawGUI(text_a, text_b):
    history = []
    s_b = (3, 2)
    col1 = [[sg.Text(f"                "), sg.Button("sa", size=s_b)],
            [sg.Text(f"STACK A :"), sg.Button("ra", size=s_b)],
            [sg.Text(f"                "), sg.Button("rb", size=s_b)],
            [sg.Text(f"STACK B :"), sg.Button("sb", size=s_b)]]

    col2 = [[sg.Text(f"                ", size=(None, 5))],
            [sg.Text(text_a, key='T_SA'), sg.Button("rra", size=s_b)],
            [sg.Text(text_b, key='T_SB'), sg.Button("rrb", size=s_b)],
            [sg.Button("ss", size=s_b)]]

    col3 = [[sg.Button("pa", size=s_b)],
            [sg.Button("rr", size=s_b)],
            [sg.Button("rrr", size=s_b)],
            [sg.Button("pb", size=s_b)]]

    col4 = [[sg.Text("HISTORY")],
            [sg.Multiline("History", key='T_H', size=(
                None, 20), disabled=True)],
            [sg.Button("Reset", size=(5, 2)), sg.Button("Undo", size=(5, 2))]]

    layout = [[sg.Column(col1, vertical_alignment='top'),
               sg.Column(col2, vertical_alignment='top'),
               sg.Column(col3, vertical_alignment='top'),
               sg.VSeparator(),
               sg.Column(col4, vertical_alignment='top')]]

    # Create the Window
    window = sg.Window('Window Title', layout,)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'Undo':
            history.pop()
            window['T_H'].update(" ".join(map(str, history)))
        if event == 'sa':
            sa(window, text_a)
        if event == 'sb':
            sb(window, text_b)
        if event == 'pa':
            pa(window, text_a, text_b)
        if event == 'pb':
            pb(window, text_a, text_b)
        if event == 'ra':
            ra(window, text_a)
        if event == 'rra':
            rra(window, text_a)
        if event == 'rrb':
            rrb(window, text_b)
        if event == 'rr':
            rr(window, text_a, text_b)
        if event == 'rrr':
            rrr(window, text_a, text_b)

    window.close()


input = sg.popup_get_text('Input stack A', title="Textbox")
stack_a = input.split()
text_a = stack_a.copy()
text_b = []

if (len(input)):
    DrawGUI(text_a, text_b)
