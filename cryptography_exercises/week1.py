def one_one_one():
    s = [ord(c) for c in "XJHRFTNZHMZGAHIUETXZJNBWNUTRHEPOMDNBJMAUGORFAOIZOCC"]
    r = 1
    for i in range(len(s)):
        s[i] = (s[i] - 65 - r) % 26 + 65
        r = (r + 1) % 26
    print(''.join(chr(s[i]) for i in range(len(s))))


def one_one_two():
    for r in range(26):
        s = [ord(c)
             for c in "BGUTBMBGZTFHNLXMKTIPBMAVAXXLXTEPTRLEXTOXKHHFYHKMAXFHNLX"]
        for i in range(len(s)):
            s[i] = (s[i] - 65 + r) % 26 + 65
        print(
            f"shift {r:>2} clockwise -> {''.join(chr(s[i]) for i in range(len(s)))}")


def one_one_three():
    # R -> E, J -> T, N -> H, I -> A, T -> I, Q -> N
    emsg = """
            JNRZR BNIGI BJRGZ IZLQR OTDNJ GRIHT USDKR ZZWLG OIBTM
            NRGJN IJTZJ LZISJ NRSBL QVRSI ORIQT QDEKJ JNRQW GLOFN IJTZX QLFQL WBIMJ
            ITQXT HHTBL KUHQL JZKMM LZRNT OBIMI EURLW BLQZJ GKBJT QDIQS LWJNR
            OLGRI EZJGK ZRBGS MJLDG IMNZT OIHRK MOSOT QHIJL QBRJN IJJNT ZFIZL WIZTO
            MURZM RBTRZ ZKBNN LFRVR GIZFL KUHIM MRIGJ LJNRB GKHRT QJRUU RBJLW
            JNRZI TULGI EZLUK JRUST QZLUK EURFT JNLKJ JNRXR S
        """
    ft = {}
    for c in emsg:
        if c == '\n' or c == ' ':
            continue
        if c in ft:
            ft[c] += 1
        else:
            ft[c] = 1
    len = sum(ft[c] for c in ft)
    fb = {
        "JN": 11,
        "NR": 8,
        "TQ": 6,
        "LW": 5,
        "RB": 5,
        "RZ": 5,
        "JL": 5,
    }
    eng_ft = {
        'E': 12.0,
        'T': 9.10,
        'A': 8.12,
        'O': 7.68,
        'I': 7.31,
        'N': 6.95,
        'S': 6.28,
        'R': 6.02,
        'H': 5.92,
        'D': 4.32,
        'L': 3.98,
        'U': 2.88,
        'C': 2.71,
        'M': 2.61,
        'F': 2.30,
        'Y': 2.11,
        'W': 2.09,
        'G': 2.03,
        'P': 1.82,
        'B': 1.49,
        'V': 1.11,
        'K': 0.69,
        'X': 0.17,
        'Q': 0.11,
        'J': 0.10,
        'Z': 0.07,
    }
    ft = dict(sorted(ft.items(), key=lambda x: x[1], reverse=True))
    print(ft)
    dmsg = ""
    # first hypothesis, substitute the most frequent letters
    # in the encrypted text with the most frequent letters in english
    for c in emsg:
        if c == '\n' or c == ' ':
            continue
        else:
            dmsg += list(eng_ft)[list(ft).index(c)]
    # print(dmsg)
    # Now let's try to substitute the most frequent bigrams
    dmsg = ""
    for c in emsg:
        if c == '\n' or c == ' ':
            continue
        else:
            if c == 'N':
                dmsg += 'H'
            elif c == 'T':
                dmsg += 'I'
            elif c == 'Q':
                dmsg += 'N'
            else:
                dmsg += list(eng_ft)[list(ft).index(c)]
    # print(dmsg)

    # 1. R -> E, J -> T, N -> H, I -> A, T -> I, Q -> N
    print()
    dmsg = ""
    for c in emsg:
        if c == '\n' or c == ' ':
            continue
        if c == 'R':
            dmsg += 'e'
        elif c == 'J':
            dmsg += 't'
        elif c == 'N':
            dmsg += 'h'
        elif c == 'I':
            dmsg += 'a'
        elif c == 'T':
            dmsg += 'i'
        elif c == 'Q':
            dmsg += 'n'
        elif c == 'Z':
            dmsg += 's'
        elif c == 'B':
            dmsg += 'c'
        elif c == 'G':
            dmsg += 'r'
        elif c == 'M':
            dmsg += 'p'
        elif c == 'D':
            dmsg += 'g'
        elif c == 'K':
            dmsg += 'u'
        elif c == 'L':
            dmsg += 'o'
        elif c == 'S':
            dmsg += 'y'
        elif c == 'W':
            dmsg += 'f'
        elif c == 'X':
            dmsg += 'k'
        elif c == 'F':
            dmsg += 'w'
        elif c == 'U':
            dmsg += 'l'
        elif c == 'E':
            dmsg += 'b'
        elif c == 'O':
            dmsg += 'm'
        elif c == 'H':
            dmsg += 'd'
        elif c == 'V':
            dmsg += 'v'
        else:
            dmsg += c
    print(dmsg)


one_one_three()
