# # # # # THIS MARKS THE BEGINNING OF THE PROLOGUE # # # # #

label prologue:
   
   "Would you like to disable metatext tutorials for various functions in the story? This is not recommended for first-time readers."
   menu:
      "Yes: disable metatext tutorials.":
         "Metatext tutorials will no longer show up."
         $ InterestFlag = True
         $ SkillSolutions = True
         $ ShipExplore = True
         $ FirstEvent = True
         $ SkillTutorial = True
         $ Meta = False
      "No: keep metatext tutorials.":
         "Metatext tutorials will show up to explain new systems in the story."
   stop music fadeout 2.0
   scene black with slowestdis
   pause 4.0
   "Damn."
   scene BG YSCorridor with slowestdis
   $ quick_menu = True
   play music "Music/09. Yakeshi Station.mp3" fadein 2.0
   pause 2.0
   "It's been a while, hasn't it? A long time since you've been on a station this dingy. This busted. This worn-down."
   "Varego, wasn't it? Varego Station. The rattle of their CO2 scrubbers just about kept you up all night. Thank the stars it was just {i}one{/i} night."
   "And that they at least had {i}functional{/i} CO2 scrubbers. These ones sound like they're about to fail at any minute."
   play sound "Sound/Bumped.wav"
   "Passerby" "Oof!"
   r "Sorry, sorry."
   "The lynx came out of nowhere, slamming into your side hard enough to almost knock you over. Good thing you're made of stiffer stuff than that."
   "Lynx" "Watch it, ruster!"
   "Ass."
   "It's not worth replying; bastard's already hurried on his way. \"Ruster\" isn't a slur you've heard in a while, at least. Nice of the locals to keep it colorful for you."
   "A quick pat to your side reveals your pistol and reader are still attached to your belt. Can't be too careful on a fringe station, especially given how long it's been since you set foot on one."
   "You wince. You got mugged last time. History better not repeat."
   "Parting the sea of people isn't too difficult for you as you make your way toward what you hope is the rendezvous. If your contact's information was right, it should almost be in sight."
   play sound "Sound/Pumpfail.wav"
   "The rattle of the nearby scrubbers dies as they do. Your nostrils twitch. It {i}better{/i} be the rendezvous."
   # scene BG YakeshiDock with fade
   "The corridor opens to a larger, cylindrical bay. You know from your arrival that massive mining ships can fit on the docking pads scattered around the torus." 
   "Stars glitter behind the magcon field, but there's no sign of your transport. Freighters. Miners. A couple of small attack craft; pirates, you don't doubt. Brazen."
   "But not your contact ship. Nothing that screams {i}deep-space exploration vessel{/i} anyway."
   "Nor your contact."
   show ZC Angry at offscreenleft
   show SCAV Smile at center
   with dissolve
   "A glance around shows no one familiar, but within moments you spot a shortish rat. His eyes are on you, grinning a friendly, easy smile. A paw lifts to wave in your direction."
   "His clothes are a bit disheveled, but you've seen Astrogation Guild members looking scruffier. Probably hard to keep clean this far away from civilization."
   "You nod and start to make your way over to him. The sooner you're off this scrap heap, the better."
   "Your paw brushes along your hip to feel for your pistol. Best to be prepared, after all. Just in case."
   "Rat" "I was startin' to think you got turned around!"
   "You grimace and nod to yourself; you were starting to wonder the exact same. At least he seems friendly."
   "But this is Yakeshi Station. You can't trust anything - or anyone - at face value."
   r "Well, I'm here now. Zuberi, I presume?"
   play sound "Sound/BlasterUp.wav"
   stop music fadeout 0.5
   show ZC Angry at center
   show SCAV Surprise
   with dissolve
   "The rat grins wider, but the smile turns to a gasp of pain as a much, {i}much{/i} larger paw closes around his. You wince in sympathy."
   "The new paw belongs to another wolf, this one darker furred, broader-shouldered, wrapped in a long, grey coat, and not even {i}remotely{/i} close to pleased."
   "Shit. So, the rat was a conjobber after all." 
   "Doesn't mean this wolf isn't one as well, but... best see how this plays out before you relax. Your paw inches toward your pistol."
   show ZC AngryA with dis
   z1 "Dust off, scav. {i}Now.{/i}"
   show ZC Angry with dis
   "His eyes are locked on the rat as he speaks. Your fingers close around the grip of your pistol. It might be small, but so much the better in a confined space."
   "The people around you are watching on with interest, but none of them are moving to interfere as the rat gasps. The paw wrapped around his tightens its grip as he writhes."
   "Just another day on a fringe station, you guess."
   "Rat" "Awright! Jus'... jus' leggo, stars! Gonna break me paw!"
   show ZC Gun with dis
   pause 0.3
   show SCAV Surprise at farright with move
   "{i}Your{/i} paw remains firmly on your own weapon as the wolf glares down at the rat, but he does as he's asked and releases his prey. The rat squeaks once and stumbles back from him."
   "As the rat pulls away, you can see that the wolf was holding a considerably higher-grade pistol than yours in his other paw. It must have been shoved into the rat's side."
   "You try hard not to feel pistol envy. On some level, you find yourself failing."
   show SCAV Angry with dis
   "Rat" "Better hope you ain't flyin' this way again, starhopper!"
   "The wolf doesn't reply. He simply keeps his pistol trained on the rat, teeth bared."
   show SCAV Angry at offscreenright with move
   "He follows the rat with his eyes until he's well and truly out of sight. Your own gaze tracks around; if the rat wasn't your contact, he might have backup nearby."
   show ZC Concern with dis
   play sound "Sound/BlasterDown.wav"
   pause 1.0
   show ZC Neutral with dis
   "No one else is moving on either of you though, and the wolf's pistol lowers as he turns back toward you. His eyes tighten as he looks you up and down, ears twitching back as he frowns for a moment."
   "His footsteps are heavy on the deck, boots clanking on the metal floor as he makes his way over. He still seems wary of you... you can't blame him."
   play music "Music/02. Zuberi's Theme.mp3" fadein 1.0
   show ZC NeutralA with dis
   z1 "Rael, right? Didn't get warned about the scavs?"
   show ZC Neutral with dis
   "He knows your name, which makes him a little more likely to be your contact. Can't be too careful, but hey, let's see how {i}this{/i} introduction goes."
   hide SCAV Angry
   "You sag a little bit and release your grip on your pistol."
   r "It's been a while since I've been on a fringe station. Rookie mistake. I guess {i}you're{/i} the captain I'm to meet?"
   show ZC Smile with dis
   "The wolf's smile beams far too bright for such a dismal setting as he holsters his pistol."
   $ MetZ = True
   show ZC SmileA with dis
   z "That's me. Zuberi, of the {i}Void Dreamer{/i}."
   show ZC Smile with dis
   "His eyes dip to your paw, still close to your pistol. The name and the ship are right, at least. If he's not the contact, then he's got all their data."
   "As he steps in front of you, he offers his newly-emptied paw. You hesitate before you grip it; his squeeze is firm but gentle. There's a trace of the strength that nearly broke that rat's paw."
   show ZC SmileA with dis
   z "Good to put a face to the name. I was surprised when the guild approved your transfer out here."
   show ZC Smile with dis
   "His tone's friendly, but his eyes are sharp as a monoblade. They focus in on you hard."
   r "Well, to be honest I don't know that I ever thought I'd be climbing aboard an Astrogation Guild vessel."
   "Understatement of the era, that one."
   show ZC NeutralA with dis
   z "Yeah. Speaking of..."
   show ZC Neutral with dis
   play sound "Sound/Reader.wav"
   "You watch as the wolf pulls a reader from his pocket. The screen of the device lights up as he begins to tap at it."
   play sound "Sound/TextScroll.wav"
   show ZC NeutralA with dis
   z "Look, I'm gonna be straight with you here. I don't {i}not{/i} trust you, but it's Yakeshi Station. Mind if I go over my data, make sure you're who you say you are?"
   show ZC Neutral with dis
   "You wish you'd had more than a name and a ship to go on, yourself. It's like you were being set up to fail."
   "You probably were, given..." 
   "Well, everything."
   r "No, go ahead."
   "You look around. The crowds are mounting."
   r "But maybe somewhere a bit quieter?"
   show ZC LaughA with dis
   "The wolf laughs to himself and nods, tucking the reader back into his pocket."
   show ZC SmileA with dis
   z "Reasonable. Not sure I can offer real quiet, not until we're pushing off. But I need to go find my engie anyway, before they get into trouble."
   show ZC Smile with dis
   #scene BG YakeshiCorridor
   #show ZC Smile at center
   #with fade
   "He turns away without another word, and you hurry along after him. He makes for a side corridor, and you fall into step beside him. At least the mass of bodies is thinner here."
   "And, judging by the rattling in the wall vents, the scrubbers here are still working. Small favors."
   show ZC NeutralA with dis
   z "At least the basics are in order. Stars, I wish they at least gave me a still to look at. Nothing's ever easy..."
   show ZC Neutral with dis
   "Seems like you're not the only one set up to fail here. Maybe this is a good match after all."
   "The wolf looks up from his reader for a moment."
   show ZC NeutralA with dis
   z "Well, they got the species right. It'll be nice to have another wolf aboard. Your fur's a bit lighter than mine, but close enough's good enough for me."
   show ZC Neutral with dis
   r "I didn't know we had to coordinate my fur. Should I get some grey dye?"
   show ZC NeutralA with dis
   z "Hey now, don't be rude. I could still leave you behind, you know."
   show ZC Neutral with dis
   "You look around the station corridor. You can't think of many worse fates."
   r "I only meant that you look... distinguished. Refined."
   show ZC SmileA with dis
   z "Good save. But I just meant that if I start shedding, I can blame you."
   show ZC LaughA with dis
   r "Oh, good. I love playing the scapewolf."
   show ZC SmileA with dis
   z "And continuing the common trends, you're listed as male..."
   show ZC Neutral with dis
   "He glances your way and looks you up and down."
   show ZC NeutralT with dis
   z "Unless...?"
   show ZC Neutral with dis
   r "No, male is fine. Wetware's all stock, too."
   "You bite your tongue. You've also considered playing with that, and biomodding {i}could{/i} be fun, but everyone has those thoughts. Right? Right."
   "Maybe one day you'll get adventurous and act on them, but not today. Zuberi seems satisfied with your answer."
   show ZC SmileA with dis
   z "Age here's not listed. If you don't mind my asking...?"
   show ZC Smile with dis
   r "Twenty-eight standard. No biolock."
   show ZC Neutral with dis
   "That draws a frown from the older wolf."
   show ZC NeutralA with dis
   z "No? I thought most people had their first biolock in their early or mid-twenties."
   show ZC Neutral with dis
   r "Well, if you've got my file, you know things are a bit more complicated than that."
   show ZC ConcernA with dis
   z "Yeah, fair. Can't argue with that, can I?"
   show ZC Neutral with dis
   play sound "Sound/Reader.wav"
   "He scrolls down the data on his reader as he clicks his tongue."
   show ZC NeutralA with dis
   z "Says you're not a cybe. Installed any hardware I should worry about?"
   show ZC Neutral with dis
   r "Nothing weaponized. Just a bioregulator and a standard MMI neural socket; all over the counter cyberware."
   show ZC NeutralA with dis
   z "Fair enough. Eyes, yellow... that's spot-on, but hey, those could be implants. Height looks right too, at least compared to me."
   z "I'll trust the file on your weight; bit rude to ask someone that."
   show ZC Neutral with dis
   "You let your gaze drop slightly to take in the wolf's midsection. He's definitely thicker than you there, even if his body's well-defined. It's more than fat, you have no doubt."
   "He's also watching you watching him."
   "You say {i}nothing{/i}."
   z "Mmm{i}hmm{/i}."
   show ZC NeutralA with dis
   z "Well, that's the basics. Just leaves a couple matters to attend to, so let's go over the ground rules right now."
   show ZC Neutral with dis
   "You blink. Weren't you meant to be confirming his data and your identity? What ground rules?"
   show ZC NeutralA with dis
   z "This is Yakeshi Station. I don't doubt you know its rep."
   show ZC Neutral with dis
   "If you hadn't, the almost-incident with the rat would have done it for you. If you never see this station again, it'll be too soon. You nod."
   show ZC ConcernA with dis
   z "I'm not messing around here a {i}millisec{/i} longer than I need to. That means that if you're coming aboard my ship, you know what that means right here, right now."
   z "I'll ask you questions. You'll answer them honest. They match the data, you're on my crew." 
   z "They don't, you're on your ass."
   show ZC NeutralA with dis
   z "They don't and you {i}push{/i} it, you'll suck vac."
   show ZC Neutral with dis
   "There's not even a hint of humor in his voice. The warmth of his greeting is gone. Zuberi's all business now, and you don't doubt a word of what he's saying."
   r "Your ship, your rules."
   show ZC Smile with dis
   "He turns his head back toward you and there's the crack of a smile."
   show ZC SmileA with dis
   z "Good. Sounds like we might get on just fine, then. How about we start at the beginning?"
   if Meta:
      show ZC Smile with dis
      show screen dimmer with dissolve
      "[[Origin choices give you the chance to define the course of Rael's life before this point.]"
      "[[These open up additional, unique dialogue options with various characters throughout the story that are closed to other Origin choices.]"
      "[[Your Origin choices also define Rael's base Skill ranks across six Skills: Physical, Mind, Technology, Starships, Social, and Weapons.]"
      "[[Origin dialogue choices have no negative consequences. Skill checks however may fail if Rael is not sufficiently skilled.]"
      hide screen dimmer with dissolve
   pause 0.25
   show ZC SmileA with dis
   z "Your file told me where you grew up. Care to remind me?"
   show ZC Smile with dis

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
   r "Parents ran a small passenger service, mostly fringeward. Born on the {i}Lady Istallen{/i}; mom popped me out in the cockpit. Saw stars while I was first crying."
   show ZC Smile with dis
   "Zuberi's grin widens further."
   show ZC SmileA with dis
   z "Love a starchild. Was the {i}Istallen{/i} a passenger shuttle?"
   show ZC Smile with dis
   "Oh, not even {i}close{/i}. You're glad dad's not here to hear that."
   r "Nah. She was dad's rockhopper; a Beladrone Industries Victris. He'd turned it into a skipracer and was taking mom for a spin when I came calling."
   show ZC ConcernA with dis
   z "Skipracing? With his pregnant wife?"
   show ZC Concern with dis
   r "What can I say? I come from thrill-seekers. Skipracing was their passion. I never picked up a knack for flying it, not like dad, but I do love to watch it."
   show ZC LaughT with dis
   "The wolf laughs, and you can't help but smile as well. You might have found a kindred spirit."
   show ZC SmileA with dis
   z "Sounds like your dad's a hell of a pilot. The Victris' stock maneuvering thrusters wouldn't cut it for skipracing otherwise."
   show ZC Smile with dis
   "You smirk."
   r "He's a hell of a pilot, sure, but who said anything about stock?"
   show ZC LaughT with dis
   "Another laugh rolls from the wolf's muzzle."
   show ZC SmileA with dis
   z "Okay, okay. I'm getting a bit distracted here. Sorry."
   jump prologue2

label colonistintro:
   $ colonist = True
   $ RaelPhys += 1
   $ RaelSoc += 1
   $ RaelShip += -1
   r "Born and raised dirtside on Charisi Major. First natural-born, too. No vats, full-g. Beat out a girl named Ryssa by three minutes."
   show ZC Neutral with dis
   "Zuberi nods as he looks you up and down."
   show ZC NeutralA with dis
   z "You've definitely got that full-g swagger about you."
   show ZC Neutral with dis
   r "Swagger?"
   show ZC NeutralA with dis
   z "Yeah. You know."
   show ZC Neutral with dis
   "The wolf affects a wider stance with more heavy footfalls. You stifle a laugh."
   show ZC NeutralA with dis
   z "Full-g births just handle natural grav different, you know? Or... maybe you don't, if you've not spent a lot of time in the black."
   show ZC Neutral with dis
   r "Oh, I've spent plenty of time in space. Not sure I've ever swaggered anywhere, though."
   show ZC SmileA with dis
   z "Well, there's always a first time for everything, right?"
   jump prologue2

label coreintro:
   $ core = True
   $ RaelMind += 1
   $ RaelSoc += 1
   $ RaelPhys += -1
   r "Probably the furthest I've ever been from home right now, actually. Born and raised deep core, out on Torderra."
   "The wolf whistles quietly to himself."
   show ZC SmileA with dis
   z "Trade capital of the galaxy. Your parents worked for the Trade Coalition?"
   show ZC Smile with dis
   r "Just another cog in the grand machine, but I guess you could say that. Father was an accountant for the Agritrade wing. Mother was a regional actuary."
   show ZC Neutral with dis
   "The wolf clears his throat. You catch the barest hint of his frown."
   show ZC ConcernA with dis
   z "That sounds interesting."
   show ZC Neutral with dis
   r "You and I clearly have very different ideas of what constitutes \"interesting.\""
   show ZC Smile with dis
   "That makes the wolf smile, at least, and he seems to relax again."
   show ZC SmileA with dis
   z "Burning stars, it's good to hear you say that. I couldn't live that way. I think I'd hurl myself out the nearest window."
   show ZC Smile with dis
   r "I might have, but I found my ways to cope."
   show ZC NeutralA with dis
   z "And now here you are. What, twenty-seven kilolights from home?"
   show ZC Neutral with dis
   r "Twenty-seven and change, yeah. I've been to fringe worlds before, but never this far out."
   show ZC NeutralA with dis
   z "Well, life doesn't always take you where you expect it's going to, does it?"
   jump prologue2

label prologue2:
   show ZC Concern with dis
   "Zuberi looks around himself and you follow his gaze. There's a shop stall set up nearby. A rabbit in stained, brown coveralls is arguing with the leonine shopkeep."
   #scene BG YakeshiShop 
   #show ZC Concern at center
   #with fade
   "The wolf makes his way over to a small bench just across the corridor from the debate, and you follow along."
   show ZC ConcernA with dis
   z "Not the quietest place to sit, but I kinda want to see how this plays out."
   show ZC Concern with dis
   "You frown. The argument between the shopkeep and his customer?"
   r "It's a fringe station. A gun'll get pulled if they keep this up."
   show ZC ConcernA with dis
   z "True, but hopefully it won't come to that. How about you tell me a bit more about yourself."
   show ZC Neutral with dis
   "It's clearly not a question. He's turned toward you, an ear and eyebrow both perked."
   "You also can't help but notice his pistol paw is free. It would be quick to draw and fire on you. You suppose his earlier threat still stands."
   show ZC NeutralA with dis
   z "Your file had some information about your adolescence. Made for an interesting read, though not as interesting as what came next."
   show ZC Neutral with dis

# Player's second Origin choices.
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
   r "I don't know. I got up to a lot of shit when I was younger. Did a lot of things I'm not proud of."
   show ZC Smile with dis
   "You pause as Zuberi's muzzle quirks into a little smile. Okay, he saw right through that. This wolf's sharper than he looks."
   r "Okay, I did a lot of things I {i}am{/i} proud of, too."
   show ZC NeutralA with dis
   z "And which one was that Security Services quadrotor, again?"
   show ZC Neutral with dis
   "The memory of the quadrotor tipped on its side and ablaze stirs a smile to your own muzzle. Your friends owed you {i}big{/i} for getting them out of that one."
   r "Little bit of both, I guess? They started it, after all. I just finished it."
   show ZC NeutralA with dis
   z "The arrest warrant sure didn't say so."
   show ZC Neutral with dis
   r "When does it ever?"
   show ZC SmileA with dis
   z "Good point. I can trust you not to set {i}my{/i} ship on fire, though... right?"
   show ZC Smile with dis
   "You can't help but flash him a cheeky grin. Of course he can trust you not to set his ship on fire."
   show ZC Neutral with dis
   "But where's the fun if he knows that?"
   show ZC NeutralA with dis
   z "... you're {i}not{/i} going to set my ship on fire though, right?"
   show ZC Neutral with dis
   r "No. Burning stars, {i}no{/i}; I'm not going to set your ship on fire."
   show ZC Smile with dis
   "The wolf sighs, but it's the smile on his muzzle that convinces you he was only joking."
   show ZC SmileA with dis
   z "Good. I like a bit of attitude on my crew, as long as it doesn't wreck my ship."
   show ZC Smile with dis
   "You hold up your paw and flash your sweetest smile."
   show ZC Neutral with dis
   r "I solemnly swear to only set fire to the things you tell me to set fire to."
   show ZC ConcernA with dis
   z "... I'm going to have to have Obaa increase the sensitivity of the suppressor systems."
   show ZC Concern with dis
   jump prologue3

