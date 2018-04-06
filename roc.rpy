#init python hide:
#    config.developer = True

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
    show cornelia a_0
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

    show jack a_3
    commie "I'm a rich, young boy {i}again{/i}, haha! Let me examine the crucial memories first..."

    show cornelia b_3 at centerright, faceleft with easeinright
    roc_c "WAIT!!!!!!!"

    show jack a_0
    prc "What's up, Taiwan?"

#    show cornelia b_3 at centerleft
#    show john a_3 at centerright, faceleft
#    swap john a_0 : a_1, cornelia a_1 : a_0
#    cornelia "When you swap bodies, you also swap expression banks, so you have to use the expressions that are native to the body and not the person."
#    john "Now that I'm in Ms. Winter's body, I can make her {q}b{/q} expression by putting {q}show john b_1{/q} above my text."

#    show john b_1
#    roc_c "This feels {i}weird{/i}."



    placeholder
