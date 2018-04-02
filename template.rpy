#init python hide:
#    config.developer = True

define roc = FakePerson("Republic of China", "john")
define tw = FakePerson("Taiwan","cornelia")

label scenario_test:

    show john a_0 at center
    roc "Hi, I'm China!"
    tw "I'm Taiwan!"
