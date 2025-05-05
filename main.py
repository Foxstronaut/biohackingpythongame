import time
import platform
import os
import random as rd

# Removed global score and multiplier variables

# Removed scoring functions

mydata = r"""
            ╔═══════════╦═══════════╦═════════════╦═══════════════╦════════════════╦══════════════╗
            ║ Date      ║ Hydration ║ Hobby time  ║ Climbing Time ║ Miles traveled ║ Scale/Rating ║
            ╠═══════════╬═══════════╬═════════════╬═══════════════╬════════════════╬══════════════╣
            ║ 3/17/2025 ║     4 oz. ║       0     ║  120 minutes  ║    1.21 miles  ║      2       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/18/2025 ║    26 oz. ║       0     ║  120 minutes  ║    0.81 miles  ║      3       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/19/2025 ║     0 oz. ║       0     ║   30 minutes  ║    2.06 miles  ║      4       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/20/2025 ║    30 oz. ║       5     ║  120 minutes  ║    1.08 miles  ║      3       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/21/2025 ║    10 oz. ║      30     ║    0 minutes  ║    2.14 miles  ║      3.5     ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/22/2025 ║    42 oz. ║      10     ║  225 minutes  ║    0.53 miles  ║      5       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/23/2025 ║    20 oz. ║       5     ║    0 minutes  ║    0.43 miles  ║      3       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/24/2025 ║     0 oz. ║      15     ║  120 minutes  ║    2.28 miles  ║      3.5     ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/25/2025 ║     0 oz. ║       3     ║  120 minutes  ║    2.50 miles  ║      3       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/26/2025 ║     2 oz. ║       2     ║    0 minutes  ║    2.90 miles  ║      2.7     ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/27/2025 ║    17 oz. ║       0     ║  120 minutes  ║    0.87 miles  ║      3       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/28/2025 ║    16 oz. ║      14     ║    0 minutes  ║    1.67 miles  ║      3       ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/29/2025 ║    11 oz. ║       0     ║  240 minutes  ║    0.60 miles  ║      3.5     ║
            ╟───────────┼───────────┼─────────────┼───────────────┼────────────────┼──────────────╢
            ║ 3/30/2025 ║     0 oz. ║      10     ║    0 minutes  ║    2.86 miles  ║      3       ║
            ╚═══════════╩═══════════╩═════════════╩═══════════════╩════════════════╩══════════════╝"""
mydata1 = r"""
                                        ╔═══════════╦════════════╦═════════╗
                                        ║ Date      ║ Hobby Time ║ Rating  ║
                                        ╠═══════════╬════════════╬═════════╣
                                        ║ 4/1/2025  ║ 10 min     ║ 3.5/5   ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/2/2025  ║ 45 min     ║ 3/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/3/2025  ║ 0 min      ║ 4/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/4/2025  ║ 0 min      ║ 3/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/5/2025  ║ 0 min      ║ 4/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/6/2025  ║ 0 min      ║ 3/5     ║
                                        ╟───────────┼───────────┼─────────╢
                                        ║ 4/7/2025  ║ 0 min      ║ 3.5/5   ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/8/2025  ║ 0 min      ║ 3/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/9/2025  ║ 4 min      ║ 5/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/10/2025 ║ 0 min      ║ 3.5/5   ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/11/2025 ║ 20 min     ║ 4/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/12/2025 ║ 0 min     ║ 3/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/13/2025 ║ 0 min      ║ 4/5     ║
                                        ╟───────────┼────────────┼─────────╢
                                        ║ 4/14/2025 ║ 30 min     ║ 4.5/5   ║
                                        ╚═══════════╩════════════╩═════════╝ """

