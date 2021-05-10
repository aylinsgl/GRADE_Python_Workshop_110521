from random import sample, choices, randint
from time import sleep

mailbox_codes = list(map(lambda n: str(n), sample(range(0,10), 5)))

instruction_letter = f"""\
{'=' * 32}

I have captured your friend Python. If you want to have it back, you will have to prove yourself first! I need to find out if you are truly worthy of keeping it.
So, to test you I have created a number of challenges you will need to complete. Whenever you have finished a challenge you can submit your answer to me, the challenger, by running the following python command:

    challenger.submit(key = ___)
    
You need to supply your solution as the key. If your solution is correct you will receive important information about your next challenge. If not, well that's just bad luck. Let's see if you can do this!

{'=' * 32}
"""

class Task:
    def __init__(self, index, data, checker, msg_correct, msg_err, descr):
        self.index       = index
        self.data        = data
        self.checker     = checker
        self.msg_correct = msg_correct
        self.msg_err     = msg_err
        self.descr       = descr
        self.info        = f"The data that is provided for the task is:\n\n{self.data}"

class Challenger:
    def __init__(self):
        self.challenge_nr = 0

        # generate tasks
        tasks = []

        tasks.append(
            Task(
                0,
                "test",
                lambda s: s == "test",
                "Good. Everything is working as intended.\nOk, Ok ... I feel a little bit harsh not providing you with any help. If you need help with any of the challenges just use the phone I've provided for you to call someone for help:\n\n    helper.call()",
                "Something went wrong. Are you sure you submitted the right argument?",
                "I'll get you warmed up by testing this function call."
            )
        )

        c2_data = sample(range(1,50), 20)
        tasks.append(
            Task(
                1,
                c2_data,
                lambda s: s == c2_data[::-1],
                "This list looks right to me. How'd you learn so fast?",
                "Something is not right about this list. Can you spot the error?",
                "For the first task, you will need the list you will be provided with below. Simply copy and paste it and store it in a variable in order to work with it. Remember, you can always call challenger.task_info() to get this task description. Scroll further down to see the description of task 1."
            )
        )

        tasks.append(
            Task(
                2,
                42,
                lambda s: s == (42 * (2.5**5)),
                "Perfect. This would have been a pain to work out by hand.",
                "You didn't provide me with the right number. Maybe the number of iterations is not correct?",
                "You can find a number below. Scroll further down to the description of task 2 to see what you are supposed to do with it."
            )
        )

        tasks.append(
            Task(
                3,
                [ord(c) for c in "mozzarella"],
                lambda s: (s == "mozzarella") or (s == ['m','o','z','z','a','r','e','l','l','a']),
                "Yum. Move on to the next task.",
                "This gives off the wrong taste. Are you sure the word you provided me with makes sense?",
                "Below you can find a weird-looking list. Find out what to do with it by scrolling further down and reading the description of task 3."
            )
        )

        tasks.append(
            Task(
                4,
                sample(["Flour","Banana","Sugar","Milk","Eggs","Salt"], 6),
                lambda s: set(["Milk", "Flour", "Salt", "Eggs"]) == set(s),
                "Perfect. I will set off to the Supermarket Of My Trust™ to get what's missing.",
                "I don't think that is enough to bake Python's favourite cake.",
                "Below you can find a shopping list. Scroll further down and read the description of task 4."
            )
        )

        tasks.append(
            Task(
                5,
                32,
                lambda s: (s(1) == 365) and (s(2) == 2*365) and (s(10) == 10*365),
                "This function works for me.",
                "That's not correct.",
                "Given below is the age of Python in years. Scroll further down to read the description of task 5."
            )
        )

        c6_helper = {"*": 1, "#": -1, "->": 3, "<-": -3}
        c6_data = choices(["*", "#", "->", "<-"], k=randint(11, 17))
        tasks.append(
            Task(
                6,
                c6_data,
                lambda s: s == sum([c6_helper[s] for s in c6_data]),
                "You open the door. You see Python. United at last, everything is fine again.",
                "You open the door to an empty room. This must have been the wrong door.",
                "Below you find a list of cryptic codes. Copy them and solve the final task that is given further down to get Python back."
            )
        )

        self.__tasks = tasks

    def task_info(self):
        t = self.__tasks[self.challenge_nr]  # current task
        print(f"Your current task is the following:\n\n{t.descr}\n\n{t.info}")

    def submit(self, key):
        print(f"You submitted the the following value:\n\n{key}.\n")
        t = self.__tasks[self.challenge_nr]  # current task
        if (t.checker(key)):
            print(f"{t.msg_correct}\n\n{'=' * 32}\n")
            self.challenge_nr += 1
            if self.challenge_nr <= 6:
                t = self.__tasks[self.challenge_nr]
                print(f"{t.descr}\n\n{t.info}")
        else:
            print(t.msg_err)
        return
            
        
    def get_challenge_nr(self):
        return self.challenge_nr


