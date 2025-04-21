         $ InterestFlag = True
         $ SkillSolutions = True
         $ ShipExplore = True
         $ FirstEvent = True
         $ SkillTutorial = True
         $ Meta = False
   $ quick_menu = True
   $ MetZ = True
   if Meta:
         jump spacerintro
         jump colonistintro
         jump coreintro
   $ spacer = True
   $ RaelShip += 1
   $ RaelTech += 1
   $ RaelSoc += -1
   jump prologue2
   $ colonist = True
   $ RaelPhys += 1
   $ RaelSoc += 1
   $ RaelShip += -1
   jump prologue2
   $ core = True
   $ RaelMind += 1
   $ RaelSoc += 1
   $ RaelPhys += -1
   jump prologue2
      jump punkintro
      jump dreamerintro
      jump techintro
   $ punk = True
   $ RaelPhys += 1
   $ RaelWep += 1
   $ RaelMind += -1
   jump prologue3
   $ dreamer = True
   $ RaelSoc += 1
   $ RaelMind += 1
   $ RaelWep += -1
   jump prologue3
   $ tech = True
   $ RaelTech += 1
   $ RaelMind += 1
   $ RaelPhys += -1
   jump prologue3
      jump pirateintro
      jump adminintro
      jump innovatorintro
   $ pirate = True
   $ RaelWep += 1
   $ RaelPhys += 1
   $ RaelShip += 1
   if core:
   jump prologue4
   $ admin = True
   $ RaelPhys += 1
   $ RaelMind += 1
   $ RaelSoc += 1
   jump prologue4
   $ innovator = True
   $ RaelMind += 1
   $ RaelTech += 1
   $ RaelShip += 1
   jump prologue4
      if spacer:
         $ RaelShip += -1
         $ RaelTech += -1
         $ RaelSoc += 1
         $ spacer = False
      if colonist:
         $ RaelPhys += -1
         $ RaelSoc += -1
         $ RaelShip += 1
         $ colonist = False
      if core:
         $ RaelMind += -1
         $ RaelSoc += -1
         $ RaelPhys += 1
         $ core = False
      if punk:
         $ RaelPhys += -1
         $ RaelWep += -1
         $ RaelMind += 1
         $ punk = False
      if dreamer:
         $ RaelSoc += -1
         $ RaelMind += -1
         $ RaelWep += 1
         $ dreamer = False
      if tech:
         $ RaelTech += -1
         $ RaelMind += -1
         $ RaelPhys += 1
         $ tech = False
      if pirate:
         $ RaelWep += -1
         $ RaelPhys += -1
         $ RaelShip += -1
         $ pirate = False
      if admin:
         $ RaelPhys += -1
         $ RaelMind += -1
         $ RaelSoc += -1
         $ admin = False
      if innovator:
         $ RaelMind += -1
         $ RaelTech += -1
         $ RaelShip += -1
         $ innovator = False
      jump originstart
      $ OriginSet = True
      jump originset
   $ MetS = True
   if spacer:
      $ SamApproval += 5
   else:
   if spacer:
      $ ZuberiApproval += 5 
   if (dreamer) and (spacer == False):
      $ ZuberiApproval += 3
   if core:
   if tech:
      $ ObaaApproval += 5
   else:
   if spacer:
   else:
   if Meta:
         $ ZuberiInterest += 2
         $ CaleiaInterest += 2
         $ BrommInterest += 2
         $ MizzInterest += 2
         $ TulemeniInterest += 2
         $ SamInterest += 2
         $ AnwillInterest += 2
         $ InterestFlag = True
         $ RaelAce = True
   if (punk) and (Meta):
         jump nonplussed
         jump watcher
         jump flaunt
         jump punkcasual
   if RaelAce:
   else:
   jump prologue5
   jump prologue5
   jump prologue5
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   jump prologue5
   $ MetB = True
   $ MetC = True
   if dreamer:
   if core:
   else:
   if (tech) and (Meta):
      jump grrcaleia
      jump silent
      jump geekout
   $ BrommApproval += 3
   $ CaleiaApproval += -5
   jump prologue6
   if pirate:
      jump prologue6
   else:
      jump prologue6
   $ CaleiaSurname = True
   if pirate:
   if admin:
   if innovator:
   if innovator:
   else: 
   if BrommApproval > 25:
   else:
   if spacer:
   if pirate:
   if admin:
   if innovator:
   if dreamer:
      jump takefirst
      jump takesecond
   $ TakeFirst=True
   jump prologue7
   if TakeFirst:
      jump prologue8
   else:
      jump prologue8
         jump homesweethome
   if core:
   else:
   $ MetT = True 
   if tech:
   else:
   if tech:
   else:
   if spacer:
   if colonist:
   if core:
   if spacer:
   if tech and (spacer == False):
   if innovator and (tech == False) and (spacer == False):
   $ ObsSeen = True
   $ MetM = True
   if (dreamer) and (Meta):
      jump coldmizz
      jump greetmizz
      jump niceduds
   jump meetmizz
   jump meetmizz
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   $ MizzApproval += 3
   $ MizzLust += 5
   if core:
      $ MizzDad=True
   else:
      if dreamer:
      else:
   if spacer:
   if punk:
      $ MizzApproval += 3
   if dreamer:
      $ BrommApproval += 3
   if tech:
      if core:
   if spacer:
   if innovator:
   if innovator:
   else:
   if spacer:
   if tech:
   if TakeFirst:
   else:
      $ BrommApproval += 1
   if spacer:
   if spacer:
   if TakeFirst:
   else:
   $ WatchedLaunch += 1
   jump homesweethome2
   if spacer:
   if colonist:
   if core:
   if spacer:
   if colonist:
   if core:
         $ Commando=True
         $ Briefs=True
         $ BBs=True
         $ Boxers=True
   if spacer:
   if colonist:
   if core:
      if WatchedLaunch == 1:
      else:
   if punk:
   if dreamer:
   if tech:
   if pirate:
   if admin:
   if innovator:
      if WatchedLaunch == 1:
      else:
   if Commando:
   else:
   if WatchedLaunch == 1:
   else:
      if spacer:
   if TakeFirst:
   else:
   if TakeFirst:
   else:
      if innovator:
      else:
   jump Day1Startlabel prologue:
   menu:
         $ InterestFlag = True
         $ SkillSolutions = True
         $ ShipExplore = True
         $ FirstEvent = True
         $ SkillTutorial = True
         $ Meta = False
   $ quick_menu = True
   $ MetZ = True
   if Meta:
