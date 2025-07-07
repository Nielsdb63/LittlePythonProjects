import random
import sys
import time

player = input('What is your name? ' )

races = ['Bahrain', 'Imola', 'Portugal', 'Spain','Monaco', 'Azerbaijan', 'France', 'Steiermark', 'Austria', 'Great Britain', 'Hungary', 'Belgium', 'The Netherlands', 'Italy', 'Russia', 'Turkey', 'United States', 'Mexico', 'Brazil', 'Qatar', 'Saudi Arabia', 'Abu Dhabi']

drivers = {'Verstappen': 395.5, 'Hamilton': 387.5, 'Bottas': 226, 'Perez': 190, 'Sainz': 164.5, 'Norris': 160, 'Leclerc': 159, 'Ricciardo': 115, 'Gasly': 110, 'Alonso': 81, 'Ocon': 74, 'Vettel': 43, 'Stroll': 34, 'Tsunoda': 32, 'Russell': 16, 'Raikkonen': 10, 'Latifi': 7, 'Giovinazzi': 3, 'Schumacher': 0, 'Mazepin': 0}

results = {}

def williams():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print("Williams did not finish their car in time for the season. You're out. Back to F2.")
    sys.exit()
  else:
    team = "williams"
    for i in range(len(races)):
      currentrace = races[i]
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition

  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)

def haas():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print("Oh no! Turns out your daddy isn't as rich as Mazepin's daddy! Guenther Steiner doesn't want such a wanker on his team. Back to F2.")
    sys.exit()
  else:
    team = "haas"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)


def alfaromeo():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print ("Oh no! Kimi has changed his mind, and wants to keep his hobby going for yet another year, there won't be a seat left for you. Back to F2.")
    sys.exit()
  else:
    team = "alfa romeo"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def alphatauri():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print ("Oh no! The second driver at Red Bull was not winning every race! They were transferred back to Alpha Tauri, so no seat for you! Back to F2!")
    sys.exit()
  else:
    team = "alpha tauri"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def ferrari():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print ("Oh no! Ferrari is caught with an illegal power unit. Since this is the second time in two years they are caught with illegal parts, they are disqualified for this season. Back to F2! ")
    sys.exit()
  else:
    team = "ferrari"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def mclaren():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print("Oh no! McLaren wants TWO funny drivers, not one! Gotta work on those jokes, kid. Better luck next time. Back to F2!")
    sys.exit()
  else:
    team = "mclaren"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def alpine():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print ("Oh no! Alonso decided that he want to have another shot at the WDC this season, and alpine decides not to get you a seat. Better luck next season. Back to F2.")
    sys.exit()
  else:
    team = "alpine"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def astonmartin():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print  ("Oh no! Aston martin was caught copying the Mercedes of last season, again. They are disqualified, wich means no seat for you this season. Back to F2!")
    sys.exit()
  else:
    team = "astonmartin"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def redbull():
  rand = random.random()
  if rand < 0.1:
    time.sleep(2)
    print ("Oh no! Red Bull doesn't have an engine manufacturer and can't create a finished car. No seat for you pal. Back to F2!")
    sys.exit()
  else:
    team = "red bull"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def mercedes():
  rand = random.random()
  if rand < 0.1:
    print("Hamilton decides you are too good and decides you can't be the second driver. You're out. Back to F2.")
    sys.exit()
  else:
    team = "mercedes"
    for i in range(len(races)):
      currentrace = races[i]
      time.sleep(6)
      print('\n \n \n \n')
      position = quali(team, currentrace)
      raceposition = race(position, team, currentrace)
      results[currentrace] = raceposition
  points = pointcalc(results)
  print('\n\n\n\n')

  time.sleep(5)
  print(results, points)

  time.sleep(2)
  print('\n\n\n\n')
  standing = standings(team, points)

  print(standing)



def quali(team, race):
  time.sleep(2)
  print("Welcome to the Grand Prix of " + str(race) +'!')

  if team == "williams" or team == 'haas' or team == 'alfa romeo':
    chance = random.random()
    if chance < 0.4:
      position = 20
    elif chance < 0.75:
      position = 19
    elif chance < 0.90:
      position = 18
    else:
      position = 17

  elif team == "mercedes" or team == "red bull":
    chance = random.random()
    if chance < 0.45:
      position = 4
    elif chance < 0.75:
      position = 3
    elif chance < 0.90:
      position = 2
    else:
      position = 1

  elif team == "mclaren" or team ==  "ferrari":
    chance = random.random()
    if chance < 0.4:
      position = 8
    elif chance < 0.6:
      position = 9
    elif chance < 0.8:
      position = 7
    elif chance < 0.9:
      position = 6
    else:
      position = 10

  elif team == "alpine" or team == "alpha tauri":
    chance = random.random()
    if chance < 0.3:
      position = 7
    elif chance < 0.4:
      position = 6
    elif chance < 0.5:
      position = 8
    elif chance < 0.55:
      position = 4
    elif chance < 0.6:
      position = 9
    elif chance < 0.8:
      position = 11
    else:
      position = 12

  elif team == "aston martin":
    chance = random.random()
    if chance < 0.5:
      position = 12
    if chance < 0.7:
      position = 11
    if chance < 0.9:
      position = 13
    if chance < 0.95:
      position = 14
    else:
      position = 10

  time.sleep(2)
  if position > 18:
    print("You left a lot on the table there, your team is not happy. You will start at position " + str(position) + "!")
  else:
    print("Good job at qualifying! You will start at position " + str(position) + "!")
  time.sleep(2)
  return position



def race(position, team, currentrace):
  if position < 11:
    print("You made it to Q3 on soft tyres, so you will have to start the race on the softs.")
    tyre = "softs"
  else:
    tyre = input("You did not make it to Q3, what tyre would you like to start on? Softs, Mediums or Hards? " )

  chance = random.random()
  #chance = 2
  if chance < 0.005:
    print("You drive into the wall during the formation lap!")
    time.sleep(3)
    hitwalldeath()
  
  if chance < 0.04:
    finishposition = covid(team)

  elif chance < 0.08:
    finishposition = mechfailure(team)
  
  elif chance < 0.35:
    finishposition = rain(position, team, tyre, currentrace) 
  
  elif chance < 0.65:
    finishposition = klapband(position, team, tyre, currentrace) 

  elif chance < 0.75:
    finishposition = frontwing(position, team, tyre, currentrace)

  elif chance < 0.85: 
    finishposition = spin(position, team, tyre, currentrace)

  elif chance < 0.98:
    finishposition = bottasbowlen(position, team, tyre, currentrace)

  elif chance < 1:
    finishposition = crashgate(team, currentrace)

  return finishposition



