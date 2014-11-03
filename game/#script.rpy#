# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
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
    
    show text "UI Art: Andeh" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return
        
    ##GAME START
label start:
   scene dark
   "My name is Ashley McGlothlin. I'm a thirty-eight year old office worker and part time writer. In the summer of 2009, after the end of a long relationship, I decided to take a sabbatical. I lived in Ellsworth, a suburb of River City, which was the only city for about a hundred miles around. Even though my work had taken me to a drab office in South Dakota, the intervening years couldn't fully strip away my love of the outdoors. I grew up as a plucky girl who played explorer in the woods of Northern Oregon. It was time to return to my roots. "
   scene bg kitchen
   "In addition to the neglected adventurer in me, I also coveted the chance to work on my writing, something that had fallen to the wayside during more stressful proceedings."
    #scene bg kitchen dining
   "I hadn't decided on a destination yet when, on the drive home from the office, I saw a sign for an estate auction happening that afternoon. "
   nvl clear
   "Being a bit of a treasure hunter, I decided to go. The event was on the other side of town and in a neighborhood that was known for its bigger, richer houses."
   "When I arrived, the auctioneer was on the lawn in front of an audience in folding chairs. They were bidding on various statues and artifacts the deceased had acquired in his travels. I watched for a little while, but when a single oil painting sold for over two thousand dollars, I knew the crowd was too rich for my blood."
   "Wandering around the tables covered with trinkets and small pieces of furniture, I noticed that the deceased had a very nice collection of camping gear. I picked through it, most of it was well worn but a few coats and pairs of raingear were in good condition. I would have bought them, but they were all in men's sizes. Instead, I settled on a single wrinkled book, priced for a dollar and left next to a table full of old ice climbing gear. It was a guide to the trails and parks of the Dakotas."
   "That night, while paging through faded descriptions of serene lakes and hidden hot springs, I found a reference to an obscure campground nestled inside the Black Hills. It wasn't a formal entry in the in the guide book. Instead, written in the margins, was directions to a place called Castle Hill Park. "
   "Next to the writing was a small map, showing where a trail opened between the trees on the shoulder of a rural highway and led into an unnamed forest. At first I figured it was a recent addition, after all the book had been published in the mid 1970s and was easily outdated. I quickly flipped through the rest of the book, looking for any other handwritten entries. There were none until I reached the last few pages. "
   nvl clear
   "At the end, after the acknowledgements and lists of revisions, the publisher had left several ruled pages so that the reader might keep a log of the places they've visited. The earliest entry was from 1978, a visit to the trails behind Mt. Rushmore. This was followed by years of hiking and camping at nearly every park in the region. It wasn't until September 28, 1991 when the first entry for Castle Hill Park appeared. Then on May 2nd, 1994, and again in late March of 1995. After that, at least once every single year until december 31st, 1999. After that, entries became sparse. Between the years of 2001 and 2005 there wasn't a single trip recorded until September 12th, 2006 when he returned one final time to Castle Hill Park."
   "I researched Castle Hill Park on the internet, and in other guidebooks. I even sought out revisions specifically from the nineties, thinking the park might have been abandoned after a decade or so. It was all fruitless. As far as every reference was concerned, Castle Hill Park simply didn't exist."
   "In a move of desperation, I called the estate which I'd purchased the map from. The paralegal who answered the phone informed me that the gentlemen who had passed away had kept to himself, especially after his wife passed before him. He said he didn't think any of his children would be able to answer specific questions about a camping but promised to ask them. I don't think he ever did."
   "The old man, whose name I found out was Henry Albert Burns, continued to return to Castle Hill Park until it was the single most visited place in his log. "
   "This whole situation sat in the back of my mind while I worried about more present things. The divorce was going poorly. After ten years married there were so many complications, even the simplest proposals were met with objections and sustainments and postponements. I couldn't decide if the lawyers were earning their pay or robbing me blind."
   nvl clear
   "We'd been separated for a year and proceedings had just entered into the fifth month. The end was in sight though, and just when I'd forgotten about that Henry Burns, his name came up on the evening news."
   "The family, it seems, was in the middle of a settlement of their own. It seems that the auction I had seen was for his third home. One of his children, a step child, had been shut out illegally and now the whole probate was in question. The report was over and I was about to turn off the television when they announced there would be a brief biography on Henry after the normal newscast."
   "It turns out he owned several small manufacturing companies and sat on the board of a regional oilfield contractor. He was known to be secretive, often disappearing without notice. The public knew him from the evening news. Twice in the 1990s, he was reported missing by his wife and colleges, only to turn up a few weeks later, hitchhiking home. The story ended up in Reader's Digest under the humor column."
   "I didn't have to research the old news reports to know, but I did anyway. When I cross referenced the dates of the reports and the old trails guide, it was a perfect match. I sat in my room looking at the log. I had the punchline a Jay Leno joke, and as far as I could tell I was the only one who knew."
   "Eventually the legal proceedings were wrapped up. I notified my office that I would be out and started planning my sabbatical. After purchasing a new tent and some other things, I loaded everything into my Ranger, which I'd almost lost when the judge assumed was my ex-husband's vehicle, and pulled out onto the interstate."
   nvl clear
   "Maybe it was the sense of secrecy, or mystery, or maybe I was just looking for an excuse to get away. Whatever the reason, I knew where I was going. "
   
   
   scene cg2
   "Once you add a story, pictures, and music, you can release it to the world!"
   return