label originstart: # Player's first Origin choices.
   menu:
         jump spacerintro
         jump colonistintro
         jump coreintro
label spacerintro:
   $ spacer = True
   $ RaelShip += 1
   $ RaelTech += 1
   $ RaelSoc += -1
   jump prologue2
label colonistintro:
   $ colonist = True
   $ RaelPhys += 1
   $ RaelSoc += 1
   $ RaelShip += -1
   jump prologue2
label coreintro:
   $ core = True
   $ RaelMind += 1
   $ RaelSoc += 1
   $ RaelPhys += -1
   jump prologue2
label prologue2:
menu:
      jump punkintro
      jump dreamerintro
      jump techintro
label punkintro:
   $ punk = True
   $ RaelPhys += 1
   $ RaelWep += 1
   $ RaelMind += -1
   jump prologue3
label dreamerintro:
   $ dreamer = True
   $ RaelSoc += 1
   $ RaelMind += 1
   $ RaelWep += -1
   jump prologue3
label techintro:
   $ tech = True
   $ RaelTech += 1
   $ RaelMind += 1
   $ RaelPhys += -1
   jump prologue3
label prologue3:
menu:
      jump pirateintro
      jump adminintro
      jump innovatorintro
label pirateintro:
   $ pirate = True
   $ RaelWep += 1
   $ RaelPhys += 1
   $ RaelShip += 1
   if core:
   jump prologue4
label adminintro:
   $ admin = True
   $ RaelPhys += 1
   $ RaelMind += 1
   $ RaelSoc += 1
   jump prologue4
label innovatorintro:
   $ innovator = True
   $ RaelMind += 1
   $ RaelTech += 1
   $ RaelShip += 1
   jump prologue4
