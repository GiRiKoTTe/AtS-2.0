##############################_______Math_Def________################################
def x_round(number, rounding):
      return round(number * (1/rounding)) / (1/rounding)
##############################_______Quick Setup_______##############################

quick_setup_main_rounding = .25

quick_setup_main_target_percent = [50.0,52.5,55.0,57.5,60.0,62.5,65.0,67.5,70.0,72.5,75.0,77.5,80.0,82.5,85.0,87.5,90.0,92.5,95.0,97.5,100.0
]

#Main
quick_setup_main = "main"
quick_setup_main_max = 490.0
quick_setup_main_single_at_8 = 90.0
quick_setup_main_behavior_RIR_sets = [5]*21
quick_setup_main_behavior_RIR_adjust =      [-5,-2,0,.5,1,1.5,2,3]
quick_setup_main_rep_target =       [8,8,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,1,1,1]
quick_setup_main_last_set_RIR_target =      [3,3,3,3,3,3,3,3,3,3,2,2,2,2,1,1,1,1,1,0,0]
quick_setup_main_intensity =        [70.0,75.0,80.0,72.5,77.5,82.5,60.0,75.0,80.0,85.0,77.5,82.5,87.5,60.0,80.0,85.0,90.0,85.0,90.0,95.0,60.0]

##############################______Setup______##############################

#Main

setup_main_intensity = quick_setup_main_intensity
setup_main_sets = quick_setup_main_behavior_RIR_sets
setup_main_behavior_RIR_adjust = quick_setup_main_behavior_RIR_adjust

def setup_main_reps_per_set (w):
    if setup_main_intensity[w-1] == quick_setup_main_target_percent[0]:
      return quick_setup_main_rep_target[0]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[1]:
      return quick_setup_main_rep_target[1]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[2]:
      return quick_setup_main_rep_target[2]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[3]:
      return quick_setup_main_rep_target[3]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[4]:
      return quick_setup_main_rep_target[4]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[5]:
      return quick_setup_main_rep_target[5]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[6]:
      return quick_setup_main_rep_target[6]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[7]:
      return quick_setup_main_rep_target[7]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[8]:
      return quick_setup_main_rep_target[8]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[9]:
      return quick_setup_main_rep_target[9]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[10]:
      return quick_setup_main_rep_target[10]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[11]:
      return quick_setup_main_rep_target[11]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[12]:
      return quick_setup_main_rep_target[12]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[13]:
      return quick_setup_main_rep_target[13]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[14]:
      return quick_setup_main_rep_target[14]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[15]:
      return quick_setup_main_rep_target[15]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[16]:
      return quick_setup_main_rep_target[16]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[17]:
      return quick_setup_main_rep_target[17]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[18]:
      return quick_setup_main_rep_target[18]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[19]:
      return quick_setup_main_rep_target[19]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[20]:
      return quick_setup_main_rep_target[20]
    elif setup_main_intensity[w-1] == quick_setup_main_target_percent[21]:
      return quick_setup_main_rep_target[21]
    else:
      print ("check")

def setup_main_last_set_RIR (w):
  if setup_main_intensity[w-1] == quick_setup_main_target_percent[0]:
    return quick_setup_main_last_set_RIR_target[0]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[1]:
    return quick_setup_main_last_set_RIR_target[1]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[2]:
    return quick_setup_main_last_set_RIR_target[2]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[3]:
    return quick_setup_main_last_set_RIR_target[3]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[4]:
    return quick_setup_main_last_set_RIR_target[4]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[5]:
    return quick_setup_main_last_set_RIR_target[5]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[6]:
    return quick_setup_main_last_set_RIR_target[6]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[7]:
    return quick_setup_main_last_set_RIR_target[7]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[8]:
    return quick_setup_main_last_set_RIR_target[8]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[9]:
    return quick_setup_main_last_set_RIR_target[9]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[10]:
    return quick_setup_main_last_set_RIR_target[10]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[11]:
    return quick_setup_main_last_set_RIR_target[11]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[12]:
    return quick_setup_main_last_set_RIR_target[12]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[13]:
    return quick_setup_main_last_set_RIR_target[13]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[14]:
    return quick_setup_main_last_set_RIR_target[14]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[15]:
    return quick_setup_main_last_set_RIR_target[15]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[16]:
    return quick_setup_main_last_set_RIR_target[16]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[17]:
    return quick_setup_main_last_set_RIR_target[17]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[18]:
    return quick_setup_main_last_set_RIR_target[18]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[19]:
    return quick_setup_main_last_set_RIR_target[19]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[20]:
    return quick_setup_main_last_set_RIR_target[20]
  elif setup_main_intensity[w-1] == quick_setup_main_target_percent[21]:
    return quick_setup_main_last_set_RIR_target[21]
  else:
    print ("check")

##############################______Untouched______##############################

##############################MAIN########################