def rain(position, team, tyre, currentrace):
  chance = random.random()
  if chance < 0.4:
    rainchance = "50"
    rdec = 0.5
  elif chance < 0.7:
    rainchance = "80"
    rdec = 0.8
  else:
    rainchance = "20"
    rdec = 0.2

  print("It's raceday and there is a chance of rain lurking here at the Grand Prix of " + currentrace + '!')
  chance = random.random()
  raceposition = position
  if position > 10:
    if tyre == 'softs': 
      raceposition = int(position) - 2
      print("You had an amazing start and made up 2 places! You are now in P" + str(raceposition)+ "!")

      time.sleep(5)

      pit = input("Your softs are getting pretty worn. It is lap 15, with 45 more to go. You could pit now to go to the hards and finish the race on that tyre. However, your engineer told you there is a "+rainchance+"% chance of rain in the next 10 laps. If you would pit for hards now you would have to pit again. It's your choice, do you pit? " )
      lap = 15
      opptyre = 'hards'
    if tyre == "mediums":
      print("You had an average start and you maintained your start position.")
      time.sleep(3)
      pit = input("Your mediums are getting pretty worn. It is lap 25, with 35 more to go. You could pit now to go to the hards and finish the race on that tyre. However, your engineer told you there is a "+rainchance+"% chance of rain in the next 10 laps. If you would pit for hards now you would have to pit again. It's your choice, do you pit? " )
      lap = 25
      opptyre = 'hards'
    if tyre == "hards":
      if position < 18:
        raceposition = position + 2
        print("You had a terrible start to the race and you have dropped back 2 places! You are now in position " + str(raceposition) + ".")
      else:
        print("You had a bad start and made up no positions.")
      time.sleep(3)
      pit = input("Your hards are getting pretty worn. It is lap 40, with 20 more to go. You could pit now to go to the softs and finish the race on that tyre. However, your engineer told you there is a "+rainchance+"% chance of rain in the next 10 laps. If you would pit for softs now you would have to pit again. It's your choice, do you pit? " )

      lap = 40
      opptyre = 'softs'

    if chance < rdec:
      if pit.lower() == 'yes':
        print("You pitted for "+opptyre+" tires on lap "+str(lap)+".")
        time.sleep(2)
        print("It has started to rain! You have to pit again for the wet tyres!")
        time.sleep(3)
        print("After that major pitblunder you end the race in P19.")
        raceposition = 19
      else:
        if position != 20:
          print("You chose not to pit for "+opptyre+" on lap "+str(lap)+".")
          time.sleep(2)
          raceposition += 1
          print("You lost one position due to your tyres falling off, your position is " + str(raceposition))
          time.sleep(2)
          raceposition -= 6
          print("It has started to rain! Thank God you didn't pit for "+opptyre+" like the others did! You pit for the wets.")
          time.sleep(3)
          print("You made up 6 positions! You are in P" + str(raceposition) + "!")
          time.sleep(2)
          print("After your genius pitstrategy you end up in P" + str(raceposition) + "!")
        else:
          print("You chose not to pit for "+opptyre+" on lap "+str(lap)+".")
          time.sleep(2)
          print("You lose a lot of time due to your tyres falling off")
          time.sleep(2)
          raceposition -= 5
          print("It has started to rain! Thank God you didn't pit for "+opptyre+" like the others did! You pit for the wets.")
          time.sleep(3)
          print("You made up 6 positions! You are in P" + str(raceposition) + "!")
          time.sleep(2)
          print("After your genius pitstrategy you end up in P" + str(raceposition) + "!")

    else:
      if pit.lower() == "yes":
        print("You lose 2 positions and you go to the "+opptyre+", others around you continue on the "+tyre+".")
        raceposition += 2
        time.sleep(2)
        raceposition -= 3
        print("You start to pass the people on older "+tyre+" around you! You are now in position " + str(raceposition) + "!")
        time.sleep(2)
        print("The people who stayed out are only now pitting for "+opptyre+". You win another 3 places")
        raceposition -= 3
        time.sleep(2)
        print("Your brilliant pit strategy has delivered you a P" + str(raceposition) + "! Well done!")
      else:
        print("You did not pit for the "+opptyre+", others around you did. You win 3 positions!")
        time.sleep(3)
        print("It has become painfully clear it will not rain, so you pit for "+opptyre+" as well. In the meantime the other have come closer.")
        time.sleep(2)
        print("It is now lap 42 and you are in P20, but you are on newer "+opptyre+"!")
        time.sleep(3)
        print("Your failed pitstrategy, but late overtaking resulted in a P18")
        raceposition = 18
  elif position < 5:
    print("You start off brilliantly from P"+ str(position) +", and you manage to keep it! You settle into the race.")
    time.sleep(4)

    pit = input("Your softs are getting pretty worn. It is lap 15, with 45 more to go. You could pit now to go to the hards and finish the race on that tyre. However, your engineer told you there is a "+rainchance+"% chance of rain in the next 10 laps. If you would pit for hards now you would have to pit again. It's your choice, do you pit? " )

    chance = random.random()
    if chance < rdec:
      if pit == "yes":
        print("You decided to pit while the others kept driving. You are now in lap 20 and it starts to rain. You regret pitting for hards, as you now have to pit for wets. But before you enter the pitlane, you slip and lose control.")
        time.sleep(5)
        print("You spin, but save half the car as you lose your frontwing. You lose time on your inlap, and even more in the pit.")
        time.sleep(2.5)
        print("You fall back to eighth, but manage to climb back to fifth.")
        raceposition = 5
      else:
        print("You decide to stay out, while the others box for hards.")
        time.sleep(3)
        print("Come lap 20 it has started to rain, you come in to box for wets.")
        time.sleep(2)
        print("Your pitstrategy worked brilliantly and you secure the win! " + team.capitalize() +" is very happy with you!")
        raceposition = 1
    else:
      if pit == "yes":
        print("The threat of rain does nothing to you as you decide to box, the others mostly stay out.")
        time.sleep(3)
        print("It is now lap 35 and it has not rained, the others fall behind on their older tyres.")
        time.sleep(3)
        print("Your pitstrategy worked brilliantly and you secure the win!" + team.capitalize() +" is very happy with you!")
        raceposition = 1

      else:
        if pit == "no":
          print("The treat of rain gets the best of you and you decide not to box, all the others decide to change their tyres.")
          time.sleep(3)
          print("You fall behind on your older tyres as the rain stays out, you regret your decision.")
          time.sleep(3)
          print("You fall back to eighth, but manage to climb back to fifth.")
          raceposition = 5

  else:
    print("You start off brilliantly from P"+ str(position) +", and you manage to keep it! You settle into the race.")
    time.sleep(4)

    pit = input("Your softs are getting pretty worn. It is lap 15, with 45 more to go. You could pit now to go to the hards and finish the race on that tyre. However, your engineer told you there is a "+rainchance+"% chance of rain in the next 10 laps. If you would pit for hards now you would have to pit again. It's your choice, do you pit? " )

    if chance < rdec:
      if pit == "yes":
        print("You decided to pit while the others kept driving. You are now in lap 20 and it starts to rain. You regret pitting for hards, as you now have to pit for wets. But before you enter the pitlane, you slip and lose control.")
        time.sleep(5)
        print("You spin, but save half the car as you lose your frontwing. You lose time on your inlap, and even more in the pit.")
        time.sleep(2.5)
        print("You fall back to twelfth, but manage to climb back to tenth.")
        raceposition = 10
      else:
        print("You decide to stay out, while the others box for hards.")
        time.sleep(3)
        print("Come lap 20 it has started to rain, you come in to box for wets.")
        time.sleep(2)
        print("Your pitstrategy worked brilliantly and you secure P4! " + team.capitalize() +" is very happy with you!")
        raceposition = 4
    else:
      if pit == "yes":
        print("The threat of rain does nothing to you as you decide to box, the others mostly stay out.")
        time.sleep(3)
        print("It is now lap 35 and it has not rained, the others fall behind on their older tyres.")
        time.sleep(3)
        print("Your pitstrategy worked brilliantly and you secure P4! " + team.capitalize() +" is very happy with you!")
        raceposition = 4

      else:
        if pit == "no":
          print("The treat of rain gets the best of you and you decide not to box, all the others decide to change their tyres.")
          time.sleep(3)
          print("You fall behind on your older tyres as the rain stays out, you regret your decision.")
          time.sleep(3)
          print("You fall back to twelfth, but manage to climb back to tenth.")
          raceposition = 10
  return raceposition




