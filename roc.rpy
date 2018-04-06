init python hide:
    config.developer = True

define commie = FakePerson("???", "jack")
define prc = FakePerson("China", "jack")
define roc = FakePerson("China", "john")
define roc_c = FakePerson("China", "cornelia")
define tw = FakePerson("Taiwan","cornelia")

label scenario_roc:
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
    play music bgm_mirage

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
    "I bearly get up from my tiny arms."

    show cornelia a_0
    roc_c "Wow these hands are ... {i}small{/i}."

    show cornelia a_5
    "A high-pitched feminine voice run through my scalp in a weird but rather familiar way. Is someone talking?"

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
    roc_c "Don't call me {i}that{/i}! I'm {b}China{/b}!"

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
    roc_c "{size=+5}I'm not his girlfriend! I {b}am{/b} China and he is {b}{s}not{/s}{/b} China!!!{/size}{w=0.5}I can prove it by answering anything about China!"

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

    show cornelia a_0 at center
    "I standed still for a whole few minutes, after staring 'me' walking into my own house with a smirk."
    think "What now?"
    "I knew Taiwan long time ago, a lovely girl going through the same school as me. She's probably the most or second popular girl in the grade."
    "Sharing some classes and friends, we have even hung out a few times. But besides that, we're just acquaintances. All I know is that she's been dating Japan recently, so does everyone."

    show cornelia a_7
    think "Does that mean {b}I{/b} am dating Japan now? {w=1}But my mom thinks I'm dating {b}me{/b}... This is getting complicated."

    show cornelia a_3
    think "Anyway, I'll have to go {b}home{/b} now. {w=0.5}Where do I even live? Maybe I should try {i}this{/i}."
    "I tried to recall the action that I have done before, by instinction."

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

    menu:
        think "Go"
        "Do nothing":
            $ flag1 = 0
        "Do something":
            $ flag1 = 1

    show cornelia a_7
    tw "What?! Somebody's in MY BODY? {size=+5}{b}GET OUT RIGHT NOW!!!{/b}{/size}"

    show cornelia b_3:
#        rotate_pad False
#        block:
#            parallel:
#                linear 0.05 yanchor 0.4
#            parallel:
#                linear 0.05 ypos 0.53
        block:
            parallel:
                rotate_pad False
                linear 0.3 rotate 30
            repeat
#            parallel:
#                linear 0.3 xpos 0.54
#            parallel:
#                linear 0.3 ypos 0.87
    with vpunch

    roc_c "STOP!!"

    show cornelia b_3:
        block:
            parallel:
                linear 1.0 xpos 1.10
                linear 1.0 xpos 1.12
                repeat

#    with vpunch
#    play sound sfx_whack
    "{i}We{/i} almost fell down, fighting against each other for the control of the body. This {b}has{/b} to be dealt with, I've had enough of these!"

    show cornelia a_5
    roc_c "{spell}Let me control the body!{/spell}"


#    show cornelia b_3 at centerleft
#    show john a_3 at centerright, faceleft
#    swap john a_0 : a_1, cornelia a_1 : a_0
#    cornelia "When you swap bodies, you also swap expression banks, so you have to use the expressions that are native to the body and not the person."
#    john "Now that I'm in Ms. Winter's body, I can make her {q}b{/q} expression by putting {q}show john b_1{/q} above my text."

#    show john b_1
#    roc_c "This feels {i}weird{/i}."



    placeholder