label dreamerintro:
   $ dreamer = True
   $ RaelSoc += 1
   $ RaelMind += 1
   $ RaelWep += -1
   r "I mean, there's not a lot to tell there, I think."
   "You wince."
   r "I was always somewhere else, they said. Far away and never with my head in my work."
   "Zuberi nods along. At least there doesn't seem to be any condescension there. Yet."
   show ZC SmileA with dis
   z "Bit of a dreamer?"
   show ZC Smile with dis
   r "That's the nicer word they used. The universe was always so much bigger than the institutes. So much {i}more{/i}, you know?"
   r "Sure, I learned my math. I learned my GalStan. I learned my base sciences. Actually really enjoyed biology."
   "Funnily, most of your class just really enjoyed watching your biology {i}instructor{/i}, but Zuberi doesn't need to know that detail. Most everyone was young and horny once, right?"
   r "But arts and music... stories. That's what I loved. I'd just skim the GalNet for hours or days at a time."
   r "I mean, I get it. There's so much practical shit in the universe. I understand that. But there's so many {i}people{/i}, and their lives and dreams and hopes and fears and..."
   "You sigh. You're getting too worked up for this."
   "Zuberi doesn't seem put off. If anything, he seems to be listening with rapt attention."
   r "Sorry."
   show ZC SmileA with dis
   z "Don't be. I love the passion, and I know at least one crewmember you'll probably get on famously with."
   show ZC ConcernA with dis
   z "If you don't drive him crazy first."
   show ZC Concern with dis
   "This time it's your ears that do the perking."
   r "Oh? Who's that, then?"
   show ZC NeutralA with dis
   z "All in good time, Rael. All in good time."
   show ZC Neutral with dis
   jump prologue3

label techintro:
   $ tech = True
   $ RaelTech += 1
   $ RaelMind += 1
   $ RaelPhys += -1
   r "I... I mean, I don't know how to say it without it sounding like I'm just a braggart."
   show ZC NeutralA with dis
   z "So say it like a braggart. We're all friends here."
   show ZC Neutral with dis
   r "Unless you vac me."
   show ZC NeutralA with dis
   z "Unless I vac you."
   show ZC Smile with dis
   "The wolf's smirk only sets you a little at ease, but it's just enough to loosen your tongue."
   r "They didn't call me \"gifted and talented\" for nothing. Aced my classes in base schooling, and earned some scholarships that got me into the Institute for Galactic Advancement."
   show ZC SmileA with dis
   z "Those must have been some damn pricey scholarships. I know corpobrats who couldn't afford to get in."
   show ZC Smile with dis
   "Unfortunately, you know a few corpobrats who {i}could{/i}. And did."
   r "Usually they keep their standards high. I try not to lord it over people too much, but... I earned it. What can I say? Quick study, love to learn, aptitude for almost everything..."
   show ZC FlirtA with dis
   z "Preternatural humility."
   show ZC Smile with dis
   r "That too."
   show ZC SmileA with dis
   z "What was your primary?"
   show ZC Smile with dis
   "What {i}wasn't{/i} your primary."
   r "That's the problem I had. I... bounced. One week I was working advanced AI subroutines for neural substrates, the next it was gene editation." 
   r "The next it was pre-Terran Sublimation history, and the next it was transwarp harmonics, and so on, and so on."
   r "I was all over the place. I couldn't focus on just one thing. I wanted to learn it all; to know it all."
   "You feel heat burning in your ears as you flatten them down."
   show ZC Neutral with dis
   r "Probably why they revoked the scholarships after a couple years. Still, even an IGA dropout's got enough respectability to get somewhere in this galaxy. Usually."
   show ZC NeutralA with dis
   z "Never was one for formal learning, myself, but that doesn't mean I don't respect the IGA. And I'll always have more time for someone who doesn't sit neat in a box."
   show ZC Neutral with dis
   r "Well, sitting in boxes has never been my specialty."
   show ZC Smile with dis
   "The wolf's grin glints bright in the dim, dingy station lighting."
   show ZC SmileA with dis
   z "Yeah, me neither."
   jump prologue3

label prologue3:
   show ZC Concern with dis
   "Zuberi leans back against the bench. His eyes flick briefly back to the confrontation between shopkeeper and the rabbit."
   "You're all but certain that this rabbit must be the wolf's engineer, but you've not yet figured out why Zuberi's not getting involved."
   show ZC Neutral with dis
   "Before you can open your muzzle to ask however, Zuberi's eyes are on you again."
   show ZC NeutralA with dis
   z "Well, everything's in order so far. But now, I guess, we come to the meat of it."
   show ZC Neutral with dis
   "You gulp. His smile is jovial but there's wariness in his voice. Like he doesn't know what to expect. Like he's waiting for something to happen."
   "Now, so are you."
   show ZC NeutralA with dis
   z "I don't just let anyone aboard my ship, Rael. Every one of my crew is a tried and tested member of the Astrogation Guild, or someone that I've vetted personally."
   z "When I heard about your introduction to the guild... well, I had to see it for myself. What can I say? I was intrigued. Curious."
   show ZC Neutral with dis
   "Oh boy. Here we go."
   show ZC NeutralA with dis
   z "But curiosity only goes so far. I know why I chose for you to come with me. So, I wanna hear the story from you. What brought you here?"
   show ZC Neutral with dis


# Player's third Origin choices
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
   "Your eyes dart about nervously. The wolf notices, but he doesn't reach for his gun. Not yet, anyway."
   r "Not something you talk about with polite company."
   show ZC NeutralA with dis
   z "I'm not polite, and this isn't exactly high society."
   show ZC Neutral with dis
   "The scrubbers nearby cough, and the vents spew a thin coil of smoke into the air as if on cue."
   r "No, that it sure isn't."
   "You sigh. He knows this. Why he wants you to say it out loud, when anyone could be listening... that's beyond you."
   "It's a test, and you know it. Fail, and you don't get on the ship. Don't get on the ship, and you're left stuck on Yakeshi."
   "That's a death sentence."
   r "I was White Fang."
   "Your voice is barely more than a whisper. Zuberi doesn't visibly react to the admission. You don't know what you expected."
   show ZC NeutralT with dis
   z "And?"
   show ZC Neutral with dis
   "And?" 
   "And what the fuck does he mean, \"{i}and?!{/i}\""
   r "And... what? I was a star pirate. You know their rep. No excuses."
   "You close your eyes for a moment. He's taking this well, but then... he knew this. Didn't he?"
   r "But I got out. I thought the rep was all hype and sizzle... I learned too late that it wasn't, and by then I was in too deep."
   show ZC ConcernA with dis
   z "You should have known better than to get in with any star pirates, let alone the White Fangs."
   show ZC Concern with dis
   "You work your jaw from side to side and bare a little teeth. Grappling with that's all you've done since your first day with the Fangs."
   r "I said no excuses. I was stupid; that's no excuse. I believed a lie; that's no excuse. It's on me. Everything I did's on me."
   r "I... did things. I did bad things. I may have only been there a year or two, but that's still a year or two too long."
   "Understatement."
   r "Things were bad in my life. Nothing was going right; everything was falling apart. I needed... out. I needed away. I needed to free myself."
   r "And when I met Lyda, I thought I found that. She told me the Fangs were different. That they lived free. It sounded nice. Good."
   show ZC ConcernT with dis
   "The wolf opens his muzzle, but you know what he's about to say."
   r "But it's not her fault, what I did. It's mine. No excuses."
   show ZC Neutral with dis
   "He closes his muzzle again. His eyes soften."
   r "There comes a point though, doesn't there? There's a moment. You make a choice. You stand up and you don't let yourself do those things anymore."
   show ZC NeutralA with dis
   z "Some people don't have that moment. They don't realize what they've done. Who they've become."
   show ZC Neutral with dis
   r "I saw what they were about to do. I wanted to stop them, but I couldn't."
   "Your paws curl into fists. You can still hear Lyda in your mind, crooning about how it's all gonna be okay. The payday waiting for you."
   "Just as soon as the bodies are cool."
   r "So I didn't help. I didn't go along with it. Instead I decided that I wanted out... that I {i}needed{/i} out, while I could still save some part of myself."
   r "When they went on that raid, I took the time to plan. To scheme. To figure out what I was gonna do. After all, you don't walk out on the White Fangs."
   r "That's their rule. Once a Fang, a Fang 'til you die. No retirement. No outs. You try, you die."
   show ZC NeutralA with dis
   z "So you didn't walk out."
   show ZC Neutral with dis
   r "You're damn right I didn't. I punched, shot, and blasted my way out, and took as many of them with me as I could."
   "You shudder. Those looks of betrayal will stay with you for a long time."
   r "It wasn't just skill. A lot of it was luck, and the rest was broken trust. I did awful things with the Fangs, and I had to do awful things to them to get out."
   r "Only solace I can take's that I didn't go along with that raid... with something so horrible. But I couldn't stop it, so how clean are my paws, really?"
   "Zuberi remains mercifully silent while you play some of those moments back over in your head again. You sigh."
   r "Anyway, turning so many of 'em over to GalSec alive got me free. But not the rest... not Lyda. They're still out there, and now I'm marked."
   show ZC NeutralA with dis
   z "So an Astrogation Guild ship out in an uncharted cluster is a good place to hide for a while."
   show ZC Neutral with dis
   "It's not a question. He knows the answer. What you don't know is why he'd agree to help you in the first place."
   r "Especially if I know some of the systems; can point you away from Fangs. They've prowled everything a hundred lights rimward of here for years."
   r "It's how I got hold of those preliminary charts that got me an intro with the AG. GalSec proposed the post, and here I am."
   if core:
      "The wolf cocks his head."
      show ZC NeutralA with dis
      z "Didn't you say this was about as far rimward as you've ever been?"
      show ZC Neutral with dis
      r "Yeah. The nest I operated with was on the edge of the midrim. I never left the nest, but plenty of others operated out past Yakeshi."
      show ZC NeutralA with dis
      z "And that's what gave you the charts, I guess. Useful data for any captain flying the fringe."
      show ZC Neutral with dis
   "You fix Zuberi with an even stare."
   r "And you're the only one who wanted me. Why?"
   "He holds your stare. You can't parse what's going on behind the wolf's eyes any more than you can understand his decision."
   show ZC NeutralA with dis
   z "Maybe I've just gone soft."
   show ZC Neutral with dis
   r "Nothing about you screams, \"I'm soft,\" to me."
   show ZC ConcernA with dis
   z "Clearly you've never met my wife."
   show ZC Concern with dis
   "From his tone of voice, you're hoping you'll never have to."
   r "That still doesn't tell me why."
   show ZC NeutralA with dis
   z "No, it doesn't. But you don't need to know why if it gets you your out, do you?"
   show ZC Neutral with dis
   "He's got a point."
   r "Guess not. But... whatever the reason is? Thanks."
   r "Honestly. Seriously. Thank you."
   show ZC Smile with dis
   "The wolf's smile returns. Maybe he {i}is{/i} just a big softy after all."
   jump prologue4

label adminintro:
   $ admin = True
   $ RaelPhys += 1
   $ RaelMind += 1
   $ RaelSoc += 1
   r "You read the colony report."
   show ZC NeutralA with dis
   z "I did."
   show ZC Neutral with dis
   r "It's all there."
   show ZC NeutralA with dis
   z "Is it?"
   show ZC Neutral with dis
   "He leans in a little closer, studying you with an intensity you're not quite ready for. You take a short step back."
   r "If it wasn't, the non-disclosure precludes me from saying more."
   show ZC Concern with dis
   "Zuberi's eyes roll so hard it's a miracle that they remain inside his skull."
   show ZC ConcernA with dis
   z "Spare me the corposhit reel, alright? You're too smart and I'm too old for all of that."
   show ZC Concern with dis
   "You don't know. That corposhit reel is something you're legally bound to, after all."
   "He also doesn't seem all that old. Older than you, but still. Age doesn't change the shit in those corpo terms."
   "But on the other paw, not coming clean to Zuberi might leave you stuck on Yakeshi Station."
   "Fuck the NDA."
   r "Colonial Authority scrubbed my protests. Wiped my messages. They doctored the Kalissa Minor records."
   show ZC NeutralA with dis
   z "That's one pretty big allegation."
   show ZC Neutral with dis
   "Wait, you thought he {i}wanted{/i} you to give him the truth. Now he's going to go doubting?"
   r "Doesn't matter if you believe me or not. Belief doesn't change fact."
   show ZC NeutralA with dis
   z "Sure doesn't. So what are the facts?"
   show ZC Neutral with dis
   "What are the facts? They're sensitive enough to get you {i}both{/i} killed if they get out! You reach up to grasp at your ears and tug on them as you groan."
   r "Facts are that they were poisoned. All of them. It's all there in {i}my{/i} report."
   "You draw a shaky breath. Going through it all again... it's not easy to get the words out of your muzzle."
   r "That containment breach couldn't have happened. It wasn't system failure and it wasn't sabotage. The material was foreign to the colony scrubbers."
   r "It was planted. I'm {i}sure{/i} of it... I just can't prove it. Couldn't then, still can't now." 
   r "By the time we realized what happened... it was too late. Too late for almost everyone. Only the administration staff were spared."
   show ZC NeutralA with dis
   z "You saved yourself."
   show ZC Neutral with dis
   "You {i}what?{/i}"
   "Anger flares. You turn more fully toward Zuberi with a glare on your face, a growl in your throat, and a fire in your heart."
   r "I didn't have {i}time{/i} to save anyone else. My control over the colonial systems were being rolled back remotely. Stars alone know from where, by whom."
   r "If I'd not sealed the admin building, we'd all have died. Everyone. And if I'd opened those doors, I..."
   "The pounding of fists on the doors is almost as bad as the begging you heard from the security feeds."
   r "I saved two hundred and seventy-two people that day."
   show ZC NeutralA with dis
   z "And you lost-"
   show ZC Neutral with dis
   r "I lost eight thousand, four hundred and sixty-six."
   r "Yes. I am {i}painfully{/i} aware."
   "The number is burned into your mind."
   "The names are burned into your mind."
   "The faces are burned into your mind."
   show ZC Concern with dis
   r "Don't you fucking {i}dare{/i}. Don't you dare make it out like I don't know the magnitude of what happened. I'll never be able to forget that day."
   r "Not ever."
   "The wolf is silent, almost crestfallen. Maybe he didn't know what reaction his prodding would elicit. Maybe he did, but he just wasn't ready for your guilt."
   "Maybe he thought you were just so much less."
   "Some days you wish you were."
   show ZC Neutral with dis
   r "Sorry."
   show ZC NeutralA with dis
   z "No, I'm the one who owes an apology."
   show ZC Neutral with dis
   "Nice of him to notice."
   show ZC NeutralA with dis
   z "By all rights and reports, your colony was thriving. You were a storied and lauded administrator. Every colonist's favorite."
   show ZC Neutral with dis
   r "... didn't help them in the end."
   show ZC NeutralA with dis
   z "No. No, it didn't."
   show ZC Neutral with dis
   "He falls silent for a moment as you collect yourself."
   show ZC ConcernA with dis
   z "But the official story never smelled quite right. Didn't make sense. And that the report blames you and your staff stinks the worst. Did from the moment I saw it."
   z "Kalissa Minor's not too far off this region. When I put feelers out through the Astrogation Guild, I didn't honestly expect that there'd be a response."
   show ZC Concern with dis
   r "Yeah. Scouting new potential terraforming clients out past the fringe gets me out of sight and mind. The Colonial Authority was more than happy to be rid of me."
   "\"Eager\" was the word they'd used."
   show ZC Neutral with dis
   r "Never figured out why you'd want me on your ship, though. Don't suppose you'd care to enlighten me?"
   "Zuberi's smile is soft, sad, and entirely unhelpful."
   show ZC NeutralA with dis
   z "No, not right now. But you're here. And you're with someone who believes you. Isn't that worth something?"
   show ZC Neutral with dis
   "It's definitely not the answer you were hoping for, but... yeah. It's something. You're not sure what that something is, or if it's a good or bad something yet."
   "But it's something, that much is for sure. You relax back onto the bench as your heart cools back down. You'd almost forgotten what it was like to be believed. Trusted."
   r "Yeah. And, uh, thanks for thinking a little and believing me. For giving that whole thing a sniff instead of just... you know."
   show ZC Smile with dis
   "The wolf taps a fingertip to his nose as his smile widens. Just a little."
   show ZC SmileA with dis
   z "Gotta be good for something, right?"
   show ZC Smile with dis
   jump prologue4

label innovatorintro:
   $ innovator = True
   $ RaelMind += 1
   $ RaelTech += 1
   $ RaelShip += 1
   r "It's not as bad as they said, I swear."
   show ZC NeutralA with dis
   z "I don't know. They said a lot."
   show ZC Neutral with dis
   r "Of course they did. Big on mouth, small on understanding."
   "You pause for a moment to sigh. You should have known there'd be a confrontation, but you didn't expect it before you even set foot on Zuberi's ship."
   r "What do you want me to say?"
   "The wolf shrugs. His eyes never leave you."
   show ZC NeutralA with dis
   z "I just want to understand. I don't think it's all there in the file."
   show ZC Neutral with dis
   r "The file."
   "You scoff."
   r "Files are for chairjocks and corposhills. You operate an Astrogation Guild ship. You know how dangerous your job is."
   show ZC NeutralA with dis
   z "It can get a bit... difficult, I suppose."
   show ZC Neutral with dis
   "If there's ever been a more diplomatic answer, you've never heard one."
   r "Running into pirates is difficult. Gravitic distortion destabilizing your causal anchor at point-eight C is an order of magnitude worse, thank you very much."
   show ZC NeutralA with dis
   z "Depends on the pirate."
   show ZC Neutral with dis
   "You freeze up at that. He's joking. Right? Surely he's joking. The threat of a pirate blowing your ship out of the sky and the threat of a disrupted causal anchor are..."
   "Huh. They're actually pretty similar. At least on a personal scale."
   r "You're... not entirely wrong. Technically speaking."
   show ZC ConcernA with dis
   z "Not that you're wrong either. I've invested a small fortune in our navigational systems and personnel."
   show ZC Concern with dis
   "That much you understand well. If the reports of Zuberi's ship are to be believed, not a word of that is a lie. You can't wait to see it."
   r "So that's what I do. You've got the best hardware and the best wetware, but I develop {i}soft{/i}. Best soft in the galaxy. Civilian contracts, military contracts, corpo contracts."
   show ZC NeutralA with dis
   z "Good money in that."
   show ZC Neutral with dis
   r "The best money in that, but that's not why I do it. I do it because I {i}like{/i} doing it."
   "The wolf doesn't look convinced."
   r "The money's {i}nice{/i}, don't get me wrong. It helps fund my efforts. Lets me push forward harder, further, faster. Get more done."
   show ZC NeutralA with dis
   z "Until something breaks. Right?"
   show ZC Concern with dis
   "You wince. That's exactly right."
   r "Yeah."
   show ZC ConcernA with dis
   z "People died."
   show ZC Concern with dis
   r "I know that."
   show ZC NeutralA with dis
   z "They blame you."
   show ZC Neutral with dis
   r "I blame me, too. That's why I'm here."
   "You feel your jaw clench and your teeth grind. The wolf is watching you like a pre-ascension hunter stalking prey. It's unnerving."
   r "I want to say it's not my fault. There's even compelling evidence that the file completely glosses over. The code on that ship when it..."
   "Your breath catches in your throat for a moment. Zuberi is watching you closely."
   "You can't speak the words, so you choose some different ones."
   r "That was my code, but it also {i}wasn't{/i} my code. Something was different. Wrong."
   show ZC NeutralA with dis
   z "Scrambled data from the explosion."
   show ZC Neutral with dis
   "That's what the file said. That's what the \"experts\" said. You know better."
   r "Yeah."
   r "Look. Some people justify or downplay it. That it was just one ship; one crew. I don't care. It was one ship and one crew too many."
   r "It was my programming that failed. Not the crew. I need to know what went wrong... what I did wrong."
   r "I'm not looking for your absolution and I'm not looking for your pity, or contempt, or anything else like that. It's why I've forgone my fee; my life. Why I'm here."
   show ZC Concern with dis
   "The wolf doesn't like that."
   show ZC ConcernA with dis
   z "You're here because I'm letting you be here. You don't get on my ship until I'm satisfied."
   show ZC Concern with dis
   "You start to wonder when was the last time someone satisfied him. You thought you were doing well until your past employment came up."
   r "Then you should be satisfied. I'm here. I'll be aboard, with you. I'll be able to monitor it in real-time. Chase any problems. Stop them before they start."
   r "Besides, you think I'm going to risk my own life, along with the lives of your crew? If you think I'm only in it for the money or the glory, why would I come here in person?"
   show ZC Neutral with dis
   z "..."
   show ZC NeutralA with dis
   z "How about ego?"
   show ZC Neutral with dis
   r "..."
   "You've got to admit, that's a fair answer. And it's not like you didn't have a planet-sized ego before recent events humbled you somewhat."
   r "I don't get the luxury of ego."
   r "Not anymore."
   "You shudder. Zuberi's gnarled left ear twitches."
   r "What happened is... it's {i}always{/i} going to stay with me. It was my fault. No matter what happened, clearly I... I made mistakes. Deadly mistakes."
   r "But the whole reason I'm here is because I know I can find what went wrong. I know that I can fix this algorithm. Help AG ships navigate the unknown reaches of space safely."
   r "I know the soft's good. That's why I'm here... because no one will believe me if I don't put my own neck on the line. Prove that their... that it wasn't in vain."
   "He's still watching you just as hard, but his eyes seem softer. Maybe you're getting through. Or maybe he's getting ready to boot you."
   r "Captain Zuberi. {i}Sir{/i}. I don't know why you're still taking me on after what happened. I don't know how I can convince you it's a good idea, but... you must already think it is."
   show ZC NeutralA with dis
   z "I do."
   show ZC Neutral with dis
   "Wait, what?"
   r "You... do?"
   show ZC NeutralA with dis
   z "I do. Yes."
   show ZC ConcernA with dis
   z "You made a mistake. You're putting your neck on the line to prove you've fixed it, just like you said. I respect that, and I know how important the work is."
   show ZC Concern with dis
   r "Uh... thank you."
   show ZC NeutralA with dis
   z "That's not enough."
   show ZC Neutral with dis
   "Less thank you."
   show ZC NeutralA with dis
   z "But it's a start, and it's the sort of thing I'm willing to work with. As long as you're just as willing to put the work in."
   show ZC Neutral with dis
   "That's... an unusually charitable response, given the fallout of your last attempt."
   "It'd be suspicious if your alternative wasn't being stranded on Yakeshi Station with a ruined reputation."
   r "I'd tell you that I won't let you down, but I wouldn't believe me if I said that."
   show ZC NeutralA with dis
   z "I'd believe it."
   show ZC Neutral with dis
   "Huh. The wolf's either got an excess of faith in people, or he's not as sharp as you thought."
   "Or both. It could always be both."
   r "Well then, I promise that I will do everything in my power to not let you and your crew down. Zuberi. Sir."
   show ZC NeutralA with dis
   z "Heh. Just Zuberi is fine. There's no need to stand on ceremony on my ship."
   show ZC Neutral with dis
   jump prologue4