def crashgate(team, currentrace):
  print(f'After the qualifying of the Grand Prix of {currentrace}, {team.capitalize()} has not been performing as well as they would like. They decide they have to resort to extreme measures. They enlist the help of Flavio Briatore and start planning.')

  time.sleep(5)
  
  chance = random.random()
  if chance > 0.4:
    crash = input(str(team).capitalize()+' comes to you and tell you they are planning to have your teammate crash on purpose so you can use the perfect strategy to win the race. They say if you agree with their plan you are guaranteed the win. \nDo you say yes or no? ' )
    if crash == 'yes':
      chance2 = random.random()
      if chance2 > 0.5:
        print('You agree with the plan and everything goes ahead as planned, you use a strange but good strategy.')

        time.sleep(3)

        print('The plan works and you win the race!')

        raceposition = 1
      
      else:
        print('You agree with the plan and everything goes ahead as planned, you use a strange but good strategy.')

        time.sleep(3)

        print('The plan works, but people are having a lot of doubts about the validity of your teammates crash. The FIA decides to investigate.')

        time.sleep(4)

        print('The FIA finds you, your teammate and the whole of '+str(team).capitalize()+' guilty. Your win is taken away, you are disqualified from the race, and it is unlikely any team wants to be associated with you in the future.')
    else:
      print(str(team).capitalize()+' is angry with you, they tell you you will not be racing with them next year, and they sabotage your car for the Grand Prix of '+str(currentrace)+'. You DNF.')

      raceposition = 'DNF'

  else:
    crash = input(str(team).capitalize()+' comes to you and tell you they are planning to have you crash on purpose so your teammate can use a perfect strategy to win. They say if you agree with their plan he is guaranteed the win and you are guaranteed another year with the team. \nDo you say yes or no? ' )
    if crash == 'yes':
      chance2 = random.random()
      if chance2 > 0.5:
        print('You agree with the plan and everything goes ahead as planned, your teammate uses a strange but good strategy.')

        time.sleep(3)

        print('The plan works and he wins the race! You DNF')

        raceposition = 'DNF'
      
      else:
        print('You agree with the plan and everything goes ahead as planned, your teammate uses a strange but good strategy.')

        time.sleep(3)

        print('The plan works, but people are having a lot of doubts about the validity of your crash. The FIA decides to investigate.')

        time.sleep(4)

        print('The FIA finds you, your teammate and the whole of '+str(team).capitalize()+' guilty. His win is taken away, you are disqualified, and you are not allowed to continue racing in Formula 1.')

        sys.exit()
    else:
      print(str(team).capitalize()+' is angry with you, they tell you you will not be racing with them next year, and they sabotage your car for the Grand Prix of '+str(currentrace)+". You DNF.")

      raceposition = 'DNF'

  return raceposition



def klapband(raceposition, team, tyre, currentrace):
  print("It's race day at the Grand Prix of " + currentrace +"!")
  position = raceposition
  chance = random.random()
  if chance < 0.75:
    klaplap = '35'
  else:
    klaplap = '58'

  time.sleep(2)

  if position > 10:
    if tyre == 'softs':
      print('You start on the softs and you immediately make up a place in the first corner! However, you immediately lose it in the second.')
      raceposition = int(raceposition)

      time.sleep(4)

      pit = input('It is lap 20/60, you can choose to pit now and go to the hards, or you could stay out on your old softs and go to the mediums. \nThe hard strategy would be slower, but staying out could lead to a spin or a puncture. \nDo you pit? ' )
      
      time.sleep(5)

      if pit.lower() == 'yes':
        if klaplap == '58':
          print('You chose to go with the safer strategy, it is paying off as you made up 2 positions so far!')

          time.sleep(4)

          print('The driver in front of you crashes and leaves debris all over the place! You drive straight through it and you get a puncture in your tyre! \nYou pit and as it is the last lap now, you end up only above the driver that crashed in P19')

          raceposition = 19

        else:
          print('You chose to go with the safer strategy, it is paying off as you made up 2 positions so far!')

          time.sleep(4)

          raceposition = int(raceposition) - 2

          print('You drive a good and safe race to a reasonable finishing position of '+ str(raceposition)+ '!')
      
      else:
        if klaplap == '35':
          print('You try to stay out until lap 30, but you start to slide around more and more.')

          time.sleep(3)

          print('You get a punture on lap 28! You lose all the positions you have gained so far, and you roll into the pits in last place!')

          time.sleep(3)

          print('There was still some time to catch up again, but you only manage a lowly P19.')
          
          raceposition = 19

        else:
          print('You try to stay out until lap 30, but you start to slide around more and more.')

          time.sleep(3)

          print('You manage to keep the car on track and keep the tyres in good condition! You go into the pits for new mediums.')

          time.sleep(4)

          raceposition = int(raceposition) - 4

          print('You made the strategy work perfectly! You made up 4 positions with your great driving! You end up in P' +str(raceposition)+'!')
          
    elif tyre == 'mediums':
      print('You start on the mediums and you immediately make up a place in the first corner!')
      raceposition = int(raceposition) - 1

      time.sleep(4)

      pit = input('It is lap 30/60, you can choose to pit now and go to the hards, or you could stay out on your old mediums and go to the softs. \nThe hards strategy would be slower, but staying out could lead to a spin or a puncture. \nDo you pit? ' )
      
      time.sleep(5)

      if pit.lower() == 'yes':
        if klaplap == '58':
          print('You chose to go with the safer strategy, it is paying off as you made up 1 position so far!')

          time.sleep(4)

          print('The driver in front of you crashes and leaves debris all over the place! You drive straight through it and you get a puncture in your tyre! \nYou pit and as it is the last lap now, you end up only above the driver that crashed in P19')

          raceposition = 19

        else:
          print('You chose to go with the safer strategy, it is paying off as you made up 1 positions so far!')

          time.sleep(4)

          raceposition = int(raceposition) - 1


          print('You drive a good and safe race to a reasonable finishing position of '+ str(raceposition)+ '!')
      
      else:
        if klaplap == '35':
          print('You try to stay out until lap 40, but you start to slide around more and more.')

          time.sleep(3)

          print('You get a punture on lap 37! You lose all the positions you have gained so far, and you roll into the pits in last place!')

          time.sleep(3)

          print('There was still some time to catch up again, but you only manage a lowly P18.')
          
          raceposition = 18

        else:
          print('You try to stay out until lap 40, but you start to slide around more and more.')

          time.sleep(3)

          print('You manage to keep the car on track and keep the tyres in good condition! You go into the pits for new softs.')

          time.sleep(4)

          raceposition = int(raceposition) - 5

          print('You made the strategy work perfectly! You made up 5 positions with your great driving! You end up in P' +str(raceposition)+'!')
    
    else:
      print('You start on the hards and you immediately make up a place in the first corner!')
      raceposition = int(raceposition) - 1

      time.sleep(4)

      pit = input('It is lap 35/60, you can choose to pit now and go to the mediums, or you could stay out on your old hards and go to the softs. \nThe mediums strategy would be slower, but staying out could lead to a spin or a puncture. \nDo you pit? ' )
      
      time.sleep(5)

      if pit.lower() == 'yes':
        if klaplap == '58':
          print('You chose to go with the safer strategy, it is paying off as you made up 1 position so far!')

          time.sleep(4)

          print('The driver in front of you crashes and leaves debris all over the place! You drive straight through it and you get a puncture in your tyre! \nYou pit and as it is the last lap now, you end up only above the driver that crashed in P19')

          raceposition = 19

        else:
          print('You chose to go with the safer strategy, and you keep your position so far!')

          time.sleep(4)

          raceposition = int(raceposition) 


          print('You drive a good and safe race to a reasonable finishing position of '+ str(raceposition)+ '!')
      
      else:
        if klaplap == '35':
          print('You try to stay out until lap 42, but you start to slide around more and more.')

          time.sleep(3)

          print('You get a punture on lap 38! You lose all the positions you have gained so far, and you roll into the pits in last place!')

          time.sleep(3)

          print('There was still some time to catch up again, but you only manage a lowly P18.')
          
          raceposition = 18

        else:
          print('You try to stay out until lap 38, but you start to slide around more and more.')

          time.sleep(3)

          print('You manage to keep the car on track and keep the tyres in good condition! You go into the pits for new softs.')

          time.sleep(4)

          raceposition = int(raceposition) - 4

          print('You made the strategy work perfectly! You made up 4 positions with your great driving! You end up in P' +str(raceposition)+'!')
  
  elif position < 5:
    print('You start on your used softs and you lose a place on the first lap!')
    raceposition = int(raceposition) + 1
    time.sleep(1)
    print('Now you want to win this race using strategy. You can go try and go to lap 26 and go to the mediums, or you can pit on lap 19 and go to the hards. \nThe hards strategy is slower, but the if you stay on the softs for too long you might spin or get a punture.')
    
    time.sleep(1)

    pit = input('It is lap 19, do you pit? ' )

    if pit == 'yes':
      if klaplap == '58':
        print('You decide to play safe and think about the bigger picture.')

        time.sleep(2)
        
        print('It is now lap 57/60 and you have not regained the position you lost at the start, when you suddenly see the driver in front of you crash!')
        
        time.sleep(1)

        print('You are forced to drive through the debris, and you get a puncture! You limp home to the pits to put on new softs.')

        time.sleep(2)

        print('You try your best, but you can only manage a P7')
        
        raceposition = 7
      
      else:
        print('You decide to play safe and think about the bigger picture.')

        time.sleep(2)

        print('You drive to the finish line safely but you do not retake the position you lost at the start.')
    else:
      if klaplap == '35':
        print('You decide to gamble and you try to make it to lap 26 on your old softs.')
        
        time.sleep(3)
        
        print('The gamble does not pay off as you get a puncture on lap 24. You do go to the mediums in hopes of regaining some of the many positions you lost.')

        time.sleep(2)
        raceposition = int(raceposition) + 3
        print('You manage to climb back a bit to P'+str(raceposition)+'.')
        
      else:
        print('You decide to gamble and you try to make it to lap 26 on your old softs.')
        
        time.sleep(3)

        print('With a lot of slipping and sliding you finally make it to the pits without losing a position.')
        
        time.sleep(2)

        if position < 3:
          print('Your gamble worked out perfectly and you manage to pass the drivers in front of you to take the win! Good job!')

          raceposition = 1
          
        else:
          print('Your gamble worked out very well! You even end up on the podium in P3!')

          raceposition = 3
      
  else:
    print('You start on your used softs and you lose a place on the first lap!')
    raceposition = int(raceposition) + 1
    time.sleep(1)
    print('Now you want to gain places using strategy. You can go try and go to lap 26 and go to the mediums, or you can pit on lap 19 and go to the hards. \nThe hards strategy is slower, but the if you stay on the softs for too long you might spin or get a punture.')
    
    time.sleep(2)

    pit = input('It is lap 19, do you pit? ' )

    if pit == 'yes':
      if klaplap == '58':
        print('You decide to play safe and think about the bigger picture.')

        time.sleep(2)
        
        print('It is now lap 57/60 and you have regained the position you lost at the start, when you suddenly see the driver in front of you crash!')
        
        
        time.sleep(1)

        print('You are forced to drive through the debris, and you get a puncture! You limp home to the pits to put on new softs.')

        time.sleep(2)

        raceposition = int(raceposition) + 3
        
        print('You try your best, but you can only manage a P'+str(raceposition)+'.')
        
      
      else:
        print('You decide to play safe and think about the bigger picture.')

        time.sleep(2)

        print('You drive to the finish line safely and you retake the position you lost at the start.')

        raceposition = int(raceposition) -1
    else:
      if klaplap == '35':
        print('You decide to gamble and you try to make it to lap 26 on your old softs.')
        
        time.sleep(3)
        
        print('The gamble does not pay off as you get a puncture on lap 24. \nYou do go to the mediums in hopes of regaining some of the many positions you lost.')

        time.sleep(2)
        raceposition = int(raceposition) + 4
        print('You manage to climb back a bit to P'+str(raceposition)+'.')
        
      else:
        print('You decide to gamble and you try to make it to lap 26 on your old softs.')
        
        time.sleep(3)

        print('With a lot of slipping and sliding you finally make it to the pits without losing a position.')
        
        time.sleep(2)

        if position < 7:
          print('Your gamble worked out very well! You even end up on the podium in P3!')

          raceposition = 3
          
        else:
          print('Your gamble worked out very well! You even almost make it to the podium in P4!')

          raceposition = 4
    
  return raceposition
  


