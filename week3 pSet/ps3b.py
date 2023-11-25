# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import random
import pylab

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        # random.seed(0)
        chance = random.random()

        if chance <= self.clearProb:
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # random.seed(0)
        chance = random.random()
        reproductionChance = self.maxBirthProb * (1 - popDensity)

        if chance <= reproductionChance:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """
        size = len(self.viruses)

        return size

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """
        newViruses = []

        for virus in self.viruses:
            if virus.doesClear():
                continue
            else:
                newViruses.append(virus)

        density = len(newViruses) / self.getMaxPop()

        finalViruses = []
        for virus in newViruses:
            finalViruses.append(virus)

            try:
                babyVirus = virus.reproduce(density)
                finalViruses.append(babyVirus)
            except NoChildException:
                continue

        self.viruses = finalViruses

        return len(newViruses)


#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    startingViruses = [SimpleVirus(maxBirthProb, clearProb) for _ in range(numViruses)]
    listsOfVirusesPerTrial = [[] for _ in range(300)]

    for _ in range(numTrials):
        patient = Patient(startingViruses, maxPop)

        for index in range(300):
            updatedPatient = patient.update()
            listsOfVirusesPerTrial[index].append(updatedPatient)

    virusAvgPerTrial = []

    for virusesList in listsOfVirusesPerTrial:
        virusAvgPerTrial.append(sum(virusesList) / numTrials)

    # return virusAvgPerTrial

    pylab.plot(virusAvgPerTrial, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

# print(simulationWithoutDrug(100, 1000, .1, .05, 300))


#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        super().__init__(maxBirthProb, clearProb)  # Call __init__ of the superclass
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        resistant = True
        for drug in activeDrugs:
            if self.resistances.get(drug, False) != True:  # False: Don't reproduce
                resistant = False

        if resistant:
            chance = random.random()
            if chance <= self.maxBirthProb * (1 - popDensity):  # Reproduction commence below
                offspring_resistances = self.resistances.copy()  # Create a copy of the resistances
                for drug, value in self.resistances.items():
                    resistChance = random.random()

                    if value:  # If it IS resistant to the drug 90%/10% - win/lose
                        if resistChance <= (1 - self.mutProb):
                            offspring_resistances[drug] = True
                        else:
                            offspring_resistances[drug] = False
                    else:  # It's NOT resistant to the drug 10%/90% - win/lose
                        if resistChance <= 1 - self.mutProb:
                            offspring_resistances[drug] = False
                        else:
                            offspring_resistances[drug] = True

                return ResistantVirus(self.maxBirthProb, self.clearProb, offspring_resistances, self.mutProb)
            else:
                raise NoChildException
        else:
            raise NoChildException


# virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
# for num in range(10):
#     child = virus.reproduce(0, [])
#     print("this is child ",child)


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The maximum virus population for this patient (an integer)
        """
        super().__init__(viruses, maxPop)  # Call __init__ of the superclass
        self.currentDrugs = [] ## A list of current drugs the TreatedPatient takes

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.currentDrugs:
            self.currentDrugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.currentDrugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistantViruses = 0

        for virus in self.viruses:
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    break
            else:
                resistantViruses +=1

        return resistantViruses

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        newViruses = []

        for virus in self.viruses:
            if virus.doesClear(): ## Virus got cleared
                continue
            else:
                newViruses.append(virus)
                density = len(newViruses) / self.getMaxPop()

                try:
                    babyVirus = virus.reproduce(density, self.currentDrugs)
                    newViruses.append(babyVirus)
                except NoChildException:
                    continue

        self.viruses = newViruses

        return len(self.viruses)


# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
# patient = TreatedPatient([virus1, virus2], 1000000)
# patient.addPrescription("drug1")

# for _ in range(5):
#     print(patient.update())

# print("Final update: ", patient.getTotalPop())


#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    virusList = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for _ in range(numViruses)]
    avgVirusPerUpdate = [[] for _ in range(300)]
    avgResistantVirus = [[] for _ in range(300)]

    for _ in range(numTrials):
        patient = TreatedPatient(virusList, maxPop)

        for index in range(150):
            avgVirusPerUpdate[index].append(patient.update())

            count = 0
            for virus in patient.viruses: ## Every update check how many viruses are resistant
                if virus.resistances.get("guttagonol", False):
                    count += 1
            avgResistantVirus[index].append(count)

        patient.addPrescription("guttagonol")

        for index in range(150):
            avgVirusPerUpdate[index + 150].append(patient.update())

            count = 0
            for virus in patient.viruses: ## Every update check how many viruses are resistant
                if virus.resistances.get("guttagonol", False):
                    count += 1
            avgResistantVirus[index + 150].append(count)

    finalAvgVirusPerUpdate = [] ## Calculating avg for total pop
    for specificUpdate in avgVirusPerUpdate:
        avg = sum(specificUpdate) / len(specificUpdate)
        finalAvgVirusPerUpdate.append(avg)

    secondFinalResistantVirus = [] ## Calculating avg for RESISTANT pop
    for specificUpdate in avgResistantVirus:
        avg = sum(specificUpdate) / len(specificUpdate)
        secondFinalResistantVirus.append(avg)

    pylab.plot(finalAvgVirusPerUpdate, label = "Non-Resistant")
    pylab.plot(secondFinalResistantVirus, label = "Resistant")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend(loc = "best")
    pylab.show()

print(simulationWithDrug(100, 1000, .1, .005, {"guttagonol": False}, .005, 2))
print("Done!")