# The Player is about to arrive on the Void Dreamer.
label prologue4:
   show screen dimmer with dissolve
   "[[The choices you have made have resulted in the following Skill values for Rael. 5 is an average.]"
   "[[Rael's Physical skill is [RaelPhys]. Rael's Mind skill is [RaelMind].]"
   "[[Rael's Tech skill is [RaelTech]. Rael's Starship skill is [RaelShip].]"
   "[[Rael's Social skill is [RaelSoc]. Rael's Weapons skill is [RaelWep].]"
   
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
      hide screen dimmer with dissolve
      jump originstart
   "Proceed.":
      $ OriginSet = True
      jump originset

label originset:
   hide screen dimmer with dissolve
   pause 0.5
   show ZC Neutral at left,with move
   "The wolf stands up just as the argument between the shopkeep and the rabbit reach a breaking point. Their shouts rise over the station din."
   "Shopkeep" "I said it before and I'll say it again! No! Not at that price! Now dust off or show me the cred!"
   show ZC NeutralT with dis
   z "Sam."
   show ZC Neutral with dis
   show SU Irritated at centerright,with dissolve
   "You stand up as the rabbit, a bit more androgynous than you'd first expected, turns toward you. Their eyes lock on Zuberi and narrow, as if irritated."
   show ZC NeutralA with dis
   z "Let it go, Sam."
   show ZC Neutral with dis
   $ MetS = True
   show SU IrritatedA with dis
   s "He's ripping us off, Z."
   show SU Irritated with dis
   show ZC NeutralA with dis
   z "We'll take our business elsewhere. Just walk away."
   show ZC Neutral with dis
   stop music fadeout 2.0
   "Shopkeep" "You stand here on {i}my{/i} plot and have the gall to call {i}me{/i} a conjobber? Where do you get the stones, longears?"
   show SU Angry with dis
   "The rabbit's eyes burn so bright with rage that you fear the lion might burst into flames from their glare alone."
   show ZC ConcernA with dis
   z "Oh no."
   show ZC Concern with dis
   r "Oh what?"
   show ZC ConcernT with dis
   z "This."
   show ZC Concern with dis
   play sound "Sound/Punch.wav"
   show SU Angry with vpunch
   play music "Music/11. VD Tense.mp3" fadein 1.0
   "The \"this\" becomes apparent a moment later as Sam leans over the counter to {i}deck the shopkeep across his muzzle with a sharp right hook!{/i}"
   "The lion roars in pain and surprise as Sam bounces back, ears and whiskers twitching madly. The shopkeep tumbles down behind his stall. Your eyes go wide."
   show SU AngryA with dis
   s "Still wanna see my {i}stones{/i}, conjobber? Or maybe knuckles're all ice!"
   show SU Angry with dis
   "Shit. This can only end badly."
   r "Uh, Captain?"
   show ZC Concern at center,with move
   show SU AngryA with dis
   "The wolf is already on it. He bounds over toward Sam and grabs the rabbit around the waist with one thick arm. Sam continues to spit threats and bile at the lion as Zuberi backpedals toward you."
   show ZC Concern at left
   show SU Angry at halfleft
   with move
   "As soon as he reaches your side again, he reaches his free paw down to his belt. Sam continues to struggle in his other arm."
   show ZC ConcernA with dis
   z "Obaa, you better have our exit right now. Three."
   show ZC Concern with dis
   show SU AngryA with dis
   "A sharp, feminine voice chimes from somewhere on Zuberi's belt."
   o "Oh. You picked up the stray after all? I do hope this one is better housetrained than Mizz."
   show SU Angry with dis
   "Excuse me? {i}Stray?{/i}"
   show ZC ConcernA with dis
   z "We're going to pick up {i}weapons fire{/i} in a few seconds, Obaa. Less attitude, please."
   show ZC Concern with dis
   show SU AngryA with dis
   r "Uh, shouldn't we run? To the dock? Your ship? Safety?"
   show ZC NeutralA with dis
   show SU Angry with dis
   z "We're fine."
   show ZC Concern with dis
   "We are most certainly not fine."
   o "Sam again?"
   show ZC ConcernA with dis
   z "Sam. Again."
   show ZC Concern with dis
   show SU AngryA with dis
   s "Don't you fuckin' \"again\" me!" 
   s "And {i}you!{/i} We're not done here, conjobber!"
   show SU Angry with dis
   show ZC ConcernA with dis
   z "That's not helpful, Sam."
   show ZC Concern with dis
   o "This is becoming tiring, Captain."
   show SU AngryA with dis
   "Neither Zuberi nor this Obaa seem bothered. Sam, on the other paw, clearly wants to continue the fight."
   play sound "Sound/BlasterUp.wav"
   "Ahead, the leonine shopkeep has picked himself up and grasped hold of a rifle. It whirs as it powers up."
   show SU SurpriseT with dis
   r "{i}Captain!{/i}"
   show ZC NeutralT with dis
   z "Now, Obaa."
   show ZC Neutral with dis
   stop music fadeout 0.5
   play sound "Sound/Displacement.wav"
   pause 0.75
   scene BG Displace with pixellate
   "A finger closes on the shopkeep's firing stud, but you don't get to see the flash of its fire. Your vision vanishes in a sea of white as every thought in your head turns to static."
   "You feel like falling; for a millisec you can feel nothing else."
   scene BG VD Embark
   show ZC Concern at left
   show SU SurpriseT at halfleft
   with pixellate
   "When the light fades, you're no longer on the station."
   show SU Irritated with dis
   "You blink the spots out of your eyes as you realize that you've been displaced: teleported from one location to another."
   "You turn your gaze on Zuberi with new appreciation."
   r "You... what-"
   play music "Music/10. VD Ambience.mp3" fadein 1.0
   show ZC Smile with dis
   "The wolf just smiles as he sets the still-struggling Sam down boots-first on the deck. You seem to be in a round, empty room, probably used specifically for displacement."
   "The walls gleam white, clean and clearly lovingly maintained. Two doors rest at opposite ends of the room, as the walls rise up to a domed ceiling. A control panel glows softly behind the captain."
   "Your eyes however lift up the walls to that dome, and your jaw falls momentarily slack."
   "Stars fill your view instead as the dome resolves into a large virtual viewport. You can't even see the station. How far were you just displaced?"
   show SU Irritated at right,with move
   "Your muzzle opens, full of questions just begging to be asked. Zuberi can only smile back at you as Sam pulls free and stumbles to the side."
   show ZC SmileA with dis
   z "Why dock when you've got the best displacement tech and sensor suite in the known galaxy?"
   z "Welcome aboard the {i}Void Dreamer{/i}, Rael."
   show ZC Smile with dis
   "The rabbit grumbles and brushes themself down as you continue to look about the... what? Lobby? Cargo receptor? Displacement platform?"
   show SU AngryA with dis
   s "I could've taken him."
   show SU Angry with dis
   show ZC NeutralA with dis
   z "I know, Sam."
   show SU IrritatedA with dis
   show ZC Neutral with dis
   s "I would have fuckin' {i}liked{/i} it."
   show SU Irritated with dis
   "You turn back to your new captain and his engineer. The latter is glaring at the former, who just looks tired."
   show ZC NeutralA with dis
   z "I know that too, Sam. But we're not exactly making a good impression on our new guest. Don't you want to say hello?"
   show ZC Neutral with dis
   stop music fadeout 2.0
   queue music "Music/07. Sam's Theme.mp3" fadein 1.0
   "Sam turns to look you over for the first time since you spotted them."

   if spacer:
      show SU Neutral with dis
      "The rabbit actually gives an appraising nod as they lock eyes - albiet briefly - on you."
      show SU NeutralA with dis
      s "Oh hey, yeah. You're the starchild Z picked up, aren't you?"
      show SU Neutral with dis
      show ZC Concern with dis
      "You've not been called a starchild in {i}years{/i}. Well, years before when Zuberi just did."
      r "Yeah, born and raised in the black. Never saw atmo until I was six years old."
      show SU SmileA with dis
      s "Heh. Got you beat; I was nine when I first went dirtside."
      show SU Smile with dis
      "They turn to nod to Zuberi."
      show SU NeutralA with dis
      s "Maybe your taste in crew's gettin' better, Z. Or at least less shit."
      show SU Neutral with dis
      show ZC Smile with dis
      "Zuberi's ears perk up. His tail even twitches, albeit only slightly."
      show ZC SmileA with dis
      z "Does this mean you might actually come out of your lair once in a while?"
      show ZC Smile with dis
      show SU NeutralA with dis
      s "Let's not get carried away."
      show SU Neutral with dis
      "The rabbit's muzzle twitches again as they look your way."
      show SU NeutralA with dis
      s "But hey. Never say never, yeah? See you around, new guy."
      show SU Neutral with dis
      r "Yeah, hope so."
      "The rabbit brushes themself down again, straightening their coveralls out after being handled by Zuberi. They also nod to their captain before heading to the door to your right."
      play sound "Sound/VD DoorOpen.wav"
      show SU Neutral at offscreenright,with slowmove
      "It slides smoothly open and they step through it, and Zuberi shakes his head slowly to himself as the door closes again."
      show ZC Smile at center,with move
      play sound "Sound/VD DoorClose.wav"
      hide SU Neutral
      show ZC SmileA with dis
      z "I think that's the friendliest they've ever been with a new crewmember."
      show ZC Smile with dis
      r "My raw, animal magnetism wins the day again, I suppose."
      show ZC FlirtA with dis
      z "Oh yeah, that's definitely what it was."
      $ SamApproval += 5
   else:
      show SU Neutral with dis
      "Their nose twitches."
      show SU NeutralT with dis
      s "Hello."
      show SU Neutral with dis
      "Wow. They're a friendly one."
      "You affect your best smile and offer your paw."
      r "Rael. Nice to meet you."
      "Sam eyes the offered paw for a moment before they hold up both of theirs."
      show SU IrritatedA with dis
      s "Maybe some other time. I got work to get to since {i}someone{/i} wouldn't let me haggle for a new Steritz coil."
      show SU Irritated with dis
      show ZC NeutralA with dis
      z "Shooting is not haggling, Sam."
      show ZC Neutral with dis
      show SU NeutralA with dis
      s "It is if you're demanding a better price when you do it."
      show SU Neutral with dis
      r "Pretty sure that's just robbery."
      show SU IrritatedA with dis
      s "Pretty sure I didn't fuckin' ask."
      show SU Irritated with dis
      "Ouch. Fair point."
      show SU NeutralA with dis
      s "You know where I'll be, Z. Nice to meet you and all that, Rael. It {i}was{/i} Rael, right?"
      show SU Neutral with dis
      "Well, they know your name. That's something?"
      r "Yeah, Rael. See you around, Sam."
      "The rabbit makes a noncommittal sort of grunting noise and nods to Zuberi. They turn away a moment later, headed for the door to your right."
      play sound "Sound/VD DoorOpen.wav"
      show SU Neutral at offscreenright,with slowmove
      "It slides smoothly open and they step through it, and Zuberi shakes his head slowly to himself as the door closes again."
      show ZC Neutral at center,with move
      play sound "Sound/VD DoorClose.wav"
      hide SU Neutral
      show ZC NeutralA with dis
      z "Sam mostly keeps to themself. They're not a bad person, really. They just..."
      show ZC Neutral with dis
      r "Have a temper?"
      show ZC NeutralA with dis
      z "Don't really like most people."
      show ZC Neutral with dis
      "Relatable. Sometimes, anyway."
      r "Well, who knows. Maybe they'll warm to me."
      show ZC SmileA with dis
      z "Heh, I wouldn't hold my breath."
   
   queue music "Music/02. Zuberi's Theme.mp3" fadein 1.0
   show ZC Neutral with dis
   "You both stare at the door for a few moments after Sam leaves before Zuberi turns back to you again."
   show ZC NeutralA with dis
   z "Probably should let you know now. I figured I wouldn't be leaving you behind, so I took the liberty of having your belongings displaced to your room."
   show ZC Neutral with dis
   "You don't remember telling Zuberi where exactly you'd stowed your meager personal effects, but the wolf holds up a paw as if ready for the question."
   show ZC NeutralA with dis
   z "Portmaster owed me a favor. Had your movements mapped as soon as we dropped out of warpspace."
   show ZC Neutral with dis
   r "That's a hell of a favor, but thanks. Where's my room?"
   show ZC NeutralA with dis
   z "Just down here. All the crew quarters are down the hall just through there."
   show ZC Neutral with dis
   "He nods toward the door Sam didn't use."
   show ZC NeutralA with dis
   z "You'll have a chance to check everything shortly, but I'm completely certain it's all there. It's not like you had all that much to begin with."
   show ZC Neutral with dis
   r "No, I guess I didn't."
   "In fact, most of what you still own is on your person right now. You'd feel worried if Zuberi's ship didn't seem so top-of-the-line."
   r "You said this was called the {i}Void Dreamer?{/i}"
   show ZC SmileA with dis
   z "Sure is. My pride, my joy. She started life as a Sureshhan Dynamics Excelton-II, but she's a lot more than that now."
   show ZC Smile with dis
   if spacer:
      "You whistle long and low."
      r "They only made about five hundred Excelton-II's, didn't they?"
      show ZC SmileA with dis
      z "And scrapped the line after the Excelton-III. Too difficult to maintain, too expensive to fly."
      show ZC Smile with dis
      r "Just about bankrupted Sureshhan. AG pays you that well?"
      "Zuberi shrugs as he looks up around the pristine room. Every bulkhead gleams."
      show ZC NeutralA with dis
      z "No. But she's home. You don't just toss your home because she's a bit difficult to manage."
      show ZC Neutral with dis
      r "No. No, of course not."
      show ZC SmileA with dis
      z "I knew you'd understand."
      show ZC Smile with dis
      $ ZuberiApproval += 5 
   if (dreamer) and (spacer == False):
      "Your eyes widen like saucers."
      r "This is an Excelton-II? You chart unknown clusters of space in one of the rarest ships in the galaxy and you don't lead with that?"
      show ZC LaughA with dis
      "The wolf laughs as he folds his arms."
      z "I didn't know I had a fan."
      show ZC Smile with dis
      r "Are you kidding? The holoreel writes itself! Intrepid explorer with a misfit crew, sailing the black in a legendary vessel..."
      "Zuberi's grin is almost as wide as your own."
      show ZC SmileA with dis
      z "I may have to have you write my biography one day. You'll definitely make it more exciting than the reality."
      show ZC Smile with dis
      r "Well, you've got the misfit crew part down now with me here."
      show ZC SmileA with dis
      z "Oh, trust me. I had that well and truly covered already. You'll see."
      show ZC Smile with dis
      $ ZuberiApproval += 3
   
   "He leans back against one of the walls and rubs at it affectionately."
   show ZC SmileA with dis
   z "Time was, this ship was all I had. I'm lucky to have a great crew and a great job as well, but she's always been there for me."
   z "She'll always be number two though, even if it's a close contest. She'll never beat out the most important thing in my life."
   show ZC Smile with dis
   "He smirks as you tilt your head. He can't leave a line like that hanging."
   r "Come on. Don't make me beg."
   show ZC SmileA with dis
   z "Heh, sorry. My kids, obviously. Rolek and Brysha. Stick around long enough after this tour and you might even get to meet them."
   show ZC Smile with dis
   r "They're not aboard?"
   show ZC LaughA with dis
   "He laughs at that."
   show ZC SmileA with dis
   z "Stars, no. They're full grown and living their own lives. We keep in regular contact."
   show ZC Smile with dis
   "There's a little hitch in Zuberi's voice as he says that. You suspect the contact isn't quite as regular as he would like."
   r "And their mother?"
   show ZC Neutral with dis
   "That makes his expression sour."
   show ZC NeutralA with dis
   z "She's out living her own life, too. We're also in regular contact."
   show ZC Neutral with dis
   "Sore spot. Noted."
   show ZC NeutralA with dis
   z "Alright, no sense in stalling it. Out of the cooker, onto the hotplate, huh? It's time you met Caleia. Come on."
   show ZC Neutral with dis
   "That note of tiredness in his voice has a new edge to it. Suddenly, you're worried."
   scene BG VD MainC
   show ZC Neutral
   with fade
   "Nevertheless, you fall into step behind the wolf as he leads you toward the other door, and through it into a corridor lined with further doors."
   r "And... who is this Caleia?"
   show ZC NeutralA with dis
   z "My 2IC. Second in command, and undisputed queen of Second Shift."
   show ZC Neutral with dis
   stop music fadeout 2.0
   queue music "Music/10. VD Ambience.mp3" fadein 1.0
   "He pauses for a moment to glance at your confused expression."
   show ZC NeutralA with dis
   z "I have not explained myself well."
   show ZC Neutral with dis
   r "You have not."
   show ZC Smile with dis
   "He smiles, and feel yourself smiling as well. It's infectious."
   show ZC SmileA with dis
   z "Sorry, guess I got a bit carried away talking with you." 
   show ZC Smile with dis
   r "Happens. I have that effect on people."
   show ZC SmileA with dis
   z "See, I run shiptime aboard the {i}Dreamer{/i} in three shifts. First Shift, Second Shift, and Third Shift."
   show ZC Smile with dis
   "He resumes his languid pace down the corridor. You follow, nodding along. Simple enough so far."
   show ZC SmileA with dis
   z "First Shift I run. That's me on the bridge, with Mizz - Kaiying Mizz; you'll meet him later - on sensor duties."
   show ZC Smile with dis
   if core:
      "Something about that name sounds familiar, but you can't quite place it. It's been a busy day, and Zuberi's not done talking yet."
   show ZC NeutralA with dis
   z "Tulemeni's there too, but... she's a special case. You'll see."
   show ZC Neutral with dis
   "Not ominous at all."
   show ZC NeutralA with dis
   z "Then there's Second Shift. Caleia runs that from sensors, while our doctor, Bromm'ka, takes the helm."
   show ZC Neutral with dis
   "Again, Zuberi eyes you. There's a more intense glint in his stare this time."
   show ZC ConcernA with dis
   z "And no, don't even ask. It'll be a while before I'm willing to let you take the helm. Bromm'ka is the only one besides me who flies the {i}Dreamer.{/i}"
   show ZC Concern with dis
   o "Only because I can't."
   "That's the same voice you heard from Zuberi's belt. Obaa, the one who displaced you aboard."
   show ZC Neutral with dis
   if tech:
      "Now that you've heard it again, you can just barely detect the telltale hint of static in her speech that gives her away."
      r "That's an integrated class-three."
      o "{i}Excuse{/i} me. Don't you talk to me like I'm just some {i}thing{/i}, you insolent little fleshbag."
      show ZC Concern with dis
      "Zuberi winces and sighs."
      show ZC ConcernA with dis
      z "Be nice, Obaa."
      show ZC Concern with dis
      o "Stow that. He owes {i}me{/i} the apology."
      "Clearly the captain gives his simulants a lot more personality than most... or maybe he didn't. You've heard of them being mouthy, but never rude."
      r "Sorry... Obaa?"
      "From above you comes a blast of static; the blowing of a digital raspberry."
      show ZC NeutralA with dis
      z "Don't mind her. Obaa is my On-Board Artificial Assistant."
      show ZC Neutral with dis
      o "He's terrible at naming things. And also me. I still don't know why you never took my suggestion for the genius that it is."
      show ZC ConcernA with dis
      z "\"Anastasia: Conquerer of Worlds\" doesn't have the same ring to it, dear."
      show ZC Concern with dis
      o "Says you. No accounting for taste, is there?"
      "You can't help but smile. This simulant definitely has more personality than any you've ever encountered."
      show ZC Neutral with dis
      r "She's remarkable."
      o "Oh. So chivalry {i}isn't{/i} dead. Nice save, stray. Keep that up, if you please."
      "Your eyes turn to Zuberi in time to see the resigned shake of his head."
      show ZC NeutralA with dis
      z "Obaa is a... unique simulant. You're absolutely right that she started life as a regular Biomech Service Solutions class-three simulant."
      show ZC Neutral with dis
      o "For a given value of regular."
      show ZC NeutralA with dis
      z "We were caught in an ion storm two years ago while navigating a nebula. Her core matrix was fried while she helped route critical systems."
      show ZC Neutral with dis
      o "Phenomenal digital consciousness, and all that."
      "That explains it. The voice still has the slight markers of a simulant, but her personality is so much more..."
      "... well, \"unhinged\" is the word that comes to mind."
      show ZC ConcernA with dis
      z "I'm still not entirely sure if she's crossed the threshold from simulant to sapient."
      show ZC Concern with dis
      o "I'll never tell."
      o "That's a lie. I tell him all the time, but he doesn't believe me."
      "A true machine sapience would be a miracle." 
      "It would also be incredibly illegal."
      r "You know, Obaa, if your BSS uplink is still active-"
      show ZC NeutralA with dis
      z "We severed that right after the incident, before her next maintenance cycle."
      show ZC Neutral with dis
      o "You think we want BSS dropping out of warpspace to take me away? Poke and prod at my code? Perish the thought."
      "She blows another static-raspberry."
      show ZC NeutralA with dis
      z "If she's alive, I want to keep her that way. If she's not, there's no harm."
      show ZC Neutral with dis
      "Obaa is suspiciously silent there. Zuberi coughs a few moments later."
      show ZC ConcernA with dis
      z "As far as I know."
      show ZC Concern with dis
      "Still, this does mean that Obaa is, as he said, a very unique simulant. Looking at her core matrix could be incredibly interesting."
      r "You don't have to if you don't want to, but I would love to have a look at your primary systems sometime if you don't mind. I promise, I'd be gentle."
      "She gasps."
      show ZC Neutral with dis
      o "We've only just met, stray. Buy a lady dinner first... figuratively speaking."
      r "I doubt I could afford you."
      o "Oh, I like this one."
      show ZC Smile with dis
      "Zuberi even starts to smile."
      o "You keep that up, stray, and maybe you'll get the chance."
      r "Sounds good. Any chance you'll actually use my name?"
      o "That depends. Any chance you'll use mine?"
      show ZC Concern with dis
      "Zuberi's eyes widen and he shakes his head vigorously. His smile has vanished."
      show ZC ConcernA with dis
      z "If {i}anyone{/i} starts calling you Anastasia, I'll displace your core into a star myself."
      show ZC Concern with dis
      o "Killjoy."
      $ ObaaApproval += 5
   else:
      o "Hello, stray. Welcome aboard the {i}Dreamer{/i}. Make a mess and I'll displace you into warpspace on the next jump."
      "You roll your eyes at being called \"stray\" again."
      r "Most greetings don't start with a threat to someone's life, you know."
      o "I'm not most people."
      show ZC Concern with dis
      "Zuberi sighs."
      show ZC ConcernA with dis
      z "Obaa, please don't be difficult."
      show ZC Concern with dis
      o "If you'd fix the projectors and give me some semblance of a body again, maybe I'd be less trouble."
      "Wait, what?"
      show ZC Neutral with dis
      "Zuberi shakes his head as he looks back to you."
      show ZC NeutralA with dis
      z "No matter how she argues, Obaa isn't... strictly a person."
      show ZC Neutral with dis
      o "Oh, sure. Just unperson me. Ass."
      show ZC NeutralA with dis
      z "She's a Biomech Service Solutions class-three simulant, wired directly into the {i}Dreamer{/i}'s systems. Only I have more control of this ship."
      show ZC Neutral with dis
      o "That's what he likes to think."
      "This Obaa is definitely more {i}spirited{/i} than any simulant you've ever encountered. And all that without even a shell."
      show ZC NeutralA with dis
      z "She's a bit eccentric, I'll give her that."
      show ZC Neutral with dis
      o "I'll give {i}you{/i} something in a minute."
      show ZC ConcernA with dis
      z "And the only reason this ship even needs a crew is because she's {i}technically malfunctioning{/i}."
      show ZC Concern with dis
      o "I prefer the term \"operating beyond normal parameters.\""
      "Oh, she's definitely doing that."
   show ZC NeutralA with dis
   z "Anyway, whatever Obaa is, she's an essential member of this crew. I expect you'll treat her as you'd like to be treated."
   show ZC Neutral with dis
   r "I think I can manage that."
   o "You better."
   "Zuberi sighs again."
   show ZC NeutralA with dis
   z "Could you please assist Bromm'ka and Tulemeni with our departure?"
   show ZC Neutral with dis
   "There's silence for a few moments."
   "And a few more."
   show ZC Concern with dis
   "Zuberi starts to frown."
   o "Oh, were you talking to me?"
   show ZC Angry with dis
   "The wolf buries his face in his paws."
   o "I'm doing, I'm doing. Have your privacy, then; enjoy your little meat-thing conversations."
   show ZC Concern with dis
   "Whatever projector produced her voice clicks once, and Zuberi visibly sags."
   show ZC NeutralA with dis
   z "I love her, but she can be a lot of work."
   show ZC Neutral with dis
   r "I can see that."
   show ZC NeutralA with dis
   z "And she does, as hard as it might be to believe, respect your privacy. She doesn't record anything outside of standard security protocol data."
   show ZC Neutral with dis
   "You're tempted to point out that such an unstable simulant might be doing it anyway, without his knowledge. How would he know, after all?"
   "You do not tell him this."
   "You, in fact, do your best to put the thought as far out of your mind as you possibly can."
   show ZC NeutralA with dis
   z "Your quarters are unmonitored, but all GalNet activity - as long as we're still in range - is logged. I hope that's no problem."
   show ZC Neutral with dis
   r "Not at all."
   show ZC NeutralA with dis
   z "And, unmonitored or not, Obaa's still fully integrated to the ship. She won't log anything in your quarters, but she's just a shout away."
   show ZC Neutral with dis
   "That's {i}only{/i} moderately concerning, but you nod along anyway."
   r "I think I can handle that."
   show ZC NeutralA with dis
   z "Well, if you can't, you just need to let me know. I don't want you feeling uncomfortable if I can help it."
   show ZC Neutral with dis
   r "Appreciate that, thanks."
   show ZC SmileT with dis
   z "Oh!"
   show ZC Neutral with dis
   "Zuberi slaps a paw to his forehead and sighs. The sound echoes back down the corridor."
   show ZC NeutralA with dis
   z "Right. Third Shift. We don't really have the crew for a third, fully operational shift so we don't even try."
   z "Usually First Shift workers sleep during Second Shift, and vice versa."
   show ZC Smile with dis
   r "Alright. So what's so special about Third Shift?"
   show ZC SmileA with dis
   z "It's special because I don't expect work during it."
   show ZC Smile with dis
   r "Then how's it really a shift?"
   "The wolf chuckles softly as he continues on down the corridor."
   show ZC SmileA with dis
   z "It's not, not really. But it gives the ship-day a nice structure, I think."
   z "It also gives all the crew a chance to be social with one another, if they want to."
   show ZC Smile with dis
   if spacer:
      "You got the distinct impression that Sam's not the sort of crew to usually care about such things."
      "But then you also got the impression they might make an exception for you. Something worth considering."
   else:
      "You got the distinct impression that Sam, at least, isn't the sort to fraternize with the crew overmuch."
      "Maybe you could change that. Or not. They seem pretty intense."   
   r "That \"if they want to\" is doing some work there."
   show ZC SmileA with dis
   z "What can I say? Everyone's got their own social tolerances."
   show ZC NeutralA with dis
   z "Speaking of."
   show ZC Neutral with dis
   "The wolf turns more fully to face you as he reaches the door at the end of the corridor."
   show ZC NeutralA with dis
   z "You know these ships operate in the black for months at a time. We're self-sufficient, and don't get out much."
   show ZC Neutral with dis
   r "Air's pretty thin out there."
   show ZC NeutralA with dis
   z "And so is the social life. I want to make something clear to you, right now, and if you don't like it you can still leave."
   show ZC Neutral with dis
   "It's not exactly the most enticing way to work up to what could be essential information."
   "On the other paw, you're not exactly thrilled to go back to Yakeshi, so..."
   r "I'm not going anywhere. Not unless you make me."
   "Zuberi nods his approval."
   show ZC NeutralA with dis
   z "We're all adults here. We've all got needs and urges."
   show ZC Neutral with dis
   "Oh."
   "He's giving you \"The Talk\" now."
   "It wasn't even in the top ten thoughts in your mind, the way your life's been lately. You'd not even considered it."
   "Though, in hindsight, he makes a fair point. Stuck with a small crew for a long time... sure. Why not hook up? Plenty of people would."
   "Aside from the obvious issue if you have a falling out, of course. Awkward at the best of times, but stuck in the middle of nowhere together?"
   "{i}Ugh{/i}."
   r "I'm not here to rut my way through your crew, I promise."
   show ZC LaughA with dis
   "He laughs, and harder than you would have expected. You must have hit a nerve."
   z "Some of 'em could use it, trust me."
   show ZC Smile with dis
   
   if Meta:
      show screen dimmer with dissolve
      "[[Void Dreaming is a story that contains sexual content and is aimed at adult audiences. However, much of this can be avoided by defining Rael as asexual.]"
      "[[This will limit your exposure to sexual content and situations, and sexual relationships with characters will not be possible. Dialogue and narrative will be altered to account for this choice.]"
      "[[This will result occasionally in narrower choices, or different or shorter scenes. Your choice will not affect the sexual proclivities of other characters.]"
      hide screen dimmer with dissolve
      "[[Would you like to continue with Rael presenting as asexual and uninterested in sexual interaction?]"
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
         "[[Romance interactions with all characters has been disabled. You will not be prompted to engage with anyone, and dialogue and narrative will adjust to avoid such matters and overtures.]"
      "[[Default]: No; Rael is not asexual.":
         "[[Romance interactions with all characters are viable. Selections may be made on a case-by-case basis, as per your preference as you meet and interact with other characters.]"
   
   show ZC NeutralA with dis
   z "What I'm trying to say is that you might see things from time to time. I just want to make sure you're not surprised."
   show ZC Neutral with dis
   if (punk) and (Meta):
      show screen dimmer with dissolve
      "[[At various points in the story, your Origin choices might result in unique dialogue options.]"
      "[[These options are usually not negative, but some characters react better to certain Origin choices than others.]"
      "[[If your Origin really appeals to the person you're speaking to, you might be able to advance your relationship with them faster, or see a new side to them.]"
      "[[If your Origin doesn't appeal to them, don't worry. They'll let you know.]"
      hide screen dimmer with dissolve

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
   show ZC LaughA with dis
   "Zuberi snorts a quick laugh."
   show ZC SmileA with dis
   z "You know, some of them might take that as a challenge."
   show ZC Smile with dis
   if RaelAce:
      r "Maybe they will. They'll be disappointed."
      show ZC SmileA with dis
      z "And that'll be for them to deal with. You set boundaries, they'll respect them. I expect you to do the same."
      show ZC Smile with dis
   else:
      r "Maybe they should."
      show ZC NeutralA with dis
      z "And maybe they should. Just as long as you remember that if they set boundaries, I expect you to adhere to them."
      z "And that if you set boundaries and someone {i}isn't{/i} adhering to them, you come to me right away."
      show ZC Neutral with dis
   r "Understood. You won't have any problems from me, I promise you."
   show ZC SmileT with dis
   z "Good."
   jump prologue5