label prologue4:
menu:
      if spacer:
         $ RaelShip += -1
         $ RaelTech += -1
         $ RaelSoc += 1
         $ spacer = False
      if colonist:
         $ RaelPhys += -1
         $ RaelSoc += -1
         $ RaelShip += 1
         $ colonist = False
      if core:
         $ RaelMind += -1
         $ RaelSoc += -1
         $ RaelPhys += 1
         $ core = False
      if punk:
         $ RaelPhys += -1
         $ RaelWep += -1
         $ RaelMind += 1
         $ punk = False
      if dreamer:
         $ RaelSoc += -1
         $ RaelMind += -1
         $ RaelWep += 1
         $ dreamer = False
      if tech:
         $ RaelTech += -1
         $ RaelMind += -1
         $ RaelPhys += 1
         $ tech = False
      if pirate:
         $ RaelWep += -1
         $ RaelPhys += -1
         $ RaelShip += -1
         $ pirate = False
      if admin:
         $ RaelPhys += -1
         $ RaelMind += -1
         $ RaelSoc += -1
         $ admin = False
      if innovator:
         $ RaelMind += -1
         $ RaelTech += -1
         $ RaelShip += -1
         $ innovator = False
      jump originstart
      $ OriginSet = True
      jump originset
label originset:
   $ MetS = True
   if spacer:
      $ SamApproval += 5
   else:
   if spacer:
      $ ZuberiApproval += 5 
   if (dreamer) and (spacer == False):
      $ ZuberiApproval += 3
   if core:
   if tech:
      $ ObaaApproval += 5
   else:
   if spacer:
   else:
   if Meta:
   menu:
         $ ZuberiInterest += 2
         $ CaleiaInterest += 2
         $ BrommInterest += 2
         $ MizzInterest += 2
         $ TulemeniInterest += 2
         $ SamInterest += 2
         $ AnwillInterest += 2
         $ InterestFlag = True
         $ RaelAce = True
   if (punk) and (Meta):
   menu:
         jump nonplussed
         jump watcher
         jump flaunt
         jump punkcasual
label nonplussed:
   if RaelAce:
   else:
   jump prologue5
label watcher:
   jump prologue5
label flaunt:
   jump prologue5
label punkcasual:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   jump prologue5
label prologue5:
   $ MetB = True
   $ MetC = True
   if dreamer:
   if core:
   else:
   if (tech) and (Meta):
menu:
      jump grrcaleia
      jump silent
      jump geekout
label grrcaleia:
   $ BrommApproval += 3
   $ CaleiaApproval += -5
   jump prologue6
label silent:
   if pirate:
      jump prologue6
   else:
      jump prologue6
label geekout:
   $ CaleiaSurname = True
   if pirate:
   if admin:
   if innovator:
label prologue6:
   if innovator:
   else: 
   if BrommApproval > 25:
   else:
   if spacer:
   if pirate:
   if admin:
   if innovator:
   if dreamer:
menu:
      jump takefirst
      jump takesecond
label takefirst:
   $ TakeFirst=True
   jump prologue7
label takesecond:
label prologue7:
   if TakeFirst:
      jump prologue8
   else:
      jump prologue8
label prologue8:
   menu:
         jump homesweethome
label firstwarp:
   if core:
   else:
   $ MetT = True 
   if tech:
   else:
   if tech:
   else:
   if spacer:
   if colonist:
   if core:
   if spacer:
   if tech and (spacer == False):
   if innovator and (tech == False) and (spacer == False):
   $ ObsSeen = True
   $ MetM = True
   if (dreamer) and (Meta):
menu:
      jump coldmizz
      jump greetmizz
      jump niceduds
label coldmizz:
   jump meetmizz
label greetmizz:
   jump meetmizz
label niceduds:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   $ MizzApproval += 3
   $ MizzLust += 5
