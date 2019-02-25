import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# input vaiable cgpa ,industry_knowledge , extra_co activties
#generating Universe variables for student performance to calculate CGPA

attendence=ctrl.Antecedent(np.arange(0,6,1),'attendence')  #(Attendence)
CA=ctrl.Antecedent(np.arange(0,26,1),'CA')                 #(CA-Continous Assignment)
MTE=ctrl.Antecedent(np.arange(0,21,1),'MTE')               #MTE=(MID TERM EXAMINATIONN)
ETE=ctrl.Antecedent(np.arange(0,51,1),'ETE')               #ETE(END TERM EXAMINATION)
CGPA=ctrl.Consequent(np.arange(0,11,1),'CGPA')             #CGPA OF STUDENT (OUPUT)

#generate fuzzy membership function for above variables

attendence['low']=fuzz.trimf(attendence.universe,[0,0,2])
attendence['average']=fuzz.trimf(attendence.universe,[0,2,5])
attendence['high']=fuzz.trimf(attendence.universe,[2,5,5])

'''attendence.view()'''
# generating fuzzy membership function for CA Variables

CA['low']=fuzz.trimf(CA.universe,[0,0,12])
CA["average"]=fuzz.trimf(CA.universe,[0,12,25])
CA["high"]=fuzz.trimf(CA.universe,[12,25,25])


'''CA.view()''' #view CA Graph
# Generating fuzzy Membership for MTE Variables

MTE["low"]=fuzz.trimf(MTE.universe,[0,0,10])
MTE["average"]=fuzz.trimf(MTE.universe,[0,10,20])
MTE["high"]=fuzz.trimf(MTE.universe,[10,20,20])


'''MTE.view()'''
#ETE fuzzy membership

ETE["low"]=fuzz.trimf(ETE.universe,[0,0,25])
ETE["average"]=fuzz.trimf(ETE.universe,[0,25,50])
ETE["high"]=fuzz.trimf(ETE.universe,[25,50,50])

'''ETE.view()'''

#cgpa membership function

CGPA["low"]=fuzz.trapmf(CGPA.universe,[0,0,2,5])
CGPA['average']=fuzz.trimf(CGPA.universe,[2,5,8])
CGPA['high']=fuzz.trapmf(CGPA.universe,[5,7,10,10])

'''CGPA.view()'''

#rules for CGPA calculation

r1=ctrl.Rule(attendence['low']|CA['low']|MTE['low']|ETE['low'],CGPA['low'])
r2=ctrl.Rule(attendence['low']|CA['low']|MTE['average']|ETE['average'],CGPA['low'])
r3=ctrl.Rule(attendence['high']|CA['low']|MTE['high']|ETE['high'],CGPA['average'])
r4=ctrl.Rule(attendence['average']&CA['average']|MTE['low']&ETE['low'],CGPA['low'])
r5=ctrl.Rule(attendence['average']&CA['average']|MTE['average']&ETE['average'],CGPA['high'])
r6=ctrl.Rule(attendence['average']&CA['average']|MTE['high']&ETE['high'],CGPA['high'])
r7=ctrl.Rule(attendence['high']&CA['high']|MTE['low']&ETE['low'],CGPA['high'])
r8=ctrl.Rule(attendence['high']&CA['high']|MTE['average']&ETE['average'],CGPA['high'])
r9=ctrl.Rule(attendence['high']&CA['high']|MTE['high']|ETE['high'],CGPA['high'])             
r10=ctrl.Rule(attendence['high']&CA['high']& MTE['high']&ETE['high'],CGPA['high'])

CGPA_ctrl=ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10])      #merging rule into system
GRADE_cal=ctrl.ControlSystemSimulation(CGPA_ctrl)

#above code is for calcualting cgpa of student:

#adacmic cgpa,industrial knowledge and extra co-currilar activity as input variavle:

