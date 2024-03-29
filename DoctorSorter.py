class DoctorSorter:
    def __init__(self, doctor_list):
        self.doctor_list = doctor_list
        self.DoctorLvl1 = []
        self.DoctorLvl2 = []
        self.DoctorLvl3 = []

        for i in range(len(doctor_list)):
            if doctor_list[i].treat_level == 1:
                self.DoctorLvl1.append(doctor_list[i])
            elif doctor_list[i].treat_level == 2:
                self.DoctorLvl2.append(doctor_list[i])
            elif doctor_list[i].treat_level == 3:
                self.DoctorLvl3.append(doctor_list[i])