label meetmizz:
   if core:
      $ MizzDad=True
   else:
      if dreamer:
      else:
   if spacer:
   if punk:
      $ MizzApproval += 3
   if dreamer:
      $ BrommApproval += 3
   if tech:
      if core:
   if spacer:
   if innovator:
   if innovator:
   else:
   if spacer:
   if tech:
   if TakeFirst:
   else:
      $ BrommApproval += 1
   if spacer:
   if spacer:
   if TakeFirst:
   else:
   $ WatchedLaunch += 1
   jump homesweethome2
label homesweethome:
label homesweethome2:
   if spacer:
   if colonist:
   if core:
   if spacer:
   if colonist:
   if core:
   menu:
         $ Commando=True
         $ Briefs=True
         $ BBs=True
         $ Boxers=True
   if spacer:
   if colonist:
   if core:
      if WatchedLaunch == 1:
      else:
   if punk:
   if dreamer:
   if tech:
   if pirate:
   if admin:
   if innovator:
      if WatchedLaunch == 1:
      else:
   if Commando:
   else:
   if WatchedLaunch == 1:
   else:
      if spacer:
   if TakeFirst:
   else:
   if TakeFirst:
   else:
      if innovator:
      else:
   jump Day1Startlabel prologue:
   menu:
         $ InterestFlag = True
         $ SkillSolutions = True
         $ ShipExplore = True
         $ FirstEvent = True
         $ SkillTutorial = True
         $ Meta = False
   $ quick_menu = True
   $ MetZ = True
   if Meta:
label originstart: # Player's first Origin choices.
   menu:
         jump spacerintro
         jump colonistintro
         jump coreintro
label spacerintro:
   $ spacer = True
   $ RaelShip += 1
   $ RaelTech += 1
   $ RaelSoc += -1
   jump prologue2
label colonistintro:
   $ colonist = True
   $ RaelPhys += 1
   $ RaelSoc += 1
   $ RaelShip += -1
   jump prologue2
label coreintro:
   $ core = True
   $ RaelMind += 1
   $ RaelSoc += 1
   $ RaelPhys += -1
   jump prologue2
label prologue2:
menu:
      jump punkintro
      jump dreamerintro
      jump techintro
label punkintro:
   $ punk = True
   $ RaelPhys += 1
   $ RaelWep += 1
   $ RaelMind += -1
   jump prologue3
label dreamerintro:
   $ dreamer = True
   $ RaelSoc += 1
   $ RaelMind += 1
   $ RaelWep += -1
   jump prologue3
label techintro:
   $ tech = True
   $ RaelTech += 1
   $ RaelMind += 1
   $ RaelPhys += -1
   jump prologue3
label prologue3:
menu:
      jump pirateintro
      jump adminintro
      jump innovatorintro
label pirateintro:
   $ pirate = True
   $ RaelWep += 1
   $ RaelPhys += 1
   $ RaelShip += 1
   if core:
   jump prologue4
label adminintro:
   $ admin = True
   $ RaelPhys += 1
   $ RaelMind += 1
   $ RaelSoc += 1
   jump prologue4
label innovatorintro:
   $ innovator = True
   $ RaelMind += 1
   $ RaelTech += 1
   $ RaelShip += 1
   jump prologue4
label prologue4:
menu:
      if spacer:
         $ RaelShip += -1
         $ RaelTech += -1
         $ RaelSoc += 1
         $ spacer = False
      if colonist:
         $ RaelPhys += -1
         $ RaelSoc += -1
         $ RaelShip += 1
         $ colonist = False
      if core:
         $ RaelMind += -1
         $ RaelSoc += -1
         $ RaelPhys += 1
         $ core = False
      if punk:
         $ RaelPhys += -1
         $ RaelWep += -1
         $ RaelMind += 1
         $ punk = False
      if dreamer:
         $ RaelSoc += -1
         $ RaelMind += -1
         $ RaelWep += 1
         $ dreamer = False
      if tech:
         $ RaelTech += -1
         $ RaelMind += -1
         $ RaelPhys += 1
         $ tech = False
      if pirate:
         $ RaelWep += -1
         $ RaelPhys += -1
         $ RaelShip += -1
         $ pirate = False
      if admin:
         $ RaelPhys += -1
         $ RaelMind += -1
         $ RaelSoc += -1
         $ admin = False
      if innovator:
         $ RaelMind += -1
         $ RaelTech += -1
         $ RaelShip += -1
         $ innovator = False
      jump originstart
      $ OriginSet = True
      jump originset
