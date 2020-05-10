# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define romeo_father = Character("Romeo's Father")
define player = Character("Narrator")
default menuset = set()


# The game starts here.

label start:

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
    player "So this is the crime scene..."
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
                player "Hands"
                jump romeo_father_crimescene_body_menu
            "Feet":
                player "Feet"
                jump romeo_father_crimescene_body_menu
            "Head":
                player "Head"
                jump romeo_father_crimescene_body_menu
            "Chest":
                player "Chest"
                jump romeo_father_crimescene_body_menu

        player "Hmm, that's all the info I can get from the body."
        jump romeo_father_crimescene_menu

    label romeo_father_crimescene_surroundings:
        player "So here is the crime scene..."

        menu romeo_father_crimescene_surroundings_menu:
            set menuset
            "What should I inspect first?"

            "Documents":
                player "Looks like this is a document about the impending sale of [romeo_father.name]'s land."
                player "I can't imagine how much stress this could be..."
                player "I don't think I would have signed these documents either, to sell family fortunes like that..."
                jump romeo_father_crimescene_surroundings_menu
            "Mug":
                player "Why does [romeo_father.name] like drinking out of mugs?"
                # based on prev. conversation with Romeo, player could know the answer
                # TODO: talk to Romeo about this conversation
                if False:
                    player "Oh yeah! Romeo told me that he likes to drink TBD !"
                    player "But is that what he was drinking in this mug?"
                else:
                    player "Is he drinking a margarita or something?"
                    player "Does he have a drinking addiction?"
                    player "He must have been stressed out..."

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
    player "So this is [romeo_father.name]'s room..."

    menu romeo_father_roomscene_menu:
        set menuset
        "What should I observe?"

        "Bookshelf":
            #alchemist books, land ownership books
            jump romeo_father_roomscene_menu
        "Desk":
            #have some alchemist stuff (reference to teacher and Romeo)
            jump romeo_father_roomscene_menu
        "Bed":
            #stains, bad lead towards poison
            #made bed
            jump romeo_father_roomscene_menu

    player "Hmm, that's all there is to observe in this room."
    jump romeo_father_menu

label romeo_father_end:
    return