####mainTM####
untouched_mainTM_last_set_RIR_target = [""]*21
untouched_mainTM_sets_completed = [""]*21
untouched_mainTM_reps_per_set = ["single@8"]*21
untouched_mainTM_set_goal = [""]*21
untouched_mainTM_RIR_on_last_set = [""]
def untouched_mainTM_weight(w):
  if w==1:
    if untouched_mainTM_last_set_RIR_target[w-1] == "":
      return quick_setup_main_max
    else:
      return (untouched_mainTM_last_set_RIR_target[w-1])/(quick_setup_main_single_at_8)
  elif w >= 2 and w <= 21:
    if untouched_mainTM_last_set_RIR_target[w-1] == "":#L3
      if untouched_main_sets_completed[w-2] == "":#F4
        return untouched_mainTM_weight(w-1)
      elif (untouched_main_sets_completed[w-2] - setup_main_sets[w-2]) < -1.9:#1.9
        return (untouched_mainTM_weight(w-2))*(1+ setup_main_behavior_RIR_adjust(w)[0])
      elif (untouched_main_sets_completed[w-2] - setup_main_sets[w-2]) == -1: #-1
        return (untouched_mainTM_weight(w-2))*(1+ setup_main_behavior_RIR_adjust(w)[1])
      elif (untouched_main_RIR_on_last_set[w-2]) < (setup_main_last_set_RIR[w-2]):#g4<
        return (untouched_mainTM_weight(w-2))*(1+ setup_main_behavior_RIR_adjust(w)[1])
      elif (untouched_main_RIR_on_last_set[w-2]) == (setup_main_last_set_RIR[w-2]):#g4=
        return (untouched_mainTM_weight(w))*(1+ setup_main_behavior_RIR_adjust(w)[2])
      elif ((untouched_main_RIR_on_last_set[w-2]) - (setup_main_last_set_RIR[w-2])) == 1:#=1
        return ((untouched_mainTM_weight(w))*(1+ setup_main_behavior_RIR_adjust(w)[3]))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (setup_main_last_set_RIR[w-2])) == 2:#=2
        return ((untouched_mainTM_weight(w))*(1+ setup_main_behavior_RIR_adjust(w)[4]))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (setup_main_last_set_RIR[w-2])) == 3:#=3
        return ((untouched_mainTM_weight(w))*(1+ setup_main_behavior_RIR_adjust(w)[5]))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (setup_main_last_set_RIR[w-2])) == 4:#=4
        return ((untouched_mainTM_weight(w))*(1+ setup_main_behavior_RIR_adjust(w)[6]))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (setup_main_last_set_RIR[w-2])) > 4.1:#>4
        return ((untouched_mainTM_weight(w))*(1+ setup_main_behavior_RIR_adjust(w)[7]))
      else:
        return untouched_mainTM_weight(w)
    else:
      return (untouched_mainTM_last_set_RIR_target[w-1])/(quick_setup_main_single_at_8)

#####main#####

untouched_main_reps_per_set = setup_main_reps_per_set
untouched_main_last_set_RIR_target = setup_main_last_set_RIR
untouched_main_set_goal = setup_main_sets
untouched_main_sets_completed = ""
untouched_main_RIR_on_last_set = ""
def untouched_main_weight(w):
  return (x_round(((untouched_mainTM_weight(w))*(quick_setup_main_intensity[w-1])),quick_setup_main_rounding))/100.0

############################______p_RIR______##############################

####mainTM####
p_RIR_mainTM_reps_per_set = ["single@8"]*21
p_RIR_mainTM_last_set_RIR_target = [""]*21
def p_RIR_mainTM_weight(w):
  if w == 1:
    if p_RIR_mainTM_last_set_RIR_target[w-1] == "":
      return quick_setup_main_max
    else:
      return (p_RIR_mainTM_last_set_RIR_target[w-1]) / quick_setup_RIR_main_single_at_8
  elif (w == 8) or (w == 15):
    if p_RIR_mainTM_last_set_RIR_target[w-1] == "":
      return p_RIR_mainTM_weight(w-1)
    else:
      return ((p_RIR_mainTM_last_set_RIR_target[w-1])/(quick_setup_main_single_at_8))
  elif w >= 2 and w <= 21:
    if p_RIR_mainTM_last_set_RIR_target[w-1] == "":
      if p_RIR_main_sets_completed[w-2] == "":
        return p_RIR_mainTM_weight(w-1)
      elif ((p_RIR_main_sets_completed[w-2]) - (p_RIR_main_set_goal[w-2])) < -1.9:
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[0]))
      elif ((p_RIR_main_sets_completed[w-2]) - (p_RIR_main_set_goal[w-2])) == -1:
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[1]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) < (p_RIR_mainTM_last_set_RIR_target[w-2])) :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[1]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) == (p_RIR_mainTM_last_set_RIR_target[w-2])) :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[2]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 1 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[3]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 2 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[4]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 3 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[5]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 4 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[6]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) > 4.1 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_RIR_main_behavior_RIR_adjust[7]))
      else:
        p_RIR_mainTM_weight(w-1)
  else:
    p_RIR_mainTM_last_set_RIR_target[w-1]

####main####

def p_RIR_main_weight(w):
  return (x_round(((p_RIR_mainTM_weight(w)) * (setup_main_intensity[w-1])), quick_setup_main_rounding))/100.0
  
p_RIR_main_reps_per_set = setup_main_reps_per_set
def p_RIR_main_last_set_RIR_target(w):
  return setup_main_last_set_RIR(w)
def p_RIR_main_set_goal(w):
  return setup_main_sets[w-1]
p_RIR_main_sets_completed = [""]*21
p_RIR_main_RIR_on_last_set = [""]*21

###########################_______Table______####################################################
def table_main(w): 
  return ("Week:"+str(w)+"  |  weight:"+str((p_RIR_main_weight(w))) + "  |  reps per set:"+str((p_RIR_main_reps_per_set(w)))+"  |  Last Set RIR Target:"+str(p_RIR_main_last_set_RIR_target(w))+"  |  Set Goal:"+str(p_RIR_main_set_goal(w)))
#####################################################################################################################
def table_main_all(w):
  for n in range(1,22):
    print (table_main(n))
print(table_main_all(0))
