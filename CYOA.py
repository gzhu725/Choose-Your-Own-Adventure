
import time

intro = "Hello! Today, you will determine whether Jisoo, a korean girl, should pursue and one day become a kpop idol herself."
beginning = "Once upon a time, there was a girl named Jisoo. Jisoo has a crazy dream: to one day be a kpop idol."
to_become = "Should Jisoo pursue her dream?"
no_become = "Unfortunately, Jisoo decides not to pursue her dream job as a kpop idol. She goes to Yonsei University and majors in computer science. She later finds a job near her home in Seoul and starts a new life, even if she still yearns for her kpop dream. Thanks for playing along!"
yes_become = "Jisoo asks her parents whether they approve. Her parents frown and say no to her."
asking_parents = "Should Jisoo continue her dream, even if her parents say no?"
yes_parents = "Jisoo ignores her parents' disdain. Although Jisoo has trained herself to dance, sing, and perform when she was young, she still has to choose an entertainment company to train with in order to gain the skills of a professional kpop idol."
yg_choice = "Jisoo auditions for YG; she makes it! But, after a year of training, it seems like Jisoo isn't going anywhere with training."
to_continue = "Should she continue?"
yg_continue = "Good choice! After another year, Jisoo finally debuts with three other girls in a group called BLACKPINK. Check out their music now!"
sm_success = 'Jisoo auditions for SM. She makes it and debuts with five other girls in a group called "Red Velvet". Thanks for helping Jisoo out!'
try_again = "Should she try again?"
jyp_choice = "Jisoo auditions for JYP, she makes it!"
jyp_description = "She is placed with a group of 8 other girls. While these girls are incredibly talented, they make fun of Jisoo because they are mean."
leave_jyp = "Should she leave the company?"
yes_leave_jyp = "Jisoo leaves."
no_leave_jyp = "Jisoo is trapped as a trainee at JYP and stays in the JYP dungeon forever, never getting a single chance to debut- bad luck!"
   
def yes_or_no():
    condition_to_run = False
    while condition_to_run == False:
        output=input("Answer yes or no: ")
        if (output == 'Yes') or (output == 'yes'):
            return(True)
            condition_to_run = True
        elif (output == 'No') or (output == 'no'):
                return(False)
                condition_to_run = True
        else:
                print("Your answer is unclear, please write yes or no.")

def agency_decision():
    keep_running = False
    print("Jisoo needs to choose an agency. She decides between the following companies: YG, JYP, and SM.")
    while keep_running == False:
        decision = input("Which one should she choose? ")
        if (decision == "YG") or (decision == 'yg'):
            keep_running = True
            print(yg_choice)
            print(to_continue)
            if yes_or_no():
                print(yg_continue)
            else:
                print(no_become)
        elif (decision == 'SM') or (decision == 'sm'):
            print(sm_success)
            keep_running = True
        elif (decision == 'JYP') or (decision == 'jyp'):
            keep_running = True
            print(jyp_choice)
            print(jyp_description)
            print(leave_jyp)
            if yes_or_no():
                print(yes_leave_jyp)
                print(try_again)
                if yes_or_no():
                    print("Jisoo tries again. Although she can audition for JYP again, JYP will still lead her down the same unsuccessful path.")
                    keep_running = False
                else:
                    print(no_become)
            else:
                print(no_leave_jyp)
        else:
            print("This is not a valid agency. Please try again.")
        
        

def kpop_journey():
    print(intro)
    time.sleep(2)
    print(beginning)
    time.sleep(3)
    print(to_become)
    if not yes_or_no():
        print(no_become)
    else:
        print(yes_become)
        print(asking_parents)
        if not yes_or_no():
            print(no_become)
        else:
            print(yes_parents)
            agency_decision()
    time.sleep(3)

kpop_journey()
        
            
    
        
    
