import random


def loadNames(filename):
    names = open(filename).readlines()
    names = [n.strip('\n') for n in names]
    return names

malenames = []
femalenames = []

def generateName(gender):
    if gender == 0:
        return random.choice(malenames)
    else:
        return random.choice(femalenames)

pronouns = {
    "his" : ["his","hers"],
    "he" : ["he","she"],
    "him" : ["him","her"],
    "tl" : ["mr.","mrs."],
    "sex" : ["male","female"],
    "infant" : ["boy", "girl"],
    "adult" : ["man","woman"]
}

# https://www.verywellmind.com/the-big-five-personality-dimensions-2795422

"""
    The findings suggested that the heritability of each trait was 53 percent for extraversion, 41 percent for agreeableness, 44 percent for conscientiousness, 41 percent for neuroticism, and 61 for openness. 
    
    Longitudinal studies also suggest that these big five personality traits tend to be relatively stable over the course of adulthood. One study of working-age adults found that personality tended to be stable over a four-year period and displayed little change as a result of adverse life events.

    Studies have shown that maturation may have an impact on the five traits. As people age, they tend to become less extraverted, less neurotic, and less open to experience. Agreeableness and conscientiousness, on the other hand, tend to increase as people grow older.
    
"""

OCEAN = {
    "Openess":{
        "description": "This trait features characteristics such as imagination and insight. People who are high in this trait also tend to have a broad range of interests. They are curious about the world and other people and eager to learn new things and enjoy new experiences. People who are high in this trait tend to be more adventurous and creative. People low in this trait are often much more traditional and may struggle with abstract thinking.",
        "high" : ["Very creative", "Open to trying new things", "Focused on tackling new challenges", "Happy to think about abstract concepts"],
        "low": ["Dislikes change", "Does not enjoy new things", "Resists new ideas", "Not very imaginative", "Dislikes abstract or theoretical concepts"]
    },
    "Conscientiousness":{
        "description": "Standard features of this dimension include high levels of thoughtfulness, good impulse control, and goal-directed behaviors. Highly conscientious people tend to be organized and mindful of details. They plan ahead, think about how their behavior affects others, and are mindful of deadlines.",
        "high" : ["Spends time preparing", "Finishes important tasks right away",
                    "Pays attention to detail", "Enjoys having a set schedule"],
        "low": ["Dislikes structure and schedules", "Makes messes and doesn't take care of things", "Fails to return things or put them back where they belong", "Procrastinates important tasks", "Fails to complete necessary or assigned tasks"]
    },    
    "Extraversion":{
        "description": "Extraversion (or extroversion) is characterized by excitability, sociability, talkativeness, assertiveness, and high amounts of emotional expressiveness. People who are high in extraversion are outgoing and tend to gain energy in social situations. Being around other people helps them feel energized and excited.People who are low in extraversion (or introverted) tend to be more reserved and have to expend energy in social settings. Social events can feel draining and introverts often require a period of solitude and quiet in order to recharge.",
        "high" : ["Enjoys being the center of attention", "Likes to start conversations", "Enjoys meeting new people", "Has a wide social circle of friends and acquaintances", "Finds it easy to make new friends", "Feels energized when around other people", "Say things before thinking about them"],
        "low": ["Prefers solitude", "Feels exhausted when having to socialize a lot" , "Finds it difficult to start conversations", "Dislikes making small talk", "Carefully thinks things through before speaking", "Dislikes being the center of attention"]
    },    
    "Agreeableness":{
        "description": "This personality dimension includes attributes such as trust, altruism, kindness, affection, and other prosocial behaviors. People who are high in agreeableness tend to be more cooperative while those low in this trait tend to be more competitive and sometimes even manipulative.",
        "high" : ["Has a great deal of interest in other people", "Cares about others", "Feels empathy and concern for other people", "Enjoys helping and contributing to the happiness of other people", "Assists others who are in need of help"],
        "low": ["Takes little interest in others", "Doesn't care about how other people feel" , "Has little interest in other people's problems", "Insults and belittles others", "Manipulates others to get what they want"]
    },    
    "Neuroticism":{
        "description": "Neuroticism is a trait characterized by sadness, moodiness, and emotional instability. Individuals who are high in this trait tend to experience mood swings, anxiety, irritability, and sadness. Those low in this trait tend to be more stable and emotionally resilient.",
        "high" : ["Experiences a lot of stress", "Worries about many different things", "Gets upset easily" , "Experiences dramatic shifts in mood", "Feels anxious", "Struggles to bounce back after stressful events"],
        "low": ["Emotionally stable", "Deals well with stress", "Rarely feels sad or depressed", "Doesn't worry much", "Is very relaxed"]
    }
}

def getprofiletrait(dimension,score):
    if score < 0 :
        trait = "low"
    else:
        trait = "high"
    return "\n\t\t (+) " + random.choice(OCEAN[dimension][trait])


class Person:
    
    def __init__(self,epoch=0,father=None,mother=None):
        self.yearOfBith = epoch
        self.gender = random.choice([0,1])
        self.firstname = generateName(self.gender)
        self.cronicle = "===== oooo =====\n" 
        if (father != None and mother != None):
            self.lastname = random.choice([father.lastname,mother.lastname])
            self.cronicle += "\t (+)" + self.name() + " was born at time "+str(epoch)+".\n"
        else:
            self.lastname = generateName(random.choice([0,1]))
            self.cronicle += "\t (+)" + self.name() + " was born at time "+str(epoch)+".\n"
            self.cronicle += "\t (+)" + self.name() + " created "+ pronouns["his"][self.gender] + " own lineage.\n"
        self.age = 0
        self.sexual_active = False
        self.alive = True
        self.openess = random.randint(-1,1)
        self.conscientiousness = random.randint(-1,1)
        self.extraversion = random.randint(-1,1)
        self.agreeableness = random.randint(-1,1)
        self.neuroticism = random.randint(-1,1)
        self.cronicle = "\t (+) " + self.profile() + "\n"


    def profile(self):
        return self.name() + " are characterized by " + getprofiletrait("Openess",self.openess) + ", "  + getprofiletrait("Extraversion",self.extraversion) + ", " + getprofiletrait("Agreeableness",self.agreeableness) + ", " + getprofiletrait("Conscientiousness",self.conscientiousness) + ", "  + getprofiletrait("Neuroticism",self.neuroticism) + "."
        
    def name(self):
        return self.firstname + " " + self.lastname
    
    def atTheAgeOf(self):
        return " when " + pronouns["he"][self.gender] + " was " + str(self.age) + " epochs old." 
        
    def __str__(self):
        return self.name() +" aged " + str(self.age) + "\n" + self.cronicle
        
    def evolve_sexuality(self):
        if self.sexual_active : return
        self.sexual_active = random.randint(12,16) < self.age
        if self.sexual_active:
            self.cronicle += "\t (+)Became a " + pronouns["adult"][self.gender] + self.atTheAgeOf() + "\n"

    def evolve_ageing(self):
        self.age += 1
        if self.age > random.randint(70,99): 
            self.die()

    def die(self):
        self.cronicle += "\t (+)" + self.name() +" died of old age" + self.atTheAgeOf() + "\n"
        self.alive = False
    
    def evolve(self):
        if self.alive:
            if (self.sexual_active == False) : self.evolve_sexuality()
            self.evolve_ageing()

malenames = loadNames("male.txt")
femalenames = loadNames("female.txt")
    

somebody = Person(0)
while somebody.alive:
    somebody.evolve()

print(somebody)

