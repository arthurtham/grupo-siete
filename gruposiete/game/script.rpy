# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define joe = Character("Julio Gonzalez")
define romeo_father = joe
define romeo = Character("Romeo Gonzalez")
define player = Character("Player", what_italic=True)
default menuset = set()



# The game starts here.

label start:
    # temporary start
    # Declare booleans here
    $ baking_soda = False
    $ mug = False
    $ documents_observed = False
    $ visited_crime_scene = False
    $ visited_jorge_room = False
    #$ romeo_drink = False

    #

label romeo_father_start:
    scene bg room

    show makoto serious

    play music "audio/lesson.mp3"

    player "So it looks like [romeo_father.name] has died of something..."

    player "I wonder what I should observe first..."

label romeo_father_menu:
    scene bg room

    menu:
        "What should I observe?"
        "The crime scene":
            jump romeo_father_crimescene
        "[romeo_father.name]'s room":
            jump romeo_father_roomscene
        "I'm done":
            jump romeo_father_end

label romeo_father_crimescene:
    scene romeo father crimescene
    $ visited_crimescene = True
    player "So this is where [romeo_father.name] died mysteriously..."
    player "I think I should investigate the body and his surroundings."
    menu romeo_father_crimescene_menu:
        "Investigate body":
            jump romeo_father_crimescene_body
        "Investigate surroundings":
            jump romeo_father_crimescene_surroundings
        "Leave crime scene":
            jump romeo_father_menu


    player "I think I've investigated the entire crime scene.\
    I don't need to be here anymore."
    jump romeo_father_menu


    label romeo_father_crimescene_body:

        menu romeo_father_crimescene_body_menu:
            set menuset
            "Which part of the body should I investigate?"

            "Hands":
                player "There's some liquid left on [romeo_father.name]'s hands..."
                player "Was he sweating that hard?"
                jump romeo_father_crimescene_body_menu
            "Feet":
                player "He's actually got really nice shoes on his big feet."
                player "I wonder if he got them through the black market."
                jump romeo_father_crimescene_body_menu
            "Head":
                player "I can see the veins popping out of his head..."
                player "Could it be from all the stress?"
                jump romeo_father_crimescene_body_menu
            "Mouth":
                player "His lips seem to be burnt purple..."
                player "Is this the sign of royalty?"
                player "...NO! There has to be a reason behind this..."
                jump romeo_father_crimescene_body_menu
            "Chest":
                player "Is there a chance he's still alive?"
                player "..."
                player "...no pulse. It's way too late to revive him."
                jump romeo_father_crimescene_body_menu

        player "Hmm, that's all the info I can get from the body."
        jump romeo_father_crimescene_menu

    label romeo_father_crimescene_surroundings:
        scene romeo father crimescene
        player "So here is the crime scene..."

        menu romeo_father_crimescene_surroundings_menu:
            set menuset
            "What should I inspect first?"

            "Documents":
                $ documents = True
                player "Looks like this is a document about the impending sale of [romeo_father.name]'s land."
                player "I can't imagine how much stress this could be..."
                player "I don't think I would have signed these documents either, to sell family fortunes like that..."
                jump romeo_father_crimescene_surroundings_menu
            "Mug":
                player "Why does [romeo_father.name] like drinking out of mugs?"
                # based on prev. conversation with Romeo, player could know the answer
                # TODO: talk to Romeo about this conversation
                #if romeo_drink:
                #    player "Oh yeah! [romeo.name] told me that he likes to drink margaritas!"
                #    player "But is that what he was drinking in this mug?"
                #else:
                player "Is he drinking a margarita or something?"
                player "Does he have a drinking addiction?"
                player "He must have been stressed out..."
                $ mug = True
                jump romeo_father_crimescene_surroundings_menu
            "Pen":
                player "Was he about to sign the sale documents?"
                player "I thought he was trying to dispute the sale."
                player "Or were they ready to come up with a compromise?"
                player "Either way, that's a lot of ink for one document..."
                jump romeo_father_crimescene_surroundings_menu

        player "Hmm, there's nothing else to investigate here."
        jump romeo_father_crimescene_menu

label romeo_father_roomscene:
    scene romeo father room
    $ visited_jorge_room = True
    player "So this is [romeo_father.name]'s break room for the meeting..."

    menu romeo_father_roomscene_menu:
        set menuset
        "What should I observe here in [romeo_father.name]'s room?"

        "Bookshelf":
            #alchemist books, land ownership books
            player "[romeo_father.name] really likes to read books.
            He brought so many books with him to fill a bookshelf!"
            player "Looks like this is a book is titled \"Traité Élémentaire de Chimie.\"."
            player "Must be something about the chimneys he's about to build on his land."
            player "Wait, is that a book about volcanoes?"
            $ baking_soda = True
            player "I love mixing baking soda with my vinegar! What a mass solution!"
            jump romeo_father_roomscene_menu
        "Desk":
            #have some alchemist stuff (reference to teacher and Romeo)
            player "[romeo_father.name]'s desk is rather clean."
            player "I'm sure [romeo] picked up some habits from his father."
            player "Hm? Is this a new recipe for bread?"
            if baking_soda:
                player "Of course! That's what the baking soda was for!"
                player "But why was he trying to learn how to bake bread?"
            else:
                player "That certainly makes my tummy growl."
            jump romeo_father_roomscene_menu
        "Bed":
            #stains, bad lead towards poison
            #made bed
            player "[romeo_father.name] seems like a very neat guy. He's a grown man;
            he can make his own bed."
            player "...hmm? Why are the pillows stained?"
            if baking_soda:
                player "Is this the baking soda from his volcano experiments?"
            if mug:
                player "Is it his margarita from his mug again?"
            player "I wouldn't see any other reason..."
            jump romeo_father_roomscene_menu

    player "Hmm, that's all there is to observe in this room."
    jump romeo_father_menu

label romeo_father_end:
    player "Yeah, I suppose there's nothing else to do here. Let's check out the other evidence."
    return
