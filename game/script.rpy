# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
init python hide:
    for file in renpy.list_files():
        if file.startswith('bg') and file.endswith('.jpg'):
            name = file.replace('BG/','').replace('/', ' ').replace('.jpg','')
            renpy.image(name, Image(file))
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    style.nvl_window.background = "nvl/textbox.png"
    style.nvl_window.xpadding = 140
    style.nvl_window.ypadding = 50

init:
    $ narrator = Character(None, kind=nvl,what_font="HalleyveticaNBP.ttf")
    image cg1 = "bg/cg1.png"
    image cg2 = "bg/cg2.png"
    image cg3 = "bg/cg3.png"
    image cg4 = "bg/cg4.png"
    image cg5 = "bg/cg5.png"
    image cg6 = "bg/cg6.png"
    image field = "bg/field1.png"
    image fire = "bg/fire1.png"
    image horizon = "bg/horizon1.png"
    image road2  = "bg/road2.png"
    image stars1 = "bg/stars1.png"
    image stars2 = "bg/stars2.png"
    image stoplight = "bg/stoplight.png"
    image town1 = "bg/town1.png"
    image town2 = "bg/town2.png"
    image trail1 = "bg/trail1.png"
    image trail2 = "bg/trail2.png"
    image trail3 = "bg/trail3.png"
    image trail4 = "bg/trail4.png"
    image chap1 = "bg/chap1.png"
    image chap2 = "bg/chap2.png"
    image chap3 = "bg/chap3.png"
    image chap4 = "bg/chap4.png"
    image chap5 = "bg/chap5.png"
    image prologue = "bg/prologue.png"
    image grandpa = "bg/grandpa.png"
    
label splashscreen:
    scene black
    with Pause(1)

    show text "Nu American Horror Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "A 48 hour Production..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Written: Raithfyre & Able" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Music: McDoogle & Able" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Art: Hiko27" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
        
    show text "Coding: towicode" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "UI Art: Andeh_" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return
    
