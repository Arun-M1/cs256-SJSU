# Arun Murugan
# 2/20/2025
# This program implements simple reflex agent in a environment with 2 rooms. 
# The agent's performance is evaluated based on achieving clean rooms and how fast it cleans all rooms. 
import random

class Agent:
    # Create private variables for Agent
    def __init__(self):
        self.state = 0
        self.actionList = [0]

    def chooseAction(self):
        return self.actionList[0]
    
    def senseEnvironment(self, currentEnvironment):
        pass

    def getState(self):
        return 0

class Environment:
    # Create private variables for environment
    def __init__(self):
        self.state = 0

    def getCurrentEnvironment(self):
        return self.state

    def applyAgentAction(self, agentAction):
        pass

    def getState(self):
        return 0

# VaccuumBot inherits from the Agent superclass
class VaccuumBot(Agent):
    # Implement the specifics actions and logic of the Vaccuum Bot
    def __init__(self):
        super().__init__()
        self.location = "r1"
        self.actionList = ["move left", "move right", "clean", "stay in room"]
    
    def chooseAction(self):
        random_location = random.choice(vacEnv.getRooms())
        if self.location == "r1":
            #if room is dirty, return clean
            if vacEnv.getState() == 1:
                return "clean"
            #otherwise, move to other room
            else:
                self.location = random_location
                if self.location == "r2":
                    return "move right"
                else:
                    return "move left"
        elif self.location == "r2":
            if vacEnv.getState() == 1:
                return "clean"
            else:
                self.location = random_location
                if self.location == "r1":
                    return "move left"
                else:
                    return "move right"

    def getState(self):
        return self.location
    
    def senseEnvironment(self, currentEnvironment):
        if currentEnvironment == "r1":
            self.location = "r1"
        elif currentEnvironment == "r2":
            self.location = "r2"
    
# VaccuumEnvironment inherits from the Environment superclass
class VaccuumEnvironment(Environment):
    # Implement the specifics actions and logic of the Vaccuum Environment
    def __init__(self, scenario):
        super().__init__()
        self.roomList = ["r1", "r2"]
        #two rooms, 0 for clean, 1 for dirty
        self.scenarios = {
            "scenario one": {"r1": 1, "r2": 1, "room": "r1"}, #r1 dirty, r2 dirty, start left
            "scenario two": {"r1": 1, "r2": 1, "room": "r2"}, #r1 dirty, r2 dirty, start right
            "scenario three": {"r1": 0, "r2": 1, "room": "r1"}, #r1 clean, r2 dirty, start left
            "scenario four": {"r1": 0, "r2": 1, "room": "r2"}, #r1 clean, r2 dirty, start right
            "scenario five": {"r1": 1, "r2": 0, "room": "r1"}, #r1 dirty, r2 clean, start left
            "scenario six": {"r1": 1, "r2": 0, "room": "r2"}, #r1 dirty, r2 clean, start right
            "scenario seven": {"r1": 0, "r2": 0, "room": "r1"}, #r1 clean, r2 clean, start left
            "scenario eight": {"r1": 0, "r2": 0, "room": "r2"}, #r1 clean, r2 clean, start right
        }
        
        #assign rooms based on scenario
        if scenario in self.scenarios:
            self.rooms = self.scenarios[scenario]
            self.room = self.scenarios[scenario]["room"]
        else:
            #default
            self.rooms = self.scenarios["scenario one"]
            self.room = self.scenarios["scenario one"]["room"]

    def getCurrentEnvironment(self):
        return self.room

    def getState(self):
        return self.rooms[self.room]
    
    def applyAgentAction(self, agentAction):
        if agentAction == "clean":
            if self.room == "r1":
                self.rooms["r1"] = 0
            elif self.room == "r2":
                self.rooms["r2"] = 0
        elif agentAction == "move left":
            #change to left
            self.room = "r1"
        elif agentAction == "move right":
            #change to right
            self.room = "r2"
        #no change if action is stay
    
    def getRooms(self):
        return self.roomList

# We simulate the agent-environment interaction for several iterations
if __name__ == "__main__":
    vacBot = VaccuumBot() 
    vacEnvList = [VaccuumEnvironment("scenario one"),
                  VaccuumEnvironment("scenario two"),
                  VaccuumEnvironment("scenario three"),
                  VaccuumEnvironment("scenario four"),
                  VaccuumEnvironment("scenario five"),
                  VaccuumEnvironment("scenario six"),
                  VaccuumEnvironment("scenario seven"),
                  VaccuumEnvironment("scenario eight"),
                  ]

    #vacEnv is an object vaccuum environment from list of initialized environments
    
    for i, vacEnv in enumerate(vacEnvList):
        # print(f"Type of env: {type(env)}")
        print(f"\nScenario {i + 1}")
        for i in range(10):
            vacBot.senseEnvironment(vacEnv.getCurrentEnvironment())
            vacEnv.applyAgentAction(vacBot.chooseAction())
            print(f"Iteration: {i}")
            print(f"vacBot: {vacBot.getState()}")
            print(f"vacEnv: {vacEnv.getState()}")