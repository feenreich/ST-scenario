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

    clone katrina john
    hide john
    show katrina a_0 at centerleft

    exspirit jack a_3

    show jackGhost a_1
    commie "haha"

    possess jack katrina a_4
    hide jack
    hide katrina

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
#    show cornelia a_3:
#        parallel:
#            linear 4.5 xpos 0.1
#        parallel:
#            linear 4.5 ypos 1.0
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
    roc_c "The color is green! Also you carved a Chinese Character meaning 'ten thousand' on the turf. You gotta definitely belive me now, right?"
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
    roc_c "You'll REGRET it!"
    "Anyway, I have lost the incentive to stay with them. I growled at 'China' and walked straight pass them into the school."
    show cornelia b_3 at faceleft with easeoutleft

    stop music fadeout 1.5
    scene bg school classroom hallway day with dissolve
    play music bgm_hackbeat
    show cornelia a_0 at center
    "The first class is..."

#    "I felt something rubbing my body. The unusual tightness around my upper body, especially the breast part got released, soon replaced by a soft and silky touch."
#    "As I opened my {i}mind eyes{/i}."


#    tw "You woke up, didn't you?{w=1}Who are you and why are you doing this!?"
#    "In the next few minutes, I told her the whole story - from my crazy uncle, my magical power, to my stolen identity and my deceived mother."
#    "She seems rather calm, to be honest, the situation of her is kinda similar to me. Although the story is hard to belive, its even more difficult to deny the reality."


    placeholder
