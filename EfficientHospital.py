import random
from Patient import Patient 
from Gui import Gui
from Doctor import Doctor 
import tkinter as tk
from queue import PriorityQueue
import asyncio

class Hospital:
    def __init__(self, patient_list, doctor_list):
        self.doctor_list = doctor_list  
        self.available_doctors = []
        self.patient_list = PriorityQueue()

    #initialize patient
    def init_patient(self):
        for i in range(20):
            patient_sickness_level = random.randint(1, 3)
            inverted_priority = -patient_sickness_level
            is_patient_checked_in = random.randint(0 , 100) < 10
            patient = Patient(patient_id=i, isTreated=False, sickness_level=-patient_sickness_level , isCheckIn=is_patient_checked_in)
            self.patient_list.put((-patient_sickness_level , patient))

    #initialize doctor
    def init_doctor(self):
        for i in range(5):
            doctor = Doctor(doctor_id=i, isBusy=False, treat_level=random.randint(1, 3)) 
            self.doctor_list.append(doctor)
            self.available_doctors.append(doctor)
        
        isLevel1 = False
        isLevel2 = False
        isLevel3 = False
        for doctor in self.doctor_list:
            if doctor.treat_level == 1:
                isLevel1 = True
            elif doctor.treat_level == 2:
                isLevel2 = True
            elif doctor.treat_level == 3:
                isLevel3 = True
            
        if not isLevel1:
            self.doctor_list[0] = Doctor(doctor_id=0, isBusy=False, treat_level=1)
        if not isLevel2:
            self.doctor_list[1] = Doctor(doctor_id=1, isBusy=False, treat_level=2)
        if not isLevel3:
            self.doctor_list[2] = Doctor(doctor_id=2, isBusy=False, treat_level=3)
            
    # while the patient list is not empty
    # receivces the first patient
    # 


    async def treat_patient(self):
        while not self.patient_list.empty():
            patient = self.patient_list.get()[1]
            await self.start_treating(patient, self.available_doctors)
            await asyncio.sleep(1)

    async def start_treating(self, patient , available_doctors):
        while not patient.isTreated:
            for doctor in available_doctors:
                if patient.sickness_level <= doctor.treat_level:
                    available_doctors.remove(doctor)
                    doctor.isBusy = True
                    print(f"Patient {patient.patient_id} is being treated by doctor {doctor.doctor_id} with sickness level {-1 *patient.sickness_level}")
                    print(f"patient waited {patient.timeSpentWaiting} minuites")
                    patient.isTreated = True
                    print(f"Patient {patient.patient_id} is treated by doctor {doctor.doctor_id} it took {patient.treatmentTime} minuites")
                    doctor.isBusy = False
                    available_doctors.append(doctor)
                    return
                else:
                    print(f"Doctor {doctor.doctor_id} cannot treat patient {patient.patient_id} due to sickness level")
    

        
    

                

async def main():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()
    patient_list = PriorityQueue()
    doctor_list = []
    hospital = Hospital(patient_list, doctor_list)
    hospital.init_patient()
    hospital.init_doctor()
    await hospital.treat_patient()

if __name__ =="__main__":
    asyncio.run(main())
    print("all patients are treated")