acadmic_cgpa=ctrl.Antecedent(np.arange(0,10,1),'acadmic_cgpa')
industry=ctrl.Antecedent(np.arange(0,11,1),'industry')
extra_co=ctrl.Antecedent(np.arange(0,11,1),'extra_co')

performance=ctrl.Consequent(np.arange(0,11,1),'performance')

# universe vaiables and memvership function for input variables

acadmic_cgpa['poor']=fuzz.trapmf(acadmic_cgpa.universe,[0,0,2,5])
acadmic_cgpa['average']=fuzz.trimf(acadmic_cgpa.universe,[2,5,8])
acadmic_cgpa['good']=fuzz.trapmf(acadmic_cgpa.universe,[5,7,10,10])

industry['poor']=fuzz.trapmf(industry.universe,[0,0,2,5])         #industry knowledge
industry['good']=fuzz.trimf(industry.universe,[2,5,8])
industry['very good']=fuzz.trapmf(industry.universe,[5,7,10,10])

extra_co['not active']=fuzz.trapmf(extra_co.universe,[0,0,2,5]) #extra_cocular activity
extra_co['average']=fuzz.trimf(extra_co.universe,[2,5,8])
extra_co['active']=fuzz.trapmf(extra_co.universe,[5,7,10,10])

performance['poor']=fuzz.trapmf(performance.universe,[0,0,2,5])
performance['good']=fuzz.trimf(performance.universe,[2,5,8])
performance['very good']=fuzz.trapmf(performance.universe,[5,7,10,10])

'''acadmic_cgpa.view()
industry.view()
extra_co.view()
performance.view()'''

#rules for Perfromance Calculation

rule1=ctrl.Rule(acadmic_cgpa['poor']&industry['poor']&extra_co['not active'],performance['poor'])
rule2=ctrl.Rule(acadmic_cgpa['poor']&industry['poor']&extra_co['not active'],performance['poor'])
rule3=ctrl.Rule(acadmic_cgpa['poor']&industry['poor']&extra_co['average'],performance['poor'])
rule4=ctrl.Rule(acadmic_cgpa['poor']&industry['poor']&extra_co['active'],performance['good'])
rule5=ctrl.Rule(acadmic_cgpa['average']&industry['good']&extra_co['not active'],performance['good'])
rule6=ctrl.Rule(acadmic_cgpa['average']&industry['good']&extra_co['average'],performance['good'])
rule7=ctrl.Rule(acadmic_cgpa['average']&industry['good']&extra_co['active'],performance['very good'])
rule8=ctrl.Rule(acadmic_cgpa['good']&industry['very good']&extra_co['not active'],performance['good'])
rule9=ctrl.Rule(acadmic_cgpa['good']&industry['very good']|extra_co['average'],performance['very good'])
rule10=ctrl.Rule(acadmic_cgpa['good']|industry['very good']|extra_co['active'],performance['very good'])

performance_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10])
performance_cal=ctrl.ControlSystemSimulation(performance_ctrl)

#acadmic cgpa calualtion

GRADE_cal.input["attendence"]=int(input("Enter student attendence[0-5] for adamic cgpa"))
GRADE_cal.input["CA"]=int(input("Enter student's CA Marks [0-25] for adamic cgpa"))
GRADE_cal.input["MTE"]=int(input("Enter student's MTE marks[0-20] for adamic cgpa"))
GRADE_cal.input["ETE"]=int(input("Enter student's ETE Marks[0-50] for adamic cgpa"))
GRADE_cal.compute()


performance_cal.input['industry']=int(input('Enter industry traing grade between[1-10]'))
performance_cal.input['extra_co']=int(input('Enter student activity in extra co-curricular [1-10]'))
performance_cal.input['acadmic_cgpa']=GRADE_cal.output["CGPA"]     # calculated  CGPA as input for perfromance
performance_cal.compute()
print("CGPA Of Student:",GRADE_cal.output["CGPA"])
print("Performance Of Student is:",performance_cal.output['performance'])

performance.view(sim=performance_cal)
CGPA.view(sim=GRADE_cal)




                

































