import winsound

def eng_2_morse(words):
    dit_x, dit_y = 530, 150
    dat_x, dat_y = 500, 450
    bar_x, bar_y = 38, 300

    
    morse_dict = {'A' :	'· –', 'B' : '– · · ·', 'C' :	'– · – ·', 'D' : '– · ·', 'E' :	'·', 'F' :	'· · – ·', 'G' :	'– – ·', 'H':	'· · · ·', 'I' : '· ·', 'J': '· – – –', 'K': '– · –', 'L'	:'· – · ·', 'M':	'– –', 'N'	:'– ·', 'O':	'– – –', 'P':'· – – ·', 'Q':'– – · –', 'R':	'· – ·', 'S':	'· · ·', 'T':	'–', 'U'	:'· · –', 'V'	:'· · · –', 'W' :	'· – –', 'X':	'– · · –', 'Y'	:'– · – –', 'Z':	'– – · ·'}
    conv_lst = []

    for letter in words.upper():
        if letter in morse_dict:
            conv_lst.append(morse_dict.get(letter))
        else:
            continue
    
    for each in conv_lst:
        for every in each:
            if every == "·":
                winsound.Beep(dit_x, dit_y)
            elif every == "–":
                winsound.Beep(dat_x, dat_y)
        winsound.Beep(bar_x, bar_y)

    return conv_lst

print(eng_2_morse("Blah Blah"))