def spin(raceposition, team, tyre, currentrace):
  time.sleep(5)
  print("It's raceday at the Grand Prix of " + currentrace +"!")
  position = raceposition
  chance = random.random()
  if chance < 0.5:
    spin = '10'
  elif chance < 0.75:
    spin = '32'
  else:
    spin = '50'

  time.sleep(5)

  if position > 10:
    if tyre == 'softs': 
      print("You have an amazing start, you gain 2 places!")
      
      time.sleep(5)
      
      if spin == '10':
        raceposition = 18
        print('Oh no! You spin in lap 10 because of some rookie oversteer. \nYou fall back to P20, but because you are on soft and would pit anyways you are able to climb back to place 18 where you finish.')
       
      elif spin == '32':
        raceposition = 20
        print('Oh no! You spin right after pitting for a fresh set of tyres. \nBecause of the spin your tyres are covered in flat spots and to avoid a flat you have to pit again. You manage to finish the race, but end up in P20...')
       
      elif spin == '50':
        raceposition = 20
        print('Oh no! You spin right after pitting for a fresh set of tyres. \nBecause of the spin your tyres are covered in flat spots and to avoid a flat you have to pit again. You manage to finish the race, but end up in P20...')

    elif tyre == 'mediums':
      print('You have a good start and gain 1 position')
      
      time.sleep(3)
      
      if spin == '10':
        raceposition = 20
        print('Oh no! You spin in lap 10 and your tyres are done for. \nYou cant keep driving with the bad mediums and have to pit early. You cant make up any positions and finish in P20 ')
       
      elif spin == '32':
        raceposition = 18
        print('WHAT happened?? You spin in lap 32! Luckily you had not pitted yet, and you are able to do so right now. Even after falling back to P20 you manage to finish in P18.')
       
      elif spin == '50':
        raceposition = 20
        print('Oh no! You were doing so well, but you spin in lap 50 after pitting already! You have to pit again and lose all your progress. You finish P20.')

    else:
      print('You have an average start and hold your position.')
      
      time.sleep(3)
      
      if spin == '10':
        raceposition = 20
        print('You rookie! You spin in lap 10 and have to pit with only 10 laps on your hards. You fall back to P20 where you stay the whole race...')
       
      elif spin == '32':
        raceposition = 20
        print('You rookie! You spin in lap 32 and have to pit with only 32 laps on your hards. You fall back to P20 where you stay the whole race...')
       
      elif spin == '50':
        raceposition = 18
        print('You rookie! You spin in lap 50 and have to pit with only 10 laps on your new softs. You fall back to P20 but you climb back to P18')


  elif position < 5:
    print('Your start was good, you keep your position.')
    time.sleep(3)
    
    if spin == '10':
      raceposition = int(raceposition) + 1
      print('Crap! You spin in lap 10... You fall back, but manage to get back up again to one position lower than your starting place, damage control. \nYou finish in P'+str(raceposition)+'!')
       
    elif spin == '32':
      raceposition = 8
      print('You have just pitted to switch your old softs for a fresh pair of hards when you spin in lap 32! You have to pit again and lose so many positions... \nYou cant do good and eventually finish in P8, not a great race.')
       
    elif spin == '50':
      raceposition = 7
      print('Ten laps before the finish you spin! You have to pit again and have no time to gain back any positions. You cross the line in P7')
    

  else:
    print('Wow! Amazing start, you gain one place!')
    raceposition = int(raceposition) - 1
    time.sleep(3)
       
        
    if spin == '10':
      raceposition = int(raceposition) + 1
      print('Oh no, already in lap 10 you spin on your softs that still had some life in them... You have to pit and lose many positions. \nYou can gain some back, but you end up in the same position you started in...')
       
    elif spin == '32':
      raceposition = 17
      print('How is this possible? You just pitted for a fresh pair of hards and you lose control and spin. You will have to pit again for a fresh pair. \nYou lose many positions and end up in P17')
       
    elif spin == '50':
      raceposition = 16
      print('How is this possible? You just pitted for a fresh pair of mediums and you lose control and spin. You will have to pit again for a fresh pair. \nYou lose many positions and end up in P16')
    

  return raceposition



