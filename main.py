import PySimpleGUI as sg

movs = ['ra','rb','rr','rra','rrb','rrr','sa','sb','ss','pa','pb']

KEY_A = 'T_SA'
KEY_B = 'T_SB'

#sa and sb rules
def sx(window, t, key):
    if (len(t) > 1):
        temp = t[0]
        t[0] = t[1]
        t[1] = temp
        window[key].update(t)

#pa and pb rules
def px(window, text_a, text_b, key_a, key_b):
    if (len(text_b) > 0):
        text_a.insert(0, text_b[0])
        text_b.pop(0)
        window[key_a].update(text_a)
        window[key_b].update(text_b)

#ra and rb rules
def rx(window, t, key):
    if (len(t) > 0):
        t.append(t[0])
        t.pop(0)
        window[key].update(t)

#rra and rrb rules
def rrx(window, t, key):
    if (len(t) > 0):
        t.insert(0, t[-1:][0])
        t.pop()
        window[key].update(t)

#rr rule
def rr(window, ta, tb):
    rx(window, ta ,KEY_A)
    rx(window, tb, KEY_B)


#rrr rule
def rrr(window, ta, tb):
    rrx(window, ta, KEY_A)
    rrx(window, tb, KEY_B)

#ss rule
def ss(window, ta, tb):
    sx(window, ta, KEY_A)
    sx(window, tb, KEY_B)

# resets the Stack A and history
def reset(window, ta, tb):
        ta = stack_a.copy()
        tb =[]
        window['T_SA'].update(ta)
        window['T_SB'].update(tb)
        window['T_MC'].update(f'Mov count: 0')

# checks if the Stack A is sorted if so a PopUp is made
def check(window, ta,movcount):
    if list(map(int,ta)) == sorted(list(map(int,stack_a))):
        sg.popup(f'Sorted on {movcount} moves!!', keep_on_top=True)
        
#GUI and events
def DrawGUI(text_a, text_b):
    s_b = (3, 2)
    mov_count = 0
    history = []
    
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
            [sg.Button("Reset", size=(5, 2)), sg.Text(f'Mov count: {mov_count}', key='T_MC')]]#,sg.Button("Undo", size=(5, 2))''']]

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
            sx(window, text_a, KEY_A)
        if event == 'sb':
            sx(window, text_b, KEY_B)
        if event == 'pa':
            px(window, text_a, text_b, KEY_A, KEY_B)
        if event == 'pb':
            px(window, text_b,text_a, KEY_B,KEY_A)
        if event == 'ra':
            rx(window, text_a, KEY_A)
        if event == 'rb':
            rx(window, text_b, KEY_B)
        if event == 'rra':
            rrx(window, text_a, KEY_A)
        if event == 'rrb':
            rrx(window, text_b, KEY_B)
        if event == 'rr':
            rr(window, text_a, text_b)
        if event == 'rrr':
            rrr(window, text_a, text_b)
        if event == 'ss':
            ss(window, text_a, text_b)
        if event in movs:
            mov_count += 1
            window['T_MC'].update(f'Mov count: {mov_count}')
            history.append(event)
            window['T_H'].update(" ".join(map(str, history)))
        if event == 'Reset':
            reset(window, text_a, text_b)
            history = []
            text_a = stack_a
            mov_count = 0
            window['T_H'].update(" ".join(map(str, history)))
        check(window, text_a, mov_count)
    window.close()

#input
input = sg.popup_get_text('Input stack A', title="Textbox")
stack_a = input.split()
text_a = stack_a.copy()
text_b = []

#some filtering TODO
#numeric = [i for i in input if i.isdigit()]
#repeate = [i for i in numeric if numeric.count(i)== 1 ]
if (len(input)):# and len(numeric) == len(input) == len(repeate)):
    DrawGUI(text_a, text_b)
else:
    sg.popup('Wrong Input', keep_on_top=True)
