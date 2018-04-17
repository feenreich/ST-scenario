init python hide:
    config.developer = True

define commie = FakePerson("???", "jack")
define prc = FakePerson("China", "jack")
define roc = FakePerson("China", "john")
define roc_c = FakePerson("China", "cornelia")
define tw = FakePerson("Taiwan","cornelia")

label scenario_roc:
    $ flag_tw = 0
    $ flag_cn = 0
    $ flag_jp = 0
    $ flag_usa = 0
    $ flag_roc = 0
    outfit john casual
    scene example_bg street night
    play music bgm_mirage

    show john a_0 with dissolve
    roc "I'm China. This is a story between me and my lovely wife Taiwan."

    hide john
    show cornelia a_0 at center
    tw "Hi, my name is Taiwan, this is a story between me and ...{q}China{/q}."

    show cornelia a_5
    tw "..."

    show cornelia a_3
    play sound sfx_explosion
    tw "and, I'm {i}not{/i} his freaking wife."

    show cornelia b_5 at centerleft with easeoutleft
    show john a_3 at centerright, faceleft with ease
    roc "But you said you belong to {i}Me{/i}."
    tw "I {i}didn't!!!!!{/i}"

    hide john
    show cornelia a_1
    tw "Okay let's start."

    scene black with dissolve
    stop music fadeout 1.5

    roc "This is a long story, back to when I was still {i}me{/i}."
    roc "I lived with my family, my mom and sister."
    roc "As a normal high school student, with few friends. Except that we are pretty wealth, since my dad owns a company."
    roc "However he past to a car accident when I was small. My mom decides to transfer of management rights to other relatives."
    roc "In exchange we got plenty of real estate, and I can probably live without working during my entire life."
    roc "If {i}that{/i} didn't happen..."

    scene shrine day
    play music bgm_dark_fog

    show john a_7 at centerleft with easeinleft
    show jack a_9 at centerright with easeinright
    roc "What did you just say? Uncle jack. I am a descent of some great magician and so does you?"
    commie "Yes, but in general the spell requires you to chant the right incantation."

    show john a_0
    roc "Hum...I still cannot believe this."

    show jack a_3
    commie "Well you don't need to."

    play sound sfx_spell
    commie "{spell}Relinquo Spiritus!!{/spell}"

    clone alex john
    hide john
    show alex a_0 at centerleft

    exspirit jack a_3

    show jackGhost a_1
    commie "haha"

    possess jack alex a_4
    hide jack
    hide alex

    show john a_1 at centerleft
    commie "HaHaHaHaHaHaHaHaHa"

    show john a_4 at center with ease

    think "Why am I laughing?"
    think "Wait ... is he ... in my body ?!"

    show john a_7
    roc "Get out from my body! Why are you doing this?"

    show jack a_13 at center
    commie "How about {i}YOU{/i} get out!"

    play sound sfx_spell
    commie "{spell}Relinquo vestra Spiritus!!{/spell}"

    exspirit john a_15

    show johnGhost a_4 at centerleft with ease
    roc "Oh NO!!!"

    show jack a_0 at center
    commie "Wow I feel so young and energetic!"

    show jack a_1
    commie "HAHAHAHAHAHAHAHAHA"

    show johnGhost at faceleft with dissolve
    show johnGhost at faceright with ease:
        xalign 0.45
        yalign 0
    show johnGhost at centerleft, faceright with ease

    show jack a_10
    commie "You have no idea how I suffered from those pesky Witch-Hunters these years. {w=1.0}And how I felt about your mom, whose betrayal lead to my miserable life!"

    roc "What are you talking about!?"

    show jack a_3
    commie "Looks like {b}this body{/b} has even greater potential than my origin one!"

    show johnGhost at faceleft with dissolve
    show johnGhost at faceright with ease:
        xalign 0.45
        yalign 0
    show johnGhost at centerleft, faceright with ease
    roc "Why can't I get back?!"

    show jack a_2
    commie "Stop trying! By the way, you'd better find some body to reside before sun set."

    show jack a_1
    commie "{i}They{/i} are not friendly against wandering ghosts."

    show jack a_3
    commie "But even if you vanish somewhere, I couldn't care less anyway now, haha!"

    show johnGhost at faceleft
    roc "Oh no ... this is {b}bad{/b}!"

    scene black with dissolve
    stop music fadeout 1.5
    roc "I have to find someone -{i}anyone{/i} soon, or I will die!"

    scene bg school entrance day
    play music bgm_blown_away

    show cornelia a_2 at centerleft
    tw "Finally the school is over~"

    show johnGhost a_4 at centerright with easeinright
    roc "Finally there's {i}some body{/i}!"

    show cornelia a_8
    tw "?!"

    show johnGhost a_11
    roc "SORRY!!!"

    possess john cornelia b_3
    hide john

    show cornelia a_6 at centerleft
    tw "What...is happening"

    show cornelia a_8 at center with ease
    roc_c "Thank God..."

    show cornelia a_7
    tw "Why my mouth is moving!?"

    show cornelia a_3
    play sound sfx_spell
    roc_c "{spell}SHUT UP AND SLEEP!{/spell}"

    show cornelia a_6
    tw "Zzz......"

    show cornelia a_7
    think "That ... actually worked?"

    show cornelia a_5
    think "Whatever. It's not time for this. I need to find {i}HIM{/i}!"

#    show cornelia a_5 at centerleft, faceleft with move
#    play sound sfx_fall
    show cornelia b_3:
        rotate_pad False
        block:
            parallel:
                linear 0.05 yanchor 0.4
            parallel:
                linear 0.05 ypos 0.53
        block:
            parallel:
                linear 0.3 rotate 60
            parallel:
                linear 0.3 xpos 0.54
            parallel:
                linear 0.3 ypos 0.87
    with vpunch
    play sound sfx_whack
    roc_c "Aweee!"
    "Right after making my first step, I fell down in a way that I've never experienced.{w=0.5} The balance of this body is totally different from my own."

    show cornelia a_3:
        pause 2.2
        rotate_pad False
        block:
            parallel:
                linear 0.3 rotate 0
            parallel:
                linear 0.3 xpos 0.55
            parallel:
                linear 0.3 ypos 0.6
    with MoveTransition(1.5)
