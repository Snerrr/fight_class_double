# Меню
import console
import fight
import text
import fiyght_2

def start():
    programma_start = True
    while programma_start:
        chois_1 = console.prinytie_chisla()
        match chois_1:
            case 1:
                vibor_start = True
                boy_1 = fight.Boy()
                boy_2 = fiyght_2.Boy_2()
                print(boy_1.info_boec_1())
                print(boy_1.info_boec_2())
                while vibor_start:
                    choise_2 = console.prinytie_chisla_vibor()
                    match choise_2:
                        case 1:
                            fight_start = True
                            while fight_start:
                                choise_3 = console.prinytie_chisla_fight_1()
                                print()
                                choise_bot = boy_1.random_vibor()
                                match choise_3:
                                    case 1:
                                        print(text.udaril_golovoy)
                                        print(boy_1.udar_golovoy())
                                        print(boy_1.zdorovie_1())
                                        if boy_1.proverka_boec_2() == 0:
                                            fight_start = vibor_start = boy_1.proverka_boec_2()
                                            print()
                                            print(boy_1.fighter_2.name, text.loze)
                                            break                               
                                    case 2:
                                        print(text.udaril_rukoy)
                                        print(boy_1.udar_rukoy())
                                        print(boy_1.zdorovie_1())
                                        if boy_1.proverka_boec_2() == 0:
                                            fight_start = vibor_start = boy_1.proverka_boec_2()
                                            print()
                                            print(boy_1.fighter_2.name, text.loze)
                                            break
                                    case 3:
                                        print(text.udaril_nogoi)
                                        print(boy_1.udar_nogoy())
                                        print(boy_1.zdorovie_1())
                                        if boy_1.proverka_boec_2() == 0:
                                            fight_start = vibor_start = boy_1.proverka_boec_2()
                                            print()
                                            print(boy_1.fighter_2.name, text.loze)
                                            break
                                    case 4:
                                        console.sdatsy()
                                        vibor_start = False
                                        fight_start = False 
                                        break 
                                print() 
                                match choise_bot:
                                    case 1:
                                        print(text.udaril_golovoy)
                                        print(boy_1.udar_golovoy_1())
                                        print(boy_1.zdorovie())
                                        if boy_1.proverka_boec_1() == 0:
                                            fight_start = vibor_start = boy_1.proverka_boec_1()
                                            print()
                                            print(boy_1.fighter_1.name, text.loze) 
                                            break                               
                                    case 2:
                                        print(text.udaril_rukoy)
                                        print(boy_1.udar_rukoy_1())
                                        print(boy_1.zdorovie())
                                        if boy_1.proverka_boec_1() == 0:
                                            fight_start = vibor_start = boy_1.proverka_boec_1()
                                            print()
                                            print(boy_1.fighter_1.name, text.loze)
                                            break
                                    case 3:
                                        print(text.udaril_nogoi)
                                        print(boy_1.udar_nogoy_1())
                                        print(boy_1.zdorovie())
                                        if boy_1.proverka_boec_1() == 0:
                                            fight_start = vibor_start = boy_1.proverka_boec_1()
                                            print()
                                            print(boy_1.fighter_1.name, text.loze)
                                            break
                                                                         
                        case 2:
                            fight_start_1 = True
                            while fight_start_1:
                                choise_4 = console.prinytie_chisla_fight_2()
                                print()
                                choise_bot = boy_2.random_vibor()
                                match choise_4:
                                    case 1:
                                        print(text.udaril_golovoy)
                                        print(boy_2.udar_golovoy_1())
                                        print(boy_2.zdorovie())
                                        if boy_2.proverka_boec_1() == 0:
                                            fight_start_1 = vibor_start = boy_2.proverka_boec_1()
                                            print()
                                            print(boy_2.fighter_1.name, text.loze)
                                            break                               
                                    case 2:
                                        print(text.udaril_rukoy)
                                        print(boy_2.udar_rukoy_1())
                                        print(boy_2.zdorovie())
                                        if boy_2.proverka_boec_1() == 0:
                                            fight_start_1 = vibor_start = boy_2.proverka_boec_1()
                                            print()
                                            print(boy_2.fighter_1.name, text.loze)
                                            break
                                    case 3:
                                        print(text.udaril_nogoi)
                                        print(boy_2.udar_nogoy_1())
                                        print(boy_2.zdorovie())
                                        if boy_2.proverka_boec_1() == 0:
                                            fight_start_1 = vibor_start = boy_2.proverka_boec_1()
                                            print()
                                            print(boy_2.fighter_1.name, text.loze)
                                            break
                                    case 4:
                                        console.sdatsy()
                                        vibor_start = False
                                        fight_start_1 = False 
                                        break 
                                print() 
                                match choise_bot:
                                    case 1:
                                        print(text.udaril_golovoy)
                                        print(boy_2.udar_golovoy())
                                        print(boy_2.zdorovie_1())
                                        if boy_2.proverka_boec_2() == 0:
                                            fight_start_1 = vibor_start = boy_2.proverka_boec_2()
                                            print()
                                            print(boy_2.fighter_2.name, text.loze) 
                                            break                               
                                    case 2:
                                        print(text.udaril_rukoy)
                                        print(boy_2.udar_rukoy())
                                        print(boy_2.zdorovie_1())
                                        if boy_2.proverka_boec_2() == 0:
                                            fight_start_1 = vibor_start = boy_2.proverka_boec_2()
                                            print()
                                            print(boy_2.fighter_2.name, text.loze)
                                            break
                                    case 3:
                                        print(text.udaril_nogoi)
                                        print(boy_2.udar_nogoy())
                                        print(boy_2.zdorovie_1())
                                        if boy_2.proverka_boec_2() == 0:
                                            fight_start_1 = vibor_start = boy_2.proverka_boec_2()
                                            print()
                                            print(boy_2.fighter_2.name, text.loze)
                                            break
                                    
                                        
            case 2:
                console.vihod()
                programma_start = False
            
    