# Define detailed actions for each variable
actions = {
    "Sleep Quality": [
        "Establish a consistent bedtime routine, aiming for lights out by the same every night.",
        "Create your perfect bedroom environment: make it completely dark, cool, and quiet.",
        "Limit intense activities before bed.",
        "Practice relaxation techniques like deep breathing or meditation.",
        "Ensure you get at least 7-8 hours of uninterrupted sleep.",
        "Reserve caffeine for when you really need it."
    ],
    "Hobby Time": [
        "Schedule a dedicated hour each day specifically for your chosen hobby.",
        "Join a online community related to your hobby to increase your interest.",
        "Set a S.M.A.R.T. goal for your hobby. (Specific, Measurable, Attainable, Reasonable, Time-Bound)",
        "Create a dedicated physical space for your hobby activities to make it easier.",
        "Block out a longer session (2-3 hours) on a weekend for your hobby.",
        "Reduce time spent on passive activities (like excessive TV) to free up hobby time."
    ],
    "Water Intake": [
        "Carry a reusable water bottle with you and refill it throughout the day.",
        "Drink a glass of water when you wake up each morning.",
        "Set reminders to drink water every hour.",
        "Track your water intake diligently.",
        "Substitute water to stop boredom. Tea, Sports Drinks, and Smoothies are great options.",
        "Drink a glass of water before each meal."
    ],
    "Steps Taken": [
        "Commit to taking a walk during your lunch break.",
        "Take the stairs.",
        "Park further away to add extra steps and save money.",
        "Incorporate short walking breaks when possible.",
        "Use a step tracker and set a daily step goal.",
        "Walk or run for short errands instead of driving."
    ],
    "Miles Traveled": [
        "Plan and execute a longer walk or bike ride.",
        "Incorporate active commuting methods like biking or walking.",
        "Explore new routes or trails in your area.",
        "Set a weekly or monthly mileage goal and track your progress.",
        "Consider joining a walking or cycling group.",
        "Use apps that map and track your routes and distance."
    ],
    "Sport/Exercise Time": [
        "Schedule specific blocks of time in your week solely for engaging in your sport or other forms of exercise.",
        "Find a workout buddy or join a class to increase accountability.",
        "Set S.M.A.R.T. performance goals.(Specific, Measurable, Attainable, Reasonable, Time-Bound).",
        "Cross-train with activities that complement your main.",
        "Dedicate time for warm-ups, cool-downs, and stretching to enhance performance and prevent injury.",
        "Consult with your coach or trainer about your training plan."
    ]
}


class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Speedrun Stopwatch started!")

    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False
            print("Speedrun Stopwatch stopped!")

    def reset(self):
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset!")

    def get_elapsed_time(self):
        if self.running:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time

sw = Stopwatch()
# Removed initial sw.start() as it seems the game logic starts later

def clear():
    """Clears the terminal screen."""
    system = platform.system()
    if system == "Windows":
        time.sleep(0.5) # Reduced sleep for quicker clear
        os.system('cls')
    elif system in ["Linux", "Darwin"]: # macOS and Linux use 'clear'
        time.sleep(0.5) # Reduced sleep
        os.system('clear')
    else:
        print(system)
        time.sleep(1)
        print("Operating system not supported for clearing.")

def petc():
    """Displays a 'Press Enter to continue' prompt and waits for user input."""
    input("\nPress Enter to continue...") # Added newline for better formatting

# Removed print(system) here

name = input("Greetings! What is your name? ")
print(f"\nWelcome, {name}.")
time.sleep(2)
clear()

print(r"""
      +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+ +-+-+ +-+-+-+
      |W|e|l|c|o|m|e| |t|o| |T|h|e| |H|a|c|k|i|n|g| |o|f| |B|i|o|
      +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+ +-+-+ +-+-+-+
""")
print(r"""
            Elliott's
""")
print(r"""

                █▀▄ ▀█▀ █▀█ █ █ █▀█ █▀▀ █ █ ▀█▀ █▀█ █▀▀
                █▀▄  █  █ █ █▀█ █▀█ █   █▀▄  █  █ █ █ █
                ▀▀  ▀▀▀ ▀▀▀ ▀ ▀ ▀ ▀ ▀▀▀ ▀ ▀ ▀▀▀ ▀ ▀ ▀▀▀
                █▀█ █▀▄ █▀█ ▀▀█ █▀▀ █▀▀ ▀█▀
                █▀▀ █▀▄ █ █   █ █▀▀ █   █
                ▀   ▀ ▀ ▀▀▀ ▀▀  ▀▀▀ ▀▀▀ ▀

""")