#    show cornelia a_5 at centerleft with MoveTransition(1.5)
    "I barely get up from my tiny arms."

    show cornelia a_0
    roc_c "Wow these hands are ... {i}small{/i}."

    show cornelia a_5
    "A familiar high-pitched feminine voice run through my skull in a weird fashion. Is someone talking?"

    show cornelia a_1
    roc_c "And the school gate looks {i}huge{/i}!"

    show cornelia a_5 at faceright with ease
    "Here she is again."

    show cornelia a_1 at faceleft with ease
    show cornelia a_1 at faceright with ease
    show cornelia a_0 at faceleft with ease
    show cornelia a_3

    think ".{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}"
    roc_c "Is that ... {b}me{/b}?"
    "It is not until this second that I suddenly notice the wind climbing through my half-naked thighs. As I glanced down"

    show cornelia a_7
    think "Am I wearing a skirt? I actually picked a girl's body?{w=0.5} Are these boobs for real?!"
    "I feel a bit thrilled. But then suddenly trembled with fright, as an unpleasant thought comes up."
    think "{size=-5}Will I be stuck like this?{/size}"

    show cornelia b_5 faceleft
    think "NO WAY I'm staying like this, I gotta find {i}HIM{/i} as soon as possible!"
    "I started running, barely maintaining the balance. I wonder if this really counts as a run since each step of mine was so small and I can't really accelerate."
    play sound sfx_running

    scene black with dissolve
    stop music fadeout 1.5

    scene bg main house dark
    play music bgm_mirage

    show jack a_0 at center
    commie "So this is {i}my{/i} house now."

    show jack a_1
    commie "I'm a rich, young boy {i}again{/i}, haha! Let me examine some crucial memories first..."

    show cornelia b_3 at centerright, faceleft with easeinright
    roc_c "WAIT!!!!!!!"

    show jack a_0
    commie "What's up, Taiwan?"

    show cornelia a_7
    roc_c "Give my body back you jerk!"

    show jack a_0
    commie "I have no idea what you're talking about, Taiwan?"

    show cornelia a_3
    roc_c "Stop calling me {i}that{/i}! I'm {b}China{/b}!"

    show jack a_3
    commie "Oh, if you are China, then who am {b}I{/b}, then?"

    show cornelia a_5
    roc_c "Stop impersonating me Jack you stupid fucker. I don't know how you did that but if you don't switch me back {b}now{/b}, I will definitely tell everyone that..."

    show jack a_4
    show pentagram as pentagram behind jack at Position(pos=(placement_of(jack).xpos, 0.5))
    play sound sfx_spell

    show jack a_8
    commie "{spell}Verba obedi.{/spell}{w=1} You will reference me as 'China' always!"

    hide pentagram with dissolve

    show cornelia a_6
    "I felt dizzy and empty for a moment, but soon recovered. Did anything just happened?"

    play music bgm_dub_feral

    show cornelia a_5
    roc_c "I'll tell everyone that you are {s}Jack{/s} China and I am the real China!"

    show cornelia a_7
    roc_c "No I mean you are {s}Jack{/s} China and I {w=1}-{size=+5}WHAT{/size}"

    show cornelia a_8
    roc_c "What have you done again!?"

    outfit sandra casual

    show sandra a_0 at centerleft, faceright with easeinleft
    sandra "What's up China? I told you that if you're going home late you should...{w=0.5}Hey Taiwan, did you come with China here?"

    show cornelia a_1
    roc_c "Hey Mom! {i}This guy{/i} used some magic trick on me and took over my body. I don't know the reason but he's probably trying to steal all my life. {size=-5}I know it's hard to belive but...{/size}"

    show sandra a_3
    show cornelia a_4
    "As my mom's expression gets more and more sophiscated, I realized that how ridiculous I sounded."

    sandra "......"

    show jack a_1
    prc "Hey mom, don't worry, my new girlfriend was just playing a little game with me and got a little hyped."

    show sandra a_1
    sandra "I {i}knew{/i} this day is coming! My boy finally grown up."
    "A radiant smile appeared on my mom's face."

    show cornelia a_7
    roc_c "{size=+5}I'm not his girlfriend! I {b}am{/b} China and he is {b}{s}not{/s}{/b} China!!!{/size}{w=0.5} I can prove it by answering anything about China!"

    show sandra b_1
    sandra "Oh how cute are you! Take it easy Taiwan, now if you insist on playing this, why don't you come inside and have a cup of coffee?"

    show cornelia a_4
    "Suddenly an embarrassment comes to me. She's clearly fooled by {s}Jack{/s} China and there's little way I could assert my identity right now.{w=0.5} What's even worse is that she thinks I'm my own girlfriend now!"
    roc_c "{size=-5}He is not...{/size} no, thanks for the invitation but I need to go home now."

    show sandra b_9
    sandra "It's okay, it's sort of late now. Do you need a ride?"

    show cornelia a_7
    roc_c "Don't worry! My home is ... near."
    think "It's {i}right here{/i} actually."

    show sandra a_1
    sandra "Ok, just be careful. Let's get in, China. {size=-5}We will have {b}a lot{/b} to talk about.{/size}"

    show jack a_1
    prc "Bye {b}dear{/b}."

    "He winked at me and blew a kiss."

    show cornelia a_3 blush
    "I can't help burning my face with pure wrath, but my mom will probably assume the wrong reason."

    hide sandra with easeoutleft
    hide jack with easeoutleft
    stop music fadeout 2

    show cornelia a_0 at center with ease
    "I standed still for a whole few minutes, after staring 'me' walking into my own house with a smirk."
    think "What now?"
    "I knew Taiwan long time ago, a lovely girl going through the same school as me. She's probably the most or second popular girl in the grade."
    "Sharing some classes and friends, we have even hung out a few times. But besides that, we're just acquaintances. All I know is that she's been dating Japan recently, so does everyone."

    show cornelia a_7
    think "Does that mean {b}I{/b} am dating Japan now? Arrrgh that's fucking disgusting. {w=1}But my mom thinks I'm dating {b}me{/b}... This is getting complicated."

    show cornelia a_3
    think "Anyway, I gotta take a rest somewhere. {w=0.5}Where does she live? Maybe I should try {i}this{/i}."
    "I try to redo the maneuver that I have taken before, by instinction."

    show cornelia a_5
    play sound sfx_spell
    roc_c "{spell}Wake up!{/spell}"

    play music bgm_marty_gots_a_plan

    show cornelia a_4
    "The tension of my muscle suddenly rose. I can feel the control over my body was taking away bit by bit. {w=1}{b}It worked!{/b}"

    show cornelia a_8
    tw "Why...am I here? It should not be so late...am I daydreaming?"

    show cornelia a_1
    roc_c "Hey Taiwan, I'm sorry for borrowing your body like this... but I'll explain everything to you after getting back to your home. I promise."

    show cornelia a_7
    tw "What?! Somebody's in MY BODY? {size=+5}{b}GET OUT YOU PERVERT!!!{/b}{/size}"

    show cornelia b_3:
        xalign 0.45
        linear 1.0 xalign 0.55
        faceleft
        linear 1.0 xalign 0.45
        faceright
        repeat
    with vpunch

    roc_c "STAROP!!IAU WILFLFA EXPLARATIHIN!"

    "I felt almost crumbled fighting against each other for the control of the body. I can't even speak normally."

    menu:
        think "This {b}must{/b} be dealt with, I've had enough of these bullshit allday!"
        "Let her control the body":
            placeholder
        "Use my power":
            show cornelia a_5 at center with ease
            play sound sfx_spell
            show cornelia a_0
            roc_c "{spell}Let me control and get your memories!{/spell}"
            "While the moving of my body finally stopped, I can still feel the quivering of my feet and the anger piling up my stomach."
            "Part of me felt bad, but I cannot just let her do whatever she want. Afterall, my existence itself is in a huge pinch!"
