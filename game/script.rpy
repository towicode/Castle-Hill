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
    image cg1 = "cg/test.png"
    image cg2 = "cg/test.png"
    image cg3 = "cg/test.png"
    image cg4 = "cg/test.png"
    image cg5 = "cg/test.png"
    image cg6 = "cg/test.png"
    image cg7 = "cg/test.png"
    image cg8 = "cg/test.png"
    image cg9 = "cg/test.png"
    image cg10 = "cg/test.png"
    image town1 = "bg town1.png"
label splashscreen:
    scene black
    with Pause(1)

    show text "Nu American Whore Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "A 48 hour Production..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Written: Raithfyre & Kirby" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Music: McDoogle" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Art: UHRUHKUH" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
        
    show text "Coding: Padlockcode" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "UI Art: Andeh_" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return
    
label start:
    play music "GW_Open.ogg"
    scene road with fade
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
    #scene1
    nvl clear
    "I spent most of the day on the road before turning off of the highway and into a tiny town called Basin."
    "he population couldn’t be more than about fifty or sixty, from the look of it. I had to wonder where the one horse was."
    "It consisted of a single road with a few houses and a single municipal building."
    scene gas_day with fade
    "The only store was in an empty lot near the highway onramp.  It had one gas pump and the whole thing was maybe four hundred square feet."
    "I parked my truck and got out to stretch my legs."
    "Only one other vehicle was parked beside the entrance: a rusted old tractor with a cart on the back."
    "I went inside the store."
    "There wasn’t much to see; it smelled like an old attic and the aisles were cramped, filled with everything from gloves to granola."
    "I took a bottle of soda and a candy bar to the front to pay."
    ""
    show grandpa at right with fade
    "On a stool behind the counter was an old man reading a newspaper."
    "He didn’t look friendly but I struck up a conversation anyway."
    "I found out that he’d lived in Basin his whole life and had run this store for the last thirty years."
    " I wondered if he’d been married, maybe he still was. "
    nvl clear
    "I asked him if he knew anything about a place called Castle Hill Park."
    "He told me it was about twenty minutes out of Basin, up the main road."
    "He reached to a display on the counter and pulled out a map, photocopied and folded from a single piece of paper."
    "It had the highway exit  and the main street, as well as a few service roads that deviated further up."
    "He drew a path off one of the service roads and told me that was where the old trailhead was. "
    "He said it was an old campground they tried to restore about a decade ago."
    "There used to be some regulars who came by, but he hadn’t seen them in years."
    "He asked why I was interested in going there, he explained that there were better places to camp up the highway and the season was slow, so they weren’t likely to be crowded."
    "I had to explain the the estate sale and the trails guide. Even when I did he didn’t understand."
    nvl clear
    hide grandpa with fade
    "I thanked him and paid for my things. It wasn’t until I was back outside that I thought to ask him another question."
    show grandpa at right with fade
    "I went back in and when he looked up, visibly annoyed that I was back, I asked if he knew a man named Henry Burns. "
    "After a thoughtful moment, he said that he had. Henry would turn up a few times a year, and yes, always stayed in Castle Hill Park."
    "He described him as a lone hiker, though sometimes he had a friend with him."
    "I asked him why Henry would want to stay in an unkept park like Castle Hill."
    "The man told me, if he remembered right, there was a brook that poured over a rock formation nearby."
    "He told me it had a unique sound, something to do with cavities in the volcanic glass, he didn’t really understand. "
    "Henry had mentioned to him years ago that is was the only place he could get restful sleep."
    nvl clear
    "I asked him to show me where this brook was on my map, and he showed me."
    "It looked like it was only a short walk from the campsite. "
    "He didn’t need to draw it in, it was already marked with a black triangle and the name Devil’s Falls."
    "I smiled at the ominous name. Halloween was always my favorite holiday."
    "For a couple years we had hosted the costume parties in our neighborhood. "
    "I pushed the thought away. "
    nvl clear
    scene stoplight with fade
    "Back on the main road, I followed it to the north end of town. "
    "There it changed into a fire service road. "
    "My GPS was working, but nothing outside of Basin’s main road was in its memory."
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
    "Part of the roof had caved in and the whole south wall looked like it was about to follow."
    " Next to the station was a sign."
    nvl clear
    play sound "chimes.ogg"
    " ' CASTLE HILL PARK ' "
    nvl clear
    
    
    #scene2
    scene trail1 with fade
    "I shouldered my backpack and went for a closer look. At the edge of the woods was a metal barrier, presumably to keep off road traffic out."
    "The barrier was halfway open and so rusted that I suspected it was stuck permanently."
    "I thought about peeking into the old ranger station, but decided against it. Instead, I sidestepped the barrier and pressed further into the woods. I thought back to the gas station attendant; at least one person knew I was out here"
    " If something happened, I thought, he would bring help. Then again, if I didn’t return maybe he would assume I had just driven off."
    "As I went the trail got worse and worse. Fallen trees blocked the way and some sections were just overgrown, reduced to a game trail."
    "Eventually the path began to switch back and I gained elevation. It was late afternoon when I finally arrived on the top of what I could only assume was Castle Hill."
    nvl clear
    scene fire with fade
    "It was a small clearing to the left of the trail. I mistook it for a natural field before I saw the small circle of stones, a fire pit, barely peeking above the tall grass."
    "I got my tent setup and unpacked my bedroll. The little campsite was actually quite comfortable. There wasn’t a shortage of firewood, with felled branches over the campsite."
    "It was late afternoon and I had a fire going in short order. By the time I’d eaten and gotten to bed, I already felt fifteen years younger. The office and ex problems seemed miles away."
    "The next day I got to exploring my surroundings. It looked like the trail actually continued for a few miles. I realized it was possible that there were other campsites further down. After breakfast, I went to check them out."
    "There were three more campsites, about a quarter mile apart"
    " I stopped to survey each one, combing them as best as I could. I couldn’t say what I expected to find, but I was looking for anything."
    " Any sign that Henry Burns had been there. That this was in fact that dead man’s solitary place of refuge. "
    nvl clear
    scene trail2 with fade
    "The first site was the same, overgrown as the rest of the park. It had less grass than mine, but saplings and young trees had came up everywhere."
    "In another ten years, this would be indistinguishable from the rest of the forest. I couldn't find anything, even after a thorough check."
    nvl clear
    scene trail3 with fade
    "The next site was actually down behind Castle Hill. Like my own, it was covered in tall grass."
    play sound "crows.ogg"
    play sound "crow_noises.ogg"
    "As I walked in, a whole murder of crows darted from the grass."
    "They circled around me, cawing and driving. One came at me with claws outstretched."
    "I dodged to the side and it missed my face, snagging and tearing the shoulder of my jacket. The rest of them suddenly grew more daring and moved to attack. "
    "I gripped my walking stick with two hands; it was the only weapon I had. Another one circled around and as it came at me, I noticed that it was the biggest crow I’d ever seen."
    "When it came into range, I swung my staff like a baseball bat."
    play sound "thump.ogg"
    "It made contact and the bird was thrown away, a spinning mess of broken wings and feathers."
    "I heard it tumble into the brush beyond the treeline. "
    nvl clear
    "I had to take a few more swings, grazing the more nimble birds, before they retreated into the trees."
    "I spun around, brandishing my weapon at the tree tops and branches where they perched, quietly watching."
    "In the silence I could hear the one I’d knocked away flopping and mewing beyond the treeline."
    "I was going to turn and leave, but I noticed there was clearing in the tall grass, where the crows had sprung from. "
    " I moved closer, keeping an eye on the birds, and felt my stomach drop."
    "I had seen a lot of things, but this one was so abnormal I had to blink just to make sure I wasn’t dreaming."
    "When I got closer, I saw that the clearing wasn’t natural at all."
    nvl clear
    play sound "chimes.ogg"
    "It was a perfect circle of depressed grass, without rhyme or reason."
    "Sometimes we’d find fairy circles in the woods as kids, strange rings where nothing would grow."
    "As I child I remember discovering what caused them. It wasn’t something supernatural like a fairy’s home, but a growth of underground fungus."
    ""
    "Staring at this circle in the grass I could find no explanation. It was crushed, not simply dead. I noticed the smell while I was trying to make sense of it."
    "Some of the grass was scorched, though not completely burned, but that wasn’t the strangest part."
    play sound "chimes.ogg"
    "Strewn around the circle were five, maybe six animal carcases."
    "Rabbits, I thought, or possibly large squirrels."
    "It was hard to tell because each one of them lay headless and flayed."
    "It was hard to tell without getting closer, which I refused to do, but it looked like they had been cut open along the back and, along with the heads their whole spinal cords were removed."
    "It all made me sick."
    play sound "crow_noises.ogg"
    "The crows started to caw again, threatening that I should leave."
    "I didn’t look back, but could hear them flapping behind me as they swarmed the mutilated remains."
    stop sound
    nvl clear
    scene trail4 with fade
    "The last campsite was a considerable walk from the rest. I was thankful for this, I needed a some time to recover."
    "My first thought was some angry kid was hiding out here, but that didn’t make any sense. "
    "I didn’t think anybody, even a sick person, would do that sort of thing outside of movies."
    "As I went, the trail curved around the hill."
    "I was actually closer to my tent now, because of the roundabout path."
    "Eventually I noticed the sound of running water and quickly found the last campsite."
    " Checking the map from the gas station, the campsite was unmarked but happened to be right next to Devil’s falls. "
    "The brook was only a few feet beyond the treeline, I pushed through and stood on the shore. "
    "The small waterfall tumbled over some spiky black rocks. I listened for a few minutes but I couldn’t hear anything special about it. That suited me just fine, though. "
    nvl clear
    scene trail5 with fade
    "I didn’t want to walk back the way I came, at least not yet, so I pressed on. I thought I saw a clearing, so I cut through the woods and was surprised to emerge next to my Ranger. "
    "I decided this meant two things. First, the trail was a loop, and second, that the map I had couldn’t entirely be trusted."
    scene cg1 with fade
    "I walked back to my tent, relieved to be back before dark."    
    " I set a fire and cooked some dinner. While my hotdog roasted, I tried not to think about that fairy circle, if that’s what it was."
    "I’d brought a flask with me and now seemed like a good time for a drink. "
    "I hadn't noticed, but there was the faint roaring of the wind that provided the backdrop to crickets chirping."
    "I closed my eyes a moment, enjoying the calm atmosphere."
    
    #scene3
    scene trail1 with fade
    "I stayed for two more days, relaxing and hiking around the park and I didn’t have any more trouble with the wildlife."
    "There was another trail system close by, I had to bushwhack about about a thousand feet to get there, but spent the rest of the daytime exploring along them."
    "One thing I discovered was that Devil’s falls actually changed timbre from day-to-day. When I’d first visited, it sounded like a normal brook, but now there was a distinct overtone to the bubbling."
    play sound "chimes.ogg"
    "I didn’t see much wildlife, but one morning, I did find a set of tracks through my campsite."
    play sound "raining.ogg"
    "I didn’t see much wildlife, but one morning, I did find a set of tracks through my campsite."
    "I didn’t pay any attention at the time, but now I can see the reason the tracks were so strange. Half the prints were backwards, like two animals stuck together."
    "Whatever it was, it wasn’t natural."
    ""
    " I decided to be more cautious, especially because I’d already had to fight off animals. I went back to examine the tracks later, but they were washed away."
    "My writing hadn’t gone as well as I hoped, but progress was steady"
    scene cg2 with fade
    "I’d used a fair amount of gas over the last few days, hiking back to the parking lot and idling my truck a few hours while my laptop charged in the cab."
    "I was also running low on water, and the iodine tablets I’d brought made the brookwater taste awful."
    "All this made me decide it was time for a take a trip back into Basin."
    nvl clear
    scene road2 with fade
    "It was late afternoon when I left and I decided there would be enough time to hit the store and be back before dark. I started the truck and eased it into a three point turn to get out of the lot."
    "Somehow the road seemed further away, though I knew that was impossible."
    "Still, after a while I was back on the main road heading into town."
    "When I got to Basin, I passed all the quiet houses and the dark municipal building again, arriving at the gas station by the highway on ramp."
    nvl clear
    scene stars1 with fade
    "I pulled in and found the same tractor parked beside the building. There was a white van at the pump."
    "I walked into the gas station, looking around for the attendant I’d spoken to earlier that week."
    "Maybe, I thought, he had somebody else to tend things part time. I didn’t see anybody inside, but I picked out a candy bar and another soda, it has been a while since I’d eaten anything sweet."
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
    "Even as I told myself that, I knew it wasn’t true."
    "What I should have done, had I known what I know now, was to push that van out of the way, fill up my truck and leave immediately."
    "I even had a hose with me."
    "If I had to, I could siphon some tanks. Even if I didn’t do any of that, I probably still had enough gas to get to the closest town. "
    nvl clear
    scene trail_dark with fade
    "But I didn’t do any of that. Instead, I left the gas station, turned around and drove back to my campsite."
    "I should have ran, but a sense of rationality was prevailing."
    "Those years of experience that taught me to keep a level head, to take the unexpected in stride, were blinding me to the danger."
    play sound "chimes.ogg"
    "Even as I hiked back up Castle Hill that night, I could sense something watching me."
    "It was a struggle to keep my flashlight forward and my legs from breaking into a run."
    "When I got back to my tent, I slipped inside and immediately killed my flashlight."
    nvl clear
    window hide
    scene stars2 with fade

    
    #SCENE3
    
    
    
    

    

    
    
    return