def frontwing(raceposition, team, tyre, currentrace):
  print("It's raceday at the Grand Prix of " + currentrace +"!")
  position = raceposition
  chance = random.random()
  if chance < 0.75:
    klaplap = '35'
  else:
    klaplap = '58'

  time.sleep(2)

  if position > 10:
    if tyre == 'softs':
      print('You start on the softs and you immediately make up a place in the first corner! However, because you were a greedy basterd you lose it again in the second corner when trying to overtake again.')
      raceposition = int(raceposition)

      time.sleep(4)

      pit = input('It is lap 23/60, you have a touch with the driver in front of you, your wing suffers some damage... You can decide to keep racing, or to pit.\nThe pitting strategy would be slower, but staying out could lead to a crash. \nDo you pit? ' )
      
      time.sleep(5)

      if pit.lower() == 'yes':
        if klaplap == '58':
          print('You chose to go with the safe strategy, it cost you two positions, but now that you are back on track you gain them back in no time.')

          time.sleep(4)
          raceposition = int(raceposition) - 1

          print('Good thing you got a new wing! Turns out there was major damage to the wing and you would have crashed if you kept going. You keep the positions you made up, and even gain one more! \nYou finish in P'+str(raceposition)+'!')

        else:
          if position > 18:
            raceposition = 20
          
            print('You chose to go with the safer strategy, stopping for a new wing took a lot of time, you drop two positions.') 
          
            time.sleep(4)
          
            print('The rest of the race was okay, it turned out the wing was damaged, good thing you changed it. You finish P20')

          if position < 18:
            raceposition = position + 2
            print('You chose to go with the safer strategy, stopping for a new wing took a lot of time, you drop two positions.')

            time.sleep(4)

            print('You drive a good and safe race to a reasonable finishing position of '+ str(raceposition)+ '!')
      
      else:
        if klaplap == '35':
          print('You decide not to pit for a new front wing, did you make the right call?.')
          raceposition = position -1

          time.sleep(3)

          print('You keep driving and the front wing turns out to be fine. Good thing you did not pit!. You even gain a spot and finish P'+str(raceposition)+'!')

        else:
          print('You try to stay out. Did you make the right call? I guess we will find out soon enough.')

          time.sleep(3)

          print('You go a bit wide and take the curb, your front wing breaks off and you fly into the wall at full speed.')

          time.sleep(4)

          raceposition = 'DNF'

          print('You are lucky to survive the crash, but you can not finish the race.')
          
    elif tyre == 'mediums':
      print('You start on the mediums and you immediately make up a place in the first corner!')
      raceposition = int(raceposition) - 1

      time.sleep(4)

      pit = input('It is lap 38/60, you have a touch with the driver in front of you, your wing suffers some damage... You can decide to keep racing, or to pit.\nThe pitting strategy would be slower, but staying out could lead to a crash. \nDo you pit? ' )
      
      time.sleep(5)

      if pit.lower() == 'yes':
        if klaplap == '58':
          print('You chose to go with the safer strategy, it costs you a lot of time, did you make the right call getting a new wing?')

          time.sleep(4)

          print('You immediately feel the new wing is firmer. You make up the places you lost and even gain one spot! \nYour team finds out that the other wing was badly damaged.')

          raceposition = int(raceposition) - 1

        else:
          print('You chose to go with the safer strategy, it costs you a lot of time, did you make the right call getting a new wing?')

          time.sleep(4)
          
          print('You drive a good and safe race to a reasonable finishing position of '+ str(raceposition)+ '! Turns out the wing was not damaged, you left a lot on the table this race.')
      
      else:
        if klaplap == '35':
          print('You decide to stay out. Its a risky call, what will be the result?')

          time.sleep(3)

          print('You do great with the wing that turns out to have minor damage. You even gain a spot!')
          
          raceposition = int(raceposition) - 1

          time.sleep(3)

        else:
          print('You decide to stay out against the advice of your team. Were you greedy, or did you make the right call?')

          time.sleep(3)

          print('You are flipping through the gears, but right as you hit top speed, the wing breaks of and you swerve into the barrier!')

          time.sleep(5)

          raceposition =  'DNF'

          print('The marshalls drag you out of your burning car. They fly you into the nearest hispital. Two days later you gain conscious. \nAmazingly, you are back on the track for the next race with a few bruises and scratches. ')

          time.sleep(5)

    else:
      print('You start on the hards and you immediately make up a place in the first corner!')
      raceposition = int(raceposition) - 1

      time.sleep(4)

      pit = input('It is lap 40/60, you have a touch with the driver in front of you, your wing suffers some damage... You can decide to keep racing, or to pit.\nThe pitting strategy would be slower, but staying out could lead to a crash. \nDo you pit? ' )
      
      time.sleep(5)

      if pit.lower() == 'yes':
        if klaplap == '58':
          print('You chose to go with the safer strategy, it costs you a lot of time, did you make the right call getting a new wing?')

          time.sleep(4)
          raceposition = int(raceposition) - 1

          print('Good thing you went in! Turns out your wing has got big damage. You can even make up a few spots with your speedy driving!')

          time.sleep(4)

        if klaplap == '35':
          print('You chose to go with the safer strategy, it costs you a lot of time, did you make the right call getting a new wing?')

          time.sleep(4)
        
          print('Too bad you went in! Turns out your wing has got no big damage.')
          
          time.sleep(3)

          print('You drive a good and safe race to a reasonable finishing position of '+ str(raceposition)+ '!')
      
      else:
        if klaplap == '35':
          print('You decide to stay out, did you make the right call?')

          time.sleep(3)

          print('Are you doubting yourself yet?')

          time.sleep(3)

          print('Turns out there was no damage to your wing! Good thing you did not go in. ')
          
          raceposition = 18

        else:
          print('You try to stay out until lap 38, but you start to slide around more and more.')

          time.sleep(3)

          print('You manage to keep the car on track and keep the tyres in good condition! You go into the pits for new softs.')

          time.sleep(4)

          raceposition = int(raceposition) - 4

          print('You made the strategy work perfectly! You made up 4 positions with your great driving! You end up in P' +str(raceposition)+'!')
  
  elif position < 5:
    print('You start on your used softs, you keep your position though!') 

    raceposition = int(raceposition)
    time.sleep(3)

    print('It is lap 38/60, you have a touch with the driver in front of you, your wing suffers some damage... You can decide to keep racing, or to pit.\nThe pitting strategy would be slower, but staying out could lead to a crash.')
    
    time.sleep(3)

    pit = input('Do you pit? ' )

    if pit == 'yes':
      if klaplap == '58':
        print('You decide to play safe and think about the bigger picture. You lose quite some time there, did you make the right call?')

        time.sleep(4)
        
        print('Turns out the wing was badly damaged, good thing you switched it out. Unfortunately you did lose positions, can you get them back?')
        
        raceposition = int(raceposition) + 1
        time.sleep(3)

        print('You try your best and regain some positions, but end on P' +str(raceposition)+'!')

        time.sleep(2)
      
      else:
        print('You decide to play safe and think about the bigger picture.')

        raceposition = int(raceposition) + 1
        time.sleep(3)

        print('You drive to the finish line safely but you lost a lot of time and the wing turned out to be fine. Since they told you to fight like a lion you regain most lost positions, but end up in P' +str(raceposition)+'!')
        

    else:
      if klaplap == '35':
        print('You decide to gamble and you try to make it to the end with your risky front wing.')
        
        raceposition = int(raceposition) -1
        time.sleep(4)

        print('Turns out it was a false alarm, nothing was wrong with your front wing. Because you did not go in you finish in P'+str(raceposition)+'!!')
        
      else:
        print('You decide to gamble, big time. Your manager gets mad already but you convince him to trust you.')
        
        time.sleep(3)

        print('With a lot of slipping and sliding due to loss of downforce, you keep going.')
        
        time.sleep(5)

        print('You gambled, and lost everything. The wing was a disaster. You lose the rear end in the final corner.')

        time.sleep(4)

        print('You get out just fine, but you do not finish the race.')
        raceposition = 'DNF'
          
        time.sleep(3)
        
  else:
    print('You start on your used softs and you lose a place on the first lap!')
    
    raceposition = int(raceposition) + 1
    time.sleep(3)
    
    print('It is lap 38/60, you have a touch with the driver in front of you, your wing suffers some damage... You can decide to keep racing, or to pit.\nThe pitting strategy would be slower, but staying out could lead to a crash.')
    
    time.sleep(5)

    pit = input('Do you pit? ' )

    if pit == 'yes':
      if klaplap == '58':
        print('You decide to play safe and think about the bigger picture.')

        time.sleep(3)
        
        print('You made the right call getting that floppy front wing off. It does cost you a lot of time though...')
        
        time.sleep(3)
        raceposition = int(raceposition) + 3

        print('You end up in P'+str(raceposition)+'.')
        time.sleep(2)
        
      else:
        print('You decide to play safe and think about the bigger picture.')

        raceposition = int(raceposition) + 4
        time.sleep(3)

        print('You drive to the finish line safely, but it cost you a lot of unnecessary time. You lose a few positions and end up in P'+str(raceposition)+'.')

    else:
      if klaplap == '35':
        print('You decide to gamble and you try to make it till the end with the wing that took a hit, too risky?.')
        
        time.sleep(3)
        
        print('The gamble pays off, the wing was not damaged and you save time not stopping to change it.')

        time.sleep(2)

        raceposition = int(raceposition)

        print('You manage to finish in P'+str(raceposition)+'.')
        
      else:
        print('You decide to gamble and you try to make it till the finish, did you make the right call?')
        
        time.sleep(3)

        print('You go through the fastest corner, but on exit you lose the rear and hit the wall.')
        
        time.sleep(5)
        
        print('You survive, but your car does not. This race is a DNF...')

        raceposition = 'DNF'
    
  return raceposition



