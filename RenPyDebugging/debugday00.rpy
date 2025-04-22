label prologue:
   menu:
      "Yes: disable metatext tutorials.":
         $ InterestFlag = True
         $ SkillSolutions = True
         $ ShipExplore = True
         $ FirstEvent = True
         $ SkillTutorial = True
         $ Meta = False
      "No: keep metatext tutorials.":
   $ quick_menu = True
   $ MetZ = True
   if Meta:
label originstart: # Player's first Origin choices.
   menu:
      z "Your file told me where you grew up. Care to remind me?"
      "[[Spacer]: You were born and raised in the black.":
         jump spacerintro
      "[[Colonist]: The first natural birth on Charisi Major, actually.":
         jump colonistintro
      "[[Core-Worlder]: Deep core; you came up on Torderra.":
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
   z "Your file had some information about your adolescence. Made for an interesting read, though not as interesting as what came next."
   "[[Punk]: Hellraiser extraordinaire.":
      jump punkintro
   "[[Dreamer]: Always had your head in the clouds.":
      jump dreamerintro
   "[[Tech Student]: They didn't use \"gifted and talented\" lightly.":
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
   z "But curiosity only goes so far. I know why I chose for you to come with me. So, I wanna hear the story from you. What brought you here?"
   "[[Ex-Pirate]: Shit. Shitshitshit.":
      jump pirateintro
   "[[Colonial Administrator]: Fuckfuckfuckfuck{i}fuck!{/i}":
      jump adminintro
   "[[Innovator]: Oh, here we fucking go again...":
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
   "[[Proceed with these Origins and Skills?]"
   "No. Return to the first Origin options.":
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
   "Proceed.":
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
      "[[Would you like to continue with Rael presenting as asexual and uninterested in sexual interaction?]"
      "Yes; Rael is asexual.":
         $ ZuberiInterest += 2
         $ CaleiaInterest += 2
         $ BrommInterest += 2
         $ MizzInterest += 2
         $ TulemeniInterest += 2
         $ SamInterest += 2
         $ AnwillInterest += 2
         $ InterestFlag = True
         $ RaelAce = True
      "[[Default]: No; Rael is not asexual.":
   if (punk) and (Meta):
   menu:
      z "What I'm trying to say is that you might see things from time to time. I just want to make sure you're not surprised."
      "\"Nothing could surprise me at this point.\"":
         jump nonplussed
      "\"Hopefully they're not surprised if I watch.\"" if RaelAce == False:
         jump watcher
      "\"I'm sure they'll get an eyeful of me, too.\"" if RaelAce == False:
         jump flaunt
      "[[Punk]: \"I'm no stranger to casual sex with friends.\"" if punk:
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
   b "No, I... I mean, yes, ma'am. I did. Apologies."
   "\"He's just saying hello.\"":
      jump grrcaleia
   "Bite your tongue":
      jump silent
   "[[Tech Student]: \"Stars, is that an integrated cyberlink?\"" if tech:
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
   z "So, what would you prefer?"
   "Take the First Shift with Zuberi, Mizz, and Tulemeni.":
      jump takefirst
   "Take the Second Shift with Caleia, Bromm'ka, and Tulemeni.":
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
      "But for now..."
      "Accept Bromm'ka's invitation. Watch the hyperlaunch.":
      "It's been a day. Just head to your quarters.":
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
   "You also can't help but notice just... how much that robe does {i}not{/i} protect his modesty. Your eyes struggle not to draw down his body."
   "\"... aren't you cold?\"":
      jump coldmizz
   "\"Nice to meet you, Mizz.\"":
      jump greetmizz
   "[[Dreamer]: \"That's an {i}amazing{/i} abaya you're wearing there.\"" if dreamer:
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
      "The underwear selection, at least, seems varied enough."
      "Zero underwear. Maximum comfort.":
         $ Commando=True
      "Briefs. Classy. Snug. Bulgy.":
         $ Briefs=True
      "Boxer Briefs. Loose enough to breathe.":
         $ BBs=True
      "Boxers. Free and airy is the way.":
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