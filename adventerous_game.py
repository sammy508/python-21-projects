# Dventerous game


name = input("enter your name:")
print(f"Hello{name} Welcome to the Adventerous")

answer = input("You are on a dirt road and it comes to end , You wanna move right or left :").lower()

if answer == "right":
    answer = input(" You came to the river bank. You wanna cross it or turn back :").lower()
    if answer== "cross":

        answer = input("you wanna swim or cross by walking").lower()
        if answer == "walk":
            print("offs, you L00se. The bridge was broken")
            quit()
        elif answer == "swim":
            print("0hh, you crossed the river")

            answer = input("You have to move ahead , you wanna take shortcut or go longway. if wanna go shortway type short, if not type long")
            if answer == "short":
                print("you lazy, Dwarf you, you messedup.You looose ")
                quit()
            elif answer == "long":
                print("You reached to midhill, be ready for more adventour\n")

                answer = input("You wanna use stair or cable car. Type cable for cablecar and stair for walk").lower()

                if answer == "walk":
                    print("C0ngrats!!!! \n You reached to the top and it's your final destination")
                    quit()

                elif answer =="cable":
                    print("It was out of service! you loose bastard")
                    quit()


elif answer == "left":
      answer = input(" Here one black car was coming would you take a ride or you walk? type ride for ride and walk for walk:").lower()
      if answer == "ride":
            print("offs, you L00se. There's a murderer on car")
            quit()
      elif answer == "walk":
            print("0hh, you choose walk and reached to a mid way")

            answer = input("You have to move ahead , theres a jungle and you have 2 way which will you pick. if wanna go straight type straight, if wanna take secomd way type left")
            if answer == "straight":
                print("you loose man, you lost on a scary jungle")
                quit()
            elif answer == "straight":
                print("You reached to midhill, be ready for more adventour\n")

                answer = input("You wanna use stair or cable car. Type cable for cablecar and stair for walk").lower()

                if answer == "walk":
                    print("C0ngrats!!!! \n You reached to the top and it's your final destination")
                    quit()

                elif answer =="cable":
                    print("It was out of service! you loose bastard")
                    quit()
    


else:
    print("you are a fucking looser")        