def bottasbowlen(raceposition, team, tyre, currentrace):
  print("It's raceday at the Grand Prix of " + currentrace +"! It has rained a bit before the start, but it looks like everyone is starting on the dry tyres!")
  startpos = raceposition
  
  if team.capitalize() == 'Mercedes' or startpos > 7:
    if team.capitalize() == 'Mercedes':
        print('You have a great start and you manage to stay clear of your teammate Bottas as he misjudges his breaking point and plows into the car in front of him, who hits the car in front of them! \nIn total 6 cars get wiped out and you get away in P1!')

        time.sleep(3)

        thank = input('Your closest competition is an Alpine, so you easily drive away. You drive all the way to the end, finishing in P1. Do you thank Bottas on the radio for his help getting this win? ' )

        if thank == 'yes':
          print('People start to suspect there was foul play, and the FIA has to respond by taking your win away. You end up disqualified.') 
          raceposition = 'DNF'

        else:
          print('You leave your teammates actions alone and you celebrate your easy victory.')
          raceposition = 1
        
        
    else: 
      print('You had a good start on the '+str(tyre)+' and you make a successful pass') 

      time.sleep(3)
      
      raceposition -= 7

      print('Coming up to the first corner you see Bottas braking way to late and flying into the cars infront of him! He takes out 5 other drivers in a massive pileup! You are now in P' + str(raceposition)+ '!')

      chance = random.random()

      if chance < 0.6:
        tyre = input('You had to avoid hitting a Red Bull, causing you to lose 5 positions again to drivers who manages to fly past the broken cars with ease. You are scared you drove over some debris and you change your tires to be safe. Do you change them to softs, mediums or hards? ' )

        raceposition += 5

        chance2 = random.random()

        if tyre == 'softs':
          print('You do the restart on softs and get away great! Beating 2 other drivers to the first corner!')
          
          time.sleep(3)
          
          raceposition -= 1

          print('You have to pit again for mediums, while the people who restarted on hards can drive to the end. Because of this you lose a position again. You end this crazy race P'+str(raceposition))

        elif tyre == 'mediums':
          print('You do the restart on mediums and get away great! Beating 1 other driver to the first corner!')
          
          time.sleep(3)
          
          raceposition += 1

          print('You have to pit again for new mediums, while the people who restarted on hards can drive to the end. Because of this you lose two positions. You end this crazy race P'+str(raceposition))

        else:
          print('You start the race on hards, losing a position before the first corner.')

          time.sleep(3)

          raceposition -=3
          
          print('You drive very carefully and you manage to stay on the hards until the end without pitting! your genius pitstrategy has won you 4 positions! You end up in P'+str(raceposition))
          
      elif chance < 0.8:
        tyre = input('While driving through all the debris you get a puncture, you end up getting overtaken by everyone but you can change your tires during the red flag. What do you want to change your tires to? Softs, Mediums or Hards? ' )

        raceposition = 14

        if tyre == 'softs':
          print('You do the restart on softs and get away great! Beating 3 other drivers to the first corner!')
          
          time.sleep(3)
          
          raceposition -= 2

          print('You have to pit again for mediums, while the people who restarted on hards can drive to the end. Because of this you lose a position again. You end this crazy race P'+str(raceposition))

        elif tyre == 'mediums':
          print('You do the restart on mediums and get away great! Beating 3 other drivers to the first corner!')
          
          time.sleep(3)
          
          raceposition -= 1

          print('You have to pit again for new mediums, while the people who restarted on hards can drive to the end. Because of this you lose two positions. You end this crazy race P'+str(raceposition))

        else:
          print('You start the race on hards, but you win a position before the first corner.')

          time.sleep(3)

          raceposition -=6
          
          print('You drive very carefully and you manage to stay on the hards until the end without pitting! your genius pitstrategy has won you 5 positions! You end up in P'+str(raceposition))



      else:
        print('You manage to get past the broken cars with ease and you manage to keep your P' +str(raceposition))

        time.sleep(2)

        tyre = input('A red flag is called and you can change your tyres for free, what tyres do you go on for the restart? ' )
        
        if tyre == 'softs':
          print('You do the restart on softs and get away great! You keep position!')
          
          time.sleep(3)
          
          raceposition += 2

          print('You have to pit again for mediums, while the people who restarted on hards can drive to the end. Because of this you lose two positions. You end this crazy race P'+str(raceposition))

        elif tyre == 'mediums':
          print('You do the restart on mediums and get away great! You keep position!')
          
          time.sleep(3)
          
          raceposition += 2

          print('You have to pit again for new mediums, while the people who restarted on hards can drive to the end. Because of this you lose two positions. You end this crazy race P'+str(raceposition))

        else:
          if raceposition == 1:
            print('You start the race on hards, losing a position before the first corner.')

            time.sleep(3)
          
            print('You drive very carefully and you manage to stay on the hards until the end without pitting! your genius pitstrategy has won you the position back! You end up in P'+str(raceposition)+ ' and you win the race!')

          else:
            print('You start the race on hards, losing a position before the first corner.')

            time.sleep(3)

            raceposition -=1
          
            print('You drive very carefully and you manage to stay on the hards until the end without pitting! your genius pitstrategy has won you 2 positions! You end up in P'+str(raceposition))
      

  else:
    print('You start well at the start, flying past Bottas, who misjudges his breaking point in the damp conditions and hits the car in front of him. That car hits another and like dominos the whole top 6 cars, except the other mercedes interestingly, is wiped out of the Grand Prix. You DNF.')

    raceposition = 'DNF'

  return raceposition



