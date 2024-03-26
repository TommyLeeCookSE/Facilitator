company_dict = {
    "INFOSYS"               :   "INFOSYS LIMITED",
    "Roth"                  :   "ROTH STAFFIGNG",
    "Convergint"            :   "CONVERGINT",
    "PACIFIC BUILDING"      :   "PACIFIC BUILDING CARE",
    "DELOITTE CONSULTING"              :   "DELOITTE",
    "MBO"                   :   "MBO PARTNERS",
    "CLUNE"                 :   "CLUNE CONSTRUCTION",
    }

class Person:
    def __init__(self, fname, lname, EID, title, company, dept_num, supervisor_name,):
        self.fname              = fname
        self.lname              = lname
        self.EID                = EID
        self.title              = title
        self.company            = company
        self.dept_num           = dept_num
        self.supervisor_name    = supervisor_name
        self.location           = "IRVINE"
        self.clearance1         = "**GENERAL ACCESS - 24/7"
        self.clearance2         = "**GENERAL ACCESS (Varying Schedules)"
        self.clearance3         = "**LINC Access (0600-1800 M-F)"
        self.clearance4         = "**Parking Lot Access 24/7"

    def check_company_name(self):
        if self.company in company_dict:
            print(f'Company Name Provided: {self.company}\nCorrected Company Name: {company_dict[self.company]}')
        else:
            print(f'{self.company} is good.')



def process(data):
    split = [line.upper().split('\t') for line in data.split('\n')]
    employee_list = []
    for i,item in enumerate(split):
       employee_list.append(Person(split[i][0],split[i][1],split[i][2],split[i][3],split[i][4],split[i][5],split[i][6]))
    
    for i,item in enumerate(employee_list):
        employee_list[i].check_company_name()

#Function that takes costCenter and returns without the numbers
        
    employee_dict_list = [vars(employee) for employee in employee_list]
    
    return employee_dict_list