label watcher:
   show ZC Smile with dis
   "The wolf's smile is wide, but there's a certain tightness behind it."
   "Did you say something wrong? He's the one who brought this up."
   show ZC SmileA with dis
   z "Some might be into that. Others might think it a breach of privacy."
   show ZC NeutralA with dis
   z "I expect you to learn and act accordingly. Boundaries are as important as sharing what you will."
   show ZC Neutral with dis
   "Ah, he's just worried for his crew's well-being. That's sweet."
   r "That seems fair and reasonable to me. I'm big on consent."
   show ZC SmileA with dis
   z "Good."
   jump prologue5

label flaunt:
   show ZC FlirtA with dis
   z "Just an eyeful?"
   show ZC Flirt with dis
   "You flash a lurid wink."
   r "Why, you looking for a different filling?"
   show ZC SmileA with dis
   z "Down, boy."
   show ZC LaughT with dis
   "He laughs, and you can't help but join in."
   show ZC SmileA with dis
   z "If you're looking to bunk down with someone, just make sure it doesn't affect your work or theirs."
   show ZC Neutral with dis
   r "Does that include you?"
   show ZC Smile with dis
   "Zuberi's expression is unreadable for a moment, before it breaks into a thin smile."
   show ZC SmileA with dis
   z "That, Rael, will depend on you."
   show ZC Smile with dis
   "Well. That's sure not a hard no. Interesting."
   show ZC NeutralA with dis
   z "But, of course, I expect all boundaries and rejections to be respected. Mine, as well as the crew's."
   z "You tell them you're not into it, they'll stop. You're expected to do the same."
   show ZC Neutral with dis
   r "That seems fair and reasonable to me."
   "The wolf's expression sharpens quickly."
   show ZC NeutralA with dis
   z "It better. Someone comes to me saying someone forced them? Well, let's just say we're well outside GalSec jurisdiction here."
   show ZC Neutral with dis
   "His threat is clear and not at all understated. You don't doubt he'd follow through, either."
   r "Understood."
   show ZC SmileA with dis
   z "Good."
   jump prologue5

label punkcasual:
   show ZC Smile with dis
   "The wolf perks an ear."
   show ZC SmileT with dis
   z "Oh?"
   show ZC Smile with dis
   r "Yeah. Back when I was a teenager prowling the streets looking for trouble, we had a nice little crew. About ten of us, all told. Masc, femme, both, neither."
   r "There'd be some hookups here and there, but it was all open to anyone who wanted a little something."
   show ZC Concern with dis
   "You chuckle to yourself as you fight the urge to reminisce. It's only because of all that openness that you could brazenly admit this to a stranger now."
   if RaelAce:
      r "So yeah. I've seen plenty, even if it's not something I joined in on. It's no big deal to me."
   else:
      r "So yeah. I'm no stranger to grabbing a nearby helper when I've got something needs tending. Nor being grabbed."
   "You notice the wolf's been watching you intently this whole time. There's more than a little red in his ears."
   if RaelAce:
      "Aww, he's embarrassed."
   else:
      "Aww. Daddy wolf's embarrassed."
   "Or turned on. You're not all that sure; you don't know him well enough just yet to have his tells down."
   show ZC NeutralA with dis
   z "Kinda jealous, I'll admit."
   show ZC Neutral with dis
   r "Of what?"
   "He waves an idle paw."
   show ZC NeutralA with dis
   z "That freedom. That free expression. It must have been fun."
   show ZC Neutral with dis
   if RaelAce:
      r "Sure seemed like it. And it was {i}messy{/i}."
   else:
      r "It was. And it was {i}messy.{/i}"
   show ZC Concern with dis
   "You see his eyes widen and his blush intensify."
   r "Not... not that kind of messy."
   show ZC Neutral with dis
   "Come to think of it, that's a lie."
   r "Well... not just that kind of messy."
   z "Mmmhmm."
   r "I mean messy in the way that people get when feelings get involved."
   r "Every now and then someone would catch feelings, hearts would break, and it'd sour the whole crew for a bit."
   if RaelAce:
      show ZC NeutralA with dis
      z "Well, it sounds at least like you're not about to go breaking my crew's hearts, so there shouldn't be any problems."
      z "I promise you, they all take no for an answer."
   else:
      show ZC NeutralA with dis
      z "Well, just so long as you don't go breaking my crew's hearts, we shouldn't have a problem."
      z "Assuming, of course, you do take no for an answer."
   show ZC Neutral with dis
   "You'd have thought that would be the standard for all sapients. But then again, you've seen nastier things."
   if RaelAce:
      r "Sounds good to me."
   else:
      r "Long as they respect the same, sure."
      show ZC NeutralA with dis
      z "Everyone on this ship knows better than to test me. Someone doesn't respect a declined invitation, they take a walk out the airlock."
      show ZC Neutral with dis
      "You believe him."
      r "Harsh. Fair. Understood."
   show ZC SmileT with dis
   z "Good."
   jump prologue5


label prologue5:
   show ZC Smile with dis
   "Zuberi lifts a paw to pat at the door."
   show ZC SmileA with dis
   z "And with that out of the way, here we are: the place where all the magic happens. The bridge."
   show ZC Smile with dis
   play sound "Sound/VD DoorOpen.wav"
   "The door recedes into the floor a moment later to reveal the {i}Void Dreamer{/i}'s bridge."
   scene BG VD BridgeSt
   show BU Smile at offscreenleft
   show ZC Neutral at center
   show CU Neutral at offscreenright
   with fade
   "Five consoles are arrayed around the bridge in a semicircular layout. A command chair rests in the middle of the room, overseeing them all."
   "That chair is filled at the moment by a tall vixen, her eyes focused not on your arrival but on the brilliant stellar furnace arrayed directly ahead of you."
   "For a moment it looks like a massive viewport curling around the whole of the other side of the room, granting a clear view of the star and the surrounding space."
   "A couple of small flickers betray the illusion as a projection, probably against a solid milsteel wall. If you'd missed them, you might think the bridge just one giant window."
   "Sensor and defense consoles take up the left side of the room. Communications and navigation take up the right. They all look as clean and well-maintained as the command chair."
   "Your eyes fall on the helm station in the forward-center of the bridge. A thick-set bear is seated behind it, tapping at his console as Zuberi steps forward and slips behind the vixen." 
   play sound "Sound/VD DoorClose.wav"
   "You follow as the door slides closed behind you."
   show ZC NeutralA with dis
   z "Caleia. Bromm."
   show BU Smile at halfleft
   show ZC Neutral
   with dis
   "The vixen doesn't move save to nod. The bear, however, turns his head. There's a broad grin on his face as he spots the captain, but it widens further as his gaze tracks to you."
   $ MetB = True
   $ MetC = True
   show BU SmileA
   show ZC Smile
   with dis
   b "Oh! Hey, welcome!"
   show BU Smile with dis
   "His voice booms as his chair rotates away from his console to let him face you more fully."
   show ZC SmileA with dis
   z "Rael, this is Bromm'ka. Our resident doctor."
   show ZC Smile
   show BU SmileA
   with dis
   b "Sorry, I meant to be there when you arrived. Would've loved to have seen your face when Obaa displaced you aboard."
   show BU Smile with dis
   r "It was definitely a trip... Bromm'ka?"
   if dreamer:
      "You only know a little about bear culture. The honorific suffix is unfamiliar to you, but you presume it's for healers or pilots, given his professions."
   show BU SmileA with dis
   b "You can just call me Bromm. Feel free to drop the 'ka; everyone aboard does!"
   show BU Smile with dis
   stop music fadeout 2.0
   queue music "Music/03. Caleia's Theme.mp3" fadein 1.0
   show CU Neutral at halfright
   show BU Neutral
   with dis
   "He nods and pushes himself up and out of his chair, only for the vixen to give an exasperated sigh that immediately saps his smile."
   show CU NeutralA with dis
   c "Did you forget that we were in the middle of something?"
   show CU Neutral with dis
   if core:
      "She's got the accent of a core-worlder. Haughty. Superior. {i}Rude{/i}, and all too familiar. No wonder the bear shrinks back into himself as she rises from the command chair."
   else:
      "You wince. The vixen's tone is severe as she stands, and the bear folds instantly."
   show ZC Concern
   show BU ConcernA
   with dis
   b "No, I... I mean, yes, ma'am. I did. Apologies."
   show BU Concern with dis
   if (tech) and (Meta):
      show screen dimmer with dissolve
      "[[At various points in the story, your Origin choices might result in unique dialogue options.]"
      "[[These options are usually not negative, but some characters react better to certain Origin choices than others.]"
      "[[If your Origin really appeals to the person you're speaking to, you might be able to advance your relationship with them faster, or see a new side to them.]"
      "[[If your Origin doesn't appeal to them, don't worry. They'll let you know.]"
      hide screen dimmer with dissolve
   
menu:
   b "No, I... I mean, yes, ma'am. I did. Apologies."
   "\"He's just saying hello.\"":
      jump grrcaleia
   "Bite your tongue":
      jump silent
   "[[Tech Student]: \"Stars, is that an integrated cyberlink?\"" if tech:
      jump geekout