def normalrace(raceposition, tyre):
  position = raceposition
  
  if tyre == 'softs':
    print('')
  


def hitwalldeath():
  chance = random.random()
  if chance < 0.5:
    print("You hit another racer while trying to warm your tires. You and him hit the wall and die on impact. 3 marshalls end up in the hospital as well. 1 of them dies of injuries later. Their family is pushed into poverty because of the loss of their already little income")
    sys.exit()
  else:
    print("You hit the wall at such speed that your car catches fire and you can't get out in time. Leaving you to burn to death.")
    sys.exit()



def covid(team):
  chance = random.random()
  if chance < 0.5:
    print("You went to a huge party despite of the advice of your boss at "+str(team).capitalize+". Now you test positive for covid and miss a race, how sad.")
    
  else:
    print('You did not go to any party but you still test positive for covid. The only person you have been with is your team mate, he also tests positive. You both miss a race')
   
  finishposition = 'DNS'
  return finishposition
    


def mechfailure(team):
  chance = random.random()
  if chance < 0.33:
    print('You start the race!')
    time.sleep(3)

    print("You push way to hard in the first 17 laps, and the engine overheats. You need to retire the car after what seemed to be a good race.")
    time.sleep(3)
    
  elif chance < 0.66:
    print('You start the race smoothly')
    time.sleep(3)

    print('Unfortunately, the brakes overheat in lap 42 and the car becomes impossible to handle, you need to retire the car for your own safety.')

  else:
    print('You start the race!')
    time.sleep(3)
    
    print('You are doing great! You push the car and keep your position. \nBut wait, what is that heat?')
    
    time.sleep(5)

    print('Did you push the car too hard the final laps? With only five more corners to go, the engine starts to overheat.')
    
    time.sleep(3)

    print('Your engine catches fire, you need to retire the car with the finishline in sight. A lot was left on the table, and on the track.')
   
  finishposition = 'DNF'
  return finishposition
    


def pointcalc(results):
  points = 0
  for i in results:
    if results[i] == 'DNF' or results[i] == 'DNS' or results[i] == 'DSQ':
      points += 0
    else:
      pos = int(results[i])
      if pos == 1:
        points += 25
      if pos == 2:
        points += 18
      if pos == 3:
        points += 15
      if pos == 4:
        points += 12
      if pos == 5:
        points += 10
      if pos == 6:
        points += 8
      if pos == 7:
        points += 6  
      if pos == 8:
        points += 4
      if pos == 9:
        points += 2
      if pos == 10:
        points += 1

  return points





def standings(team, points):
  chance = random.random()
  if team == 'mercedes':
    driver = 'Hamilton'

  if team == 'mclaren':
    if chance > 0.5:
      driver = 'Ricciardo'
    else:
      driver = 'Norris'

  if team == 'ferrari':
    if chance > 0.5:
      driver = 'Sainz'
    else: 
      driver = 'Leclerc'
      
  if team == 'red bull':
    if chance > 0.5: 
      driver = 'Verstappen'
    else:
      driver = 'Perez'

  if team == 'alpine':
    if chance > 0.5:
      driver = 'Alonso'
    else:
      driver = 'Ocon'

  if team == 'alpha tauri':
    if chance > 0.5:
      driver = 'Gasly'
    else:
      driver = 'Tsunoda'

  if team == 'aston martin':
   if chance > 0.5:
     driver = 'Stroll'
   else:
     driver = 'Vettel'

  if team == 'alfa romeo':
    if chance > 0.5:
      driver = 'Giovinazzi'
    else:
      driver = 'Raikkonen'

  if team == 'haas':
    if chance > 0.5:
      driver = 'Mazepin'
    else:
      driver = 'Schumacher'
  
  if team == 'williams':
    if chance > 0.5:
      driver = 'Russell'
    else:
      driver = 'Latifi'
    
  
  drivers[player] = points
  
  del drivers[driver]
  
  sorted_drivers = sorted(drivers.items(), key=lambda x: x[1], reverse=True)
  
  return sorted_drivers



def f2races():
  points = f2race1(0)
  
  race2 = f2race2(points)

  points = race2[0]
  tifosi = race2[1]

  points = f2race3(points)

  return points, tifosi



def f2race2(points):
  tifosi = 0
  print("Now the next race in Italy! At the famous Autodromo Nazionale di Monza! A track known for having a lot of straights, and highspeed corners.")

  question1 = input("The Formula 1 race at Monza always brings out the 'Tifosi', the name of the vivid fans of what team? " )

  if question1.capitalize() == "Ferrari":
    print("Exactly right!")
    points += 1
  else:
    print("No! The Tifosi are the hardcore Ferrari fans! A must know for any driver that ever wants to join the Italian team.")
    tifosi = 1

  question2 = input("Knowing that Monza has straights and highspeed corners, do you make the set up the car with high downforce and high drag (1), or low downforce and low drag (2)? " )

  if question2 == "2":
    print("Smart choice! The drag of a high downforce car would slow you down massively on the straights!")
    points += 1
  else:
    print("No! The high drag would make your car way slower on the straights than the other cars!")
  return points, tifosi



def f2race1(points):
  print("Welcome, rookie, to the F2 season! This season, your skill and knowledge is going to be tested to see if you are a fitting candidate to earn a seat in F1.")
  time.sleep(3)
  print("The season starts in Singapore, a nightrace with a lot of tyre degradation, so the tyres will fall off very quickly.")
  time.sleep(3)
  question1 = input("Knowing there will be high tyre degradation, do you opt for the soft to medium strategy (1) or the medium to hard strategy (2)? " )

  if question1 == "1":
    print("That would not be very smart! The softs and the mediums will degrade much faster than the hards, and you wont have any tyres left at the end of the race!")
  if question1 == "2":
    print("Great choice! The mediums and the hards will degrade slower than the softs to mediums, leaving you with more tyre throughout the race!")
    points += 1
  time.sleep(3)

  question2 = input("Seeing Singapore is a nightrace it is bound to be dark. Do you pick a clear vizer (1) or do you pick a tinted vizer (2)? " )
  time.sleep(3)
  if question2 == "1":
    print("Good call, the clear vizer is going to provide a better view driving through the night than the tinted vizer!")
    points += 1
  if question2 == "2":
    print("Wrong call! The tinted vizer is going to take away a lot of the visibility when on track at night, this will result in dangerous situations! ")

  return points



def f2race3(points):
  print("Time for the third race of your F2 career! You are in Belgium for the race at Spa! Spa is a circuit with a rich history and arguably the most famous circuit on earth.")
  time.sleep(3)
  print("Drivers like to test their luck at Spa, and push to the limits. It is not uncommon to have a few cars spin during the races.")
  time.sleep(3)
  question1 = input("Say, if you were to spin your car and there is no clear damage to the car, would you keep on driving (1) or would you retire the car (2)? " )

  if question1 == "1":
    print("Good decision, there is no need to retire your car just because of a spin. In said scenario losing poinst is more costly than the risk to keep going.")
    points += 1
  if question1 == "2":
    print("Really? There is no reason to retire the car just for spinning! Think about all those points you could be losing if you don't keep driving!")
  time.sleep(3)

  question2 = input("As stated earlier, Spa has a rich history. Who do you think won most Grand Prixs in Spa, Michael Schumacher (1) or  Lewis Hamilton (2)? " )
  time.sleep(3)
  if question2 == "1":
    print("Correct, Schumacher won no less than 6 GPs in Spa alone!")
    points += 1
  if question2 == "2":
    print("Wrong! Lewis has 'only' 4 wins in Spa, while Schumacher has no less than 6!")

  return points