startyn = input("Are you ready to dive into the world of biohacking? (y/n): ").lower() # Use .lower() for case-insensitivity
if startyn == "y":
    clear()
    sw.start() # Start stopwatch when the user chooses to begin
else:
    clear()
    print("Perhaps another time. The journey of biohacking awaits when you are ready.")
    quit()

completionyn = input(r"""
            It's a calm day in March, you're sitting
            in class, and your teacher, a cheerful
            sort we'll call Barney (like the friendly
            dinosaur), introduces a new project:

                        Biohacking

            You lean in, listening intently as Barney
            explains the concept. Biohacking, he
            tells you, is the fascinating practice of
            making small, deliberate changes to your
            daily routines, habits, and environmental
            factors. The goal? To observe and analyze
            how these modifications impact your life,
            ideally leading to significant improvements.

            This project isn't just busywork; it requires
            genuine effort outside of class. It's about
            experimenting with your own life for the
            sake of SCIENCE and DATA! You'll need to
            track variables diligently and be prepared
            to adapt.

            Will you take this challenge and attempt
            the biohacking project, or will you let this
            opportunity pass?

            y - Embrace the project!
            n - Decline the project.
            """).lower() # Use .lower() for case-insensitivity

if completionyn == "y":
    print("\nA wise decision!")
else :
    print("\nThis project requires commitment.")

petc() # Use petc()
clear()

# Variables to hold the names of the tracked variables
trackvar1 = ""
trackvar2 = ""
trackvar3 = ""
trackvar4 = ""

pickvarabcd = input(r"""
            To begin your biohacking journey, you need
            to select the variables you will track.
            Think about what aspects of your life
            you want to observe and potentially improve.
            You brainstorm a few possibilities and
            consider the pros and cons of tracking each.

            Here are some sets of variables to choose from, along with potential challenges for tracking them:

            Option a:
            Variables: Sleep Quality, Hobby Time, Water Intake, Steps Taken
            Potential Challenges:
                Tracking Sleep Quality accurately can be challenging.
                Making time for Hobby Time consistently requires discipline.
                Keeping track of all Water Intake throughout the day can be easy to forget.
                Step counters aren't perfect for Steps Taken, especially with varied activities.

            Option b:
            Variables: Hobby Time, Miles Traveled, Water Intake, Sport/Exercise Time
            Potential Challenges:
                Dedicating consistent Hobby Time can be hard with other commitments.
                Miles Traveled doesn't capture effort or terrain.
                Keeping track of all Water Intake throughout the day can be easy to forget.
                Tracking Sport/Exercise Time might miss informal physical activity.

            Option c:
            Variables: Sleep Quality, Water Intake, Sport/Exercise Time, Steps Taken
            Potential Challenges:
                Tracking Sleep Quality accurately can be challenging.
                Keeping track of all Water Intake throughout the day can be easy to forget.
                Tracking Sport/Exercise Time might miss informal physical activity.
                Step counters aren't perfect for Steps Taken, especially with varied activities.

            Option d:
            Variables: Miles Traveled, Steps Taken, Sport/Exercise Time, Water Intake
            Potential Challenges:
                Miles Traveled doesn't capture effort or terrain.
                Step counters aren't perfect for Steps Taken, especially with varied activities.
                Tracking Sport/Exercise Time might miss informal physical activity.
                Keeping track of all Water Intake throughout the day can be easy to forget.

            Each set offers different insights into your daily life.
            Which combination of variables will you choose to track?

            Enter a, b, c, or d:
            """).lower() # Use .lower() for case-insensitivity
clear()