label originset:
   $ MetS = True
   if spacer:
      $ SamApproval += 5
   else:
   if spacer:
      $ ZuberiApproval += 5 
   if (dreamer) and (spacer == False):
      $ ZuberiApproval += 3
   if core:
   if tech:
      $ ObaaApproval += 5
   else:
   if spacer:
   else:
   if Meta:
   menu:
         $ ZuberiInterest += 2
         $ CaleiaInterest += 2
         $ BrommInterest += 2
         $ MizzInterest += 2
         $ TulemeniInterest += 2
         $ SamInterest += 2
         $ AnwillInterest += 2
         $ InterestFlag = True
         $ RaelAce = True
   if (punk) and (Meta):
   menu:
         jump nonplussed
         jump watcher
         jump flaunt
         jump punkcasual
label nonplussed:
   if RaelAce:
   else:
   jump prologue5
label watcher:
   jump prologue5
label flaunt:
   jump prologue5
label punkcasual:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   jump prologue5
label prologue5:
   $ MetB = True
   $ MetC = True
   if dreamer:
   if core:
   else:
   if (tech) and (Meta):
menu:
      jump grrcaleia
      jump silent
      jump geekout
label grrcaleia:
   $ BrommApproval += 3
   $ CaleiaApproval += -5
   jump prologue6
label silent:
   if pirate:
      jump prologue6
   else:
      jump prologue6
label geekout:
   $ CaleiaSurname = True
   if pirate:
   if admin:
   if innovator:
label prologue6:
   if innovator:
   else: 
   if BrommApproval > 25:
   else:
   if spacer:
   if pirate:
   if admin:
   if innovator:
   if dreamer:
menu:
      jump takefirst
      jump takesecond
label takefirst:
   $ TakeFirst=True
   jump prologue7
label takesecond:
label prologue7:
   if TakeFirst:
      jump prologue8
   else:
      jump prologue8
label prologue8:
   menu:
         jump homesweethome
label firstwarp:
   if core:
   else:
   $ MetT = True 
   if tech:
   else:
   if tech:
   else:
   if spacer:
   if colonist:
   if core:
   if spacer:
   if tech and (spacer == False):
   if innovator and (tech == False) and (spacer == False):
   $ ObsSeen = True
   $ MetM = True
   if (dreamer) and (Meta):
menu:
      jump coldmizz
      jump greetmizz
      jump niceduds
label coldmizz:
   jump meetmizz
label greetmizz:
   jump meetmizz
label niceduds:
   if RaelAce:
   else:
   if RaelAce:
   else:
   if RaelAce:
   else:
   $ MizzApproval += 3
   $ MizzLust += 5
label meetmizz:
   if core:
      $ MizzDad=True
   else:
      if dreamer:
      else:
   if spacer:
   if punk:
      $ MizzApproval += 3
   if dreamer:
      $ BrommApproval += 3
   if tech:
      if core:
   if spacer:
   if innovator:
   if innovator:
   else:
   if spacer:
   if tech:
   if TakeFirst:
   else:
      $ BrommApproval += 1
   if spacer:
   if spacer:
   if TakeFirst:
   else:
   $ WatchedLaunch += 1
   jump homesweethome2
label homesweethome:
label homesweethome2:
   if spacer:
   if colonist:
   if core:
   if spacer:
   if colonist:
   if core:
   menu:
         $ Commando=True
         $ Briefs=True
         $ BBs=True
         $ Boxers=True
   if spacer:
   if colonist:
   if core:
      if WatchedLaunch == 1:
      else:
   if punk:
   if dreamer:
   if tech:
   if pirate:
   if admin:
   if innovator:
      if WatchedLaunch == 1:
      else:
   if Commando:
   else:
   if WatchedLaunch == 1:
   else:
      if spacer:
   if TakeFirst:
   else:
   if TakeFirst:
   else:
      if innovator:
      else:
   jump Day1Start