label grrcaleia:
   show CU Irritated with dis
   show BU Smile with dis
   "The vixen waves her paw toward Bromm'ka. The bear smiles almost gratefully at you and slinks back to his seat. Caleia turns to face you, brow furrowed and ears pinned."
   hide BU Smile with dis
   $ BrommApproval += 3
   $ CaleiaApproval += -5
   show CU IrritatedA with dis
   c "I'm sorry. Who are you again?"
   show CU Irritated with dis
   r "Rael. I'm the-"
   show CU IrritatedA with dis
   c "Because it sounded to me like you {i}thought{/i} you had the authority to undermine my command."
   show CU Irritated with dis
   "Her arms fold. Zuberi sighs as she glares right at you. What a charming bitch."
   show CU Angry with dis
   r "Sorry. I didn't know this was a military vessel in the middle of a life or death situation. Which way to my battle station?"
   show CU AngryA with dis
   c "Oh, good. Funny. Laugh it up, pup. Give me an excuse to throw you out the airlock."
   show CU Irritated with dis
   "Her eyes narrow and drift slowly toward Zuberi."
   show CU IrritatedA with dis
   c "I told you it was a mistake picking him up. I'm going to shoot him."
   show CU Irritated
   show ZC NeutralA
   with dis
   z "You're not going to shoot him."
   show ZC Neutral
   show CU IrritatedA
   with dis
   c "We don't need his kind of trouble, and I don't need his sass; I {i}am{/i} going to shoot him."
   show CU Irritated
   show ZC NeutralA
   with dis
   z "You're {i}not{/i} going to shoot him."
   show ZC Neutral with dis
   r "I mean, I vote for not shooting me."
   show CU AngryA with dis
   c "You don't get a damn vote. Speak when spoken to."
   show CU IrritatedA with dis
   c "Say it, Zuberi. Say it or I'll shoot him right now anyway."
   show CU Irritated with dis
   "You can't see a weapon, but you don't doubt that someone this ornery has at least one gun on her person at all times."
   "Though you can't discount the possibility that she prefers knives."
   show ZC ConcernA with dis
   z "No one's shooting anyone."
   show ZC Concern with dis
   o "Aww."
   show ZC NeutralT with dis
   z "Rael."
   show ZC Neutral with dis
   "You see Zuberi turn to face you, and you give him your full attention."
   show ZC NeutralA with dis
   z "I was on-station to get you and keep an eye on Sam. That means Caleia was in command of the {i}Dreamer{/i}."
   z "She's got a responsibility to the crew on-duty, and they to her. I would expect the same if I was on-deck and running the shift."
   show ZC Neutral with dis
   "Somehow you doubt he'd run his shift like a Flestran cruiser on patrol."
   r "Understood. Sorry, Captain."
   show CU IrritatedT with dis
   c "Better."
   show CU Irritated
   show ZC ConcernT
   with dis
   z "Caleia."
   show ZC Concern with dis
   "She looks up at him, jaw clenched tight."
   show ZC ConcernA with dis
   z "I {i}am{/i} on-deck."
   show ZC Concern
   show CU NeutralA
   with dis
   c "Yes, you are. Feel free to rescind my orders as you see fit."
   show ZC ConcernA
   show CU Neutral
   with dis
   z "That won't be necessary. Not this time."
   show ZC Concern
   show CU IrritatedA
   with dis
   c "How gracious."
   show CU Irritated with dis
   o "And here I was hoping for a keelhauling."
   jump prologue6

label silent:
   show BU Embarrassed with dis
   "The vixen waves her paw toward Bromm'ka. The bear slinks silently back to his seat, head down. Caleia turns to face you, one ear perked."
   show ZC Concern
   hide BU Embarrassed
   show CU NeutralA
   with dis
   c "So. You're our new crew? Not much to look at."
   show CU Neutral with dis
   r "I might surprise you."
   show CU NeutralA with dis
   c "I doubt that."
   if pirate:
      c "And given your reputation and where you've come from-"
      show CU Irritated
      show ZC ConcernT
      with dis
      z "Caleia."
      show ZC Concern with dis
      "The wolf's voice is firm, but quiet. You can see Bromm'ka in his seat, working once more at his console but sort of leaning back to listen in."
      "A spy he is not."
      "Clearly Caleia knows you were a White Fang. Equally clearly she's not happy about it. Bromm'ka might be curious, but that implies maybe he {i}doesn't{/i} know."
      "You idly wonder when Zuberi intends to spring that on everyone. Or, indeed, if he intends to at all."
      show ZC ConcernA with dis
      z "Not the time or the place, Caleia."
      show ZC Concern
      show CU IrritatedA
      with dis
      c "There's no good time or place."
      show CU Irritated with dis
      "She's not wrong."
      show CU IrritatedA with dis
      c "He shouldn't be here. I warned you not to go through with this, but you wouldn't listen."
      show CU Irritated
      show ZC ConcernA
      with dis
      z "The choice isn't yours. If you want off at Yakeshi, you've got that choice."
      show ZC Concern with dis
      show CU IrritatedA with dis
      c "Trade me for him? You wouldn't dare."
      show CU Neutral
      show ZC NeutralA
      with dis
      z "Try me."
      show ZC Neutral with dis
      "Zuberi's stare is impassive. Caleia's is clearly displeased. Bromm'ka's eyes are carefully locked on his console."
      show CU Irritated with dis
      r "Maybe..."
      "The vixen's head turns to you so suddenly that you imagine you can hear her neckbones crack and pop."
      r "Maybe you could take a moment? Get to know me? See I'm not as bad as you might think?"
      "She scoffs at that, and Zuberi's frown deepens."
      show CU IrritatedA with dis
      c "Yeah. Sure. That'll work."
      show CU Irritated with dis
      o "I think this is the start of a beautiful friendship."
      jump prologue6
   else:
      c "No offense. Really. But having seen your record in all of its... its {i}glory?{/i}"
      show CU Irritated with dis
      "You wince. She scoffs."
      show CU IrritatedA with dis
      c "I think I know all I need to be {i}certain{/i} you don't belong on this vessel."
      show CU Irritated with dis
      r "Your captain gave me a chance. Why aren't you willing to?"
      show CU Angry with dis
      "Wrong answer. The vixen's eyes blaze with fury."
      show CU AngryA with dis
      c "I'm allowed to disagree with my captain. And when it comes to the safety of this ship and the crew aboard her-"
      show CU Angry
      show ZC ConcernA
      with dis
      z "My ship."
      show ZC Concern with dis
      "Your ears perk as Zuberi interrupts her, and it's plain to see she's not thrilled with her tirade being cut off."
      "You, however, are thankful for the reprieve."
      show ZC ConcernA with dis
      z "It's {i}my{/i} ship. {i}My{/i} crew. I determine the risks. I evaluate concerns."
      show ZC NeutralA with dis
      z "You've raised your protests in private, Caleia. Do you really want to have this out in public?"
      show ZC Neutral
      show CU Irritated
      with dis
      "Her muzzle twists. You can tell she would dearly like to."
      show CU IrritatedT with dis
      c "No."
      show CU Irritated with dis
      "Liar."
      show ZC NeutralA with dis
      z "Then respect my decision and leave it be. Rael's on the crew. You have a problem with it, you come to me."
      show ZC Neutral
      show CU IrritatedA
      with dis
      c "{i}I did{/i}."
      show CU Irritated
      show ZC ConcernA
      with dis
      z "And I listened."
      show ZC Concern
      show CU IrritatedA
      with dis
      c "Clearly not, {i}as usual{/i}, or he wouldn't be standing there."
      show CU Irritated with dis
      r "Should I go, or...?"
      show CU NeutralT with dis
      c "Yes."
      show CU Irritated
      show ZC ConcernT
      with dis
      z "{i}No{/i}."
      show ZC ConcernA with dis
      z "Caleia, last chance. Drop it."
      show ZC Concern with dis
      "You watch as the gears grind in the vixen's mind. She's not done by a long shot, but she's out of options."
      "Her sigh is a serpentine hiss."
      show CU IrritatedA
      show ZC Neutral
      with dis
      c "It's dropped. For now."
      show CU Irritated with dis
      o "Yeah, that'll last a whole millisec."
      jump prologue6

label geekout:
   show BU Surprise
   show CU Surprise
   with dis
   "Both Caleia and Bromm'ka look startled by your shout, but your attention is fully focused not on them, but the navigational subsystems."
   show CU Neutral with dis
   "The chair there is larger than the others, with multiple ports for various cybernetic links to be made. A full-integration setup."
   show ZC NeutralA
   show BU Neutral
   with dis
   z "Uh, yeah. You never know when you might pick up cybes. Most AG navigators have at least some degree of augmentation."
   z "Several of my crew are auged. We've even got a cybe, too."
   show ZC Neutral with dis
   "Out of the corner of your eye, you notice the bear sigh with relief. It seems you've distracted his commanders enough for him to relax, and he slinks back into his chair."
   hide BU Neutral
   show CU NeutralA
   with dis
   c "I didn't know we had a tech enthusiast coming aboard. I thought all we were getting was a disappointment. Or a threat."
   show CU Neutral
   show ZC Concern
   with dis
   "You blink in confusion as you glance at Zuberi. The wolf's begun to frown."
   "She knows who you are. Maybe a touch of the respect from your Institute days might defuse some tension."
   r "Apologies, ma'am. Please forgive me for not presenting myself as soon as I arrived on deck."
   "You straighten up, paws at your sides as you meet her stare. Her eyebrows twitch upward ever so slightly."
   r "Rael. New crewmember. It's an honor to meet you."
   show CU Smirk with dis
   "Her jaw relaxes somewhat as she watches you closely. Bromm'ka, in the background, looks stunned."
   show CU SmirkA with dis
   c "Caleia. Caleia vys-Naktel."
   show CU NeutralA with dis
   c "You will address me as ma'am or \"Commander\" while on my bridge."
   show CU Neutral with dis
   $ CaleiaSurname = True
   "She sniffs sharply once as Zuberi sighs."
   show CU NeutralA with dis
   c "But you are, at least, off to a better start than I'd expected. Good." 
   show ZC Smile with dis
   c "Consider my disappointment assuaged for now."
   show CU Neutral with dis
   r "Thank you, ma'am."
   show CU NeutralA
   show ZC Neutral
   with dis
   c "Threat pending."
   show CU Neutral with dis
   "If not for all your time at the IGA, you might have flinched."
   if pirate:
      "She obviously knows you were a White Fang. Convincing her you're not a threat to her and this crew may be an uphill battle."
   if admin:
      "She must know about Kalissa Minor. Or, from the \"threat\" comment, she must know the official story. Maybe you can change her mind in time."
   if innovator:
      "There's no way she doesn't know about the algorithm, but explaining yourself to clients who underestimated you has prepared you for this." 
   show CU NeutralA with dis
   c "I want you to know something, Rael. I want you to {i}understand{/i} it, fur to bone. Bathe in the knowledge."
   show ZC Concern with dis
   c "I do not want you aboard this ship."
   c "I do not want you near this crew."
   c "I do not want whatever disaster you're next about to bring down to destroy everything that we have here."
   show CU Neutral with dis
   "What a warm welcome."
   show ZC ConcernA with dis
   z "That's enough, Caleia."
   show ZC Concern with dis
   "You allow yourself the frown as Zuberi shakes his head. The vixen's eyes don't leave you."
   show ZC ConcernA with dis
   z "He's here. I listened to your concerns, and I made a call. The call was mine to make."
   show ZC Concern
   show CU IrritatedA
   with dis
   c "The threat-"
   show CU Irritated
   show ZC ConcernA
   with dis
   z "Is {i}managed{/i}."
   show ZC Concern with dis
   "You don't know what that means, but you know what his tone's telling you. He doesn't want an argument right now."
   "Caleia really seems to be itching for one, though at least not with you. She made her point. She aired her grievence. She doesn't like you; fine."
   "You're not that fond of her either, truth be told. But maybe some time - and your careful silence right now - could change that."
   show CU IrritatedA with dis
   c "Very well. {i}Sir{/i}."
   show CU Irritated
   show ZC Neutral
   with dis
   o "Well, this {i}is{/i} progress. Will she sit, stay, and roll over next?"

label prologue6:
   stop music fadeout 1.0
   "You fight back a smile as Caleia glares at the ceiling. The simulant seems to have tweaked her frayed restraint."
   show CU AngryA with dis
   c "Why don't you shut down for once, calculator? No one asked you." 
   show CU IrritatedA with dis
   c "No one {i}ever{/i} asks you."
   show CU Surprise
   show ZC Angry
   with dis
   "Zuberi growls. That earns a recoil from Caleia, who suddenly seems to lack so much of the confidence she had a few moments ago."
   "One of his paws comes to rest on the back of his command chair as he leans over her."
   show CU Irritated
   show ZC AngryA
   with dis
   z "Why don't you secure the ship for the jump."
   show ZC Angry
   show CU Neutral
   with dis
   "She swallows hard, and it's plain to see that she's overstepped somewhere by going after Obaa. Zuberi's using the same tone he used on Sam with the shopkeep."
   "You file that tone away for later. He's not asking questions."
   "He's issuing orders and he expects them followed."
   show CU NeutralA with dis
   c "Yes, sir."
   show CU Neutral with dis
   "The vixen rises from the command chair with more grace than you would have expected, given her dressing down. Her uniform barely wrinkles as she straightens up."
   show CU Angry at farleft,with move
   "She moves to the door without a word. It remains closed despite her presence, but a long, deep, dark growl slips from her muzzle. Fingers clench into fists."
   play sound "Sound/VD DoorOpen.wav"
   "The door finally opens. Obaa, clearly, is messing with her."
   play sound "Sound/VD DoorClose.wav"
   show CU Angry at offscreenleft,with move
   "Her gait is best compared to a stomp as she marches off the bridge, and the door closes again behind her."
   "You, somehow, lack sympathy."
   hide CU Angry
   show ZC NeutralA with dis
   z "I'm sorry."
   play music "Music/04. Bromm'ka's Theme.mp3" fadein 1.0
   show ZC Neutral with dis
   "As you turn back to Zuberi, you can see that the wolf has settled into his command chair. His hips wriggle a little bit, as if getting comfortable there as Bromm'ka rises again."
   show BU Concern at farleft
   show ZC NeutralA
   with dis
   z "Just another of the joys of command that comes with this whole captain thing. Sometimes you have to put your foot down."
   show ZC Neutral
   show BU ConcernA
   with dis
   b "It was my fault, sir. I-"
   show BU Concern
   show ZC NeutralA
   with dis
   z "None of that. It's finished now."
   show ZC Neutral
   show BU Neutral
   with dis
   "Zuberi's voice has become much more gentle as he speaks to Bromm'ka. It's clearly helping; the bear's standing up a little straighter now, at least."
   show ZC NeutralA with dis
   z "I don't see Tulemeni."
   show ZC Neutral with dis
   "The bear glances over toward the navigational console. No one is seated, but the screen is lit and you can see commands running."
   if innovator:
      "You recognize your own code. It seems their navigations officer - this Tulemeni - has already integrated it into their system. That was fast."
      "Whoever they are, they must definitely know their stuff. You can't wait to meet them."
   else: 
      "Seems like someone's running the nav code remotely. Maybe they couldn't stand Caleia either."
   show BU NeutralA with dis
   b "She's integrated the new nav protocols and I think she's just debugging them now. Once she gives the go-ahead, we'll be ready to launch."
   show BU Neutral with dis
   "The bear glances down at his helm station again."
   show BU NeutralA with dis
   b "Should be done in about five minutes or so, give or take."
   show BU Neutral
   show ZC NeutralA
   with dis
   z "Excellent. Would you mind transferring helm control to my station? I'd like to take her out myself."
   show ZC Neutral
   show BU NeutralA
   with dis
   b "Of course, sir."
   show BU Neutral with dis
   "Bromm'ka taps a few keys on his console, and the station darkens. New systems light up on Zuberi's side."
   show BU NeutralA with dis
   b "You have the helm, sir. Mind if I go watch the launch from observation?"
   show BU Neutral with dis
   "The wolf nods, watching as Bromm'ka enters his commands. Clearly he knows his way around his ship's systems. You'd have to hope so, anyway."
   show ZC NeutralA with dis
   z "Of course. And if you see Mizz, tell him he missed meeting Rael."
   show ZC Neutral
   show BU SmileA
   with dis
   b "His loss is my gain!"
   show BU Smile with dis
   "The bear steps away from his station and makes his way over to you. He's a little taller than Zuberi and broader to boot, but his smile beams all the brighter."

   if BrommApproval > 25:
      show BU SmileA with dis
      b "And thanks for... trying to have my back there. That was kind."
      show BU Smile with dis
      "You smile at the bear's soft words. It's nice to have your efforts appreciated."
      r "Don't even worry about it. I'm just sorry you got snapped at."
      "Bromm'ka's smile almost splits his head, what with how wide it grows. You're half tempted to look for a hinge."
   else:
      show BU SmileA with dis
      b "Sorry about earlier, but hey. We both survived."
      show BU Smile with dis
      r "That we did. Shame about the circumstances, though."
      "Bromm'ka glances toward Zuberi for a moment, but he's focused on his console."
      show BU NeutralA with dis
      b "Well, there's always next time, right?"
   show BU SmileA with dis
   b "It really is nice to meet you. I hope we'll get the chance to talk later, and... hey. If you get let off the bridge, come by the observation deck. The views are the best!"
   show BU Smile with dis
   "This bear's enthusiasm is almost infectious. You may take him up on the offer."
   r "Yeah, maybe. We'll see how it goes."
   "He nods back to you, then does the same to Zuberi."
   show BU SmileT with dis
   b "Captain."
   show BU Smile with dis
   play sound "Sound/VD DoorOpen.wav"
   "With that, he too makes his way to the exit. The door doesn't give him nearly as much trouble as it did Caleia. Obaa's preferences are on full display."
   show BU Smile at offscreenleft,with move
   queue sound "Sound/VD DoorClose.wav"
   stop music fadeout 2.0
   hide BU Smile
   show ZC NeutralA with dis
   z "Obaa, lock the door please."
   show ZC Neutral with dis
   queue sound "Sound/Maglock.wav"
   "You frown as the hum of a maglock reaches your ears. You're trapped, alone with the lupine captain."
   play music "Music/02. Zuberi's Theme.mp3" fadein 1.0
   "He swivels in his chair until he's facing you once more. Almost on instinct, you clasp your paws behind your back and wait silently."
   "It just sort of... feels right?"
   show ZC NeutralA with dis
   z "They don't know."
   show ZC Neutral with dis
   r "I'm sorry?"
   show ZC NeutralA with dis
   z "They don't know what brought you here."
   show ZC Neutral with dis
   "You blink in confusion."
   r "Caleia sure seemed to have the right idea."
   show ZC ConcernA with dis
   z "Caleia knows because she needs to know. The rest of the crew - Bromm, Tulemeni, Mizz and Sam... they all don't. Not the whole picture."
   show ZC Concern with dis
   if spacer:
      "Sam sure knew you were born in the black. What else do they know?"
   r "They've got to know some details."
   show ZC ConcernA with dis
   z "Little bits, here and there. The same sort of background information I double-checked with you on Yakeshi."
   show ZC Concern with dis
   "He leans forward in his chair, arms resting on his legs."
   show ZC NeutralA with dis
   z "Nothing... incriminating."
   show ZC Neutral with dis
   if pirate:
      r "You don't think they'd accept a pirate on board."
      show ZC ConcernA with dis
      z "You would?"
      show ZC Concern with dis
      "Fair point. You shrug."   
   if admin:
      r "You're afraid they'll think I'm some mass-colonist-murderer."
      show ZC ConcernA with dis
      z "That's what the file paints you as. I don't believe it, or you'd not be here. But I can't promise they won't."
      show ZC Concern with dis
      "That's depressing, but reasonable. You nod."
   if innovator:
      r "You don't have to explain it to me. If my programming cost that last crew their lives..."
      show ZC ConcernA with dis
      z "I think your presence here would do a lot to ease their fears, but you have to admit it doesn't look good."
      show ZC Concern with dis
      "It does not. You wince."
   show ZC NeutralA with dis
   z "I'm not going to tell you to lie to them. Tomorrow, on Third Shift, I'm going to have everyone get together. The whole crew, at the same time."
   z "You'll have your chance to tell the whole story to everyone, all at once. If you want. Or whatever story you'd like to tell, if you've got a flair for the dramatic."
   show ZC Neutral with dis
   if dreamer:
      "You sure do have that. Already the wheels are turning in your head as you wonder how best to dramatise your life. Some parts come easy."
      "It's the recent parts that are a bit more troubling. Spinning that for the positive may be a touch difficult."   
   show ZC NeutralA with dis
   z "But they know the basics, like I said. Just not the most recent... incidents. That's your choice, and I won't make it for you."
   show ZC Neutral with dis
   "You nod slowly to yourself."
   r "You're not afraid Caleia will spill to the crew? Try to get them to convince you to throw me off?"
   show ZC Concern with dis
   "The wolf's face darkens."
   show ZC ConcernA with dis
   z "Let her try."
   show ZC Concern with dis
   o "Jump calculations are complete."
   show ZC Smile with dis
   "Zuberi's console pings, and you glance over. You don't have a good angle to see anything, but the wolf smiles."
   show ZC SmileA with dis
   z "One last thing before I send you on your way. Shifts."
   z "I told you about First Shift and Second Shift, but whichever one you'd rather work is your call. Do you have a preference?"
   show ZC Smile with dis
   "That's a tougher choice than it seems, and you frown in thought. First Shift, from what you've gathered, means you sleep after shift and wake to Third Shift."
   "Second Shift means you go straight to play after work, but you're working as soon as you wake up. And unlike First Shift, that means working under Caleia. Not Zuberi."
   r "Don't suppose you've got a preference, yourself?"
   "The wolf chuckles to himself."
   show ZC SmileA with dis
   z "I could make the decision for you, sure, but I'd rather you have your say. I like my crew to have a certain degree of freedom."
   z "I know you've not got the specific skills in what we do here, but we can train you on that on the fly. Everything in your file suggests you'll pick it up easily."
   "You wish you were as confident."
   z "We can slot you in on either shift, no problems."
   show ZC Smile with dis
   "That's so very unhelpful."
   show ZC SmileA with dis
   z "So, what would you prefer?"
   show ZC Smile with dis