# Based on the choice, set the variables being tracked
if pickvarabcd in ["a", "1"]:
    print(f"You've chosen to track Sleep Quality, Hobby Time, Water Intake, and Steps Taken.")
    trackvar1 = "Sleep Quality"
    trackvar2 = "Hobby Time"
    trackvar3 = "Water Intake"
    trackvar4 = "Steps Taken"
elif pickvarabcd in ["b", "2"]:
    print(f"An excellent choice! You'll be tracking Hobby Time, Miles Traveled, Water Intake, and Sport/Exercise Time.")
    trackvar1 = "Hobby Time"
    trackvar2 = "Miles Traveled"
    trackvar3 = "Water Intake"
    trackvar4 = "Sport/Exercise Time"
elif pickvarabcd in ["c", "3"]:
    print(f"Okay, you've decided to track Sleep Quality, Water Intake, Sport/Exercise Time, and Steps Taken.")
    trackvar1 = "Sleep Quality"
    trackvar2 = "Water Intake"
    trackvar3 = "Sport/Exercise Time"
    trackvar4 = "Steps Taken"
elif pickvarabcd in ["d", "4"]:
    print(f"You will be tracking Miles Traveled, Steps Taken, Sport/Exercise Time, and Water Intake.")
    trackvar1 = "Miles Traveled"
    trackvar2 = "Steps Taken"
    trackvar3 = "Sport/Exercise Time"
    trackvar4 = "Water Intake"
else :
    print("That wasn't a valid choice. The experiment cannot proceed without a valid selection.")
    clear()
    quit()

petc() # Use petc()
clear()

print(r"""
            Welcome to Phase 1 of your biohacking project.
            In this initial phase, your primary goal is
            simple: tracking data.

            For a set period, you will record
            data for the variables you selected. The key
            here is observation without intervention.
            Do NOT intentionally change your habits or
            routines during this phase. The aim is to
            establish a baseline, to understand your
            current patterns before attempting any
            modifications.

            Accuracy and consistency in
            tracking are paramount.
""")

petc() # Use petc()
clear()

# --- Phase 1 Temptations (Now with specific, randomized actions) ---

# Temptation for trackvar4
tempt_var4 = trackvar4
tempt_action_4 = rd.choice(actions[tempt_var4]) # Randomly select an action for this variable
improvebig1 = input(f"""
            As you settle into the tracking routine for Phase 1,
            you notice trends in your data for {tempt_var4}.
            You have an idea for a specific action, like:

            "{tempt_action_4}"

            Taking this step now could improve your
            performance and feel like progress.
            However, it wasn't part of the plan for Phase 1,
            which is strictly for tracking your baseline.
            Making this change now would disrupt that crucial baseline data,
            potentially making it harder to understand the true
            impact of future interventions.

            Do you stick to the plan and maintain consistent
            tracking, or do you yield to make an early change?

            y - Implement this specific change now.
            n - Stick to the Phase 1 plan and just track.
            """).lower()
clear()

if improvebig1 == "y":
    print(f"""
            You decided to implement the change:
            "{tempt_action_4}"
            It feels good to take action, but you know this
            shouldn't happen in phase 1.
            Hopefully, this early intervention doesn't obscure
            your baseline.
            """)
else:
    print(f"""
            You chose to stay consistent with the Phase 1
            objective: tracking your patterns for {tempt_var4}
            without intervention. This is key
            at this crucial stage.
            """)
petc() # Use petc()

# Temptation for trackvar3
tempt_var3 = trackvar3
tempt_action_3 = rd.choice(actions[tempt_var3])
improvebig2 = input(f"""
            Another week of tracking goes by. You're looking over steps
            for improving {tempt_var3}. You see an obvious
            area where taking a specific action could lead to
            improvement, something like:

            "{tempt_action_3}"

            Starting this now is tempting and seems productive.
            But sticking to the plan means gathering pure
            baseline data first. Making a change now means
            you won't have a clean 'before' picture to compare against.

            What do you do? Do you prioritize early action or
            data integrity?

            y - Start implementing this change for {tempt_var3}.
            n - Keep tracking consistently for Phase 1.
            """).lower()
