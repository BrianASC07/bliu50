#<Brian> <Liu>
#<45>
#SoftDev
#K<04> -- <Python dictionairies and random selection/dictionairies and random selection/practiced using random selection on elements in a dict>
#<2024>-<09>-<16>
#time spent: <0.2hrs>
import random
krewes = {
           4: [ 
        'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
        'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
        'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
        'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
        ],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def chooseRandomDevo():
    classlist = list(krewes.keys())
    classrng = random.randint(0,len(krewes)-1)
    devorng = random.randint(0,len(krewes.get(classlist[classrng])) - 1)
    return krewes.get(classlist[classrng])[devorng]
print(chooseRandomDevo())