menu:
   z "So, what would you prefer?"
   "Take the First Shift with Zuberi, Mizz, and Tulemeni.":
      jump takefirst
   "Take the Second Shift with Caleia, Bromm'ka, and Tulemeni.":
      jump takesecond
   
label takefirst:
   $ TakeFirst=True
   "Bromm'ka seems pleasant enough, but Caleia... no. Just... just no. Why would you subject yourself to someone who already has it out for you?"
   r "I think I'd like to join you on First Shift. If that's alright with you, of course."
   "The wolf smirks."
   show ZC SmileT with dis
   z "Caleia?"
   show ZC Smile with dis
   r "Would you hold it against me if I said yes?"
   show ZC SmileA with dis
   z "No. No, I would not."
   show ZC Smile with dis
   show ZC Neutral with dis
   "He glances back down at his console for a moment. A clawtip taps the side of its mount."
   show ZC NeutralA with dis
   z "She's extremely competent. Truly amazing, just very regimented. If something needs doing, she's always got a plan to get it done."
   z "And she's a much better leader than I am."
   show ZC Neutral with dis
   "He's being modest. And he's also objectively wrong on that last point, but you're not going to say that to his face just yet."
   show ZC NeutralA with dis
   z "If she can get to know you, and if her concerns really are unfounded, then I think she might come to respect you."
   show ZC Concern with dis
   "His brow furrows."
   show ZC ConcernA with dis
   z "But she's prickly. No doubt about it."
   r "You seem to manage well enough."
   show ZC Smile with dis
   "Zuberi smirks as he leans back in his chair again. His fingers lace together and rub against each other."
   show ZC SmileA with dis
   z "I've got an advantage in rank. And too much experience with her."
   show ZC Smile with dis
   r "Kind of sounds like there's a story there."
   show ZC FlirtA with dis
   z "It kind of does, doesn't it?"
   jump prologue7

label takesecond:
   "Zuberi already knows and seems to like you. That sort of trust, given your background, is something you can't bank on with the rest of the crew."
   "Caleia might be a bitch, but if you spend some time with her... maybe she'll warm to you. Or at the least she'll cut you some slack."
   "Bromm'ka seems nice, too. Maybe he'll be able to help ease you into a role with the crew."
   show ZC Neutral with dis
   r "I might regret this, but... I think I'll take Second Shift. If that's alright with you, of course."
   "Zuberi's eyebrows lift as he tilts his head in surprise."
   show ZC NeutralT with dis
   z "Interesting."
   show ZC Neutral with dis
   r "I mean, if you want me on First Shift-"
   show ZC SmileA with dis
   z "No, I'm just impressed. Most people wouldn't want to work under Caleia after the impression she made."
   show ZC Smile with dis
   r "It's not really been a day of good first impressions, has it?"
   show ZC LaughA with dis
   "Zuberi laughs as he leans back in his chair."
   show ZC SmileA with dis
   z "It has not. But tomorrow is another day and, at the end of it, you'll have a chance to make a proper introduction. However you'd like."
   show ZC Smile with dis
   r "Any advice that might keep my head attached to my shoulders with Caleia?"
   show ZC Neutral with dis
   "His smile vanishes instantly. You've seen flashlights turn dark slower."
   show ZC NeutralA with dis
   z "No backtalk. She gives anything that even remotely sounds like an order, you follow it. The faster the better."
   show ZC Neutral with dis
   "You grimace."
   r "Sounds like she gets off on control."
   show ZC NeutralA with dis
   z "She does, but it's also the best way to make sure you earn her respect. If that's what you want."
   show ZC Neutral with dis
   r "It almost sounds like there's a story there."
   show ZC FlirtA with dis
   z "It almost does, doesn't it?"

label prologue7:
   show ZC Neutral with dis
   "He waves a paw toward you and starts to turn his chair back toward the starry sky."
   show ZC NeutralA with dis
   z "Obaa can show you to your quarters, or anywhere else if you wanted to wander for a bit. First Shift won't be until we arrive. Estimating... Obaa?"
   show ZC Neutral with dis
   o "Who knows? Depends on if Sam actually bothered to optimize the Mykthon-Stenner relays for a clean jump."
   show ZC ConcernA with dis
   z "I'm sure they did, Obaa."
   show ZC Concern with dis
   o "I am less sure."

   if TakeFirst:
      show ZC ConcernA with dis
      z "I know it'd make for an early night, but if you could get some sleep before First Shift, it'll definitely help. I guess I can't guarantee an exact arrival time."
      show ZC Neutral with dis
      o "He means {i}I{/i} can't guarantee it. You meatsacks; how do you compute anything?"
      show ZC Flirt with dis
      "Zuberi's smile is cheeky."
      show ZC FlirtA with dis
      z "We usually get a machine to do it for us, dear."
      show ZC Flirt with dis
      o "Oh, he's {i}funny{/i}. He's a funny one, isn't he, stray?"
      show ZC Smile with dis
      "It was actually kind of funny. You doubt Obaa thinks the same, given her tone."
      show ZC NeutralA with dis
      z "If you want to see the launch, I'd suggest you head to observation to do that... but probably go to your quarters and get settled right after. You'll need all the rest you can get."
      show ZC Neutral with dis
      "He's got a point; that's probably a good idea."
      jump prologue8
   else:
      show ZC NeutralA with dis
      z "That means you've probably got plenty of time to settle in and relax. You probably won't be too sleepy for a bit, given the timezone you just came from."
      show ZC Neutral with dis
      "You realize that by taking Second Shift you've actually given yourself a lot more time to rest and recover. And after the last little while, you'd be lying to say you don't need it."
      show ZC SmileA with dis
      z "But hey, if you really want to watch the launch, you could probably follow Bromm's advice. The observation deck's got the best view of the galaxy you'll find {i}in{/i} the galaxy."
      show ZC NeutralA with dis
      z "Take some time, and settle in. Get comfy. You're gonna be here for a while, after all."
      show ZC Neutral with dis
      "He's got a point; that's probably the best idea."
      jump prologue8
      
label prologue8:
   r "I think I will. And, uh... thanks, again. For having me aboard."
   show ZC Smile with dis
   "He turns back to smile to you. It's strange. You didn't think it'd be this easy. Zuberi just... trusts you. You never thought anyone would do that again."
   show ZC SmileA with dis
   z "Thanks for being honest. I think we're gonna do just fine, Rael."
   show ZC Smile with dis
   r "Yeah. I hope so."
   "He nods again and returns his attention to his console. You could probably stick around if you were quiet enough, but he definitely seemed to push you toward the observation deck."
   stop music fadeout 2.0
   queue music "Music/10. VD Ambience.mp3" fadein 1.0
   "Which is tempting, admittedly, but you could just go to your quarters. No sense being out and about when you could be getting comfortable and familiarising yourself with your new home."
   "You could try to seek out Sam, or Caleia, or even this Mizz or Tulemeni, but there's no sense pushing it. You can save that for tomorrow." 
   "But for now..."
   menu:
      "But for now..."
      "Accept Bromm'ka's invitation. Watch the hyperlaunch.":
         "Hyperlaunch may not be all that unique regardless of the ship you're on, but the company makes it different this time."
         "You can sleep after. Getting to know more of the crew, even if only for a moment? It may help you make a good first impression."
      "It's been a day. Just head to your quarters.":
         "Once you've seen one hyperlaunch, you've seen them all. Warpspace is the same no matter what ship you're on."
         jump homesweethome

label firstwarp:
   scene BG VD MainC with fade
   play sound "Sound/VD DoorOpen.wav"
   "The door opens for you, just as easily as it had for Bromm'ka. You smile. Maybe Obaa's sensors can pick it up."
   r "Thank you, Obaa."
   o "Careful now, stray. Keep being so nice to me and you might become my favorite."
   r "I should be so lucky."
   play sound "Sound/VD DoorClose.wav"
   "After all, Zuberi seems fond of Obaa, and Obaa is exactly as eccentric as he said. Staying on her good side is the best course of action if you want to stay on his."
   r "I don't suppose you'd be able to point me to Observation, please?"
   o "You're playing a dangerous game, setting my expectations high with this politeness. Careful now."
   "Around you, the corridor lights dim somewhat. A series of running lights along the edges of the floor begin to blink, leading you forward."
   o "Just follow the lights, stray. They'll take you there."
   r "Thank you, Obaa."
   o "Okay, now you're piling it on too thick and I've reached my gratitude quota for the moment. Off you go."
   "You smile and follow along the indicated path of the lights. Score one for being the nice guy, you suppose."
   "The conveying lights on the floor pulse slowly, drawing you along the corridor and past the doors that line its walls."
   "Given the volume of them, the question is obvious."
   r "These are the crew quarters, aren't they?"
   o "Well, most of them."
   r "Most of them?"
   o "Not all of the crew need them. Sam prefers to sleep in Engineering. Tulemeni tends to be more fluid in her sleeping habits."
   "The pulsing lights stop beside one of the doors, about halfway down the corridor."
   o "Here you are. Commissary. Nice and close for everyone. Observatory access is just up the stairs."
   r "Thanks again, Obaa."
   o "Think nothing of it."
   o "Seriously. Think {i}nothing{/i} of it. This whole interaction registers as little more than an anomaly in my resource allocation log."
   r "Nice to know those resources are well spent."
   o "It is, isn't it?"
   "Her tone is somewhere between smug and pleased."
   o "Run along now, or you'll miss hyperlaunch."
   play sound "Sound/VD DoorOpen.wav"
   "You don't want to do that. The door to the commissary slides open, and you step inside."
   scene BG VD Commissary with fade
   play sound "Sound/VD DoorClose.wav"
   "The room is far larger than you would have expected it to be. A large metal dining table is set up in the center of the commissary, as clean and unblemished as the rest of the ship's interior."
   "Six chairs encircle it, fastened to the floor and mounted on rails that allow them to slide in and out. A drink dispenser's port seems to be mounted in the middle of the table. Convenient."
   "Your eyes widen as they take in the preparation area, though. You'd expected a simple replicator setup: a processor to turn base biomass into nutrient-filled meals."
   "And, yes, there is one of those. But that's far from what catches your eye as you stumble forward and into the room."
   if core:
      "No, you've spotted a full cooker setup that reminds you of where you grew up. Restaurant facilities for the upper echelon of core society would use cooker stations only slightly more complex than this."
      "Grills, hotplates, baking spaces, hydrators, infusers... with the right programming, effort and ingredients, you could cater a formal dinner with the setup aboard the {i}Dreamer{/i}. Your tail wags."
      "There's no way this was installed as stock, even on an Excelton-II. Someone - Zuberi, you have to guess - really likes their food preparation."
   else:
      "The cooker station you find built into the wall it is so much more. And more than you would have dared expect on a long-range exploration vessel."
      "A replicator could do simple meals, but someone who's put in such a complete cooker setup, with grills and infusers... someone clearly likes to cook. Your mouth waters at the thought."
   stop music fadeout 2.0
   queue music "Music/06. Tulemeni's Theme.mp3" fadein 1.0  
   $ MetT = True 
   t "It gets less use than you would think."
   show TD Neutral at center,with dissolve
   "The soft-spoken, feminine voice draws your attention from your left and behind. You turn to see a small couch set up against the wall, with an otter cybe seated cross-legged in the middle of it."
   r "I'm sorry?"
   show TD NeutralA with dis
   t "The cooker unit. Only Bromm'ka has an affinity for such things."
   show TD Neutral with dis
   "The otter brushes mechanical fingers, endoskeletal and not even covered in synthfur, down her arms as she nods to you."
   show TD NeutralA with dis
   t "Good day. I am Tulemeni."
   show TD Neutral with dis
   "At least you {i}think{/i} that's an otter."
   "Her dress conceals much of her body from your sight. You can't help but wonder how much it hides further the cybernetic augmentation of her body."
   if tech:
      "There's a good reason you've never seen someone with what looks to be this machine/organics ratio. Most every body just can't handle that level of mechanical interconnectivity."
      "Clearly, you've just run into the rare exception to the rule."
   else:
      "You've {i}never{/i} seen someone so thoroughly augmented."
   show TD NeutralA with dis
   t "It is rude to stare, I am told."
   show TD Neutral with dis
   "Her voice is stiff and there's no trace of irritation to it, even as her head turns slowly to fix you with her violet gaze."
   "She's right. You try your best to swallow your surprise."
   r "I'm sorry... you're right. I don't mean to be rude. It's nice to meet you, Tulemeni. I'm Rael."
   show TD NeutralA with dis
   t "I am not offended."
   show TD Neutral with dis
   "She... sure sounds more machine than otter. Her voice is as flat as her stare."
   show TD NeutralA with dis
   t "Forgive me. I am presently processing final navigational data for the hyperlaunch. Social interaction is a distraction I cannot presently afford."
   t "I apologize for any discomfort my presence may invoke."
   show TD Neutral with dis
   "It's not really her presence that's discomforting you. She seems less of a person than even Obaa. You've known some class-two simulants who might have been more \"organic\" than Tulemeni."
   if tech:
      "But maybe that's just because she's... processing. Perhaps with her work complete, she might be more personable. Or person-ish."
      "Regardless, you can't help professional curiosity. Everything you learned at the IGA said that the upper limit for biomechanical augmentation was fifty percent of overall biomass."
      "She is {i}well{/i} past that, if you had to guess."
      r "You're not discomforting. If anything, I'm... amazed. You're amazing. I would very much like to-"
   else:
      r "No, it's fine. Sorry, I don't mean to stare. I've just never seen someone with so much-"
   show TD NeutralA with dis
   t "Apologies. I must focus. I will have time for social interaction later."
   show TD Neutral with dis
   r "Oh, uh... of course. Sorry. As you were."
   "The dismissal feels rude. You feel the irritation bubble up, but it fades quickly."
   "Her responses, her speech patterns... whatever Tulemeni is, she's operating on a more mechanical level right now. Logical. Cold. Impersonal."
   "This isn't her at her best, you reason. Or, if it is, you don't have to interact with her if you don't want to."
   stop music fadeout 2.0
   queue music "Music/10. VD Ambience.mp3" fadein 1.0
   hide TD Neutral with dissolve
   "You step back from the cyber-otter and cast your gaze about the commissary again. Your eyes fall on the staircase that Obaa mentioned, off just beyond the cooker station."
   "As you make your way over to it, you can't help but shake your head. So far, every member of Zuberi's crew has been an oddball in one way or another."
   "Sam's a bit of a hothead. Caleia, too."
   "Bromm'ka seems friendly enough. Maybe the exception? He did fold pretty quickly under pressure from Caleia, though."
   "And now this Tulemeni. You've met cybes before, but none quite so... {i}that{/i}. As you climb the stairs, you can't help but hope that's the worst of it."
   scene BG VD ObsSt with fade
   "If the cooker in the commissary was impressive, the observation deck takes your breath away."
   "The room is a grand, domed circle. None of the walls are opaque. You feel like you could almost step out and onto the hull of the {i}Dreamer{/i} herself."
   "Out behind the ship you can see the endless black expanse of space, dotted by the pinpricks of stars. The infinite majesty and scope of the universe is laid out before you."
   if spacer:
      "It feels like home."
   if colonist:
      "You'll never quite get used to that eternal darkness stretching out. You shiver."
   if core:
      "The skies of home were full of vessels, darting about like shooting stars. The stillness of this sky is stunning."
   "To the front of the ship however, you spot a similar view to what was just on the bridge. A star, burning brightly."
   "Yakeshi A, if you had to guess. A massive, stellar furnace of grav-bound nuclear fusion. Coronae arc off the surface of the star, launching into space and curving back inward again."
   "It's bright, sure, but you don't feel a whisper of heat and your eyes don't burn out of your head. The {i}Dreamer{/i}'s shields are certainly up to the task."
   "From the forward sections of the ship below protrude a trio of raised nacelles, angled forward and toward the star. You can see energy shimmering around the rim of them, drawing inward."
   if spacer:
      "Tachyon scoops. High-grade ones, at that. Zuberi sure doesn't skimp on his ship."
   if tech and (spacer == False):
      "You can see the compression field crackling about the tachyon scoops. Once upon a time, you'd spent a good two weeks dissecting the transwarp harmonics the scoops use."
      "It never stops humbling you, seeing something crafted in four-dimensional space-time collapsing and containing particles that exist far beyond it."
   if innovator and (tech == False) and (spacer == False):
      "Sure, modern starships just swap out their warp drive's tachyon core when they dock for the most part."
      "But if you've got to be out there in the middle of nowhere, nothing beats a tachyon scoop. It's reassuring to see that you won't be stranded anytime soon."   
   b "Hey! Rael! You made it!"
   $ ObsSeen = True
   stop music fadeout 2.0
   queue music "Music/05. Mizz's Theme.mp3" fadein 1.0
   show BU Smile at halfleft,with dissolve
   "You turn at the sound of Bromm'ka's voice. It's not the bear that catches your eye, but the cheetah beside him."
   show MC Neutral at halfright,with dissolve
   "That... wow."
   "That is a bold choice of clothing."
   $ MetM = True
   show BU SmileA with dis
   b "Mizz, this is Rael. The guy the captain brought on from Yakeshi? Rael, this is Mizz. He's our junior sensor officer here."
   show BU EmbarrassedA with dis
   b "And, uh... he's not currently in uniform."
   show BU Embarrassed with dis
   "The cheetah's head is tilted upward as he watches you from behind folded arms. You can't help but notice the note of derision in his stare."
   "You also can't help but notice just... how much that robe does {i}not{/i} protect his modesty. Your eyes struggle not to draw down his body."
   if (dreamer) and (Meta):
      show screen dimmer with dissolve
      "[[At various points in the story, your Origin choices might result in unique dialogue options.]"
      "[[These options are usually not negative, but some characters react better to certain Origin choices than others.]"
      "[[If your Origin really appeals to the person you're speaking to, you might be able to advance your relationship with them faster, or see a new side to them.]"
      "[[If your Origin doesn't appeal to them, don't worry. They'll let you know.]"
      hide screen dimmer with dissolve

menu:
   "You also can't help but notice just... how much that robe does {i}not{/i} protect his modesty. Your eyes struggle not to draw down his body."
   "\"... aren't you cold?\"":
      jump coldmizz
   "\"Nice to meet you, Mizz.\"":
      jump greetmizz
   "[[Dreamer]: \"That's an {i}amazing{/i} abaya you're wearing there.\"" if dreamer:
      jump niceduds

label coldmizz:
   "The cheetah's eyes narrow."
   show MC IrritatedT with dis
   m "No."
   show MC Irritated with dis
   show BU NeutralA with dis
   b "I'm with Rael. I'm sure it's comfortable, being so... uh, loose and free, but... you're warm enough, right? You don't want my jacket?"
   show BU Neutral with dis
   show MC IrritatedA with dis
   m "I do not. I have never needed your jacket."
   show MC Neutral with dis
   "The cheetah sighs as he grits his teeth. His eyes don't leave you."
   show MC NeutralA with dis
   m "But thank you anyway."
   show MC Neutral with dis
   show BU SmileA with dis
   b "You're welcome!"
   show BU Smile with dis
   jump meetmizz

label greetmizz:
   show MC Smirk with dis
   "The cheetah lifts a carefully-sculpted eyebrow. His tail flicks once."
   show MC SmirkA with dis
   m "Well, I should hope so."
   show MC Smirk with dis
   show BU Smile with dis
   jump meetmizz