clear()

if improvebig2 == "y":
    print(f"""
            You've started working on improving your {tempt_var3}
            sooner than planned by implementing:
            "{tempt_action_3}"
            The improvement is strong! Let's see how this
            impacts you over time.
            """)
else:
    print(f"""
            You remain committed to the goal.
            Understanding your patterns for {tempt_var3}
            before trying to change them is a solid scientific approach.
            You continue to focus on tracking.
            """)
petc() # Use petc()

# Temptation for trackvar2
tempt_var2 = trackvar2
tempt_action_2 = rd.choice(actions[tempt_var2])
improvebig3 = input(f"""
            As the weeks progress through Phase 1, your data for {tempt_var2}
            starts revealing some clear patterns. You identify a
            potential area where a targeted change could
            yield positive quickly, perhaps by trying:

            "{tempt_action_2}"

            Implementing this change now would mean
            deviating from the tracking of Phase 1,
            but the potential for early improvement is
            enticing. It feels like you could get ahead
            on the project's goals.

            Do you initiate this specific action for {tempt_var2}, or
            do you see Phase 1 through by simply tracking?

            y - Make this specific change for {tempt_var2} now.
            n - Maintain consistency in tracking for now.
            """).lower()
clear()

if improvebig3 == "y":
    print(f"""
            You've decided to jump ahead and start actively
            working on {tempt_var2} by implementing:
            "{tempt_action_2}"
            The desire for progress is a powerful motivator!
            Remember to keep tracking how this
            affects your data.
            """)
else:
    print(f"""
            Your focus on the data prevails! You continue to
            gathering reliable baseline data for {tempt_var2}
            without introducing changes. This approach
            should provide clearer insights when you reach
            the next phase.
            """)
petc() # Use petc()

# Temptation for trackvar1
tempt_var1 = trackvar1
tempt_action_1 = rd.choice(actions[tempt_var1])
improvebig4 = input(f"""
            You're nearing the end of Phase 1, focused on tracking.
            The final variable you're tracking is {tempt_var1}. You've
            gathered a good amount of data, and like the others, you
            see a potential area for significant improvement through
            a deliberate change, something like:

            "{tempt_action_1}"

            This is your last chance to potentially alter
            your baseline before Phase 1 concludes. Will
            you make an early move and implement this action,
            or see the tracking-only phase through to the end
            to preserve your pristine baseline data?

            y - Make this specific change for {tempt_var1} now.
            n - Complete Phase 1 by only tracking.
            """).lower()
clear()

if improvebig4 == "y":
    print(f"""
            You've decided to take action on {tempt_var1}
            by implementing:
            "{tempt_action_1}"
            Embarking on an improvement strategy early might
            give you a head start, but it changes the nature
            of your Phase 1 data. Observe closely!
            """)
else:
    print(f"""
            You successfully completed Phase 1 with a focus
            on consistent, unbiased tracking for {tempt_var1}
            and all your variables. This foundational data
            will be valuable for analyzing your state.
            """)
petc() # Use petc()

# --- End of Phase 1 ---
clear()
input(f"""
            Congratulations, {name}! You have successfully
            completed Phase 1 of this biohacking project:
            the dedicated tracking phase.

            You've gathered valuable baseline data on
            your chosen variables: {trackvar1}, {trackvar2},
            {trackvar3}, and {trackvar4}. This data provides
            a snapshot of your current habits and patterns.

            Now it's time to reflect. While your actual
            data is part of your personal journey, let's
            take a look at an my dataset from
            my project to see what kind
            of patterns might emerge from dedicated tracking.

            (Remember, this is just my data!)

            Press Enter to continue... """) # Use petc() function instead? Yes.
petc()
time.sleep(1)
# compare datas
if pickvarabcd.lower() == "b": # Use .lower() for consistency
    print("Interestingly, my data tracks a similar set of variables!")
    time.sleep(0.5)
    print(mydata)
