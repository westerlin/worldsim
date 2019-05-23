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
    "his" : ["his","her"],
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

attractions = { 
    "traits":["beautiful", "sexy", "wealthy", "powerful", "mysterious", "funny", "gentle", "attentive","fit"]
} 


def getUnique(listObj, noOfItems):
    output = []
    noOfItems = min(noOfItems,len(listObj))
    newlist = listObj[:]
    idx = 0
    while idx < noOfItems:
        output.append(newlist.pop(random.randint(0,len(newlist)-1)))
        idx+=1
    return output

def getprofiletrait(dimension,score):
    if score < 0 :
        trait = "low"
    else:
        trait = "high"
    return "\n\t\t (+) " + random.choice(OCEAN[dimension][trait])


class World:
    
    def __init__(self):
        self.population = []
        self.epoch = 0
        
    def progress(self):
        for person in self.population:
            person.evolve()
        self.epoch += 1
        
    def add(self,person):
        self.population.append(person)
        person.context = self

class Person:
    
    def __init__(self,epoch=0,father=None,mother=None, world=None):
        self.yearOfBirth = epoch
        self.gender = random.choice([0,1])
        self.firstname = generateName(self.gender)
        self.cronicle = "===== oooo =====\n" 
        self.age = 0
        self.sexual_active = False
        self.alive = True
        if (father != None and mother != None):
            self.lastname = random.choice([father.lastname,mother.lastname])
            self.log(self.name() + " was born at time "+str(self.yearOfBirth)+".")
        else:
            self.lastname = generateName(random.choice([0,1]))
            self.log(self.name() + " was born at time "+str(self.yearOfBirth)+".")
            self.log(self.name() + " created "+ pronouns["his"][self.gender] + " own lineage.")
        self.openess = random.randint(-1,1)
        self.conscientiousness = random.randint(-1,1)
        self.extraversion = random.randint(-1,1)
        self.agreeableness = random.randint(-1,1)
        self.neuroticism = random.randint(-1,1)
        self.log(self.profile())
        self.context = world
        self.offspring = []
        self.father = father
        self.mother = mother
        self.relationship = {}
        self.traits = getUnique(attractions["traits"],1)
        self.desires = getUnique(attractions["traits"],3)
        #print(self.name() + " is ".join(self.traits) + " and desires ".join(self.desires) )
        self.log ( ""+self.name() + " is " + str(self.traits) + " and desires "+ str(self.desires) )
        if world != None:
            world.add(self)

    def log(self, paragraph):
            self.cronicle += "\t (+)" + paragraph + " (" + str(self.age) + " epochs)\n"

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
            self.log("Became a " + pronouns["adult"][self.gender] + self.atTheAgeOf())

    def match(self, prospect):
        return abs(self.age-prospect.age) < random.randint(4,15) and self.attracted(prospect) and prospect.attracted(self)
        
    def attracted(self,prospect):
        points = 4
        for desire in self.desires:
            if desire in prospect.traits:
                points += 1
        return random.randint(1,5) < points

    def fertile(self):
        childrenCount = len(self.offspring) < random.randint(1,10)
        return self.sexual_active and (self.gender == 0 or self.age < random.randint(43,55)) and childrenCount
        
    def displayTrait(self):
        return 
        
    def meet(self, person):
        pass

    def giveBirth(self, partner): 
        if (self.gender == 1 and partner.gender == 0 and self.match(partner) and self.fertile() and partner.fertile()):
            child = Person(epoch=self.context.epoch,father=partner,mother=self,world=self.context)
            self.log("Have sexual intercourse with "+partner.name()+" and gives birth to "+child.name())
            self.offspring.append(child)
            partner.log("Have sexual intercourse with "+self.name()+" with whom he has the child "+child.name())
            partner.offspring.append(child)
            return True 
        return False

    def evolve_ageing(self):
        self.age += 1
        if self.age > random.randint(70,99): 
            self.die()

    def die(self):
        self.log(self.name() +" died of old age" + self.atTheAgeOf())
        self.alive = False
        print(self)
        self.context.population.remove(self)
    
    def evolve(self):
        if self.alive:
            if (self.sexual_active == False) : self.evolve_sexuality()
            encounters = getUnique(self.context.population,self.extraversion+1 + self.openess+1)
            for encounter in encounters:
                if self.giveBirth(encounter):
                    break
            self.evolve_ageing()
            

malenames = loadNames("male.txt")
femalenames = loadNames("female.txt")

myworld = World()

for a in range(10):
    Person(epoch=0,world=myworld)

while myworld.epoch < 500:
    print(myworld.epoch, len(myworld.population))
    myworld.progress()