class Helper:
    def __init__(self, challenger):
        self.challenger = challenger
        self.calls_received = [0 for _ in range(7)]
        self.help_msgs = []
        
        further_help = "If you need any further help, remember you can always ask for help in the Zoom call!"
        
        # task 0
        self.help_msgs.append([
            "Hey, I'm the helper. Call me beep me if you wanna reach me. You can always call me multiple times to get more specific tips."
        ])
        
        # task 1
        self.help_msgs.append([
            "You can reverse a list in multiple ways! You could use a built-in function or a for-loop (advanced). Call me again if you need more specific help.",
            "Using a built-in function is an elegant way to solve this problem. Since reversing lists is something many people frequently need, you can look up \"python reverse list\" using the search engine of your trust to find some more information.",
        ])
        
        # task 2
        self.help_msgs.append([
            "This task is about using for-loops. You can use for-loops to repeatedly apply some sequence of operations multiple times.",
            "This may look weird at first, but the statement\n\n    x = x * p\n\nmultiplies the number x by p and stores the result in x."
        ])
        
        # task 3
        self.help_msgs.append([
            "Use a for-loop to translate each number into a letter. To test whether this approach works, you can print out each letter first, without storing the result in a variable.",
            "In python, you can add characters to strings. The following equality holds:\n\n    \"Chees\" + \'e\' = \"Cheese\"",
            "Add each translated letter to a string which can be initialised as the empty string \"\"."
        ])
        
        # task 4
        self.help_msgs.append([
            "If you want to add an item i to a list L, you can simply use the following command:\n\n    L.append(i).",
            "To check whether some value x is contained in a list L, you can use the following command:\n\n    x in L\n\nThis returns True if x is contained in L, otherwise it returns False.",
            "Based on whether an item from the \'need\'-list is missing from the \'have\'-list, you need to add it to the \'buy\'-list using the command given in the first tip."
        ])
        
        # task 5
        self.help_msgs.append([
            "Remember, to have a function \'give back\' some value when it is called, you need to use a \'return\' statement.",
            "You need to multiply the function argument \'years\' with some value and return the result."
        ])
        
        # task 6
        self.help_msgs.append([
            "This is a challenging task. You need to loop over all symbols and use if-elif-statements to execute different operations based on the symbol.",
            "Try to break the task down into subproblems: what are the steps the function needs to complete in order to solve the code?",
            "You can imagine reading the symbols one after the other and walking left or right depending on which symbol you're reading. Store your current position (starting with 0) in some variable and increase or decrease it based on the symbol-to-steps mapping given above."
        ])
        
        for l in self.help_msgs:
            l.append(further_help)
            
        return
            
            
    def call(self):
        # get current task nr
        challenge_nr = self.challenger.get_challenge_nr()
        # increase number of calls received for current task
        self.calls_received[challenge_nr] += 1
        # determine how many of the help messages to print out
        max_msg_index = min(self.calls_received[challenge_nr], len(self.help_msgs[challenge_nr]))
        
        # cosmetics
        print("You call up the helper... ", end="")
        for i in range(randint(3,5)):
            sleep(1.5)
            print(" *beep* ", end="")
        sleep(1)
        print("\n")
        
        # print help messages for current task up to index max_msg_index-1
        for msg_index in range(max_msg_index):
            print(f"({msg_index+1}/{len(self.help_msgs[challenge_nr])}) ", end="")
            print(self.help_msgs[challenge_nr][msg_index])


def open_mailbox(key):
    sol = int(mailbox_codes[0]) + int(mailbox_codes[1]) + int(mailbox_codes[3])

    if key == sol:
        c = Challenger()
        h = Helper(c)
        print("You open the mailbox. In it you find the following letter:")
        print(instruction_letter)
    else:
        c, h = None, None
        print("The mailbox beeps. You entered the wrong code.")
    
    return c, h