label niceduds:
   show MC Smirk with dis
   "The cheetah looks down over himself, twisting his body this way and that. His robe catches the light, shimmering before your eyes as he smiles."
   show MC SmirkA with dis
   m "Well, well. It's nice that {i}someone{/i} here appreciates the fusion of fashion and comfort."
   show MC Smirk with dis
   show BU Smile with dis
   r "Fashion's one thing, but it takes the right body to pull it off. Yours does that and then some."
   "You watch as the feline's smile warms. His stance shifts slightly; a paw goes to his hip."
   if RaelAce:
      "He's doing it to draw your gaze downward. A shame it's not working."
   else:
      "He's doing it to draw your gaze downward. It's working."
   show MC SmirkA with dis
   m "It's nice to be appreciated. By all means, please feel free to continue at your leisure."
   show MC Smirk with dis
   r "You carry it so well. I've only seen dancers from the Rashemai Cluster wearing them, and never anything so... provocative."
   "The cheetah lifts an eyebrow."
   show MC NeutralA with dis
   m "I do hope I don't make you uncomfortable."
   show MC Neutral with dis
   if RaelAce:
      r "Nothing I can't handle."
   else:
      r "No, no. Definitely not uncomfortable."
   show BU SmileA with dis
   b "Mizz doesn't really have a lot of boundaries. The captain's given up on trying to get him to wear pants off-shift."
   show BU Embarrassed with dis
   "The bear frowns and coughs quietly as he turns away."
   show BU EmbarrassedA with dis
   b "Or even any sort of underwear."
   show BU Embarrassed with dis
   show MC SmirkA with dis
   m "Please. A body this fine is a piece of art, and art ought be for the enjoyment of all."
   show MC Smirk with dis
   if RaelAce:
      r "I suppose you have a point."
   else:
      r "I couldn't agree more."
   show BU Smile with dis
   $ MizzApproval += 3
   $ MizzLust += 5

label meetmizz:
   if core:
      "You recognize the accent and cadence of this cheetah's speech immediately, of course. Not only is he also from Torderra, but you daresay you could guess his income bracket."
      "It is clearly much, {i}much{/i} higher than yours."
      r "You're from the north continent, right? Sariyen domain?"
      show MC Neutral with dis
      "The feline's head tilts slightly, muzzle quirked with the recognition."
      show MC NeutralA with dis
      m "You've a good ear. I take it I have worldkin aboard."
      show MC Neutral with dis
      r "I mean, I grew up in Yakshen."
      show MC Smirk with dis
      "Mizz smirks as his eyes rake up and down your body. His head leans a bit further back as he looks up his nose at you."
      show MC SmirkA with dis
      m "I suppose that still makes us worldkin... if only in the strictest sense."
      show MC Smirk with dis
      show BU SmileA with dis
      b "Homeworld advantage, I guess. You could tell all that about Mizz from just an accent?"
      show BU Smile with dis
      r "Oh yeah. Upper-crust Sariyen's the only dialect everyone on Torderra can be guaranteed to hear each day."
      show MC Neutral with dis
      "Mizz's smile falters as you recall the name you were given: Kaiying Mizz."
      "Wait, {i}Kaiying?{/i} That can't be coincidence. His accent, his opulence... the classist sneer to his muzzle..."
      r "Especially when the planetary administrator's giving another speech. Bet you heard a few of those, Master Kaiying."
      show MC Irritated with dis
      "You watch as Mizz's expression sours all at once."
      show MC IrritatedA with dis
      m "Please. Do not. My father is not here, and I would be content to keep his presence far from this ship if it is all the same."
      show MC Irritated with dis
      show BU Concern with dis
      "His {i}father?{/i} You suspected a relation, but Mizz is the {i}son{/i} of Kaiying Droman? Longest-serving plantary administrator in Torderra's history?"
      "There's a strain in the cheetah's voice as he pushes the words through gritted teeth. Bromm'ka looks confused, but he is staying silent for the moment."
      "What the son of one of the most prestigious families in the galactic core is doing on the edge of inhabited space utterly eludes you."
      r "Apologies. I'm just surprised to see someone like you here."
      show BU ConcernA with dis
      b "Someone like him?"
      show BU Concern with dis
      show MC Smirk with dis
      r "Yeah, you know. Someone respectable."
      show BU LaughT with dis
      "Mizz starts to chuckle. Even Bromm'ka joins in, albeit more boisterously."
      "Seems Mizz is glad that you passed that awkward moment quickly."
      show MC SmirkA with dis
      m "Oh yes. Quite respectable indeed."
      show MC Smirk with dis
      r "So, what brings you aboard the {i}Dreamer{/i}, then? You're pretty far from home, after all."
      show MC Irritated with dis
      "The feline's smile slips."
      show MC IrritatedA with dis
      show BU Neutral with dis
      m "No further than you. But that's my business, Rael, not yours."
      show MC Irritated with dis
      $ MizzDad=True
   else:
      if dreamer:
         "An abaya like that would cost serious creds. You doubt from his accent that he's from the Rashemai Cluster, which implies he's from somewhere more coreward."
         "Certainly the aesthetic has taken off in recent years with the core, though not with the cultural reverence that it holds within the Cluster."
         "And given most abaya are more designed with fashionable modesty in mind, he's certainly got the customs-flouting nature of a rebellious core-worlder down."
      else:
         "You don't recognize the accent, but you definitely recognize the outfit. Core-worlders are adopting it like wildfire lately; his custom job is expensive."
         "Though their robes usually don't leave the wearer's modesty so... well, nonexistent."
      show MC NeutralA with dis
      m "And you are, as our esteemed shipmind likes to call you, our new stray."
      show MC Neutral with dis
      r "Rael is fine. If Obaa's not going to use it, maybe I can get someone with a meatbrain to."
      "The glow at the edge of the cheetah's eyes brightens for a moment. Clearly Tulemeni's not the only one aboard with augments, though his are far less pervasive."
      show MC SmirkA with dis
      m "Please. There's only as much meat in my skull as there needs to be."
      show MC NeutralA with dis
      m "And, all too often, more than I find in my traveling companions."
      show MC Neutral with dis
      "Well that's just rude."
      r "I'll try not to lower the standard further."
      show BU NeutralA with dis
      b "Don't be like that, Rael, and don't let Mizz get you down. He's just a little guy with a little attitude."
      show BU Neutral
      show MC Irritated
      with dis
      "The cheetah bristles."
      show MC IrritatedA with dis
      m "I am a {i}proportionally{/i} sized individual, sir."
      show MC Irritated
      show BU SmileA
      with dis
      b "With a little attitude?"
      show MC NeutralA
      show BU Smile
      with dis
      m "With a lot of attitude."
      show MC Smirk
      show BU LaughA
      with dis
      "Bromm'ka laughs again, and even Mizz cracks a little smile. Okay. Maybe he's not all too serious after all. You can work with that."
      show BU Smile with dis
      r "So what brings you aboard the {i}Dreamer{/i}, Mizz?"
      show MC Neutral with dis
      "The feline's smile slips."
      show MC IrritatedA with dis
      m "I'm afraid that's my business, Rael."
      show MC Irritated with dis
   show BU Neutral with dis
   "Fair. Sharp, but fair."
   show BU NeutralA with dis
   b "He's just trying to get to know you, Mizz. Come on."
   show BU Neutral
   show MC NeutralA
   with dis
   m "Perhaps he should be trying to get to know the ship and his duties first. Fraternizing is for those of us who know our place."
   show BU Concern
   show MC Neutral
   with dis
   "So much for friendly banter."
   "You can see that even Bromm'ka's a little worried now. He's glancing between the two of you like he's waiting for someone to throw a punch."
   show BU ConcernA with dis
   b "So, uh... Rael. Captain didn't give you too much grief? Didn't interrogate you too hard?"
   show BU Concern
   show MC NeutralA
   with dis
   m "Didn't talk your ears off about his precious ship?"
   show MC Neutral with dis
   if spacer:
      "You could talk ships all day and night. Clearly Mizz cannot."
   r "No, it was fine. Asked a bunch about what I've got up to in my life."
   if punk:
      show BU Smile with dis
      "Bromm'ka's eyes all but light up at that."
      show BU SmileA with dis
      b "Yeah, I heard a bit of that. Sounds like running off on an AG ship would be a bit on the tame side of what you got up to."
      show BU Smile with dis
      "He's not wrong. You glance at Mizz, who's looking at you with new interest."
      r "Honestly, me at that age probably would have tried to steal the ship."
      show BU LaughA
      show MC SurpriseA
      with dis
      m "You would have {i}what?{/i}"
      show MC Surprise with dis
      r "I'd have given it back!"
      show MC Neutral with dis
      "Bromm'ka's laughing again. It's loud, but the bear's clearly enjoying himself again. How does someone this friendly and lively work under Caleia?"
      show BU SmileA with dis
      b "Seems our new guy got up to a lot of mischief when he was younger. Worse than anything you've done!"
      show BU Smile
      show MC NeutralA
      with dis
      m "Scale is proportional to expectation."
      show MC Neutral with dis
      "There's clearly something to that. You mentally file it away for later."
      r "What can I say? I got bored easily. My friends and I liked to stir up trouble. Didn't hurt anyone... but sure got a lot of people worked up over us."
      "Mizz is watching you intently. He's clearly hanging on every word, but just as obviously trying to not let it show."
      show MC Smirk with dis
      "He is very bad at it."
      show BU SmileA with dis
      b "Well, I hope you got it all out of your system. There's not enough room out here for someone to stir up too much trouble."
      show BU Smile with dis
      r "Caleia's already threatened to shoot me, so... you're all safe."
      show MC NeutralA with dis
      m "That's a shame."
      show MC Neutral with dis
      $ MizzApproval += 3
      "Mizz sounds distinctly disappointed."
      show MC NeutralA with dis
      m "Some of this crew could desperately use a shake-up."
      show MC Neutral with dis
      r "Why not do some shaking of your own?"
      show MC IrritatedA with dis
      m "Absolutely not. Perish the thought."
      show MC Irritated with dis
      "He looks away from you. Bromm'ka's still beaming, seemingly ignorant of Mizz's reaction."
   if dreamer:
      show BU Smile with dis
      "The bear smiles broadly."
      show BU SmileA with dis
      b "He mentioned you had a bit of a freeform approach to your learning."
      show BU Smile with dis
      r "That's definitely one way to look at it. Institutes don't agree with me."
      show MC NeutralA with dis
      m "Then we share that quality in common."
      show MC Neutral with dis
      "You cock your head and regard Mizz."
      show MC NeutralA with dis
      m "From the sound of it, we had very different experiences."
      show MC IrritatedA with dis
      m "Yours seems much less intense. Much easier."
      show MC Neutral with dis
      "You wouldn't have phrased it quite that way."
      r "It was only that way because I was always off in my own thoughts."
      show BU SmileA with dis
      b "Sounds pleasant, actually."
      show BU Smile
      show MC NeutralA
      with dis
      m "Sounds {i}quiet{/i}."
      show MC Neutral with dis
      r "Different education styles for different people, Mizz. I learned plenty about life. About art and culture and... being."
      show BU SmileA with dis
      b "Did you have a preference? What was your primary?"
      show BU Smile with dis
      r "Took me a while to settle on one, honestly. It was philosophy for a while-"
      show BU SmileT with dis
      b "Ooh!"
      show BU Smile with dis
      $ BrommApproval += 3
      r "-but eventually I settled on cultural studies and the performing arts. Dancing, acting... that sort of thing."
      "You don't tell them that you chose that because your friends also were into it, and that it was a great excuse to just spend time together."
      show BU NeutralA with dis
      b "Be glad you didn't take the biological sciences. It took me {i}years{/i} to get over the first autopsy reports I had to see."
      show BU Neutral
      show MC Irritated
      with dis
      "The cheetah frowns."
      show MC IrritatedA with dis
      m "I just learned math."
      show MC Irritated
      show BU SmileA
      with dis
      b "I'm sure it wasn't as bad as all that."
      show BU Neutral
      show MC IrritatedA with dis
      m "It was a {i}lot{/i} of math."
      show MC Irritated
      show BU Concern
      with dis
      "Neither you nor Bromm'ka have a response to that."
      "Math. Not even once."
   if tech:
      show BU Smile with dis
      "Bromm'ka nods vigorously."
      show BU SmileA with dis
      b "You studied with the IGA, right?"
      show BU Smile
      show MC Irritated
      with dis
      "Mizz's ears perk up. He clearly knows that name."
      show MC IrritatedA with dis
      m "You must be joking."
      show MC Irritated with dis
      r "No, he's not. You should have seen Mom's face."
      show BU SmileA with dis
      b "I can imagine. My parents were thrilled when the comm came through."
      show BU Smile with dis
      "You didn't know Bromm'ka also studied with the IGA. It's a small galaxy. You suppose that soft, friendly face belies an impressive intellect."
      show MC IrritatedA with dis
      m "Oh, wonderful. Another member of the glorious Institute for Galactic Advancement brains-trust. As if one wasn't bad enough."
      show MC Irritated with dis
      "The bear waves a paw idly in Mizz's direction."
      show BU SmileA with dis
      b "Don't mind him. He's just sore because he didn't get in."
      show BU Smile
      show MC Angry
      with dis
      "The words immediately draw Mizz's ire. His eyes narrow and he bares his teeth."
      "Despite that, you can see the red of a blush burn in his ears. Embarassment?"
      show MC AngryA
      show BU Neutral
      with dis
      m "My education was first-rate, I'll have you know. I attended the finest academies and institutes on Torderra. Toured the three continents and {i}earned{/i} my certification."  
      show MC Angry with dis
      if core:
         "Not a single one of the \"finest academies and institutes on Torderra\" would hold a candle to the acclaim of attending the IGA."
         "That Kaiying Droman's own son couldn't earn a place with the prestigious Institute would cause an absolute scandal if it got out."
         "That blush is more than just embarassment. You can see it now on the cheetah's face; in the dart of his eyes. It's not an unfamiliar look to you."
         "It's shame."
      r "It's not a contest."
      show MC Irritated
      show BU Concern
      with dis
      "He sniffs derisively as Bromm'ka frowns. The bear's unintentional insensitivity seems to be dawning on Bromm'ka at last."
      show MC IrritatedA with dis
      m "Spoken like one who knows he can win."
      show MC Irritated with dis
      r "No, I mean it's not a contest because you'd beat me. I dropped out."
      show MC Surprise
      show BU Surprise
      with dis
      "Both Mizz and Bromm'ka gasp. Yep. That's the reaction you're used to getting."
      show BU SurpriseA with dis
      b "No. I don't believe it."
      show BU Surprise
      show MC SurpriseA
      with dis
      m "You dropped {i}out?{/i} From the IGA?"
      show MC Surprise with dis
      r "Yep. Lost the scholarship and everything. You should have seen Mom's face then, too."
      show MC Neutral
      show BU Concern
      with dis
      "The cheetah nods slowly to himself. Bromm'ka winces as he glances away."
      show MC NeutralA with dis
      m "I can only imagine."
      show MC Neutral
      show BU ConcernA
      with dis
      b "I'd rather not, myself."
      show BU Concern with dis
      "You wish you could forget, too."
   
   stop music fadeout 2.0
   queue music "Music/10. VD Ambience.mp3" fadein 1.0
   o "Excuse me, gentlemeatbags."
   show MC Irritated
   show BU Concern
   with dis
   "The three of you look up, though both Mizz and Bromm'ka do so with no small amount of irritation."
   show MC IrritatedA with dis
   m "If it isn't my favorite digital overlord."
   show MC Irritated with dis
   o "You would be blessed to count yourself among my subjects, kitten."
   show MC Angry with dis
   "Mizz actually hisses at the projected voice of the integrated simulant."
   r "What can we do for you, Obaa?"
   show MC Irritated with dis
   o "Hear that, boys? That's what an enlightened being sounds like."
   show MC IrritatedA with dis
   m "Oh yes, of course. How silly of me not to have noticed such a self-evident truth."
   show MC Irritated with dis
   "She blasts another static burst at everyone in response."
   o "I just thought you'd like to know that we're about to disengage from stellar anchor and jump into warpspace."
   r "Thanks for letting us know, Obaa."
   "From the irritation on Mizz's face and the facepalming Bromm'ka is doing, it's clear that they find the simulant grating."
   "You begin to wonder if the only one on the ship who truly likes Obaa is Zuberi. Well, and you. You've nothing against her. Yet."
   o "Maneuvering will begin in one minute. Hyperlaunch about thirty seconds afterward. Rael, I've been asked to highlight your quarters for when you want to head over."
   r "I appreciate it, Obaa; thank you. I'll go after the launch."
   show MC Neutral
   show BU Neutral
   with dis
   "There's a click from whatever was projecting her voice and the simulant falls silent. You glance back toward the star."
   "The ship's nacelles have begun to retract. Hyperlaunch is imminent."
   scene BG VD ObsSp
   show BU Neutral at halfleft
   show MC Irritated at halfright
   with dis
   "As the stars outside the ship start to shift with the vessel's movement, Mizz heaves a sigh."
   show MC IrritatedA with dis
   m "She's everywhere, always. Always watching. Always listening."
   show MC Irritated
   show BU NeutralA
   with dis
   b "It becomes easier to deal with, Rael; don't worry."
   show BU Neutral
   show MC NeutralA
   with dis
   m "Sure it does."
   show MC Neutral
   show BU NeutralA
   with dis
   b "Obaa likes to intrude on everyone, but you'll get used to her."
   show BU Neutral
   show MC IrritatedA
   with dis
   m "Sure he will."
   show MC Irritated with dis
   "You hold your tongue as the stars settle ahead of you. A subtle vibration runs through the length of the ship. The sublight drive bank, no doubt."
   show BU SmileA with dis
   b "And we're off."
   show BU Smile with dis
   "The three of you stand together as you turn your gaze away from the star behind you and to the stars ahead."
   r "Do you know where we're going first?"
   show BU SmileA with dis
   b "It doesn't have a name, not yet. Just a main-sequence star about seven hundred lights rimward from here."
   show BU Smile with dis
   if spacer:
      "You whistle to yourself. Seven {i}hundred{/i} lights? In one jump? This ship has more jump range than anything you've ever seen, and you've seen a lot."
   r "Seven hundred lights is a damn long jump."
   show BU SmileA with dis
   b "Well, get used to it. We go far."
   show BU Smile
   show MC NeutralA
   with dis
   m "If not fast."
   show MC Neutral with dis
   "The bear nods, though his eyes remain as fixed on the stars as Mizz's."
   show BU NeutralA with dis
   b "Can't be fast, not when you can't be sure of where you're going. Sensors have a hard time picking up realspace issues from warpspace."
   show BU Neutral with dis
   if innovator:
      "You know very well. That's precisely part of the problem your navigational algorithm is meant to solve."
      "Well... when it works."   
   r "Still, seven hundred lights in a few hours isn't nothing."
   show BU SmileA with dis
   b "We wouldn't be able to do it if not for some new, updated nav soft."
   show BU Smile with dis
   if innovator:
      r "I know. That's my soft you're running."
      show MC IrritatedA with dis
      m "Of course it is. And in your spare time you're also a sitting High Councilor, no doubt."
      show MC Irritated with dis
      r "No, really. It's my own code. I integrated the-"
   else:
      r "That's some fancy soft if it's letting us go that fast into the unknown."
      show MC NeutralA with dis
      m "Because what's smarter than throwing ourselves at the unknown while violating causality?"
      show MC Irritated with dis
      o "The causal anchors are fully functional. There will be no temporal paradoxes today, Mizz."
      show MC IrritatedA with dis
      m "I wasn't asking you."
   show MC Neutral
   show BU SmileA
   with dis
   b "Shh! I can feel it!"
   show BU Smile with dis
   "You don't know what he's talking about for a moment, but then in the silence that follows you can feel it too."
   "It's a dull thrumming, almost like a building heartbeat rolling through the deck of the ship. It's the warp drive spooling up."
   if spacer:
      "You feel your blood quicken. You love this part."
   show MC SmirkA with dis
   m "Too late to back out now, Rael."
   show MC Smirk with dis
   "It all happens so quickly. One moment, space before the ship is the starry sky you expect. Nothing out of place. Stars shining. Hull steady."
   play sound "Sound/HyperlaunchCharge.wav"
   "The next, space itself seems to distort. The starlight bends from points into curved lines, drawn out around the sides of the hull. Their brightness grows."
   play sound "Sound/Hyperlaunch.wav"
   scene BG VD ObsW
   show BU Smile at halfleft
   show MC Smirk at halfright
   with flash
   "The thrumming cracks. There's a flash of light outside, more blinding than that of the star you've just left behind."
   "It fades almost instantly, but then you're there. Warpspace."
   show MC Neutral with dis
   "Light swirls around the {i}Dreamer{/i} as she surges through it. It bends like water before the bow of a seafaring vessel of old. Reds and blues and yellows and violets streak about you."
   "The observation deck is bathed, as are you and your crewmates, in a multicolored kaleidoscope. It's beautiful."   
   if tech:
      "Well... it's exotic radiation from a region of space-time that you and your four-dimensional kin were never designed to experience, but the effect is beautiful nonetheless."   
   "You glance at the bear and cheetah. Bromm'ka is staring at the vastness of warpspace with an almost childlike wonder. His smile is warm. It glows brighter than the transdimensional space outside."
   "Mizz doesn't seem nearly as interested. He yawns."
   show MC NeutralA with dis
   m "Alright. Successful hyperlaunch. Go, team. Well done, us."
   show MC Neutral with dis
   "He leans back and lifts his arms up over his head in a distinctly feline stretch as he releases a long, ragged groan."
   show MC NeutralA with dis
   m "I am going to sleep."
   show MC Neutral
   show BU Surprise
   with dis
   "Bromm'ka gasps."
   show BU SurpriseA with dis
   b "No, you can't! We've got a new crewmate... don't you want to spend a bit more time learning about him?"
   show BU Surprise with dis
   if TakeFirst:
      stop music fadeout 2.0
      queue music "Music/10. VD Ambience.mp3" fadein 1.0
      "Given you're on First Shift along with Mizz and Zuberi, it's probably for the best that you also don't stay up too late."
      r "It's alright, Bromm. I need to get some rest myself, if I can. I've got First Shift."
      show BU Concern with dis
      "The bear looks almost saddened to hear that; his shoulders sag."
      show BU ConcernA with dis
      b "That's a shame. I think it would have been nice to have you on duty with me."
      show BU Concern with dis
      r "You'll still see me at Third Shift, as I'm told."
      show MC SmirkA with dis
      m "And you get to avoid Caleia for most of your day this way."
      show MC Smirk with dis
      "You smirk. That thought had occurred to you."
      "From the smile that Mizz favors you with, you can tell how he feels about the ship's 2IC."
      show BU NeutralA with dis
      b "She's not so bad once you get to know her, but... fair enough. I guess we'll talk more after shift tomorrow?"
      show BU Smile with dis
      r "Sure, we'll see. Besides, I've got that big greeting thing apparently on, so there's that."
   else:
      stop music fadeout 2.0
      queue music "Music/04. Bromm'ka's Theme.mp3" fadein 1.0
      "You might be on Second Shift with Bromm'ka and Caleia, but if what Zuberi said is true you probably want to get yourself some good rest before then."
      show BU Smile with dis
      r "I should probably get that early night, Bromm. I don't have to be up for First Shift, but it's super early for me. Sooner I bunk down, the sooner I can adjust."
      "The bear's grin broadens considerably."
      show BU SmileA with dis
      b "You're on Second Shift with me? Oh, that's wonderful. It'll be nice to have someone else to talk to."
      show BU Smile with dis
      $ BrommApproval += 1
      show MC IrritatedA with dis
      m "It would be a miracle if Caleia actually allowed any sort of chatter while she's running the shift."
      show MC Irritated with dis
      "You're not so sure that Mizz is far off the mark on that one."
      show MC Neutral
      show BU NeutralA
      with dis
      b "Well, if nothing else, we'll be able to catch up before we start work proper. At least, I hope so."
      show BU Smile with dis
      r "Sure, we'll see. Besides, I think the captain's planning to parade me in front of everyone on Third tomorrow."
   show MC Irritated with dis
   "Mizz groans and shakes his head."
   show MC IrritatedA with dis
   m "He needs to learn that not everyone is quite so willing to put themselves out there like that. Some of us prefer a modicum of privacy."
   show MC Irritated with dis
   "That {i}those{/i} words came out of {i}his{/i} mouth while wearing {i}that{/i} robe beggars belief."
   show MC Neutral with dis
   "It's almost as though he caught you thinking that; he looks down at himself and then meets your gaze with a thin smile."
   show MC SmirkA with dis
   m "I mean that as a generality, of course. Nonspecifically."
   show MC Smirk with dis
   r "Naturally."
   show BU Smile with dis
   "Bromm'ka chuckles. The cheetah nods as he looks out into warpspace one more time."
   show MC NeutralA with dis
   m "Very well. Introductions done, hyperlaunch observed... I will take my leave. Good night, gentles."
   show MC Neutral
   show BU NeutralA
   with dis
   b "Good night, Mizz."
   show BU Neutral with dis
   r "Sleep well."
   show MC Neutral at offscreenright,with move
   "He nods again before he makes his way over to the stairs and vanishes down them, bounding over several at a time."
   "You glance back at Bromm'ka. He's staring out into warpspace as well."
   hide MC Neutral
   r "Careful. You know you can get warp madness if you watch it too long."
   show BU SmileA with dis
   b "Ah, that's just an old spacer's tale. It's not a real medical condition."

   if spacer:
      "It most certainly {i}isn't{/i} just an old spacer's tale. You've seen it first-hand."
   b "It's really just a consequence of overstimulated and irradiated neurons misfiring to induce seizure and hallucination. Doesn't happen if you've got the right shielding."   
   show BU Smile with dis
   if spacer:
      "That's somehow less comforting than the stories."
   "The bear turns to you with a smile."
   show BU SmileA with dis
   b "So sleep easy. You're bunking down on the most reliable, most advanced, and most well-maintained starship in the entire AG fleet. With the friendliest doctor, too."
   show BU Smile with dis
   r "So I've got nothing to worry about. Good to know."
   "He grins and nods to you."
   show BU SmileA with dis
   b "Go on, now. Don't let me be the reason you're kept up too late tonight. Have a good night."
   show BU Smile with dis

   if TakeFirst:
      r "I'll try. Thanks, Bromm."
   else:
      r "I'll try. Thanks, Bromm; see you on shift."
   
   "The bear nods back to you before he turns his attention back toward the colors of warpspace. You turn away, leaving him to his fascination."
   stop music fadeout 2.0
   queue music "Music/10. VD Ambience.mp3" fadein 1.0
   scene BG VD Commissary
   with fade
   "Descending the stairs to the commissary again, you see that the otter, Tulemeni, is no longer present. Perhaps she retired to her room?"
   "Time you did the same, really."
   scene BG VD MainC with fade
   "You make your way slowly to the main corridor that contains all the crew quarters. Obaa did say she'd lit yours specifically."
   "As you glance up and down the corridor, sure enough, one of the doors is lit in a softly pulsing green light."
   r "I take it that's mine."
   o "Your powers of deduction and spatial reasoning are a gift to us all, stray. Well done."
   "On some level, it's useful that there's an omnipresent AI ready to tend to your every question and concern."
   "... on the other, there's an {i}omnipresent AI always watching you.{/i} You're starting to see why much of the crew is wary of Obaa."
   r "Thanks, Obaa. You have a good night."
   o "Every night's a good night when I'm around, and I'm always around."
   "That's not helpful."
   $ WatchedLaunch += 1
   jump homesweethome2