#            roc_c "{b}You will control the body only when I allow it.{w=1} You will go home now.{/b}"

    scene black with dissolve
    stop music fadeout 2

    show cornelia a_8 at center with vpunch
    "A lot of images and voices flooded into my mind. I can hardly perceive them as any meaningful information. My vision was twisted and I felt nausea. I almost regretted the choice immediately."
    "Right before I was about to vomit, the world regains its order and turned into tranquility."

    scene bg main house dark with dissolve

    "I gave a query to my brain about {b}home{/b}. Some vague images flowed up one by one, almost like a 3D google map."
    think "Guess the magic worked, again."
    hide cornelia

    scene bg city walkway night with dissolve
    scene black with dissolve

    "Following the VR-map, I reached the destination after about a quarter."

    scene bg neighborhood2 night
    show cornelia a_0 at center
#    tw "{i}Fine. I hope you really have a good excuse for this, asshole.{/i}"
    "It is a house of mediocre size. Somehow it looked familiar, although it's the first time I have been here. I took out the key inside my bag and entered the house by instinction."
    "I quickly slipped into my room - Taiwan's room, avoiding possible encounter of her family."
#    "I smiled wryly, letting my leg starts moving on its own. It felt like riding a tandem bike without pedalling. I felt really tired and let my consciouness go."
    play sound sfx_sliding_door_open
    scene bg yui room night table
    play music bgm_comfortable_mystery
    show cornelia a_0 at center

    think "What a long day..."
    "It has been such a bizarre day that I finally get the leisure to ruminate my situation."
    think "My body was stolen, by {s}Jack{/s} China, who claims himself to be a wizard as well as myself. He also convinced my mom that he is me and {b}I{/b} am his girlfriend."

    show cornelia a_4
    think "And I am now ... Taiwan, a girl I am not even familiar with."
    "Walking up to a mirror of my height, I saw a solemn girl frowning at me. I waved to her and she waves back simultaneously. She sighed as I heard the voice."

    show cornelia a_5
    "Sensations flowing in as I finally focus into myself. The school uniform feels tighter than usual, except that the lower part only feels empty."
    "The attachment around my breasts is even tighter, which make me uncomfortable. I start to strip. The bra takes some work, but the memory of Taiwan helps."

    outfit cornelia none
    show cornelia b_7
    "A beautiful dainty body appears right in front of me in the mirror."
    think "Gosh I am gorgeous... I mean {i}she{/i} is."

    show cornelia b_9
    "I almost stopped breathing for a while. This is the first time I see a female body naked in reality, well excluding my mom. But also in first-person view."
    "She is petite but also curvaceous. The boobs is of mediocre size that can be held in one hand - my original hand, on top of it were two little cute pink nipples standing proudly showing of their existence."

    show cornelia a_1
    "However, there is no sign of erection. I looked down only seeing nothing between my crotch."

    stop music fadeout 2
    menu:
        think "I should"

        "Explore more":
            $ flag_tw += 1
            play music bgm_easy_lemon

            show cornelia a_9
            "Besides the absent of my old partner, I can feel a drop of liquid on my thigh - my ... pussy is soaking wet!"

            think "I have to do this."

            "Since I don't have the technique nor experience of pleasing a woman, I searched through the memory of Taiwan."

            show cornelia a_6 with vpunch
            think "Argh.."
            "Flooding in my mind was the sight of Japan, naked, pounding against me heavily on the bed, again and again. I - Taiwan screamed out of both pleasure and pain. Looks like this is her first time scenario."
            "I moaned while surrounding his wide back with my slim arms."

            show cornelia b_2
            roc_c "That was a good night!"

            show cornelia a_3 with hpunch
            roc_c "NO! THAT'S FUCKING DISGUSTING!"
            "I shaked my head furiously, getting rid of the images. Looks like she's never do it herself but with Japan. I felt vomit."

            show cornelia a_2
            think "Well guess I have to try it myself then."

            show cornelia a_0
            "I slipped my finger onto the bulge, lying on the place supposed to be my penis."
            think "This is ... clitoris?"

            show cornelia a_9:
                block:
                    easein 1.8 xpos 0.49
                    easein 1.8 xpos 0.50
                    easein 1.8 xpos 0.51
                    easein 1.8 xpos 0.50
                    repeat

            roc_c "Ugh...{w=1}ugh..."
            "As I caress it, an electronic-alike sensation flow through. It's like the glans, but more sensitive and soft."
            show cornelia a_3
            roc_c "Auch!"
            "A prickling emerges as I put too much force rubbing it. Looks like it is much more delicate than my original counterpart."
            show cornelia a_1
            think "I should be more careful."
            show cornelia a_9
            roc_c "Unmm...{w=1}yes...{w=1}yes..."
            "My mouth moved itself unconsciously, but I'm not bothered."
            roc_c "More...{w=1}more..."
            "My hands accelerate according to my desire."

            show cornelia a_9:
                block:
                    easein 2.8 xpos 0.49
                    easein 2.8 xpos 0.50
                    easein 2.8 xpos 0.51
                    easein 2.8 xpos 0.50
                    repeat
            roc_c "Ahhhnmnmmmm~~"
            "I quivered as the feeling adding up. A huge spike of bliss went through my head."

            hide cornelia
            scene black with dissolve
            "I reached orgasm, as a female, as Taiwan."
            stop music fadeout 1.5

            scene bg yui room night table with dissolve
            show cornelia a_1 at center
            "Although there is no significant physical change around my body, I suddenly lost the will to keep rubbing."
            think "I heard that female are able to cum multiple times...maybe I should try the vagina part as well?"
            "I looked at my crack and enlarged it with my fingers. It's certainly tempting, but I'm kinda terrified by the idea to put something into it."
            show cornelia a_8
            "Especially the {i}last time{/i} it was that fucking guy ... Japan's {b}stuff.{/b} According to her memory."
            show cornelia b_3
            roc_c "I'm definitely breaking up with him!"


        "Get dressed":
            $ flag_tw = 0
            show cornelia a_5
            think "It is not righteous to do this, I have already done something horrible to her. The moment I find a way to my own body, I will leave and apologize to her."

    play music bgm_mirage
    show cornelia a_5
    think "Wait, maybe I can just leave the body and get a {i}boy{/i}'s body instead?"
    show cornelia a_0
    think "{b}{size=+5}Leave!{/size}{/b}"
    show cornelia a_7
    roc_c "{b}{size=+5}Leave!{/size}{/b}"
    show cornelia a_0
    think "Okay I must looked like an idiot."
    "Maybe it's that I don't know the right chanting, or my powers are restricted. It didnt' work. I gave up after a few try."
    think "It's getting cold in the night, I should find something to wear."

    play sound sfx_sizzle
    outfit cornelia pajamas
    show cornelia a_1 at center

    "It is not hard to find the pajamas Taiwan always wear through the memory. The silky soft touch was really nice, unlike my own one."
    show cornelia a_2
    think "This feels so good!"
    "Is it only she, or the female pajamas are just softer overall? I pondered."

    show cornelia a_6
    roc_c "Arrrrmmmmm"
    "A large yawning sound reminds me of how tired I am. I should go to bed, there is still school tomorrow."

    show cornelia a_0
    think "Am I gonna go to school as {i}she{/i}? It seems the only choice I have but...{w=0.5}{b}GOSH{/b}, whatever. I'll just go to bed."

    show cornelia a_6
    think "Maybe the whole day has been just a weird dream and I'll wake up just as everyday. I can share the tale to Katrina or Kiyoshi, they might mock on me but I won't mind that much, I guess."
    nvl clear
    nvl_narrator "I closed the light and laid to bed. The scent of Taiwan on the pillow is both novel and familar."
    if flag_tw > 0:
        nvl_narrator "I recalled Japan laid with me on the very same place, hugging me tightly."
        nvl_narrator "That jerk always bullies me at school...has a tender side as well."
        nvl_narrator "Maybe its Taiwan's soul inside me effecting, he's image does not look hateful as usual."
        nvl_narrator "However I still make up my mind to get my body back as soon as possible."