label start:
    #scene 0
    scene prologue with dissolve
    with Pause(2)
    
    play music "GW_Open.ogg"
    scene road2 with fade
    "My name is Ashley McGlothlin. I'm a thirty-eight year old office worker and part time writer."
    "In the summer of 2009, after the end of a long relationship, I decided to take a sabbatical. I lived in Ellsworth, a suburb of River City, which was the only city for about a hundred miles around."
    "Even though my work had taken me to a drab office in South Dakota, the intervening years couldn't fully strip away my love of the outdoors. I grew up as a plucky girl who played explorer in the woods of Northern Oregon. It was time to return to my roots. "
    "In addition to the neglected adventurer in me, I also coveted the chance to work on my writing, something that had fallen to the wayside during more stressful proceedings."
    "I hadn't decided on a destination yet when, on the drive home from the office, I saw a sign for an estate auction happening that afternoon. "
    scene town2 with fade
    nvl clear
    "Being a bit of a treasure hunter, I decided to go. The event was on the other side of town and in a neighborhood that was known for its bigger, richer houses."
    "When I arrived, the auctioneer was on the lawn in front of an audience in folding chairs. They were bidding on various statues and artifacts the deceased had acquired in his travels."
    "I watched for a little while, but when a single oil painting sold for over two thousand dollars, I knew the crowd was too rich for my blood."
    "Wandering around the tables covered with trinkets and small pieces of furniture, I noticed that the deceased had a very nice collection of camping gear."
    "I picked through it, most of it was well worn but a few coats and pairs of raingear were in good condition. I would have bought them, but they were all in men's sizes."
    "Instead, I settled on a single wrinkled book, priced for a dollar and left next to a table full of old ice climbing gear. It was a guide to the trails and parks of the Dakotas."
    nvl clear
    scene stars1 with fade
    "That night, while paging through faded descriptions of serene lakes and hidden hot springs, I found a reference to an obscure campground nestled inside the Black Hills."
    "It wasn't a formal entry in the in the guide book. Instead, written in the margins, was directions to a place called Castle Hill Park. "
    "Next to the writing was a small map, showing where a trail opened between the trees on the shoulder of a rural highway and led into an unnamed forest."
    "At first I figured it was a recent addition, after all the book had been published in the mid 1970s and was easily outdated. I quickly flipped through the rest of the book, looking for any other handwritten entries."
    "There were none until I reached the last few pages. "
    "At the end, after the acknowledgements and lists of revisions, the publisher had left several ruled pages so that the reader might keep a log of the places they've visited."
    "The earliest entry was from 1978, a visit to the trails behind Mt. Rushmore. This was followed by years of hiking and camping at nearly every park in the region."
    "It wasn't until September 28, 1991 when the first entry for Castle Hill Park appeared. Then on May 2nd, 1994, and again in late March of 1995. After that, at least once every single year until december 31st, 1999. After that, entries became sparse."
    "Between the years of 2001 and 2005 there wasn't a single trip recorded until September 12th, 2006 when he returned one final time to Castle Hill Park."
    nvl clear
    play sound "typing.ogg"
    "I researched Castle Hill Park on the internet, and in other guidebooks. I even sought out revisions specifically from the nineties, thinking the park might have been abandoned after a decade or so. It was all fruitless. "
    "As far as every reference was concerned, Castle Hill Park simply didn't exist."
    "In a move of desperation, I called the estate which I'd purchased the map from."
    "The paralegal who answered the phone informed me that the gentlemen who had passed away had kept to himself, especially after his wife passed before him. "
    "He said he didn't think any of his children would be able to answer specific questions about a camping but promised to ask them. I don't think he ever did."
    "The old man, whose name I found out was Henry Albert Burns, continued to return to Castle Hill Park until it was the single most visited place in his log. "
    "This whole situation sat in the back of my mind while I worried about more present things. The divorce was going poorly. "
    "After ten years married there were so many complications, even the simplest proposals were met with objections and sustainments and postponements."
    "I couldn't decide if the lawyers were earning their pay or robbing me blind."
    nvl clear
    scene stars2 with fade
    "We'd been separated for a year and proceedings had just entered into the fifth month."
    "The end was in sight though, and just when I'd forgotten about that Henry Burns, his name came up on the evening news."
    "The family, it seems, was in the middle of a settlement of their own. It seems that the auction I had seen was for his third home."
    "One of his children, a step child, had been shut out illegally and now the whole probate was in question. "
    "The report was over and I was about to turn off the television when they announced there would be a brief biography on Henry after the normal newscast."
    "It turns out he owned several small manufacturing companies and sat on the board of a regional oilfield contractor. He was known to be secretive, often disappearing without notice. "
    "The public knew him from the evening news. Twice in the 1990s, he was reported missing by his wife and colleges, only to turn up a few weeks later, hitchhiking home. "
    "The story ended up in Reader's Digest under the humor column."
    "I didn't have to research the old news reports to know, but I did anyway. When I cross referenced the dates of the reports and the old trails guide, it was a perfect match. "
    "I sat in my room looking at the log. I had the punchline a Jay Leno joke, and as far as I could tell I was the only one who knew."
    "Eventually the legal proceedings were wrapped up. I notified my office that I would be out and started planning my sabbatical."
    "After purchasing a new tent and some other things, I loaded everything into my Ranger, which I'd almost lost when the judge assumed was my ex-husband's vehicle, and pulled out onto the interstate."
    scene road2 with fade
    nvl clear
    "Maybe it was the sense of secrecy, or mystery, or maybe I was just looking for an excuse to get away. Whatever the reason, I knew where I was going. "
    
    scene chap1 with dissolve
    with Pause(2)
    #scene1
    nvl clear
    play sound "driving2.ogg"
    "I spent most of the day on the road before turning off of the highway and into a tiny town called Basin."
    "he population couldn't be more than about fifty or sixty, from the look of it. I had to wonder where the one horse was."
    "It consisted of a single road with a few houses and a single municipal building."
    scene cg5 with fade
    "The only store was in an empty lot near the highway onramp.  It had one gas pump and the whole thing was maybe four hundred square feet."
    stop sound
    "I parked my truck and got out to stretch my legs."
    "Only one other vehicle was parked beside the entrance: a rusted old tractor with a cart on the back."
    "I went inside the store."
    "There wasn't much to see; it smelled like an old attic and the aisles were cramped, filled with everything from gloves to granola."
    "I took a bottle of soda and a candy bar to the front to pay."
    ""
    show grandpa with fade
    "On a stool behind the counter was an old man reading a newspaper."
    "He didn't look friendly but I struck up a conversation anyway."
    "I found out that he'd lived in Basin his whole life and had run this store for the last thirty years."
    " I wondered if he'd been married, maybe he still was. "
    nvl clear
    "I asked him if he knew anything about a place called Castle Hill Park."
    "He told me it was about twenty minutes out of Basin, up the main road."
    "He reached to a display on the counter and pulled out a map, photocopied and folded from a single piece of paper."
    "It had the highway exit  and the main street, as well as a few service roads that deviated further up."
    "He drew a path off one of the service roads and told me that was where the old trailhead was. "
    "He said it was an old campground they tried to restore about a decade ago."
    "There used to be some regulars who came by, but he hadn't seen them in years."
    "He asked why I was interested in going there, he explained that there were better places to camp up the highway and the season was slow, so they weren't likely to be crowded."
    "I had to explain the the estate sale and the trails guide. Even when I did he didn't understand."
    nvl clear
    hide grandpa with fade
    "I thanked him and paid for my things. It wasn't until I was back outside that I thought to ask him another question."
    show grandpa with fade
    "I went back in and when he looked up, visibly annoyed that I was back, I asked if he knew a man named Henry Burns. "
    "After a thoughtful moment, he said that he had. Henry would turn up a few times a year, and yes, always stayed in Castle Hill Park."
    "He described him as a lone hiker, though sometimes he had a friend with him."
    "I asked him why Henry would want to stay in an unkept park like Castle Hill."
    "The man told me, if he remembered right, there was a brook that poured over a rock formation nearby."
    "He told me it had a unique sound, something to do with cavities in the volcanic glass, he didn't really understand. "
    "Henry had mentioned to him years ago that is was the only place he could get restful sleep."
    nvl clear
    "I asked him to show me where this brook was on my map, and he showed me."
    "It looked like it was only a short walk from the campsite. "
    "He didn't need to draw it in, it was already marked with a black triangle and the name Devil's Falls."
    "I smiled at the ominous name. Halloween was always my favorite holiday."
    "For a couple years we had hosted the costume parties in our neighborhood. "
    "I pushed the thought away. "
    nvl clear
    scene stoplight with fade
    play sound "driving2.ogg"
    "Back on the main road, I followed it to the north end of town. "
    "There it changed into a fire service road. "
    "My GPS was working, but nothing outside of Basin's main road was in its memory."
    "It kept telling me to turn towards the nearest highway, by now miles away. Instead, I relied on the map."
    "The distance was short, but I had to drive slow; the unmaintained road was occasionally washed out, and I had to make a calculated maneuver between the trees and the gutter. "
    "Finally, according to my odometer, the park road would be close by."
    ""
    "I had to turn around twice, but I found it. Hidden well and overgrown was a set of deep tire ruts which curved off the service road and onto one that was somehow worse."
    "I began to wonder if this was actually a park or just a local unmarked trail."
    "At a point, I thought I lost the trail, slowly plowing through grass and short brush, when I finally emerged at an old parking lot."
    "The pavement was cracked and crumbled, and scrawny windings of grass patched the entire thing."
    ""
    "In the far end of the parking lot, there was an old ranger station. It looked like it had been abandoned thirty or forty years ago."
    stop sound
    "Part of the roof had caved in and the whole south wall looked like it was about to follow."
    " Next to the station was a sign."
    nvl clear
    play sound "chimes.ogg"
    " ' CASTLE HILL PARK ' "
    nvl clear
    scene chap2 with dissolve
    with Pause(2)    
    #scene2
    scene trail1 with fade
    play music "Piano2.ogg"
    "I shouldered my backpack and went for a closer look. At the edge of the woods was a metal barrier, presumably to keep off road traffic out."
    "The barrier was halfway open and so rusted that I suspected it was stuck permanently."
    "I thought about peeking into the old ranger station, but decided against it. Instead, I sidestepped the barrier and pressed further into the woods. I thought back to the gas station attendant; at least one person knew I was out here"
    " If something happened, I thought, he would bring help. Then again, if I didn't return maybe he would assume I had just driven off."
    "As I went the trail got worse and worse. Fallen trees blocked the way and some sections were just overgrown, reduced to a game trail."
    "Eventually the path began to switch back and I gained elevation. It was late afternoon when I finally arrived on the top of what I could only assume was Castle Hill."
    nvl clear
    scene fire with fade
    "It was a small clearing to the left of the trail. I mistook it for a natural field before I saw the small circle of stones, a fire pit, barely peeking above the tall grass."
    "I got my tent setup and unpacked my bedroll. The little campsite was actually quite comfortable. There wasn't a shortage of firewood, with felled branches over the campsite."
    "It was late afternoon and I had a fire going in short order. By the time I'd eaten and gotten to bed, I already felt fifteen years younger. The office and ex problems seemed miles away."
    "The next day I got to exploring my surroundings. It looked like the trail actually continued for a few miles. I realized it was possible that there were other campsites further down. After breakfast, I went to check them out."
    "There were three more campsites, about a quarter mile apart"
    " I stopped to survey each one, combing them as best as I could. I couldn't say what I expected to find, but I was looking for anything."
    " Any sign that Henry Burns had been there. That this was in fact that dead man's solitary place of refuge. "
    nvl clear
    scene trail2 with fade
    "The first site was the same, overgrown as the rest of the park. It had less grass than mine, but saplings and young trees had came up everywhere."
    "In another ten years, this would be indistinguishable from the rest of the forest. I couldn't find anything, even after a thorough check."
    nvl clear
    scene trail3 with fade
    "The next site was actually down behind Castle Hill. Like my own, it was covered in tall grass."
    play sound "birdoff.ogg"
    play sound "crows.ogg"
    "As I walked in, a whole murder of crows darted from the grass."
    "They circled around me, cawing and driving. One came at me with claws outstretched."
    "I dodged to the side and it missed my face, snagging and tearing the shoulder of my jacket. The rest of them suddenly grew more daring and moved to attack. "
    "I gripped my walking stick with two hands; it was the only weapon I had. Another one circled around and as it came at me, I noticed that it was the biggest crow I'd ever seen."
    "When it came into range, I swung my staff like a baseball bat."
    play sound "thud.ogg"
    "It made contact and the bird was thrown away, a spinning mess of broken wings and feathers."
    "I heard it tumble into the brush beyond the treeline. "
    nvl clear
    "I had to take a few more swings, grazing the more nimble birds, before they retreated into the trees."
    "I spun around, brandishing my weapon at the tree tops and branches where they perched, quietly watching."
    "In the silence I could hear the one I'd knocked away flopping and mewing beyond the treeline."
    "I was going to turn and leave, but I noticed there was clearing in the tall grass, where the crows had sprung from. "
    " I moved closer, keeping an eye on the birds, and felt my stomach drop."
    "I had seen a lot of things, but this one was so abnormal I had to blink just to make sure I wasn't dreaming."
    "When I got closer, I saw that the clearing wasn't natural at all."
    nvl clear
    play sound "chimes.ogg"
    "It was a perfect circle of depressed grass, without rhyme or reason."
    "Sometimes we'd find fairy circles in the woods as kids, strange rings where nothing would grow."
    "As I child I remember discovering what caused them. It wasn't something supernatural like a fairy's home, but a growth of underground fungus."
    ""
    "Staring at this circle in the grass I could find no explanation. It was crushed, not simply dead. I noticed the smell while I was trying to make sense of it."
    "Some of the grass was scorched, though not completely burned, but that wasn't the strangest part."
    play sound "chimes.ogg"
    "Strewn around the circle were five, maybe six animal carcases."
    "Rabbits, I thought, or possibly large squirrels."
    "It was hard to tell because each one of them lay headless and flayed."
    "It was hard to tell without getting closer, which I refused to do, but it looked like they had been cut open along the back and, along with the heads their whole spinal cords were removed."
    "It all made me sick."
    play sound "crows.ogg"
    "The crows started to caw again, threatening that I should leave."
    "I didn't look back, but could hear them flapping behind me as they swarmed the mutilated remains."
    stop sound
    nvl clear
    scene trail4 with fade
    "The last campsite was a considerable walk from the rest. I was thankful for this, I needed a some time to recover."
    "My first thought was some angry kid was hiding out here, but that didn't make any sense. "
    "I didn't think anybody, even a sick person, would do that sort of thing outside of movies."
    "As I went, the trail curved around the hill."
    "I was actually closer to my tent now, because of the roundabout path."
    "Eventually I noticed the sound of running water and quickly found the last campsite."
    " Checking the map from the gas station, the campsite was unmarked but happened to be right next to Devil's falls. "
    "The brook was only a few feet beyond the treeline, I pushed through and stood on the shore. "
    "The small waterfall tumbled over some spiky black rocks. I listened for a few minutes but I couldn't hear anything special about it. That suited me just fine, though. "
    nvl clear
    scene trail1 with fade
    "I didn't want to walk back the way I came, at least not yet, so I pressed on. I thought I saw a clearing, so I cut through the woods and was surprised to emerge next to my Ranger. "
    "I decided this meant two things. First, the trail was a loop, and second, that the map I had couldn't entirely be trusted."
    scene cg1 with fade
    "I walked back to my tent, relieved to be back before dark."    
    " I set a fire and cooked some dinner. While my hotdog roasted, I tried not to think about that fairy circle, if that's what it was."
    "I'd brought a flask with me and now seemed like a good time for a drink. "
    "I hadn't noticed, but there was the faint roaring of the wind that provided the backdrop to crickets chirping."
    "I closed my eyes a moment, enjoying the calm atmosphere."
    scene chap3 with dissolve
    with Pause(2)
    nvl clear
    
    #scene3
    scene chap3 with dissolve
    with Pause(2)    
    play music "jam1.ogg"
    scene trail1 with fade
    "I stayed for two more days, relaxing and hiking around the park and I didn't have any more trouble with the wildlife."
    "There was another trail system close by, I had to bushwhack about about a thousand feet to get there, but spent the rest of the daytime exploring along them."
    "One thing I discovered was that Devil's falls actually changed timbre from day-to-day. When I'd first visited, it sounded like a normal brook, but now there was a distinct overtone to the bubbling."
    play sound "chimes.ogg"
    "I didn't see much wildlife, but one morning, I did find a set of tracks through my campsite."
    "I didn't see much wildlife, but one morning, I did find a set of tracks through my campsite."
    "I didn't pay any attention at the time, but now I can see the reason the tracks were so strange. Half the prints were backwards, like two animals stuck together."
    "Whatever it was, it wasn't natural."
    ""
    
    " I decided to be more cautious, especially because I'd already had to fight off animals. I went back to examine the tracks later, but they were washed away."
    "My writing hadn't gone as well as I hoped, but progress was steady"
    scene cg2 with fade
    "I'd used a fair amount of gas over the last few days, hiking back to the parking lot and idling my truck a few hours while my laptop charged in the cab."
    "I was also running low on water, and the iodine tablets I'd brought made the brookwater taste awful."
    "All this made me decide it was time for a take a trip back into Basin."
    nvl clear
    scene road2 with fade
    "It was late afternoon when I left and I decided there would be enough time to hit the store and be back before dark. I started the truck and eased it into a three point turn to get out of the lot."
    "Somehow the road seemed further away, though I knew that was impossible."
    play sound "driving2.ogg"
    "Still, after a while I was back on the main road heading into town."
    "When I got to Basin, I passed all the quiet houses and the dark municipal building again, arriving at the gas station by the highway on ramp."
    nvl clear
    scene stars1 with fade
    "I pulled in and found the same tractor parked beside the building. There was a white van at the pump."
    "I walked into the gas station, looking around for the attendant I'd spoken to earlier that week."
    "Maybe, I thought, he had somebody else to tend things part time. I didn't see anybody inside, but I picked out a candy bar and another soda, it has been a while since I'd eaten anything sweet."
    "After a few minutes, without seeing anybody in the store, I took a walk around the back, expecting to find somebody on break."
    "Behind the store were a few rusty drums of used oil and a small pile of scrap metal."
    play sound "chimes.ogg"
    "Not a single sign of a human. I must have waited at the store for fifteen minutes, noticing that the van was unattended with the pump nozzle still in the tank."
    nvl clear
    scene stars2 with fade
    "I decided to take a walk up the street."
    "When I got about halfway up, I noticed that many of the houses had one or two cars parked out front."
    "Some even had lights on indoors. But there was no noise, no sign of life anywhere."
    "'"
    "At this point, I turned back towards the gas station."
    "It took me much longer to get back because I was stopping to peer into the windows of each house as I passed."
    "When I got back to the gas station, the daylight was starting to fade."
    "I left some money on the counter, trying to believe that sometime tonight, or maybe tomorrow morning, everything would be back to normal."
    "Even as I told myself that, I knew it wasn't true."
    "What I should have done, had I known what I know now, was to push that van out of the way, fill up my truck and leave immediately."
    "I even had a hose with me."
    "If I had to, I could siphon some tanks. Even if I didn't do any of that, I probably still had enough gas to get to the closest town. "
    nvl clear
    scene cg4 with fade
    "But I didn't do any of that. Instead, I left the gas station, turned around and drove back to my campsite."
    "I should have ran, but a sense of rationality was prevailing."
    "Those years of experience that taught me to keep a level head, to take the unexpected in stride, were blinding me to the danger."
    play sound "chimes.ogg"
    "Even as I hiked back up Castle Hill that night, I could sense something watching me."
    "It was a struggle to keep my flashlight forward and my legs from breaking into a run."
    "When I got back to my tent, I slipped inside and immediately killed my flashlight."
    nvl clear
    window hide
    scene stars2 with fade 
    
    
    scene chap4 with dissolve
    with Pause(2)    
    #SCENE4
    
    play music "Piano1.ogg"
    window show
    scene cg3 with fade
    "Somehow I must have slept because I woke up, rubbing my eyes from the light."
    "Then I checked my watch and noticed it was still dark outside."
    "I screamed, bolting awake and trying to get out from the grip of my bedroll."
    "I tripped over myself, flailing around for a few seconds before I saw the source of the light."
    "My flashlight was on. I fell asleep clutching it and must have clicked it on in my sleep. "
    "took a moment to breathe, trying to calm myself down"
    "I clicked the light off and collapsed back onto my bedroll, laughing to myself."
    "I found my pillow, thrown across the tent and tucked it under my head, trying to rid the tension from my body. "
    nvl clear
    play sound "sting.ogg"
    "Then I heard the footsteps. I froze."
    "It couldn't be anything but a trick of my imagination. I told myself that even as I lay frozen, listening with every inch of my being, praying that I was alone."
    "My heartbeat was like a drum."
    "I heard it again. It was crisp and clear, as if it was right next to me. As if feet were crunching the leaves just on the other side of a single sheet of lightweight poly cotton."
    "The footsteps walked away from the tent. I could hear clearly, two footfalls. It sounded heavier than a man."
    ""
    "The steps disappeared into the background of the forest, and I thought for a moment I was safe."
    "A blinding white light filled the tent. It came in from above, illuminating my backpack and a roll of dirty clothes in the corner."
    "I got out of my bedroll just as the walls of the tent were ripped away into the night."
    nvl clear
    "I was exposed, and probably surrounded."
    "The light was still shining, but brighter now against the blackness that surrounded us."
    "I looked around, waiting for something to lunge from the shadows. Then I saw them."
    "They were in the trees. I couldn't tell how many; I didn't care."
    "The black figures loomed; nearly imperceptible in the twilight between the light and void."
    nvl clear
    scene stars2 with fade
    "I ran. "
    ""
    "I could hear them turn to chase me."
    "The spotlight had followed me as I ran towards the trail, but then it went dark, leaving me blind."
    "I stumbled down the trail; my eyes hadn't adjusted and I tried to follow it from memory. "
    "I turned right, which would bring me down the hill towards the parking lot."
    ""
    "I made it the first hundred feet without stumbling, but then I ran full speed into a downed tree; I'd forgot it was there."
    "I must have tumbled over it and hit my head, because when I opened my eyes, I couldn't tell if I was standing up or lying down."
    "It took precious seconds to recover, get my bearings and start back down the trail."
    nvl clear
    scene stars1 with fade
    "Immediately I was conscious of the fact I was not wearing shoes and my socks offered little protection."
    "It hurt to run, but I forced myself through."
    "I could hear them behind me, stomping like giants on the hunt."
    "My eyes had adjusted but I didn't dare look back. I knew if I could just get to the truck I could outrun them. Afterall, they were on foot."
    "The parking lot was only a few meters away."
    "The dirt and rocks under my feet changed to broken pavement."
    "Squinting, I could see the outline of my Ranger in the faint starlight. I ran to the drivers side door and pulled the handle..."
    nvl clear
    play sound "horror.ogg"
    "...It was locked."
    nvl clear
    "My keys were back in the tent."
    "I didn't have any room to think or plan, only instinct ruled."
    "And my instinct knew the only way to survive was to keep running."
    "I bolted again, this time down the service road, towards town."
    "I don't know how long I ran, but my feet were already bloody."
    "Every step was a triumph of will and every breath was a conscious exertion."
    "Eventually I had to pace myself. The adrenaline rush was gone, and I was starting to crash."
    "Still, I kept going, knowing that any second those things could be on top of me."
    nvl clear
    scene stars2 with fade
    "When the dirt road changed back into pavement, I knew the town was only a few miles away."
    "My heart rose when I felt the pavement, and once again when when I saw headlights up ahead."
    "I stopped in the road, waving to them. I was sure I was saved. Whoever it was, I didn't care."
    ""
    "After a minute of standing in the road, I realized I hadn't been saved at all. I had to force myself forward, this time because I feared what was ahead."
    play sound "chimes.ogg"
    nvl clear
    "The car was frozen in the middle of the road, still in drive. What kept it in place was the parking brake, which made an awful grinding sound. "
    "As I circled the car, just to verify what I already knew, I saw that there weren't any obvious signs of a struggle."
    "Just the driver's side door hanging open."
    ""
    "There was no time to wonder what may have happened."
    "I slammed myself into the driver's seat and stomped on the gas pedal, all in one motion."
    "As the car roared to life, I buckled my seatbelt with one hand."
    ""
    nvl clear
    scene road2 with fade
    "I sped away from the town, without a clear idea of where I would end up."
    "All I knew was that it was just as dangerous to be in Basin as it was in the woods."
    "I planned to take the first exit I could; ask for help at the first sign of civilization."
    "Multiple other cars dotted the road, lights on but unmoving."
    "In the same condition as I had found the car I was in. "
    "With horror, I noticed a trend shared between the abandoned vehicles that didn't have their doors open: the roofs of the cars had gaping holes in them, torn metal poking skywards."
    "Ignore them, I told myself. Keep your eyes on the road. "
    "At the same time, I was fiddling with the radio, trying to get anything beyond the awful static that buzzed from every frequency. "
    "A news channel, a college radio station, even the Spanish soap operas."
    "I just wanted to hear a human voice, but got the same wretched noise no matter what I tried."
    nvl clear
    "As soon as I realized that I wasn't getting any reception, I had another awful revelation: I still hadn't passed any exits."
    "It was too dark to see anything at the sides of the road. At one point, I looked out and up at the sky, just in time to see a strange light flicker and shoot overhead and behind me."
    ""
    "Just ignore them."
    play sound "chimes.ogg"
    "A beeping from inside the car made me panic for a moment, until I realized it was an alarm for the gas gauge."
    "The needle hovered in the orange zone, dangerously close to empty."
    "Ten minutes down the highway at an insane speed and I still hadn't seen an exit sign."
    "There was no way I'd have the gas to make it to the next town."
    nvl clear
    
    scene chap5 with dissolve
    with Pause(2)    
    scene road2 with fade
    
    #scene 5
    play music "chase.wav"
    "I had no real options. Abruptly, I jerked the wheel to the left and crossed the median, doubling back the way I came."
    "There was probably enough gas in the tank to make it back to Basin."
    "Probably."
    "In the rearview mirror, I spotted more lights in the sky. I pushed them from my head and kept driving."
    "Basin came into view in the highbeams, looking like a specter of its former self."
    "While there had at least been a few lights on before, now almost the whole town was dark."
    scene cg6 with fade
    nvl clear
    "I navigated to the gas station almost purely by memory."
    "Naturally, the same cars blocked the gas tanks as before."
    "My whole body was shaking with fear, but I leaped out of the car I was in and climbed into the parked van."
    "The plush seat was sticky and an empty soda bottle rattled around by my feet"
    "My shoes stuck to the pedal as I moved forward just far enough to fit my car in."
    "By some miracle the machine still had some life in it."
    "I swiped my debit card through several times, messing up my PIN entry the first time."
    "It was nearly impossible to hold onto anything as I was shaking so much."
    "All of my practice keeping a level head had abandoned me."
    nvl clear
    "Finally I was able to start pumping gas, but just barely. It flowed slowly; way too slowly."
    "A muffled clanking sound echoed from inside the device, too."
    "Something was definitely wrong with the pump, but I had no choice but to deal with it."
    "Then I heard another noise, coming from the building."
    "I spun around, hand still on the pump. After fumbling around in the car for a moment, I retrieved my flashlight."
    "I didn't even remember carrying it with me, but apparently I had clung to it in my flight from the tent."
    "I flicked it on just as I heard the first words."
    "At least, they sounded like words. I got the impression that it was someone asking for help; it sounded like the gas station attendant."
    "But it was just a moan, not speech."
    nvl clear
    "Flicking on the flashlight, I pointed it straight at the station door."
    "A figure stood there, and at first I thought that it was in fact the man from before."
    "It was his face, at least. But then the eyes glowed a sinister red, the light reflecting off them, and I realized it was a ruse."
    nvl clear
    scene road2 with fade
    "I screamed, ripping out the gas pump and diving in through the passenger-side door."
    "The engine barely rumbled to life as the creature dashed from the door to the car, lunging at me just as I began to drive away."
    play sound "thud.ogg"
    "It collided with the back of the car, hitting it with enough force that the whole car rocked to one side."
    "As I began to fly down the street, I could see it in the rearview; It was still clutching at the rear bumper through some insane force of will."
    "Just as its spindly fingers began to reach for the backseat's door handle, I turned a sharp left, scraping the monster against another parked car."
    "It howled with inhuman agony as it was torn away, and I sped on. "
    "I thought that I was safe. Then, out of nowhere, a blinding light shone down from above - a spotlight from some sort of craft."
    "For one brief, delusional moment, I thought that perhaps it was the military, here to save the day."
    nvl clear
    "But when I saw more figures stalking towards me from the shadow, directed by the floodlight, I knew I was wrong."
    "On the edge of my vision, I realized that something was on fire as tendrils of smoke crawled into the air."
    "There were a few trees, planted for decoration, and as I passed one I saw that it was nearly bent in half, trembling under the pressure of some unseen force"
    "Its leaves burst into flames behind me."
    "I recalled the bent, charred grass near the campsite. This was clearly the same thing."
    "I took an exit out of the city and raced back to the highway, heading for a mountain pass and the hills."
    "The gas pedal was pressed to the floor, and I was going well over a hundred."
    "Something big had caught fire in the town, either spreading from the trees or set directly aflame."
    "I could see it in the rearview, and I could also see the aircraft pull away from Basin."
    nvl clear
    "From the way the aircraft followed me now, I knew I had their full attention."
    "It poised itself over me, vanishing out of sight from my rearview but flooding the road with light"
    "It was somehow able to hover just over me, keeping pace despite the fact that I was pushing the car to its limits."
    "Grass sizzled and burned on either side of the highway."
    "Suddenly, and without warning, I felt an immense tugging feeling, like I was being lifted up."
    "There was no specific part of me that was being “held,” but rather I was being lifted all at once."
    "Screaming with terror now, I wrapped my arms as tightly around the steering wheel as I could, simply keeping the car pointed forward and flooring the gas pedal."
    "The yanking sensation was so strong that I felt my bones might break, or that I might even be snapped in half."
    "I couldn't even scream anymore, because the force  pushed all the air out of my lungs."
    "Just as I was ready to give up and resign myself, the sensation abruptly stopped."
    nvl clear
    scene stars2 with fade
    play music "piano2.ogg"
    "I was in the forest now, trees surrounding me. The light from the craft was still there, but it had to pull up and away, apparently to avoid damage."
    "With nothing but blind panic and survival instinct fueling me, I kept driving. The road became curvy, and I had to pay attention to my surroundings."
    "It took nearly five minutes before I realized that the light from the craft was gone, and that I was alone."
    "I didn't slow down, but my heartbeat did."
    "I was aware that it was likely a false sense of security, but it was the best I'd had for hours."
    "I drove at a reasonable speed, expecting to have to floor it again any moment."
    "That moment never came. Ten minutes passed, but I never saw another light."
    play sound "truckoff.ogg"
    "It was unwise, but I slowed to a stop, pulling off to the side of the road."
    "The trees were thick here, and it was probably the safest place to be."
    "Leaving the shelter of the woods meant putting myself in the open again."
    "I waited. Ten minutes passed, and part of me was certain that another attack was imminent. "
    "That at any moment, another monster would throw itself against the car door and drag me out. "
    nvl clear
    "Another ten minutes passed. I was so tense that my muscles were sore, but I didn’t dare move."
    "After half an hour, I decided I was safe."
    "I breathed a long sigh that turned into a sob. Seconds later I was bawling. Fear and pain and confusion were all let out at once."
    "My feet were a bloody mess; my socks shredded to tatters. Every single part of me hurt and I had no idea what I had just been through."
    "The more I tried to think about it, the more my head hurt. I just wanted to close my eyes for a second, just to breathe; just to rest."
    "..."
    nvl clear
    scene stoplight with fade
    play sound "thud.ogg"
    "A tapping at the window woke up. As I groggily woke up and remembered where I was, I was profoundly certain that the tapping meant I was about to die."
    "But when I uncurled from my ball and sat up, there was no monster outside my window. Instead, there was a police officer, worry creasing his face."
    "I fumbled with the lock and opened the door, but couldn’t muster the strength to stand."
    "The officer explained that there had been a fire and asked if I had been there; if I had been okay."
    "I just nodded. He wasn’t wrong. There had been a fire, and then some."
    "The officer, whose name I can’t remember, helped me to his squad car. I mumbled something about how the car I was in wasn’t mine, but he didn’t seem to take me seriously."
    "On the short ride to the police station, he questioned me about what I had been through, and what I had seen."
    "My head was killing me, and I was still somewhat groggy, so I just made sounds that agreed with him. I didn’t mention the lights or the monsters. It seemed unbelievable in retrospect."
    "Being questioned at the station was more of the same. They gave me a water bottle and a muffin and an aspirin."
    "Told me that an accident at the gas station in Basin had set the whole town ablaze."
    "I was the only survivor, they told me."
    nvl clear
    "When I asked about the other abandoned cars on the road, they all looked uncomfortable and said they belonged to people who had tried to escape but couldn’t"
    "When I asked about the holes in the roof, they told me I was fatigued and remembering things wrong."
    "I didn’t ask many questions after that. Just assured them that I didn’t need a hospital, or at least not one before I got home."
    "Even though they seemed hesitant to let me leave, they didn’t try too hard to stop me. "
    "My truck was, unfortunately, lost in the fire too. Apparently it had spread all the way to the campground. "
    "It fell to a rookie officer to drive me back home. We made awkward, unmemorable small talk the whole time."
    "'Sorry about your truck, mam,' he said before he was gone."
    "I couldn’t even find it in me to regret losing the truck. I’d gotten out with a damn sight more than I’d expected to."
    "Unlocking my front door, and being home, was strange."
    "Less than 24 hours ago I had been running for my life, yet I was already making tea on my own stove."
    "In the bathroom, I peeled off my bloody, ruined socks and threw them in the trash."
    "The stained scraps of cloth were all the proof that I really had of the previous night’s events."
    nvl clear
    "I thought about Henry Burns while I spooned sugar into my tea. His family and friends all thought he was insane."
    "Most people didn’t even remember him."
    "I thought about the gas station attendant, presumed dead, while I waited for my tea to cool. "
    "Would anyone remember him? Who would direct people to Castle Hill now? Maybe it was for the better that everyone forget about that place."
    "..."
    "Everyone except me, of course."
    nvl clear
    "I retrieved Henry Burns’ journals and maps from my study. I read through them, one last time."
    "Then I struck a match, and set the whole thing ablaze. The pages caught fire quickly, dry as dirt."
    "Henry Burns."
    "A fitting name."
    return