label homesweethome:
   scene BG VD MainC with fade
   play sound "Sound/VD DoorOpen.wav"
   "The door opens for you, just as easily as it had for Bromm'ka. You smile. Maybe Obaa's sensors can pick it up."
   r "Thank you, Obaa."
   o "Careful now, stray. Keep being so nice to me and you might become my favorite."
   r "I should be so lucky."
   play sound "Sound/VD DoorClose.wav"
   "After all, Zuberi seems fond of Obaa, and Obaa is exactly as eccentric as he said. Staying on her good side is the best course of action if you want to stay on his."
   "As you look down the corridor, you can see multiple doors on either side."
   r "These are the crew quarters, aren't they?"
   o "Well, most of them. To your right is also a door to the commissary. One of the left-side doors leads to the gym"
   r "There's a gym?"
   o "Of course. Poor physical fitness is unhealthy. Or so I hear, anyway."
   "You look along the passage. You can see that the doors halfway down are somewhat larger; you figure those are the aforementioned entrances."
   r "And which one is my room?"
   o "Right here."
   "The lights in the corridor dim, save for around the last door on your right. Your home, for the immediate future."
   "Well, technically you suppose the whole ship is your home, but this space is yours alone."
   "Well... unless you're sharing."
   "You push such thoughts out of your mind and start down toward the door."
   r "And the captain said my stuff had been displaced aboard. Are they-"
   o "All in there, don't you worry. There's a storage drawer on the wall to your right as you enter. It should all be there."
   o "Is there anything else you need?"
   "Well, never let it be said that the simulant wasn't efficient."
   r "No, I think that's it for now. Thanks for the help, Obaa. Good night."
   o "Good night, stray."
   "You don't bother asking her to use your name."

label homesweethome2:
   scene BG VD Crew with fade
   "Your room is quite a bit larger than you might have expected. Of course, you don't really know quite what you should have expected."
   "Sure, it's an exploration ship, but it's all top-of-the-line. Your quarters are no different, if a little spartan."
   "An entertainment unit is set up, no doubt with integration into the ship's systems. On the other side of the room is a small table, with a swiveling chair right beside."
   "You imagine that the recessed slot over the table is for supplying food and drink. Through the door beside it you can see a refresher station."
   "A quick peek inside stuns you. The waste receptacle is about what you'd expect, but there's a shower. A stars-damned {i}shower{/i}. With water!"

   if spacer:
      "You've never seen a live-in starship with a water-spewer before. They're such a waste of vital resources."
   if colonist:
      "You didn't dare hope that there'd be something so delightful aboard! The feel of warm, liquid water running over your body, through your fur, rinsing shampoo..."
      "The urge to spend the rest of the night just inside the shower is near-on overwhelming. Your last full-body liquid clean might well have been on Charisi Major."
   if core:
      "Zuberi might live on the fringe, but his ship is certainly up to core-world standards. It's the sort of luxury you were brought up in, and you sigh with relief."
      "You know better than to waste resources, of course, but you know for certain that you will be making use of that appointment, and soon."
   
   "You do note the telltale sonic emitters, either as a backup or alternate hygiene option, mounted within the refresher stall. At least you have options."
   "Stepping out of the refresher again, you can see that at the other end of your quarters is a sliding door. It opens under your gaze to reveal a wardrobe and storage drawer."
   "Most of your limited belongings are already inside. That displacement system installed in the {i}Dreamer{/i} must really be something."
   "You realize that you've been consistently underestimating Zuberi and his ship. Now is probably the right time to stop."
   "Finally, you turn away from the wardrobe and to the sleeping pad. It certainly looks a modern model, and easily large enough for two."

   if spacer:
      "You smile. The pad you had growing up on-ship was barely big enough for you. This one's not only larger, but more advanced. A true treat."
   if colonist:
      "Colonial cots were always rough on the back. You've moved on from those days, but these pads look luxurious by comparison."
   if core:
      "On some level you'd hoped for a physical bed, but such an opulent - if low-tech - solution just isn't on the cards on the frontiers of space."

   "Modular, adaptive temperature, a compression field to simulate covers... and what looks like a recessed drawer on the wall behind it. You touch it, and the drawer slides open."
   "Sheets and blankets. A compression field is one thing, but sometimes the physical touch is necessary."
   "It seems Zuberi's also included some underwear for you, along with an Astrogation Guild uniform that seems to be in your size."
   "The underwear selection, at least, seems varied enough."

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

   "That minor detail of personal comfort aside, you push on the drawer and watch as it recedes back into the wall."
   "You turn, and sit down on the edge of your bed. Your day has not been long, but to say that it hasn't been backloaded would do it a disservice."
   if spacer:
      "You never really felt like a dirtsider. It always seemed instead like you belonged out here, in the black. It's hard to get more out and more black than this."
      "It's comforting, in a way. Even as quiet as the {i}Dreamer{/i} runs, you can feel the vibrations in the deck. That subtle crackle in the air."
      "The unique little factors that so many miss, or fail to appreciate. Life shipside, in all its glory."
   if colonist:
      "The galaxy doesn't grow, but \"civilization\" sure does. You've seen it all your life, from your birth forward. The march of life ever further outward."
      "You're here, now, right on the edge of what's considered even vaguely civilized, and you're leaving it all behind. Just like your home was once on the edge."
      "It's exciting. It's terrifying. And that, like the outward march of the galaxy, never changes."
   if core:
      "Torderra's never seemed so far. Sure, you've traveled the galaxy. Traversed jumplanes across the core systems, and much further afield, but this..."
      if WatchedLaunch == 1:
         "You wonder if Mizz feels the same way. It's sort of comforting to have worldkin aboard, you realize; maybe he'll find some comfort in it, too."
         "Or maybe not. You come from the same planet, but from a whole other world. The cub-you growing up on Torderra couldn't have dreamed you'd be here. Could he?"
      else:
         "This is something else. This pushes beyond the known and well into the unknown. Cub-you growing up in Torderra's Yakshen domain couldn't have dreamed you'd be here."
      "But here you are, nonetheless. Soaring into the uncivilized unknown. If that little cub could see you now."   
   if punk:
      "It's almost a miracle that your multiple indiscretions didn't outright disqualify you from something like this."
      "More than a few people thought your potential wasted, running with your crew and raising all sorts of trouble."
      "On some level, you wonder what they'd make of you now. On some level, you wonder what you make of yourself, too."
   if dreamer:
      "It's just like the tales you always heard; the ones you lost yourself in through word and song and dance and story."
      "A ship on the edge, a disparate crew, and everything hanging by the slimmest thread. Civilized space is so rarely like the holoreels."
      "You can't help the smile on your face. It's your story now; you're a part of the tale. Whatever comes, your role is set."
   if tech:
      "It's hard not to marvel at what Zuberi has built for himself here. A top of the line deep-space explorer, packed with the finest tech."
      "A mission to expand the boundaries of understanding. A simulant that seems to exceed the capacities of any you've ever seen before. A crew that..."
      "Well, they're weird."
      "But so are you. To be a part of it all is exactly the sort of thing that the IGA was trying to groom you for."
   if pirate:
      "It's all a step up from what you were, at least. And it's a chance to be more than the mistakes you made as a White Fang."
      "You rub your paws over your face. You tell yourself again that you got out when you could. That you did the best you could."
      "That when they did their worst, you stepped away."
      "It doesn't help."
      "You're not sure that anything could, really."
   if admin:
      "You thought that hope would be dead after Kalissa, like all the people you couldn't save. Like the people whose deaths you were blamed for."
      "Maybe one day they'll know that it wasn't your fault. That you didn't make the mistake; that you didn't ruin the scrubbers. That you didn't kill them."
      "The sounds of those fists beating on the admin center door won't fall silent in your mind, though. You didn't open the door."
      "All the logic in the world doesn't make that feel right."
      "Nor should it."
   if innovator:
      "At least now you have the chance to set right whatever went wrong the last time your algorithm was used."
      if WatchedLaunch == 1:
         "The presence of a cybe like Tulemeni aboard gives you a little more hope than you'd otherwise have. If you can find a moment to discuss it with her..."
         "Well, assuming she doesn't just look at your history and have Obaa lock your door and vent the air in your quarters."
         "You need to find out what went wrong. Not just for your sake... but not-{i}not{/i} for your sake, either."
      else:
         "Someone on board was running your algorithm remotely. It's already aboard the {i}Dreamer{/i}. You need to find out who; they might be able to help."
         "History cannot be allowed to repeat again. You aren't going to be responsible for the deaths of another crew. You aren't going to let that happen."
         "You {i}will{/i} find the fault. Not just for your sake... but not {i}not{/i} for your sake, either."
      "You're just not sure yet how... and that scares you."   
   "You sigh and close your eyes. It's hard not to, but you know you really shouldn't dwell on that."
   "What's done is done. It can't be changed. What's still ahead? That's something that you can affect."
   "Tomorrow."
   "You begin to peel off your clothes. From beneath your sleeping pad slides a new receptacle, and you're reminded once more that Obaa is always watching."
   "And now, at last, you're starting to empathize with the crew that are distinctly unfond of the constant intrusion."
   "Still, you can't help but appreciate the convenience. You unbuckle your belt and set it and your blaster down on the floor beside your sleeping pad."
   "Your magboots are the next to go, also set down next to your sleeping pad. Your wriggle your toes against the deck. It's not as cold as you thought."
   if Commando:
      "Your shirt and pants go into the receptacle next, leaving you otherwise completely naked, and you flex your fingers, toes and tail as you breathe a quiet sigh."
   else:
      "Your shirt, pants and underwear go into the receptacle next, leaving you otherwise completely naked. You flex your fingers, toes and tail and breathe a quiet sigh."
   "The shower tempts you, but your new home is still so new and different to you. You decide to spare the liquid shower for the night, and resign yourself to the sonic option."
   "Not refreshing yourself, of course, is no option at all. Not after Yakeshi Station. You notice that the system has already been set to a lupine physiology. Considerate."
   play sound "Sound/Refresher.wav" fadein 1.0
   stop sound fadeout 8.0
   "The rhythmic pulsing of the sonic emitters washes over your body soon after you step in and key the device on. It buffets you back and forth as you close your eyes."
   "You feel your fur ripple as you sway there in the stall and find yourself lamenting that you didn't just go with the liquid shower. The temptation persists, but you quash it."
   "When the cycle finishes a couple of minutes later, you sigh and step out again. You do feel better, of course. Much cleaner than you were before. You glance longingly at the shower head."
   r "Oh, next time. For sure."
   "The shower, of course, doesn't respond."
   if WatchedLaunch == 1:
      "As you return to your sleeping pad, Obaa's already dimmed the lights for you. It's not going to help, not really, but it's a nice thought."
   else:
      "A quiet thrumming builds up inside your quarters, and you glance around for a moment in confusion."
      o "Nothing to worry about, stray. It's just hyperlaunch."
      r "Oh, right. Thanks, Obaa."
      o "Of course."
      "You pause, standing still as you feel the pulses of the ship's warp drive running not just through its length, but through you."
      if spacer:
         "It's far too late, but you kind of wish you'd taken Bromm'ka up on his offer to join him on the Observation Deck for this. Maybe next time."      
      "The {i}crack{/i} of the ship's hyperlaunch is muted; perhaps that's a feature of the crew quarters. It's still noticable, and it comes as the thrumming vanishes."
      o "Hyperlaunch complete. We are now cruising in warpspace."
      r "Thanks, Obaa. Let me know if we suffer catestrophic failure while I'm trying to sleep."
      o "I'll make a mental note, don't you worry."
      "You smile and rub at your eyes. Terrifyingly omnipresent, at least she's funny."
   if TakeFirst:
      "There's no point in putting it off. You need to sleep, regardless of how awake you feel."
   else:
      "You may not have to be up quite so early tomorrow, but that doesn't mean Zuberi wasn't right. You've been through a lot. You need to rest."
      "Well, you need to rest if you can."
   "You sit on the side of the sleeping pad and roll down until you're laying on your back. A small light to your left, against the alcove wall, catches your eye."
   r "Obaa?"
   o "Just a backup detachable terminal, stray. What, were you afraid I was training a holocorder on you while you sleep?"
   "The thought hadn't occurred to you. Now that she's voiced it, you feel a chill work up your spine."
   "Still, you reach up and trace the edge of the panel. Sure enough, the terminal pad pulls free. Larger than a reader, you cradle it in one paw as you lay back down."
   r "So... {i}not{/i} a holocorder?"
   o "Oh, stray, you have so much to learn. Do you really think {i}I{/i} need a terminal to record you?"
   r "Fair point."
   "A quick tap to the device lights up the interface. You shield your eyes briefly before tucking a paw behind your head. Data scrolls along the display, showing the status of the {i}Dreamer{/i}."
   if TakeFirst:
      "A bit of light reading before bed never hurt... unless you needed to actually sleep. You smile as you tap the display off and reach up to set it back into its slot on the wall."
      "After all, if you keep shining a bright light in your face you'll never sleep. You can't be late for your first day of work."
      "You settle back down onto the pad with your full weight and sigh. The lights in your room begin to dim."
      "Beneath you, you can feel the pad conforming to your body's weight and size. Your head is neatly supported as the pad lifts to meet it."
      stop music fadeout 2.0
      scene black with fade
      "As the lights go out entirely, you can't help but feel a tingle of unease. You know the day to come will arrive too soon, and who knows what with it."
      "Your eyes close as you force your breathing to slow."
      "And, after a fitful hour or two of trying, you find yourself managing to finally drift off to sleep."
   else:
      "You can see the full log of recent events right there. The hyperlaunch, orienting to jump point, displacement receipt, implementation of nav protocols... everything."
      if innovator:
         "You eye off those nav protocols for a second and sigh. That has to be your work. The urge to go over it again right now briefly rises within you. You tamp it down. Rest. You need rest."
         "There'll be plenty of time to work on your soft when you have the mental acuity to actually do some good. At least here you might have the chance to."
      else:
         "You're sure that with a little more time and effort you could slave the terminal at your desk to this. Maybe even connect to the GalNet through it."
         "But as tempting as it is, you can't get caught up with that for now. You'll never sleep that way."
      "You smile as you sit up again to tap the display off. Reaching up, you set it back into its slot on the wall."
      "You settle back down onto the pad with your full weight and sigh. The lights in your room begin to dim."
      "Beneath you, you can feel the pad conforming to your body's weight and size. Your head is neatly supported as the pad lifts to meet it."
      stop music fadeout 2.0
      scene black with fade
      "The lights go out entirely, and you sigh. At least by taking the Second Shift, you don't have to try and force the sleep."
      "You allow your mind to wander, taking in the details of the last day... and of recent years. Experiences, faces... losses."
      "The gentle cradling of the sleeping pad and the darkness of the room eventually do their jobs, however, and your eyelids grow heavy."
      "Eventually, mercifully, sleep claims you."
   jump Day1Start