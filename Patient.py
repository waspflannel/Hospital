import random

class Patient:
    def __init__(self ,patient_id , isTreated , sickness_level , isCheckIn) -> None:
        self.patient_id = patient_id
        self.isTreated = isTreated
        self.sickness_level = sickness_level
        self.isCheckedIn = isCheckIn
        self.timeSpentWaiting = self.WaitingTime()
        self.treatmentTime = self.TreatmentTime()

    # comparison to break ties in the priority queue
    def __lt__(self, other):
        return self.patient_id < other.patient_id

    #generate a random time for how long it will take for a doctor to treat a patient
    def WaitingTime(self):
        return random.randint(10,21) * self.sickness_level * -1

    def TreatmentTime(self):
        return random.randint(10,19) * self.sickness_level * -1
    