#    nvl_narrator "I made up my mind to get my body back"
    else:
        nvl_narrator "The bed is comfortable, I fell asleep right away."

    stop music fadeout 1.5
    scene black with dissolve
    ".{w=0.5}.{w=0.5}.{w=0.5}"

    scene bg yui room day table with dissolve
    play music bgm_airport_lounge
    ".{w=0.5}.{w=0.5}.{w=0.5}"

    show cornelia a_2 at center
    roc_c "*Yawn"
    "I stretched my body."
    show cornelia b_2
    roc_c "What a nice morning."
    "Warming sunshine pierces through the curtain. I felt cozy but in the mean time."
    show cornelia a_5
    roc_c "Do I have a curtain?..."
    show cornelia a_7
    think "Oh no! This is not my room. I haven't get my body back from that asshole yet!"
    show cornelia a_4
    "I quickly put on the school uniform...Taiwan's of course. The white stockings is quite repelling, but I feel like putting the usual suit of her might be better so I endured it."
    show cornelia a_3
    "Again the tightening bra make me itchy that I almost wanted to skip it."
    outfit cornelia uniform
    show cornelia a_5
    think "It's really harsh for girls to wear them {b}every day{/b}. My - I mean her breasts are not huge but still it's not pleasing. Maybe I'll just wear the sports bra later on."
    show cornelia b_1
    "My hands tied my hair to the double ponytail naturally."
    show cornelia a_7
    think "Is Taiwan inside of me doing this? What happened to her actually, is she sleeping or aware of all of these?"
    "Anyway, I should departure. I don't want to confront her parents or siblings yet, even if that means skipping the breakfast. What class does she have today?..."
    "I examined the memory. The schedule of her usual day came into my mind."
    show cornelia a_0 with vpunch
    think "I see...let's go."
    play sound sfx_door_open
    stop music fadeout 2


    scene bg school entrance day with dissolve
    play music bgm_cut_and_run

    show jack a_0 at center
    show kiyoshi a_0 at centerright, faceleft
    show cornelia b_0 at centerleft with easeinleft
    "Upon reaching the school entrance, I saw two familiar faces - one of my best male friend Kiyosi and the one I've only seen in the mirror before yesterday."
    show cornelia b_3
    roc_c "{size=+5}Hey, what the heck are {i}you{/i} doing here!{/size}"
    show kiyoshi a_3
    show jack a_1 at faceleft
    prc "Morning, dear. I know you would've missed me so much."
    show kiyoshi a_1
    kiyoshi "I can't believe it is true, C-man. You really take Taiwan from Japan! Looks like I underestimated your Man-Power."
    roc_c "Don't call me C-man, I've told you many many times."
    show kiyoshi a_2
    kiyoshi "Ha C-man, she's acting so well just as you said!{w=1} Morning mi-lady Taiwan - or should I call you C-woman?"
    roc_c "I'm {b}NOT{/b} a woman and I'm not acting! This guy is just a body stealer, I promise that I can prove it! Just ask him anything only I-China and you knows, he wouldn't be able to answer but {b}I{/b} can!"
    show kiyoshi a_0
    kiyoshi "Humm, really interesting C-man. How do you come up with this sort of play without my wisdom advice?"
    show jack a_1
    prc "Well while I was left idle and you're busy dealing with the lawn mower trying to communicate with alien last week. By the way only you and me knows the episode right?"
    show kiyoshi a_1
    kiyoshi "Ha, sasuga my C-man. Lady Taiwan you just missed one point!"
    show cornelia a_8
    roc_c "No...he must have stalked into my memory, that's it! He is really not {b}me{/b}! You gotta believe me ... Kiy-master!"
    show kiyoshi a_1 with vpunch
    kiyoshi "Wow, finally my expertise has made its fame to the entire school! Nice try Taiwan-chan. Let me ask...what is the lawn-mower's color?"
    show cornelia a_2
    think "Nice job Kiyoshi, I can finally prove my identity! A normal people wouldn't have belived me but its Kiyoshi - the sci-fi maniac Kiymaster!"
    roc_c "The color is green! Also you carved a Chinese Character meaning 'ten thousand' on the turf. You gotta definitely belive me now, right?"
    show jack a_3
    show kiyoshi a_3
    kiyoshi "Wow, I didn't expect you to be so detailed! However you have lost Fake-China-chan, the lawn mower is blue and I what carved is 'dragon'!"
    show kiyoshi a_0
    kiyoshi "I can still call you Miss-China though, if you want, mi-lady."
    show cornelia a_7
    think "What?! This cannot be, I clearly remembered...it's just last week!"
    "I saw a smirk on 'China's face."
    think "I suppose he did {i}something{/i} on Kiyoshi, maybe modified his memory with magic or something like that. However there's no way to verify it."
    show cornelia a_4
    think "Great, now I have no way to prove myself without using the power. But I don't know how to use it besides commanding Taiwan through out pure will."
    show cornelia a_5
    think "Maybe it's because my soul is in her body so no incantation is required? sounds Logic."
    show cornelia a_3
    "Anyway, I have lost the incentive to stay with them. I growled at 'China' and walked straight pass them into the school."
    roc_c "You'll REGRET it!"
    show cornelia b_3 at faceleft
    hide cornelia with easeoutleft

    stop music fadeout 1.5
    scene bg school classroom hallway day with dissolve
    play music bgm_hackbeat

    show cornelia a_0 at center with easeinleft
    show cornelia a_1
    think "Her first class is...math, the same as mine. Great, if I can convince the teacher my real identity, I might get some help!"
    show sayaka a_1 at centerleft with easeinleft
    sayaka "Morning lil' bitch, why you look so blank? finally got dumped by Japan?"
    show cornelia a_7
    think "Oh shit! She's Taiwan's friend, Sayaka, probably the most popular girl at school. Taiwan has always been her lackey."
    think "Sayaka has been quite mean to students in the lower pyramid. Although their relation is good, the harsh tongue of Sayaka doesn't change looks like."
    roc_c "Nah, I was just feeling a bit...off I guess."
    show sayaka a_2
    sayaka "Ha, I thought {b}baka{/b} like you will never get sick! Anyway I gotta go, take care of yourself.{w=0.5} Go to the infirmary if necessary, I'll tell the teachers."
    hide sayaka with easeoutleft
    show cornelia a_2
    roc_c "No need right now, thanks. See'ya."
    show cornelia a_0
    think "Glad that she didn't ask much, I'm kinda nervous talking to such a pretty girl like her.{w=0.5} Besides the joking attitude, she does seem to care about her friend's health condition."
    show cornelia a_4
    think "However it's quite frustrating she doesn't even doubt that I'm actually not her usual accompany."
    think "How do I even convince anyone, if {s}Jack{/s} China insists to obscure with his power anyway?"
    play sound sfx_bell
    show cornelia a_0
    roc_c "The class is starting soon, let's solve the problem later."
    hide cornelia with easeoutright

    scene bg classroom 1 with dissolve
    show cornelia b_1 at center with easeinleft
    menu:
        think "I should sit at"
        "{b}My{/b} seat!":
            $ flag_cn += 1
            show cornelia b_1 at centerright with ease
            "I went to my usual seat without hesitation."
            show connie a_0 at right
            connie "Wrong seat Taiwan. It's already middle of the semester, pay some attention please."
            show cornelia a_7 at center with ease
            roc_c "But this ... I ... {size=+5}I was supposed to sit here! {b}Belive it or not{/b}!{/size}"
            "I can hear classmates snickering behind me. I know it sounded stupid, but I can't just do {b}nothing{/b}! I have to remind them, metaphorically or not."
            show connie a_1
            connie "Well, I don't think China own such a high grade that you eager to be in his position so much."
            show connie a_5
            connie "However since he is still absent, I will let you stay there. If you just want to get closer to the blackboard then just state it."
            show cornelia a_3
            think "What, she thinks I was too short to see the chalkboard clear enough?! How can this dumb woman be my math teacher!"
            show cornelia a_5
            roc_c "No, I just want to sit {size=+5}here{/size}. This place belongs to me!"
            "I can hear the crowd whispering and girls gasping. But I don't care, it's {b}truth{/b}!"
            show connie a_2
            connie "Fine, just get out when China is back."
            hide cornelia
            show connie b_0 at center, faceleft with ease
            connie "Okay guys be quiet, where did we end last time? ... As I mentioned before, complex numbers can sometimes be very tricky ..."
            "And the class began. My body never showed up, I don't really want to confront him but that still annoyed me. That body-thief just make {b}me{/b} ditched the class! What is he doing!"
            show katrina a_4 at centerleft with ease
            "And the piercing glance from Katrina -my best female friend- from behind also made me quite nervous. I haven't revealed myself to her, did she have some repulsion against Taiwan?"
            hide katrina at ease

        "{s}My seat.{/s}":
            placeholder
            "I went to Taiwan's seat after some struggle. I cannot just go to my own seat cause it will be too weird."

    ".{w=0.5}.{w=0.5}."
    show connie a_0
    connie "Okay that'll be it today, don't forget that we'll have a test next week."
    "I can hear groaning and moaning all around."
    show connie a_1
    connie "If you don't prepare enough, your {i}imaginary{/i} problem might become {i}real{/i}!"
    "The class went silence, is there crow cawing?"
    show connie a_2
    connie "{size=-5}I thought this one was funny, though.{/size}"
    hide connie at ease
    stop music fadeout 1.5

    scene bg school classroom hallway day with dissolve
    play music bgm_hidden_agenda

    show cornelia b_0 at center with easeinleft
    show katrina b_3 at centerleft with easeinleft
    katrina "Hey, Taiwan!"
    show cornelia a_1
    roc_c "Hi Kat.. Katrina, what's up?"
    show katrina a_4
    katrina "What what's up! Where's China and what's your demeanor today? What happened between you and China?!"
    show cornelia a_7
    think "!!! {b}CHANCE{/b}. I've heard that girls are more sensitive and awaring of little changes of a person, I guess it's true!"
    show cornelia a_2
    roc_c "Kat! I KNEW you'll find me, let's talk at some secret place."
    show katrina a_5
    katrina "Okay, {w=1}...Kat?"
    hide cornelia with easeoutright
    hide katrina with easeoutright

    scene bg school bathroom day with dissolve
    show cornelia b_0 at center with easeinleft
    show katrina b_0 at centerleft with easeinleft
    "We went to the women's restroom, the nearest quiet place I can find."
    show cornelia a_0 at center
    show katrina a_4 at centerleft
    katrina "So what is this all about?"
    show cornelia a_4
    roc_c "It's a long story...Please listen and belive me."
    show katrina a_0
    katrina "I'll do it."
    "I elaborated everything, from the awful encounter of my uncle Jack -who I used the phrase 'body-stealer' to describe avoiding the magic effect-, my accidental residence on Taiwan's body, my deceived mom, the manipulated memories of Kiyoshi, to the shenanigan just occurred."
    if flag_tw > 0:
        "Omitting the little fun last night of course."
    show katrina a_3
    show cornelia a_8
    "I squirmed and trembled while telling. I have a premonition that If she doesn't believe me, then no one will ever do."
    katrina "......"
    show katrina a_0
    katrina "Chi..na?"
    show cornelia a_7
    roc_c "You...believed in me?"
    show katrina a_5
    katrina "It's quite bizarre but...I cannot image Taiwan acting this to me. I mean it's that little BITCH always following Sayaka and mocking me like hell!"
    show katrina a_1
    katrina "And you should look at yourself, you're soooo adorable like a chick right now."
    show cornelia a_8
    "I glanced at the mirror, a lovely girl bearing tears in her eye. Her tiny frame shaking for help. I have never seem Taiwan, or any girl looking so helpless."
    "The male part of me almost wanted to hug her tightly and pat her head, however that thought only humiliated me more."
    think "She ... is that what I look like now? what a shame!"
    show cornelia a_5
    "I wiped out the tears"
    think "It's the tear of being moved that she trusted me. Definitely not out of fear or anything like that!"
    show katrina b_5
    katrina "On the other hand...you {b}are{/b} a chick for real! HaHaHaHaHa!"
    show cornelia b_3 at faceleft
    roc_c "This is not funny! I'm {b}not{/b} a woman!"

    show katrina b_1:
        block:
            easein 0.5 xpos 0.45
            easein 0.5 xpos 0.25
    with vpunch
    "She grabbed my breasts and touched my flat groin in a flash."
    show cornelia a_3
    roc_c "Heeeeeyyyy what the heck man!"
    show katrina b_1
    katrina "Looks like there's nothing manly there lil'lady?"
    show cornelia b_3 blush
    roc_c "I...you PERVERT!!"
    "I blushed and yelled out of anger."
    show katrina a_1
    katrina "Pervert hum? You even {b}sounded{/b} like a girl! Are you actually tricking me Taiwan-chan?"
    show cornelia b_5
    roc_c "I'm not Taiwan and {b}DON'T{/b} call me that, Kat. A hundred percent serious here."
    show katrina a_2
    katrina "Affrimative, I was just teasing. Anyway, what's your plan? I mean if he really has that...magical power, then how're you gonna fight him?"
    show cornelia a_6
    roc_c "I'm still wondering...{w=0.5}maybe you should pretend not knowing this in front of {i}China{/i}, or you might be controlled too!"
    show katrina a_0
    katrina "Sure, just remember I'll always be on your side."
    show cornelia a_2
    roc_c "Thank you Kat. It's such a relief to me."
    show katrina a_1
    katrina "Well, who can really give up such a cute puppy like you?"
    show cornelia a_3 blush
    roc_c "{size=+5}Kat!!!!!{/size}"

    play sound sfx_bell
    hide cornelia with easeoutright
    hide katrina with easeoutright
    stop music fadeout 1.5

    scene bg school hallway day with dissolve
    play music bgm_hackbeat

    "We headed toward next classes separately."
    show cornelia a_1 at center

    menu:
        roc_c "I should go to"
        "{b}MY{/b} class":
            $ flag_roc += 1
            think "There is no way I go to Taiwan's class, I'm not gonna impersonate her!"
            scene bg classroom 2 with dissolve
            show jack a_3 at center
            "I walked straight into the classroom. However my seat was already occupied by a familiar face grinning at me."
            think "It will be awkward to quarrel with him now. Guess I'll have to go to Taiwan's class."
        "My class":
            $ flag_tw += 1
            think "It will be awkward for Taiwan to attend {b}my{/b} class. Guess I'll have to go to Taiwan's class."

    scene bg classroom 3 day with dissolve
    show sayaka a_1 at center
    show cornelia b_0 at centerleft, faceright with easeinleft
    "I sat besides sayaka, as Taiwan usually does."
    sayaka "Have you been better?"
    show cornelia a_1
    roc_c "I feel much better now. Thanks buddy."
    show sayaka a_0
    sayaka "{i}...Buddy? gosh she's definitely not fine.{/i}"
    "Sayaka gave me a concerned eye."
    show cornelia a_0 blush
    roc_c "I'm ra-really{w=0.5}...{w=0.5}fe-fine"
    "I stuttered."
    think "Oh God she is even more adorable with the confusing eyes. She never looked at me right at the face before!"
    "I can feel my blood pressure suring. I do not lack the experience talking with girls. However this is different, the most beautiful girl in the school gazing at me, worrying about my health."
    show cornelia a_9
    roc_c "{size=-5}This is heaven...{/size}"
    show sayaka a_5
    sayaka "Hum..."
    show cornelia a_4
    "I snapped out."
    think "Stop indulging yourself China! She is just concerning about her friend Taiwan, not you! I have to keep that in mind."
    roc_c "I'm really fine. Let's focus on the class."
    hide cornelia with dissolve
    hide sayaka with dissolve
    "And so the class passed safely. I went to the school cafeteria."

    stop music fadeout 1.5
    show bg lunch with dissolve

    show cornelia a_1 at center
    "I took eggplant, cabage and fried tofu, not what I accustomed to. However I feel like having them would be fine today."

    show cornelia a_5
    "Looking around, I can see my usual gang, including {i}myself{/i} in the corner and Taiwan's friends at the center."
    menu lunch_choice:
        "I should eat with"
        "{b}MY{/b} friends":
            $ flag_roc += 1
            "I had no willing to eat with Taiwan's friends at all, so I eyed Kat and walked toward my friends. She smiled back to me."
            show jack a_0 at centerright
            show kiyoshi a_0 at right, faceleft
            show katrina a_0 at centerleft
            show kyoko a_0 at left
            show cornelia a_2
            roc_c "Hey guys, may I join you?"
            show kyoko b_3
            "Kyoko turned into an awkward look. I knew Sayaka and Taiwan teased her a lot, in an excessively harsh fashion for tender girl like Kyoko. I used to think they are just hostile against Kyoko."
            "But considering how Sayaka talked to me, maybe that's just the wording and they don't really dislike Kyoko."
            show jack a_1
            show kiyoshi a_1
            kiyoshi "Of course, did C-woman finally decides to join our great team for alien hunting?"
            prc "Just sit besides me, {i}Wan-chan~{/i}"
            show cornelia a_1
            "I dodged his hand trying to grab me at the waist and sat down. The only empty seat is besides him so I have no choice."
            show cornelia a_0
            "Once again I was reminded how tiny Taiwan is. I can barely put my foot on the ground when sitting now. And the table now lies at a very different height also."
            think "This is horrible.. I feel like back to the elementary school!"
            show katrina a_1
            katrina "So what wind blew you here, {i}Wan-chan{/i}?"
            show jack a_1
            prc "Well, she just became my girlfriend yesterday."
            show kiyoshi a_1
            kiyoshi "C-man really learned a lot from me, haha."
            show kyoko b_4
            show cornelia a_3
            "{i}KILL ME{/i}. I frowned. However it's better to not trigger him right now, so I nodded begrudgingly."
            kyoko "China..and Taiwan? But I thought you're dating Japan."
            show cornelia a_4
            roc_c "I broke up with him."
            think "I {b}WILL{/b}."
            kyoko "But when did you start? I barely see you even talking."
            show jack a_2
            prc "Guess she just fell for my superior figure? Afterall I-China is an extremely intelligent handsome charming guy, don't you think so? Japan was just an assole that bewitched her."
            "He glanced at me."
            show cornelia a_1
            roc_c "I can't really deny that."
            show kyoko b_6
            kyoko "..."
            show katrina a_3
            katrina "Wow how do you make her agree with {b}THAT{/b}. We all know that {i}China{/i} just have middle-bottom grade and not particularly hot. The only advantage of him is that he don't bite!"
            show cornelia a_7
            roc_c "{size=+5}NO! That's because he didn't pay too much on studying. And what do you mean by not HOT, my-China's figure is {b}GREAT{/b}!{/size}"
            show katrina a_1
            show jack a_3
            "I shouted and blushed noticing that the cafeteria became quiet for a full 5-second."
            show cornelia a_8 blush
            think "Dammit Kat!"
            prc "Taiwan was true, I do have hidden muscles all around. {i}She had seen it{/i}."
            show kiyoshi a_6
            show kyoko b_5
            think "Oh No, I don't want to keep the topic.. Kat help me!"
            roc_c "*cough*. Anyway, what's your guys plan after school?"
            show katrina a_0
            katrina "I and China have D&D club today, you wanna join us?"
            show cornelia a_2
            roc_c "Sure!"
            think "I almost forgot that today is Thursday."
            show jack a_5
            prc "Hmm, I'll pass today Kat, got stuff to do. Just let Taiwan take my position, I've told her everything."
            "I don't know what he's planning, but it'd be great that I can play my own character, as {b}China{/b}."
            show cornelia a_1
            show jack a_1
            show katrina a_0
            show kyoko a_0
            "We continued our normal topic, around alies, sci-fi dramas, with Kat touching me occasionally in a teasing girl-to-girl way."
            show cornelia a_1 at faceleft
            "I can't blend in too much in this form. But hearing them is quite a relish as well. I can temporarily forget my predicament, as long as I don't look at my own face."

        "{s}My friends{/s}":
            placeholder
            #block of code to run
    play sound sfx_bell
    hide cornelia
    hide jack
    hide katrina
    hide kyoko

    stop music fadeout 2
    scene black with dissolve
    scene bg school hallway day with dissolve

    "And the bell rang. We headed towards our own classes."
    think "Since {s}the fake{/s} China has back, I could only go to Taiwan's class, which is P.E. I entered the female lockerroom the first time in my life."

    scene black with dissolve
    scene bg lockerroom day  with dissolve
    play music bgm_porch_swing_days_slower

    show cornelia a_1 blush at center
    "Although nobody was here since I'm already late, I can still feel my body temperature rising."
    think "How unfortunate, I should've come earlier!"
    "According to the memory. Taiwan is in the school girls swimming team so the teacher allows her to go practice during class."
    show cornelia a_3 at center with vpunch
    think "Swimming?!"
    "I cringed realizing the implied meaning, that I have to wear the swimming suit of her, in front of people."
    show cornelia a_5
    "I took her swimwear, a blue-white stripped cute bikini."
    show cornelia a_7
    think "How can she cover her body with a little piece of cloth like this? The two pieces together is even smaller than my underpants."
    show cornelia a_4
    think "It's a pleasure to watch girls wearing bikinis, but {b}wearing{/b} one is quite another matter."
    "My male pride would never allow me to do that. On the other hand if I don't ditch, then I will be surrounded by the school's best bodies in swimsuits."
    show cornelia a_9
    think "And I can probably change clothes with them afterward. A {b}LIFE TIME CHANCE{/b}!"
    "After some struggle between self-esteem and lust, the devil won by a large margin."
    outfit cornelia none
    show cornelia b_0
    "I took off the uniform and underwears. The naked body of Taiwan is still dazzling to me. I put on the suits hastily."
    outfit cornelia swimwear
    show cornelia b_2
    think "{b}Perfect!{/b}"
    show cornelia b_1
    "I looked at the mirror and spun. On my back was a perfectly tied knot."
    show cornelia b_7
    think "Wow, did my hand just tied the strings automatically? It felt so natural that I didn't even notice."
    show cornelia b_0
    think "The bottom-part felt like a super tight briefs. However the tightness is mainly on the hip side instead of the front, which made me quite frustrated. The cups supporting my new accompany is looser than the bras and I liked it better."
    show cornelia b_4
    think "To have something covering my chest also make me ashamed, like hiding some dirty secrets from the public. Although it's the most marvelous thing in the universe covered."
    think "I should go now."

    scene bg school pool day
    outfit mel swimsuit
    outfit flavia swimsuit
    show flavia a_0 at right, faceright
    hide flavia with easeoutright
    show cornelia b_1 at center with easeinleft
    show mel a_0 at centerright
    roc_c "Sorry I'm late~...{w=1}Mel."
    "In front of me was the vise captain of the team, Mel. Anyone can tell at one glance that she's a sunshine girl by her healthy tanned skin. Also, very importantly, she has very large boobs."
    show cornelia b_4
    think "So envious..."
    show cornelia b_7
    "{b}NO{/b} I'm not jeaous! I'm a MAN! I'm just wondering how it feels to have such large boobies."
    show mel b_0 at faceleft
    mel "Hello Taiwan~~it's so unlike you to be tardy. Flavia has already started the routine, I guess you'll have to make up for it later."
    show cornelia b_2
    roc_c "Okaaaay."
    "I feel light and bright at the sight of pool. I wasn't particularly into swimming. But Taiwan liked it a lot. From the memory I saw that she started swimming at the ocean with her family in her childhood."
    show cornelia b_5
    "Basically Taiwan is a sea-girl, very different from me. But maybe her body is effecting me, I have an eager to jump into the pool."
    show cornelia b_0:
        xalign 0.45
        faceright
        linear 1.0 xalign 0.55
        faceleft
        linear 1.0 xalign 0.45
        repeat 2
    "After a brief warmup I began my training."
    hide cornelia with vpunch
    show mel a_1
    mel "I should start too."
    hide mel with vpunch

    nvl clear
    nvl_narrator "And so the time passed peacefully. I was not good at swimming, but the body seemed to remember it. I can easily acclimate to the training by calling up some memories."
    nvl_narrator "No one doubted my identity since there's not too much chance to chat."
    nvl_narrator "To my surprise, the whole experience was enjoyable. Caressed by cool water was way better than running around catching ball-shape objects."
    nvl_narrator "The pool consists of only girls, so nobody really paid attention on me. I almost forgot that I was crossdressing - mentally."
    nvl_narrator "Flavia and Mel's mature bodies were voluptuous, but I found myself indulged in the training more. Maybe not having a dick does effect your focus."
    nvl_narrator "Flavia asked me to do three more round after class to compensate my tardiness, so I didn't manage to get into the angels' secret garden."

    scene black with dissolve
    scene bg lockerroom day with dissolve
    show cornelia b_4 at center
    roc_c "I should {b}never{/b} be late again!"
    show cornelia b_1
    think "There's a school swimming contest incoming next week also, and I'm {b}NOT{/b} losing it."
    show cornelia b_4
    think "Wait..I should not plan for this body. I'm not gonna stay like this!"
    "I dressed up and headed towards the next class."
    hide cornelia
    outfit cornelia uniform

    stop music fadeout 1.5

    scene black with dissolve
    scene bg classroom 4 day with dissolve
    play music bgm_hackbeat
    "The last class today is history."

    placeholder
