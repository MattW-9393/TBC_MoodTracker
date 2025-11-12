import datetime
import sqlite3
import csv


# Set up Mood-Journal DB
con = sqlite3.connect("proto-mood.db")
cur = con.cursor()
res = cur.execute("SELECT name FROM sqlite_master")

if con == None: 
   cur.execute("CREATE TABLE MoodRatings (date, moodLabel, commentary)")


# Get today's date and save as variable
xdate = datetime.datetime.now()
the_date = xdate.strftime("%d-%m-%Y")

mood_tag = ["Very Happy", "Happy", "Moderate", "Unhappy", "Very Unhappy"]
negative_secondary_mood = ["Anxious", "Stressed", "Angry", "Sad"]
positive_secondary_mood = ["Excited", "Satisfied", "Relieved"]
todays_mood = ""

name = "Bob"

def daily_mood_check():
    print(f"""Hi {name}, welcome to your mood checker.
          I'd like to ask you a couple of questions about your mood if that's okay?""")
    mood_rating = int(input("On a scale of 1-10, how do you feel today? 1 being 'Very Unhappy' and 10 being 'Very Happy: "))

    match mood_rating:
        case 1 | 2:
            todays_mood = mood_tag[4]
        case 3 | 4:
            todays_mood = mood_tag[3]
        case 5 | 6:
            todays_mood = mood_tag[2]
        case 7 | 8:
            todays_mood = mood_tag[1]
        case 9 | 10:
            todays_mood = mood_tag[0]
    
    if todays_mood == "Moderate":
        commentary = "Moderate score given - No commentary required"
        print("Moderate score given - No commentary required")

    else:
        commentary = input("Please add some commentary explaining your answer (250 char max): ")
    

    # Define data that will be added to the table
    data = [the_date, todays_mood, commentary]

    # Insert the latest entries into the DB
    cur.execute("INSERT INTO MoodRatings (date, moodlabel, commentary) VALUES (?, ?, ?)", data)
    con.commit()
    
    # Closing notes on the script
    print("Thanks! I've saved your records. What would you like to do next?") 
    what_next = int(input("Press '1' to view all your entries so far, or Press '0' to exit the program"))

    cur.execute("SELECT * FROM MoodRatings;")
    allrows = cur.fetchall()

    if what_next == 1:
        #display database records
        print("Here are your previous entries: ")
        for row in cur.execute("SELECT date, moodlabel, commentary FROM MoodRatings"):
            print(row)
        
        print("Would you like a csv or JSON file containing all your previous submissions?")
        export_file = int(input("If you would like a CSV export - press 1; If you would like to exit without exporting your data - press 0" \
        "Action: "))

        if export_file == 1:
            print("Exporting data into CSV............")
            with open("table.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([header[0] for header in cur.description])
                writer.writerows(allrows)
            print("File successfully exported!!")

        elif export_file == 0:
            print("Thanks, see you again tomorrow!")

    elif what_next == 0:
        #exit function
        print("Thanks, see you again tomorrow!")

    else: "Invalid entry, please press '1' to view your previous records, or press '0' to exit the program: "

daily_mood_check()

