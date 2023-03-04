import PySimpleGUI as sg

history = []

KEY_A = 'T_SA'
KEY_B = 'T_SB'

def sx(window, t, key, move):
    if (len(t) > 1):
        history.append(move)
        temp = t[0]
        t[0] = t[1]
        t[1] = temp
        window[key].update(t)
        window['T_H'].update(" ".join(map(str, history)))


def px(window, text_a, text_b, key_a, key_b, move):
    if (len(text_b) > 0):
        history.append(move)
        window['T_H'].update(" ".join(map(str, history)))
        text_a.insert(0, text_b[0])
        text_b.pop(0)
        window[key_a].update(text_a)
        window[key_b].update(text_b)


def rx(window, t, key, move):
    if (len(t) > 0):
        history.append(move)
        window['T_H'].update(" ".join(map(str, history)))
        t.append(t[0])
        t.pop(0)
        window[key].update(t)


def rrx(window, t, key, move):
    if (len(t) > 0):
        history.append(move)
        window['T_H'].update(" ".join(map(str, history)))
        t.insert(0, t[-1:][0])
        t.pop()
        window[key].update(t)


def rr(window, ta, tb, move):
    rx(window, ta ,KEY_A,'')
    rx(window, tb, KEY_B, '')
    history.append(move)
    window['T_H'].update(" ".join(map(str, history)))


def rrr(window, ta, tb, move):
    rrx(window, ta, KEY_A, '')
    rrx(window, tb, KEY_B, '')
    history.append(move)
    window['T_H'].update(" ".join(map(str, history)))

def ss(window, ta, tb, move):
    sx(window, ta, KEY_A, '')
    sx(window, tb, KEY_B, '')
    history.append(move)
    window['T_H'].update(" ".join(map(str, history)))

def reset(window, ta, tb):
        history = []
        window['T_H'].update(" ".join(map(str, history)))
        ta = stack_a.copy()
        tb =[]
        window['T_SA'].update(ta)
        window['T_SB'].update(tb)
                
def check(window, ta):
    print(list(map(int,ta)))
    print(sorted(list(map(int,ta))))
    if list(map(int,ta)) == sorted(list(map(int,ta))):
        sg.popup_auto_close('Sorted !!', keep_on_top=True)
        
        
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
            [sg.Button("Reset", size=(5, 2))]]#,sg.Button("Undo", size=(5, 2))''']]

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
            sx(window, text_a, KEY_A, event)
        if event == 'sb':
            sx(window, text_b, KEY_B, event)
        if event == 'pa':
            px(window, text_a, text_b, KEY_A, KEY_B, event)
        if event == 'pb':
            px(window, text_b,text_a, KEY_B,KEY_A, event)
        if event == 'ra':
            rx(window, text_a, KEY_A, event)
        if event == 'rb':
            rx(window, text_b, KEY_B, event)
        if event == 'rra':
            rrx(window, text_a, KEY_A, event)
        if event == 'rrb':
            rrx(window, text_b, KEY_B, event)
        if event == 'rr':
            rr(window, text_a, text_b, event)
        if event == 'rrr':
            rrr(window, text_a, text_b,event)
        if event == 'ss':
            ss(window, text_a, text_b,event)
        if event == 'Reset':
            reset(window, text_a, text_b)
    check(window, text_a)
    window.close()


input = sg.popup_get_text('Input stack A', title="Textbox")
stack_a = input.split()
text_a = stack_a.copy()
text_b = []

if (len(input)):
    DrawGUI(text_a, text_b)