else:
    print("Here is an example of what tracking data might look like:")
    time.sleep(0.5)
    print(mydata)

petc() # Use petc()
clear()

# --- Phase 2: Strategic Improvement (Now with specific, randomized actions) ---

# p
#   h       2   it
#     a   e       is
#       s         time...
p2varsel = input(f"""

            It has been several weeks since you began
            your biohacking journey, diligently tracking
            your chosen variables. You've completed Phase 1,
            establishing a baseline and gaining insight
            into your current habits.

            Now, {name}, the project enters an exciting
            new stage. It's time to move from pure
            observation to active intervention.

            Welcome to PHASE 2: Strategic Improvement.

            In this phase, you will select ONE variable
            from the ones you tracked in Phase 1. You will
            then focus your efforts on making deliberate,
            positive changes specifically to improve that
            chosen aspect of your life.

            Based on the data you've gathered and your own
            intuition, which single variable do you believe
            holds the greatest potential for positive impact
            on your well-being?

            Choose wisely, {name}.

            a - Variable 1: {trackvar1}
            b - Variable 2: {trackvar2}
            c - Variable 3: {trackvar3}
            d - Variable 4: {trackvar4}

            Enter a, b, c, or d:
""").lower() # Use .lower() for case-insensitivity

clear()

# Set p2var based on selection - Corrected mapping for 'c' and 'd' and added number support
p2var = "" # Initialize p2var
if p2varsel in ['a', '1']:
    p2var = trackvar1
    print(f"You've chosen to focus your improvement efforts on {p2var} during Phase 2.")
elif p2varsel in ['b', '2']:
    p2var = trackvar2
    print(f"An excellent choice, {name}! You've selected {p2var} as your primary focus for improvement.")
elif p2varsel in ['c', '3']:
    p2var = trackvar3 # Corrected mapping
    print(f"You've decided to concentrate your efforts on improving {p2var} in Phase 2.")
elif p2varsel in ['d', '4']:
    p2var = trackvar4 # Corrected mapping
    print(f"Alright, {p2var} will be your primary focus for positive change during Phase 2.")
else:
    print(f"That wasn't a valid selection. The project needs a clear focus.")
    quit() # Exit if no valid choice

petc() # Use petc()
clear()
input(f"""
            One of the core principles of biohacking is to
            actively work towards improving your life based
            on the data you've gathered.

            Now, in Phase 2, this principle becomes your mission.

            Your task is to implement changes and strategies
            specifically aimed at enhancing your performance
            or consistency in your chosen variable: {p2var}.

            For the duration of Phase 2, you will actively try
            to make positive changes related to {p2var} and
            continue tracking to see the effects.

            Good luck, {name}. Let the journey begin!
""")
time.sleep(2)
petc() # Use petc()
clear()