def begin():
  points, tifosi = f2races()
  
  #points = 6 #use this to skip F2
  if points == 0 or points == 1:
    print('You were last in F2, no team wants you to drive for them. Try again!')
  elif points == 2 or points == 3:
    print('You were 5th in your rookie season in F2! That is pretty good, and there are a couple of teams who are interested in you! You can only pick three teams to negotiate with, choose wisely!')
    team1 = input('Team 1: ' )
    team2 = input('Team 2: ' )
    team3 = input('Team 3: ' )
    listteams = [team1, team2, team3]

    dictteams = {}
    for i in range(len(listteams)):
      if listteams[i].capitalize() == "Williams":
        dictteams[listteams[i]] = 0.40
      elif listteams[i].capitalize() == "Haas":
        dictteams[listteams[i]] = 0.30
      elif listteams[i].capitalize() == "Alfa romeo":
        dictteams[listteams[i]] = 0.25
      elif listteams[i].capitalize() == "Alpha tauri":
        dictteams[listteams[i]] = 0.25
      elif listteams[i].capitalize() == "Ferrari":
        dictteams[listteams[i]] = 0
      elif listteams[i].capitalize() == "Alpine":
        dictteams[listteams[i]] = 0.1
      elif listteams[i].capitalize() == "Mercedes":
        dictteams[listteams[i]] = 0
      elif listteams[i].capitalize() == "Aston martin":
        dictteams[listteams[i]] = 0.1
      elif listteams[i].capitalize() == "Red bull":
        dictteams[listteams[i]] = 0
      elif listteams[i].capitalize() == "Mclaren":
        dictteams[listteams[i]] = 0.1
    
      for i in dictteams:
        chance = dictteams[i]
        rand = random.random()
        if chance > rand:
          time.sleep(3)
          print(i.capitalize() + " accepts you on their team!")
          if i.capitalize() ==  "Williams":
            williams()
            sys.exit()
          if i.capitalize() == "Haas":
            haas()
            sys.exit()
          if i.capitalize() == "Alfa romeo":
            alfaromeo()
            sys.exit()
          if i.capitalize() == "Alpha tauri":
            alphatauri()
            sys.exit()
          if i.capitalize() == "Ferrari":
            ferrari()
            sys.exit()
          if i.capitalize() == "Red bull":
            redbull()
            sys.exit()
          if i.capitalize() == "Mercedes":
            mercedes()
            sys.exit()
          if i.capitalize() == "Aston martin":
            astonmartin()
            sys.exit()
          if i.capitalize() == "Alpine":
            alpine()
            sys.exit()
          if i.capitalize() == "Mclaren":
            mclaren()
            sys.exit()

        else:
            time.sleep(3)
            print(i.capitalize() + " does not want you on their team.")

  elif points == 4 or points == 5:
    print('You were 2nd in your rookie season in F2! That is very good, and there are a couple of teams who are interested in you! You can only pick three teams to negotiate with, choose wisely!')
    team1 = input('Team 1: ' )
    team2 = input('Team 2: ' )
    team3 = input('Team 3: ' )
    listteams = [team1, team2, team3]

    dictteams = {}
    for i in range(len(listteams)):
      if listteams[i].capitalize() == "Williams":
        dictteams[listteams[i]] = 0.60
      elif listteams[i].capitalize() == "Haas":
        dictteams[listteams[i]] = 0.40
      elif listteams[i].capitalize() == "Alfa romeo":
        dictteams[listteams[i]] = 0.35
      elif listteams[i].capitalize() == "Alpha tauri":
        dictteams[listteams[i]] = 0.35
      elif listteams[i].capitalize() == "Ferrari":
        dictteams[listteams[i]] = 0.05
      elif listteams[i].capitalize() == "Alpine":
        dictteams[listteams[i]] = 0.15
      elif listteams[i].capitalize() == "Mercedes":
        dictteams[listteams[i]] = 0.05
      elif listteams[i].capitalize() == "Aston martin":
        dictteams[listteams[i]] = 0.2
      elif listteams[i].capitalize() == "Red bull":
        dictteams[listteams[i]] = 0.1
      elif listteams[i].capitalize() == "Mclaren":
        dictteams[listteams[i]] = 0.2
    for i in dictteams:
        chance = dictteams[i]
        rand = random.random()
        if chance > rand:
          time.sleep(3)
          print(i.capitalize() + " accepts you on their team!")
          if i.capitalize() ==  "Williams":
            williams()
            sys.exit()
          if i.capitalize() == "Haas":
            haas()
            sys.exit()
          if i.capitalize() == "Alfa romeo":
            alfaromeo()
            sys.exit()
          if i.capitalize() == "Alpha tauri":
            alphatauri()
            sys.exit()
          if i.capitalize() == "Ferrari":
            ferrari()
            sys.exit()
          if i.capitalize() == "Red bull":
            redbull()
            sys.exit()
          if i.capitalize() == "Mercedes":
            mercedes()
            sys.exit()
          if i.capitalize() == "Aston martin":
            astonmartin()
            sys.exit()
          if i.capitalize() == "Alpine":
            alpine()
            sys.exit()
          if i.capitalize() == "Mclaren":
            mclaren()
            sys.exit()

        else:
          time.sleep(3)
          print(i.capitalize() + " does not want you on their team.")

  else:  
      team1 = input("Congratulations!! You became the F2 Champion in your rookie season, amazing! All F1 teams are considering to give you a seat for coming season. You can only pick three teams to negotiate with, choose wisely!\nTeam 1: " )
      team2 = input('Team 2: ' )
      team3 = input('Team 3: ' )

      listteams = [team1, team2, team3]

      dictteams = {}
      for i in range(len(listteams)):
        if listteams[i].capitalize() == "Williams":
          dictteams[listteams[i]] = 0.80
        elif listteams[i].capitalize() == "Haas":
          dictteams[listteams[i]] = 0.70
        elif listteams[i].capitalize() == "Alfa romeo":
          dictteams[listteams[i]] = 0.65
        elif listteams[i].capitalize() == "Alpha tauri":
          dictteams[listteams[i]] = 0.70
        elif listteams[i].capitalize() == "Ferrari":
          dictteams[listteams[i]] = 0.15
        elif listteams[i].capitalize() == "Alpine":
          dictteams[listteams[i]] = 0.35
        elif listteams[i].capitalize() == "Mercedes":
          dictteams[listteams[i]] = 0.10
        elif listteams[i].capitalize() == "Aston martin":
          dictteams[listteams[i]] = 0.35
        elif listteams[i].capitalize() == "Red bull":
          dictteams[listteams[i]] = 0.20
        elif listteams[i].capitalize() == "Mclaren":
          dictteams[listteams[i]] = 0.38
      for i in dictteams:
          chance = dictteams[i]
          rand = random.random()
          if chance > rand:
            time.sleep(3)
            print(i.capitalize() + " accepts you on their team!")
            if i.capitalize() ==  "Williams":
              williams()
              sys.exit()
            if i.capitalize() == "Haas":
              haas()
              sys.exit()
            if i.capitalize() == "Alfa romeo":
              alfaromeo()
              sys.exit()
            if i.capitalize() == "Alpha tauri":
              alphatauri()
              sys.exit()
            if i.capitalize() == "Ferrari":
              ferrari()
              sys.exit()
            if i.capitalize() == "Red bull":
              redbull()
              sys.exit()
            if i.capitalize() == "Mercedes":
              mercedes()
              sys.exit()
            if i.capitalize() == "Aston martin":
              astonmartin()
              sys.exit()
            if i.capitalize() == "Alpine":
              alpine()
              sys.exit()
            if i.capitalize() == "Mclaren":
              mclaren()
              sys.exit()

          else:
            time.sleep(3)
            print(i.capitalize() + " does not want you on their team.")
  
  print("You did not get a seat for this season. Back to F2. ")
  sys.exit

begin()