from fileinput import close
import sys


wordsfile = open("words.txt", "r")
words_list = []

for word in wordsfile:
    stripped_word = word.strip()
    good_word = stripped_word.split()
    word_str = ''.join(good_word)
    if len(word_str) == 5:
        words_list.append(good_word)

wordsfile.close()

def poopy():
    number_range = range(0, 6)
    green_number_range1 = range(0,5)
    green_number_range2 = range(0,4)
    green_number_range3 = range(0,3)
    green_number_range4 = range(0,2)
    green_number_range5 = range(0,1)
    number_placement = range(1, 6)
    awnsers = []
    temporary_awnsers = []
    try:
        q1 = int(input("Hoeveel gele letters heb je: "))
        if q1 in number_range: 
            if q1 == 1:
                q2 = input("Welke letter is geel: ")
                if q2.isalpha():
                    if len(q2) == 1:
                        gel1 = q2.lower()
                        for w in words_list:
                            wordle_str = ''.join(w)
                            if gel1 in wordle_str:
                                temporary_awnsers.append(wordle_str)

                        try:
                            q3 = int(input("Hoeveel groene letters heb je: "))
                            if q3 in number_range:
                                if q3 == 1:
                                    try:
                                        q4 = int(input("Op welke plek staat de groene letter: "))
                                        if q4 in number_placement:
                                            q5 = input("Wat is de groene letter: ")
                                            if q5.isalpha():
                                                if len(q5) == 1:
                                                    grl1 = q5.lower()
                                                    q4 = q4 - 1
                                                    for a in temporary_awnsers:
                                                        if grl1 == a[q4]:
                                                            awnsers.append(a)
                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                else:
                                                    print("jij verpest alles")
                                            else:
                                                print("fuckkkk offff")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 2:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                q5_1 = input("Wat is de eerste groene letter: ")
                                                q5_2 = input("Wat is de tweede groene letter: ")
                                                if q5_1.isalpha():
                                                    if q5_2.isalpha():
                                                        if len(q5_2) == 1: 
                                                            if len(q5_1) == 1:
                                                                grl1 = q5_1.lower()
                                                                grl2 = q5_2.lower()
                                                                
                                                                q4 = q4 - 1
                                                                q4_2 = q4_2 - 1
                                                                for a in temporary_awnsers:
                                                                    if grl1 == a[q4]:
                                                                        if grl2 == a[q4_2]:
                                                                            awnsers.append(a)
                                                                if not awnsers:
                                                                    print("rip er zijn geen woorden met deze combinatie")
                                                                else:
                                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("jij verpest alles")
                                                    else:
                                                        print("fuckkkk offff")
                                                else:
                                                    print("fuckkkk offff")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 3:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                if q4_3 in number_placement:
                                                    q5_1 = input("Wat is de eerste groene letter: ")
                                                    q5_2 = input("Wat is de tweede groene letter: ")
                                                    q5_3 = input("Wat is de derde groene letter: ")
                                                    if q5_1.isalpha():
                                                        if q5_2.isalpha():
                                                            if q5_3.isalpha():
                                                                if len(q5_1) == 1: 
                                                                    if len(q5_2) == 1:
                                                                        if len(q5_3) == 1:
                                                                            grl1 = q5_1.lower()
                                                                            grl2 = q5_2.lower()
                                                                            grl3 = q5_3.lower()
                                                                            q4 = q4 - 1
                                                                            q4_2 = q4_2 - 1
                                                                            q4_3 = q4_3 - 1
                                                                            for a in temporary_awnsers:
                                                                                if grl1 == a[q4]:
                                                                                    if grl2 == a[q4_2]:
                                                                                        if grl3 == a[q4_3]:
                                                                                            awnsers.append(a)
                                                                            if not awnsers:
                                                                                print("rip er zijn geen woorden met deze combinatie")
                                                                            else:
                                                                                print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                        else:
                                                                            print("among us??") 
                                                                    else:
                                                                        print("its about power") 
                                                                else:
                                                                    print("its about drive")                
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("jij verpest alles")
                                                    else:
                                                        print("fuckkkk offff")
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 4:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                        q4_4 = int(input("Op welke plek staat de vierde groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                if q4_3 in number_placement:
                                                    if q4_4 in number_placement:
                                                        q5_1 = input("Wat is de eerste groene letter: ")
                                                        q5_2 = input("Wat is de tweede groene letter: ")
                                                        q5_3 = input("Wat is de derde groene letter: ")
                                                        q5_4 = input("Wat is de vierde groene letter: ")
                                                        if q5_1.isalpha():
                                                            if q5_2.isalpha():
                                                                if q5_3.isalpha():
                                                                    if q5_4.isalpha():
                                                                        if len(q5_1) == 1: 
                                                                            if len(q5_2) == 1:
                                                                                if len(q5_3) == 1:
                                                                                    if len(q5_4) == 1:
                                                                                        grl1 = q5_1.lower()
                                                                                        grl2 = q5_2.lower()
                                                                                        grl3 = q5_3.lower()
                                                                                        grl4 = q5_4.lower()

                                                                                        q4 = q4 - 1
                                                                                        q4_2 = q4_2 - 1
                                                                                        q4_3 = q4_3 - 1
                                                                                        q4_4 = q4_4 - 1
                                                                                        for a in temporary_awnsers:
                                                                                            if grl1 == a[q4]:
                                                                                                if grl2 == a[q4_2]:
                                                                                                    if grl3 == a[q4_3]:
                                                                                                        if grl4 == a[q4_4]:
                                                                                                            awnsers.append(a)
                                                                                        if not awnsers:
                                                                                            print("rip er zijn geen woorden met deze combinatie")
                                                                                        else:
                                                                                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                                    else:
                                                                                        print("stop plz :(((")
                                                                                else:
                                                                                    print("stop :(")
                                                                            else:
                                                                                print("AAAAAAAAAAAAAAAAA")
                                                                        else:
                                                                            print("among us??") 
                                                                    else:
                                                                        print("its about power") 
                                                                else:
                                                                    print("its about drive")                
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("jij verpest alles")
                                                    else:
                                                        print("moet getal tussen 1-5")
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 5:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                        q4_4 = int(input("Op welke plek staat de vierde groene letter: "))
                                        q4_5 = int(input("Op welke plek staat de vijfde groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                if q4_3 in number_placement:
                                                    if q4_4 in number_placement:
                                                        if q4_5 in number_placement:
                                                            q5_1 = input("Wat is de eerste groene letter: ")
                                                            q5_2 = input("Wat is de tweede groene letter: ")
                                                            q5_3 = input("Wat is de derde groene letter: ")
                                                            q5_4 = input("Wat is de vierde groene letter: ")
                                                            q5_5 = input("Wat is de vijfde groene letter: ")
                                                            if q5_1.isalpha():
                                                                if q5_2.isalpha():
                                                                    if q5_3.isalpha():
                                                                        if q5_4.isalpha():
                                                                            if q5_5.isalpha():
                                                                                if len(q5_1) == 1: 
                                                                                    if len(q5_2) == 1:
                                                                                        if len(q5_3) == 1:
                                                                                            if len(q5_4) == 1:
                                                                                                if len(q5_5) == 1:
                                                                                                    grl1 = q5_1.lower()
                                                                                                    grl2 = q5_2.lower()
                                                                                                    grl3 = q5_3.lower()
                                                                                                    grl4 = q5_4.lower()
                                                                                                    grl5 = q5_5.lower()

                                                                                                    q4 = q4 - 1
                                                                                                    q4_2 = q4_2 - 1
                                                                                                    q4_3 = q4_3 - 1
                                                                                                    q4_4 = q4_4 - 1
                                                                                                    q4_5 = q4_5 - 1
                                                                                                    for a in temporary_awnsers:
                                                                                                        if grl1 == a[q4]:
                                                                                                            if grl2 == a[q4_2]:
                                                                                                                if grl3 == a[q4_3]:
                                                                                                                    if grl4 == a[q4_4]:
                                                                                                                        if grl5 == a[q4_5]:
                                                                                                                            awnsers.append(a)
                                                                                                    if not awnsers:
                                                                                                        print("rip er zijn geen woorden met deze combinatie")
                                                                                                    else:
                                                                                                        print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                                                else:
                                                                                                    print("jij wint ik geef op")
                                                                                            else:
                                                                                                print("stop plz :(((")
                                                                                        else:
                                                                                            print("stop plz :(((")
                                                                                    else:
                                                                                        print("stop plz :(((")
                                                                                else:
                                                                                    print("stop :(")
                                                                            else:
                                                                                print("AAAAAAAAAAAAAAAAA")
                                                                        else:
                                                                            print("among us??") 
                                                                    else:
                                                                        print("its about power") 
                                                                else:
                                                                    print("its about drive")                
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("moet getal tussen 1-5")
                                                    else:
                                                        print("moet getal tussen 1-5")
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 0:
                                    awnsers = temporary_awnsers
                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                            else:
                                print("moet cijfer tussen 0-5")
                        except ValueError:
                            print("fuck off")
            elif q1 == 2:
                q2 = input("Wat is de eerste gele letter: ")
                q2_2 = input("Wat is de tweede gele letter: ")
                if q2.isalpha():
                    if q2_2.isalpha():
                        if len(q2) == 1:
                            if len(q2_2) == 1:
                                gel1 = q2.lower()
                                gel2 = q2_2.lower()
                                for w in words_list:
                                    wordle_str = ''.join(w)
                                    if gel1 in wordle_str:
                                        if gel2 in wordle_str:
                                            temporary_awnsers.append(wordle_str)
            
                        try:
                            q3 = int(input("Hoeveel groene letters heb je: "))
                            if q3 in number_range:
                                if q3 == 1:
                                    try:
                                        q4 = int(input("Op welke plek staat de groene letter: "))
                                        if q4 in number_placement:
                                            q5 = input("Wat is de groene letter: ")
                                            if q5.isalpha():
                                                if len(q5) == 1:
                                                    grl1 = q5.lower()
                                                    q4 = q4 - 1
                                                    for a in temporary_awnsers:
                                                        if grl1 == a[q4]:
                                                            awnsers.append(a)
                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                else:
                                                    print("jij verpest alles")
                                            else:
                                                print("fuckkkk offff")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 2:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                q5_1 = input("Wat is de eerste groene letter: ")
                                                q5_2 = input("Wat is de tweede groene letter: ")
                                                if q5_1.isalpha():
                                                    if q5_2.isalpha():
                                                        if len(q5_2) == 1: 
                                                            if len(q5_1) == 1:
                                                                grl1 = q5_1.lower()
                                                                grl2 = q5_2.lower()
                                                                
                                                                q4 = q4 - 1
                                                                q4_2 = q4_2 - 1
                                                                for a in temporary_awnsers:
                                                                    if grl1 == a[q4]:
                                                                        if grl2 == a[q4_2]:
                                                                            awnsers.append(a)
                                                                if not awnsers:
                                                                    print("rip er zijn geen woorden met deze combinatie")
                                                                else:
                                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("jij verpest alles")
                                                    else:
                                                        print("fuckkkk offff")
                                                else:
                                                    print("fuckkkk offff")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 3:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                if q4_3 in number_placement:
                                                    q5_1 = input("Wat is de eerste groene letter: ")
                                                    q5_2 = input("Wat is de tweede groene letter: ")
                                                    q5_3 = input("Wat is de derde groene letter: ")
                                                    if q5_1.isalpha():
                                                        if q5_2.isalpha():
                                                            if q5_3.isalpha():
                                                                if len(q5_1) == 1: 
                                                                    if len(q5_2) == 1:
                                                                        if len(q5_3) == 1:
                                                                            grl1 = q5_1.lower()
                                                                            grl2 = q5_2.lower()
                                                                            grl3 = q5_3.lower()
                                                                            q4 = q4 - 1
                                                                            q4_2 = q4_2 - 1
                                                                            q4_3 = q4_3 - 1
                                                                            for a in temporary_awnsers:
                                                                                if grl1 == a[q4]:
                                                                                    if grl2 == a[q4_2]:
                                                                                        if grl3 == a[q4_3]:
                                                                                            awnsers.append(a)
                                                                            if not awnsers:
                                                                                print("rip er zijn geen woorden met deze combinatie")
                                                                            else:
                                                                                print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                        else:
                                                                            print("among us??") 
                                                                    else:
                                                                        print("its about power") 
                                                                else:
                                                                    print("its about drive")                
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("jij verpest alles")
                                                    else:
                                                        print("fuckkkk offff")
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 4:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                        q4_4 = int(input("Op welke plek staat de vierde groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                if q4_3 in number_placement:
                                                    if q4_4 in number_placement:
                                                        q5_1 = input("Wat is de eerste groene letter: ")
                                                        q5_2 = input("Wat is de tweede groene letter: ")
                                                        q5_3 = input("Wat is de derde groene letter: ")
                                                        q5_4 = input("Wat is de vierde groene letter: ")
                                                        if q5_1.isalpha():
                                                            if q5_2.isalpha():
                                                                if q5_3.isalpha():
                                                                    if q5_4.isalpha():
                                                                        if len(q5_1) == 1: 
                                                                            if len(q5_2) == 1:
                                                                                if len(q5_3) == 1:
                                                                                    if len(q5_4) == 1:
                                                                                        grl1 = q5_1.lower()
                                                                                        grl2 = q5_2.lower()
                                                                                        grl3 = q5_3.lower()
                                                                                        grl4 = q5_4.lower()

                                                                                        q4 = q4 - 1
                                                                                        q4_2 = q4_2 - 1
                                                                                        q4_3 = q4_3 - 1
                                                                                        q4_4 = q4_4 - 1
                                                                                        for a in temporary_awnsers:
                                                                                            if grl1 == a[q4]:
                                                                                                if grl2 == a[q4_2]:
                                                                                                    if grl3 == a[q4_3]:
                                                                                                        if grl4 == a[q4_4]:
                                                                                                            awnsers.append(a)
                                                                                        if not awnsers:
                                                                                            print("rip er zijn geen woorden met deze combinatie")
                                                                                        else:
                                                                                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                                    else:
                                                                                        print("stop plz :(((")
                                                                                else:
                                                                                    print("stop :(")
                                                                            else:
                                                                                print("AAAAAAAAAAAAAAAAA")
                                                                        else:
                                                                            print("among us??") 
                                                                    else:
                                                                        print("its about power") 
                                                                else:
                                                                    print("its about drive")                
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("jij verpest alles")
                                                    else:
                                                        print("moet getal tussen 1-5")
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q3 == 5:
                                    try:
                                        q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                        q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                        q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                        q4_4 = int(input("Op welke plek staat de vierde groene letter: "))
                                        q4_5 = int(input("Op welke plek staat de vijfde groene letter: "))
                                        if q4 in number_placement:
                                            if q4_2 in number_placement:
                                                if q4_3 in number_placement:
                                                    if q4_4 in number_placement:
                                                        if q4_5 in number_placement:
                                                            q5_1 = input("Wat is de eerste groene letter: ")
                                                            q5_2 = input("Wat is de tweede groene letter: ")
                                                            q5_3 = input("Wat is de derde groene letter: ")
                                                            q5_4 = input("Wat is de vierde groene letter: ")
                                                            q5_5 = input("Wat is de vijfde groene letter: ")
                                                            if q5_1.isalpha():
                                                                if q5_2.isalpha():
                                                                    if q5_3.isalpha():
                                                                        if q5_4.isalpha():
                                                                            if q5_5.isalpha():
                                                                                if len(q5_1) == 1: 
                                                                                    if len(q5_2) == 1:
                                                                                        if len(q5_3) == 1:
                                                                                            if len(q5_4) == 1:
                                                                                                if len(q5_5) == 1:
                                                                                                    grl1 = q5_1.lower()
                                                                                                    grl2 = q5_2.lower()
                                                                                                    grl3 = q5_3.lower()
                                                                                                    grl4 = q5_4.lower()
                                                                                                    grl5 = q5_5.lower()

                                                                                                    q4 = q4 - 1
                                                                                                    q4_2 = q4_2 - 1
                                                                                                    q4_3 = q4_3 - 1
                                                                                                    q4_4 = q4_4 - 1
                                                                                                    q4_5 = q4_5 - 1
                                                                                                    for a in temporary_awnsers:
                                                                                                        if grl1 == a[q4]:
                                                                                                            if grl2 == a[q4_2]:
                                                                                                                if grl3 == a[q4_3]:
                                                                                                                    if grl4 == a[q4_4]:
                                                                                                                        if grl5 == a[q4_5]:
                                                                                                                            awnsers.append(a)
                                                                                                    if not awnsers:
                                                                                                        print("rip er zijn geen woorden met deze combinatie")
                                                                                                    else:
                                                                                                        print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                                                else:
                                                                                                    print("jij wint ik geef op")
                                                                                            else:
                                                                                                print("stop plz :(((")
                                                                                        else:
                                                                                            print("stop plz :(((")
                                                                                    else:
                                                                                        print("stop plz :(((")
                                                                                else:
                                                                                    print("stop :(")
                                                                            else:
                                                                                print("AAAAAAAAAAAAAAAAA")
                                                                        else:
                                                                            print("among us??") 
                                                                    else:
                                                                        print("its about power") 
                                                                else:
                                                                    print("its about drive")                
                                                            else:
                                                                print("jij verpest alles")    
                                                        else:
                                                            print("moet getal tussen 1-5")
                                                    else:
                                                        print("moet getal tussen 1-5")
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")    
                                        else:
                                            print("moet getal tussen 1-5")
                                    except ValueError:
                                        print("ik haat jou")
                                elif q4 == 0:
                                    awnsers = temporary_awnsers
                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                            else:
                                print("moet cijfer tussen 0-5")
                        except ValueError:
                            print("fuck off")
            elif q1 == 3:
                q2 = input("Wat is de eerste gele letter: ")
                q2_2 = input("Wat is de tweede gele letter: ")
                q2_3 = input("Wat is de derde gele letter: ")
                if q2.isalpha():
                    if q2_2.isalpha():
                        if q2_3.isalpha():
                            if len(q2) == 1:
                                if len(q2_2) == 1:
                                    if len(q2_3) == 1:
                                        gel1 = q2.lower()
                                        gel2 = q2_2.lower()
                                        gel3 = q2_3.lower()
                                        for w in words_list:
                                            wordle_str = ''.join(w)
                                            if gel1 in wordle_str:
                                                if gel2 in wordle_str:
                                                    if gel3 in wordle_str:
                                                        temporary_awnsers.append(wordle_str)
                                        try:
                                            q3 = int(input("Hoeveel groene letters heb je: "))
                                            if q3 in green_number_range3:
                                                if q3 == 1:
                                                    try:
                                                        q3 = int(input("Op welke plek staat de groene letter: "))
                                                        if q3 in number_placement:
                                                            q4 = input("Wat is de groene letter: ")
                                                            if q4.isalpha():
                                                                if len(q4) == 1:
                                                                    grl1 = q4.lower()
                                                                    q3 = q3 - 1
                                                                    for a in temporary_awnsers:
                                                                        if grl1 == a[q3]:
                                                                            awnsers.append(a)
                                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                else:
                                                                    print("jij verpest alles")
                                                            else:
                                                                print("fuckkkk offff")    
                                                        else:
                                                            print("moet getal tussen 1-5")
                                                    except ValueError:
                                                        print("ik haat jou")
                                                elif q3 == 2:
                                                    try:
                                                        q3 = int(input("Op welke plek staat de eerste groene letter: "))
                                                        q3_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                                        if q3 in number_placement:
                                                            if q3_2 in number_placement:
                                                                q4_1 = input("Wat is de eerste groene letter: ")
                                                                q4_2 = input("Wat is de tweede groene letter: ")
                                                                if q4_1.isalpha():
                                                                    if q4_2.isalpha():
                                                                        if len(q4_2) == 1: 
                                                                            if len(q4_1) == 1:
                                                                                grl1 = q4_1.lower()
                                                                                grl2 = q4_2.lower()
                                                                                
                                                                                q3 = q3 - 1
                                                                                q3_2 = q3_2 - 1
                                                                                for a in temporary_awnsers:
                                                                                    if grl1 == a[q3]:
                                                                                        if grl2 == a[q3_2]:
                                                                                            awnsers.append(a)
                                                                                if not awnsers:
                                                                                    print("rip er zijn geen woorden met deze combinatie")
                                                                                else:
                                                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                            else:
                                                                                print("jij verpest alles")    
                                                                        else:
                                                                            print("jij verpest alles")
                                                                    else:
                                                                        print("fuckkkk offff")
                                                                else:
                                                                    print("fuckkkk offff")
                                                            else:
                                                                print("moet getal tussen 1-5")    
                                                        else:
                                                            print("moet getal tussen 1-5")
                                                    except ValueError:
                                                        print("ik haat jou")
                                                elif q3 == 0:
                                                    awnsers = temporary_awnsers
                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                            else:
                                                print("moet cijfer tussen 0-2")
                                        except ValueError:
                                            print("fuck off")
                                    else:
                                        print("FUCK OFF")
                                else:
                                    print("fuck off")
            elif q1 == 4:
                q2 = input("Wat is de eerste gele letter: ")
                q2_2 = input("Wat is de tweede gele letter: ")
                q2_3 = input("Wat is de derde gele letter: ")
                q2_4 = input("Wat is de vierde gele letter: ")
                if q2.isalpha():
                    if q2_2.isalpha():
                        if q2_3.isalpha():
                            if q2_4.isalpha():
                                if len(q2) == 1:
                                    if len(q2_2) == 1:
                                        if len(q2_3) == 1:
                                            if len(q2_4) == 1:
                                                gel1 = q2.lower()
                                                gel2 = q2_2.lower()
                                                gel3 = q2_3.lower()
                                                gel4 = q2_4.lower()
                                                for w in words_list:
                                                    wordle_str = ''.join(w)
                                                    if gel1 in wordle_str:
                                                        if gel2 in wordle_str:
                                                            if gel3 in wordle_str:
                                                                if gel4 in wordle_str:
                                                                    temporary_awnsers.append(wordle_str)
                                                try:
                                                    q3 = int(input("Hoeveel groene letters heb je: "))
                                                    if q3 in green_number_range4:
                                                        if q3 == 1:
                                                            try:
                                                                q3 = int(input("Op welke plek staat de groene letter: "))
                                                                if q3 in number_placement:
                                                                    q4 = input("Wat is de groene letter: ")
                                                                    if q4.isalpha():
                                                                        if len(q4) == 1:
                                                                            grl1 = q4.lower()
                                                                            q3 = q3 - 1
                                                                            for a in temporary_awnsers:
                                                                                if grl1 == a[q3]:
                                                                                    awnsers.append(a)
                                                                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                        else:
                                                                            print("jij verpest alles")
                                                                    else:
                                                                        print("fuckkkk offff")    
                                                                else:
                                                                    print("moet getal tussen 1-5")
                                                            except ValueError:
                                                                print("ik haat jou")
                                                        elif q3 == 0:
                                                            awnsers = temporary_awnsers
                                                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                    else:
                                                        print("moet cijfer tussen 0-2")
                                                except ValueError:
                                                    print("fuck off")
                                            else:
                                                print("FUCK OFF")
                                        else:
                                            print("fuck off")
            elif q1 == 5:
                q2 = input("Wat is de eerste gele letter: ")
                q2_2 = input("Wat is de tweede gele letter: ")
                q2_3 = input("Wat is de derde gele letter: ")
                q2_4 = input("Wat is de vierde gele letter: ")
                q2_5 = input("Wat is de vijfde gele letter: ")
                if q2.isalpha():
                    if q2_2.isalpha():
                        if q2_3.isalpha():
                            if q2_4.isalpha():
                                if q2_5.isalpha():
                                    if len(q2) == 1:
                                        if len(q2_2) == 1:
                                            if len(q2_3) == 1:
                                                if len(q2_4) == 1:  
                                                    if len(q2_5) == 1:
                                                        gel1 = q2.lower()
                                                        gel2 = q2_2.lower()
                                                        gel3 = q2_3.lower()
                                                        gel4 = q2_4.lower()
                                                        gel5 = q2_5.lower()
                                                        for w in words_list:
                                                            wordle_str = ''.join(w)
                                                            if gel1 in wordle_str:
                                                                if gel2 in wordle_str:
                                                                    if gel3 in wordle_str:
                                                                        if gel4 in wordle_str:
                                                                            if gel5 in wordle_str:
                                                                                awnsers.append(wordle_str)
                                                        print(awnsers)
            elif q1 == 0:
                try:
                    q3 = int(input("Hoeveel groene letters heb je: "))
                    if q3 in number_range:
                        if q3 == 1:
                            try:
                                q4 = int(input("Op welke plek staat de groene letter: "))
                                if q4 in number_placement:
                                    q5 = input("Wat is de groene letter: ")
                                    if q5.isalpha():
                                        if len(q5) == 1:
                                            grl1 = q5.lower()
                                            q4 = q4 - 1
                                            for a in words_list:
                                                if grl1 == a[q4]:
                                                    awnsers.append(a)
                                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                        else:
                                            print("jij verpest alles")
                                    else:
                                        print("fuckkkk offff")    
                                else:
                                    print("moet getal tussen 1-5")
                            except ValueError:
                                print("ik haat jou")
                        elif q3 == 2:
                            try:
                                q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                if q4 in number_placement:
                                    if q4_2 in number_placement:
                                        q5_1 = input("Wat is de eerste groene letter: ")
                                        q5_2 = input("Wat is de tweede groene letter: ")
                                        if q5_1.isalpha():
                                            if q5_2.isalpha():
                                                if len(q5_2) == 1: 
                                                    if len(q5_1) == 1:
                                                        grl1 = q5_1.lower()
                                                        grl2 = q5_2.lower()
                                                        
                                                        q4 = q4 - 1
                                                        q4_2 = q4_2 - 1
                                                        for a in temporary_awnsers:
                                                            if grl1 == a[q4]:
                                                                if grl2 == a[q4_2]:
                                                                    awnsers.append(a)
                                                        if not awnsers:
                                                            print("rip er zijn geen woorden met deze combinatie")
                                                        else:
                                                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                    else:
                                                        print("jij verpest alles")    
                                                else:
                                                    print("jij verpest alles")
                                            else:
                                                print("fuckkkk offff")
                                        else:
                                            print("fuckkkk offff")
                                    else:
                                        print("moet getal tussen 1-5")    
                                else:
                                    print("moet getal tussen 1-5")
                            except ValueError:
                                print("ik haat jou")
                        elif q3 == 3:
                            try:
                                q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                if q4 in number_placement:
                                    if q4_2 in number_placement:
                                        if q4_3 in number_placement:
                                            q5_1 = input("Wat is de eerste groene letter: ")
                                            q5_2 = input("Wat is de tweede groene letter: ")
                                            q5_3 = input("Wat is de derde groene letter: ")
                                            if q5_1.isalpha():
                                                if q5_2.isalpha():
                                                    if q5_3.isalpha():
                                                        if len(q5_1) == 1: 
                                                            if len(q5_2) == 1:
                                                                if len(q5_3) == 1:
                                                                    grl1 = q5_1.lower()
                                                                    grl2 = q5_2.lower()
                                                                    grl3 = q5_3.lower()
                                                                    q4 = q4 - 1
                                                                    q4_2 = q4_2 - 1
                                                                    q4_3 = q4_3 - 1
                                                                    for a in words_list:
                                                                        if grl1 == a[q4]:
                                                                            if grl2 == a[q4_2]:
                                                                                if grl3 == a[q4_3]:
                                                                                    awnsers.append(a)
                                                                    if not awnsers:
                                                                        print("rip er zijn geen woorden met deze combinatie")
                                                                    else:
                                                                        print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                else:
                                                                    print("among us??") 
                                                            else:
                                                                print("its about power") 
                                                        else:
                                                            print("its about drive")                
                                                    else:
                                                        print("jij verpest alles")    
                                                else:
                                                    print("jij verpest alles")
                                            else:
                                                print("fuckkkk offff")
                                        else:
                                            print("moet getal tussen 1-5")
                                    else:
                                        print("moet getal tussen 1-5")    
                                else:
                                    print("moet getal tussen 1-5")
                            except ValueError:
                                print("ik haat jou")
                        elif q3 == 4:
                            try:
                                q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                q4_4 = int(input("Op welke plek staat de vierde groene letter: "))
                                if q4 in number_placement:
                                    if q4_2 in number_placement:
                                        if q4_3 in number_placement:
                                            if q4_4 in number_placement:
                                                q5_1 = input("Wat is de eerste groene letter: ")
                                                q5_2 = input("Wat is de tweede groene letter: ")
                                                q5_3 = input("Wat is de derde groene letter: ")
                                                q5_4 = input("Wat is de vierde groene letter: ")
                                                if q5_1.isalpha():
                                                    if q5_2.isalpha():
                                                        if q5_3.isalpha():
                                                            if q5_4.isalpha():
                                                                if len(q5_1) == 1: 
                                                                    if len(q5_2) == 1:
                                                                        if len(q5_3) == 1:
                                                                            if len(q5_4) == 1:
                                                                                grl1 = q5_1.lower()
                                                                                grl2 = q5_2.lower()
                                                                                grl3 = q5_3.lower()
                                                                                grl4 = q5_4.lower()

                                                                                q4 = q4 - 1
                                                                                q4_2 = q4_2 - 1
                                                                                q4_3 = q4_3 - 1
                                                                                q4_4 = q4_4 - 1
                                                                                for a in words_list:
                                                                                    if grl1 == a[q4]:
                                                                                        if grl2 == a[q4_2]:
                                                                                            if grl3 == a[q4_3]:
                                                                                                if grl4 == a[q4_4]:
                                                                                                    awnsers.append(a)
                                                                                if not awnsers:
                                                                                    print("rip er zijn geen woorden met deze combinatie")
                                                                                else:
                                                                                    print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                            else:
                                                                                print("stop plz :(((")
                                                                        else:
                                                                            print("stop :(")
                                                                    else:
                                                                        print("AAAAAAAAAAAAAAAAA")
                                                                else:
                                                                    print("among us??") 
                                                            else:
                                                                print("its about power") 
                                                        else:
                                                            print("its about drive")                
                                                    else:
                                                        print("jij verpest alles")    
                                                else:
                                                    print("jij verpest alles")
                                            else:
                                                print("moet getal tussen 1-5")
                                        else:
                                            print("moet getal tussen 1-5")
                                    else:
                                        print("moet getal tussen 1-5")    
                                else:
                                    print("moet getal tussen 1-5")
                            except ValueError:
                                print("ik haat jou")
                        elif q3 == 5:
                            try:
                                q4 = int(input("Op welke plek staat de eerste groene letter: "))
                                q4_2 = int(input("Op welke plek staat de tweede groene letter: "))
                                q4_3 = int(input("Op welke plek staat de derde groene letter: "))
                                q4_4 = int(input("Op welke plek staat de vierde groene letter: "))
                                q4_5 = int(input("Op welke plek staat de vijfde groene letter: "))
                                if q4 in number_placement:
                                    if q4_2 in number_placement:
                                        if q4_3 in number_placement:
                                            if q4_4 in number_placement:
                                                if q4_5 in number_placement:
                                                    q5_1 = input("Wat is de eerste groene letter: ")
                                                    q5_2 = input("Wat is de tweede groene letter: ")
                                                    q5_3 = input("Wat is de derde groene letter: ")
                                                    q5_4 = input("Wat is de vierde groene letter: ")
                                                    q5_5 = input("Wat is de vijfde groene letter: ")
                                                    if q5_1.isalpha():
                                                        if q5_2.isalpha():
                                                            if q5_3.isalpha():
                                                                if q5_4.isalpha():
                                                                    if q5_5.isalpha():
                                                                        if len(q5_1) == 1: 
                                                                            if len(q5_2) == 1:
                                                                                if len(q5_3) == 1:
                                                                                    if len(q5_4) == 1:
                                                                                        if len(q5_5) == 1:
                                                                                            grl1 = q5_1.lower()
                                                                                            grl2 = q5_2.lower()
                                                                                            grl3 = q5_3.lower()
                                                                                            grl4 = q5_4.lower()
                                                                                            grl5 = q5_5.lower()

                                                                                            q4 = q4 - 1
                                                                                            q4_2 = q4_2 - 1
                                                                                            q4_3 = q4_3 - 1
                                                                                            q4_4 = q4_4 - 1
                                                                                            q4_5 = q4_5 - 1
                                                                                            for a in words_list:
                                                                                                if grl1 == a[q4]:
                                                                                                    if grl2 == a[q4_2]:
                                                                                                        if grl3 == a[q4_3]:
                                                                                                            if grl4 == a[q4_4]:
                                                                                                                if grl5 == a[q4_5]:
                                                                                                                    awnsers.append(a)
                                                                                            if not awnsers:
                                                                                                print("rip er zijn geen woorden met deze combinatie")
                                                                                            else:
                                                                                                print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                                                                                        else:
                                                                                            print("jij wint ik geef op")
                                                                                    else:
                                                                                        print("stop plz :(((")
                                                                                else:
                                                                                    print("stop plz :(((")
                                                                            else:
                                                                                print("stop plz :(((")
                                                                        else:
                                                                            print("stop :(")
                                                                    else:
                                                                        print("AAAAAAAAAAAAAAAAA")
                                                                else:
                                                                    print("among us??") 
                                                            else:
                                                                print("its about power") 
                                                        else:
                                                            print("its about drive")                
                                                    else:
                                                        print("jij verpest alles")    
                                                else:
                                                    print("moet getal tussen 1-5")
                                            else:
                                                print("moet getal tussen 1-5")
                                        else:
                                            print("moet getal tussen 1-5")
                                    else:
                                        print("moet getal tussen 1-5")    
                                else:
                                    print("moet getal tussen 1-5")
                            except ValueError:
                                print("ik haat jou")
                        elif q3 == 0:
                            awnsers = temporary_awnsers
                            print("Hier zijn je antwoorden LOSER " + ', '.join(awnsers))
                    else:
                        print("moet cijfer tussen 0-5")
                except ValueError:
                    print("fuck off")
            else:
                print("ik weet niet wat je hebt gedaan maar tis heel fucked")
        else:
            print("moet cijfer tussen 1-5")
    except ValueError:    
            print("fuck off")
    

while True:
    poopy()
 