def phase2_scenario():
    """Presents a scenario during Phase 2 focusing on the chosen variable."""
    global p2var, actions # Need p2var and the actions dictionary

    # Get the list of actions for the chosen Phase 2 variable
    p2_actions_list = actions.get(p2var, ["Work on your chosen variable."]) # Default if variable not found

    # Randomly select a specific action to highlight in the scenario
    specific_action = rd.choice(p2_actions_list)

    # Use random.choice to select a general scenario type
    scenario_type = rd.choice([1, 2, 3, 4]) # Added a 4th type for more variety

    # Add a rare "birthday" scenario chance before presenting standard ones
    if rd.randint(1, 10) == 10: # 10% chance of birthday scenario
        input(f"""
            Just as you were planning to work on {p2var} today,
            perhaps by trying to:
            "{specific_action}"
            you suddenly remember... it's YOUR BIRTHDAY!

            Plans for improving {p2var} are momentarily
            forgotten in the face of cake and celebration.
            You decide to take the day off and just enjoy it.

            Happy Birthday, {name}!!!

            Press Enter to continue...""")
        petc()
        return "y" # Treat birthday as a "day off" from the specific action

    # Standard scenarios incorporating the specific action
    if scenario_type == 1:
        p2track1_input = input(f"""
            Okay, {name}, you're deep into Phase 2, actively
            working on improving {p2var}. Today presents an opportunity
            to take a step like:

            "{specific_action}"

            This is exactly the kind of action Phase 2 is for!
            However, you're feeling a pull towards slacking off,
            taking it easy. It would mean postponing this action.

            Do you push through and take the action, or relax today?

            y - Skip the action and relax today.
            n - Stay disciplined and take the action.
            """).lower()
    elif scenario_type == 2:
        p2track1_input = input(f"""
            Well, well, well, {name}. Time to put in the work
            to improve {p2var}. Today's goal could be something
            like:

            "{specific_action}"

            This requires getting up and making an effort.
            Alternatively, the call of the couch, bedrotting,
            and doomscrolling is strong. It requires zero effort.

            What's your decision? Do you embrace the task or the comfort?

            y - Do nothing but bedrot and doomscroll today.
            n - Get up and do whatever it takes to implement the action for {p2var}.
            """).lower()
    elif scenario_type == 3:
        p2track1_input = input(f"""
            You have an opportunity to really work on {p2var}
            today by attempting to:

            "{specific_action}"

            This would mean dedicating a significant
            chunk of time and effort.

            However, your friends just invited you out for a fun
            get-together. It would be great to
            hang out and relax with them.

            The choice is yours, {name}. Project goals or social plans?

            y - Go out with your friends.
            n - Stay focused and work on implementing the action for {p2var}.
            """).lower()
    else: # scenario_type == 4
        p2track1_input = input(f"""
            You've planned some time today to focus on improving {p2var},
            specifically aiming to:

            "{specific_action}"

            As the time approaches, you start feeling a bit of resistance.
            It feels like a chore, and finding motivation is tough right now.
            You could easily skip it today.

            Do you push through the resistance, or give in to the lack of motivation?

            y - Give in to the resistance and skip the action today.
            n - Push through and implement the action for {p2var}.
            """).lower()


    # Provide narrative feedback based on the choice
    while p2track1_input not in ['y', 'n']:
        print("\nInvalid input. Please enter 'y' or 'n'.")
        p2track1_input = input("Enter y or n: ").lower()

    if p2track1_input == "y":
        print(f"\nYou chose to skip the action today. Biohacking requires consistent effort, but sometimes life gets in the way. Note how this affects your data for {p2var}.")
    elif p2track1_input == "n":
        print(f"\nYou chose to stay committed! You worked on implementing: \"{specific_action}\". Keep observing your data for {p2var} to see the results.")

    petc() # Use petc()
    clear()
    return p2track1_input # Return choice if needed later (currently not used)


# Call the phase2 scenario multiple times to simulate progress
print(f"\nPhase 2 in progress: Focusing on {p2var}...")
phase2_scenario()
print(f"\nContinuing Phase 2: Working on {p2var}...")
phase2_scenario()
print(f"\nDeep into Phase 2: Maintaining focus on {p2var}...")
phase2_scenario()
print(f"\nNearing the end of Phase 2: Final push for {p2var}...")
phase2_scenario()


# Stopwatch was started earlier, stopping it here
sw.stop()
print(f"\nTime spent on this biohacking simulation: {sw.get_elapsed_time():.2f} seconds")
sw.reset() # Resetting after stopping might not be necessary if the program is ending

# Final message, removing score display
petc() # Use petc() before the final message input
input(f"""
            You have reached the end of this biohacking simulation, {name}.
            You tracked your variables in Phase 1, navigated temptations,
            and focused on actively improving {p2var} in Phase 2
            by making deliberate changes.

            Remember, real biohacking is an ongoing process
            of learning, experimenting, and adapting based on your
            own observations and goals.

            I hope this simulation was an interesting glimpse
            into the process of using data to understand and
            potentially improve aspects of your life.

            heres my data from phase 2""")
print(mydata1)

petc() # Use petc() one last time