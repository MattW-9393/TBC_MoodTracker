import datetime

# Get today's date and save as variable
xdate = datetime.datetime.now()
the_date = xdate.strftime("%d-%m-%Y")

mood_tag = ["Very Happy", "Happy", "Moderate", "Unhappy", "Very Unhappy"]
negative_secondary_mood = ["Anxious", "Stressed", "Angry", "Sad"]
positive_secondary_mood = ["Excited", "Satisfied", "Relieved"]

no_comment_required = "Moderate score given - No commentary required"

name = "Matt"

def daily_mood_check():
    print("""Hi, welcome to your mood checker.
          I'd like to ask you a couple of questions about your mood if that's okay?""")
    mood_rating = int(input("On a scale of 1-10, how do you feel today? 1 being 'Very Unhappy' and 10 being 'Very Happy' /n"))

    match mood_rating:
        case 1 | 2:
            mood_tag[4]
        case 3 | 4:
            mood_tag[3]
        case 5 | 6:
            mood_tag[2]
        case 7 | 8:
            mood_tag[1]
        case 9 | 10:
            mood_tag[0]
    
    if mood_tag == mood_tag[4] or mood_tag == mood_tag[3] or mood_tag == mood_tag[1] or mood_tag == mood_tag[0]:
        commentary = input("Please add some commentary explaining your answer (250 char max): /n")
    else:
        print(no_comment_required)
    
    print("Thanks! I've saved your records. What would you like to do next? /n") 
    what_next = int(input("Press '1' to view all your entries so far, or Press '0' to exit the program /n"))

    if what_next == 1:
        #display database records
        print("Here are your previous entries: /n")
    elif what_next == 0:
        #exit function
        print("Thanks, see you again tomorrow!")
    else: "Invalid entry, please press '1' to view your previous records, or press '0' to exit the program /n"

    # Need to add various DB features to send this information somewhere...

daily_mood_check()
