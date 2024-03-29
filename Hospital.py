import random
from Patient import Patient 
from Doctor import Doctor 
from tkinter import *
from tkinter import ttk
import asyncio
import time
class Hospital:
    def __init__(self, patient_list, doctor_list):
        self.patient_list = patient_list  
        self.doctor_list = doctor_list  
        self.available_doctors = []

    def init_patient(self):
        for i in range(500000):
            patient = Patient(patient_id=i, isTreated=False, sickness_level=random.randint(1, 3) , isCheckIn=False)
            self.patient_list.append(patient)
            #print(f"Patient {patient.patient_id} has sickness level {patient.sickness_level}")

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
            
    async def treat_patient(self, patients, doctors):
            untreated_patients = [patient for patient in patients if not patient.isTreated]
            available_doctors = [doctor for doctor in doctors if not doctor.isBusy]
            tasks = []
            for patient in untreated_patients:
                await self.start_treating(patient, available_doctors)

    async def start_treating(self,patient , available_doctors):
                    while not patient.isTreated:
                        for doctor in available_doctors:
                            if patient.sickness_level <= doctor.treat_level:
                                available_doctors.remove(doctor)
                                doctor.isBusy = True
                                #print(f"Doctor {doctor.doctor_id} starts treating patient {patient.patient_id}")
                                #await asyncio.sleep(patient.sickness_level)  
                                patient.isTreated = True
                                #print(f"Doctor {doctor.doctor_id} has finished treating patient {patient.patient_id} it took {patient.sickness_level} minutes")
                                doctor.isBusy = False
                                available_doctors.append(doctor)
                                return  
                            #else:
                                #print(f"Doctor {doctor.doctor_id} cannot treat patient {patient.patient_id} due to insufficient treat level")
                        #await asyncio.sleep(1)  
    

                

async def main():
    patient_list = []
    doctor_list = []
    hospital = Hospital(patient_list, doctor_list)
    hospital.init_patient()
    hospital.init_doctor()
    start = time.time()
    await hospital.treat_patient(patient_list, doctor_list)
    end = time.time()
    print(end - start)

if __name__ =="__main__":
    asyncio.run(main())
    print("all patients are treated")


