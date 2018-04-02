#init python hide:
#    config.developer = True

define roc = FakePerson("Republic of China", "john")
define tw = FakePerson("Taiwan","cornelia")

label scenario_roc:


    show john a_0
    roc "I'm China."
    show cornelia a_0
    tw "Hi, my name is Taiwan. I hate China!"
    show john a_2
    roc "But you {i}are{\i} China."
    show cornelia a_2
    tw "I'm {i}not!!!!!{\i}"
