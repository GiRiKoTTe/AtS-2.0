##############################_______Math_Def________################################
a=int()
def x_round(number):
      return round(number * (1/quick_setup_main_rounding)) / (1/quick_setup_main_rounding)
##############################_______Quick Setup_______##############################
quick_setup_main_rounding = .25
quick_setup_main_target_percent = [0.500,0.525,0.550,0.575,0.600,0.625,0.650,0.675,0.700,0.725,0.750,0.775,0.800,0.825,0.850,0.875,0.900,0.925,0.950,0.975,1.000]
#main
quick_setup_main = "main"
quick_setup_main_max = 100
quick_setup_main_single_at_8 = .9
quick_setup_main_behavior_RIR_sets = [5]*21
quick_setup_main_behavior_RIR_adjust =  [-0.05000,-0.02000,0.00000,0.00500,0.01000,0.01500,0.02000,0.03000]
quick_setup_main_rep_target =   [8,8,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,1,1,1]
quick_setup_main_last_set_RIR_target =  [3,3,3,3,3,3,3,3,3,3,2,2,2,2,1,1,1,1,1,0,0]
quick_setup_main_intensity =    [0.700,0.750,0.800,0.725,0.775,0.825,0.600,0.750,0.800,0.850,0.775,0.825,0.875,0.600,0.800,0.850,0.900,0.850,0.900,0.950,0.600]
##############################______Setup______##############################
#main
setup_main_intensity = quick_setup_main_intensity
setup_main_sets = quick_setup_main_behavior_RIR_sets
setup_main_behavior_RIR_adjust = quick_setup_main_behavior_RIR_adjust
def setup_main_reps_per_set (w):
  if w == 7 or w == 14 or w == 21:
    return 5
  else:
    for n in range (0,22):
      if quick_setup_main_intensity[w-1] == quick_setup_main_target_percent[n]:
        return quick_setup_main_rep_target[n]
        break
      else:
       n=+1
def setup_main_last_set_RIR (w):
  if w == 7 or w == 14 or w == 21:
    return a
  else:
    for n in range (0,22):
        if setup_main_intensity[w-1] == quick_setup_main_target_percent[n]:
            return quick_setup_main_last_set_RIR_target[n]
            break 
        else:
            n=+1
##############################______Untouched______##############################
####mainTM####
untouched_mainTM_last_set_RIR_target = [a]*21
untouched_mainTM_sets_completed = [a]*21
untouched_mainTM_reps_per_set = ["single@8"]*21
untouched_mainTM_set_goal = [a]*21
untouched_mainTM_RIR_on_last_set = [a]
def untouched_mainTM_weight(w):
  if w==1:
    if untouched_mainTM_last_set_RIR_target[w-1] == a:
      return x_round(quick_setup_main_max)
    else:
      return x_round((untouched_mainTM_last_set_RIR_target[w-1])/(quick_setup_main_single_at_8))
  elif w >= 2 and w <= 21:
    if untouched_mainTM_last_set_RIR_target[w-1] == a:#L3
      if untouched_main_sets_completed[w-2] == a:#F4
        return x_round(untouched_mainTM_weight(w-1))
      elif (untouched_main_sets_completed[w-2] - untouched_main_set_goal[w-2]) < (-1.9):#1.9
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[0]/1)))
      elif (untouched_main_sets_completed[w-2] - untouched_main_set_goal[w-2]) == (-1): #-1
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[1]/1)))
      elif (untouched_main_RIR_on_last_set[w-2]) < (untouched_main_last_set_RIR_target(w-1)):#g4<
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[1]/1)))
      elif (untouched_main_RIR_on_last_set[w-2]) == (untouched_main_last_set_RIR_target(w-1)):#g4=
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[2]/1)))
      elif ((untouched_main_RIR_on_last_set[2]) - (untouched_main_last_set_RIR_target(w-1))) == 1:#=1
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[3]/1)))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (untouched_main_last_set_RIR_target(w-1))) == 2:#=2
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[4]/1)))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (untouched_main_last_set_RIR_target(w-1))) == 3:#=3
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[5]/1)))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (untouched_main_last_set_RIR_target(w-1))) == 4:#=4
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[6]/1)))
      elif ((untouched_main_RIR_on_last_set[w-2]) - (untouched_main_last_set_RIR_target(w-1))) > 4.1:#>4
        return x_round((untouched_mainTM_weight(w-1))*(1+ (setup_main_behavior_RIR_adjust[7]/1)))
      else:
        return x_round(untouched_mainTM_weight(w-1))
    else:
      return x_round((untouched_mainTM_last_set_RIR_target[w-1])/(quick_setup_main_single_at_8))
####main####
def untouched_main_reps_per_set(w):
    return setup_main_reps_per_set(w)
def untouched_main_last_set_RIR_target(w) :
    return setup_main_last_set_RIR(w)
untouched_main_set_goal = setup_main_sets
untouched_main_sets_completed = a
untouched_main_RIR_on_last_set = a
def untouched_main_weight(w):
  return (x_round(((untouched_mainTM_weight(w))*(quick_setup_main_intensity[w-1]))))/1
############################______p_RIR______##############################
####mainTM####
p_RIR_mainTM_reps_per_set = ["single@8"]*21
p_RIR_mainTM_last_set_RIR_target = [a]*21
def p_RIR_mainTM_weight(w):
  if w == 1:
    if p_RIR_mainTM_last_set_RIR_target[w-1] == a:
      return (quick_setup_main_max)
    else:
      return ((p_RIR_mainTM_last_set_RIR_target[w-1]) / (quick_setup_main_single_at_8))
  elif (w == 8) or (w == 15):
    if p_RIR_mainTM_last_set_RIR_target[w-1] == a:
      return (p_RIR_mainTM_weight(w-1))
    else:
      return ((p_RIR_mainTM_last_set_RIR_target[w-1])/(quick_setup_main_single_at_8))
  elif w >= 2 and w <= 21:
    if p_RIR_mainTM_last_set_RIR_target[w-1] == a:
      if p_RIR_main_sets_completed[w-2] == a:
        return (p_RIR_mainTM_weight(w-1))
      elif ((p_RIR_main_sets_completed[w-2]) - (p_RIR_main_set_goal(w-1))) < -1.9:
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[0]))
      elif ((p_RIR_main_sets_completed[w-2]) - (p_RIR_main_set_goal(w-1))) == -1:
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[1]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) < (p_RIR_mainTM_last_set_RIR_target[w-2])) :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[1]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) == (p_RIR_mainTM_last_set_RIR_target[w-2])) :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[2]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 1 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[3]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 2 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[4]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 3 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[5]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) == 4 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[6]))
      elif ((p_RIR_main_RIR_on_last_set[w-2]) - (p_RIR_mainTM_last_set_RIR_target[w-2])) > 4.1 :
        return ((p_RIR_mainTM_weight(w-1)) * (1 + setup_main_behavior_RIR_adjust[7]))
      else:
        return ((p_RIR_mainTM_weight(w-1)/(quick_setup_main_single_at_8)))
  else:
    return (p_RIR_mainTM_last_set_RIR_target[w-1])
####main####
def p_RIR_main_weight(w):
  return (x_round(((p_RIR_mainTM_weight(w)) * (setup_main_intensity[w-1]))))
def p_RIR_main_reps_per_set(w):
    return setup_main_reps_per_set(w)
def p_RIR_main_last_set_RIR_target(w):
  return setup_main_last_set_RIR(w)
def p_RIR_main_set_goal(w):
  return setup_main_sets[w-1]
p_RIR_main_sets_completed = [a]*21
p_RIR_main_RIR_on_last_set = [a]*21
###########################_______Table______####################################################
def table_main(w): 
  return ("Week:"+str(w)+"  |  weight:"+str((p_RIR_main_weight(w))) + "  |  reps per set:"+str((p_RIR_main_reps_per_set(w)))+"  |  Last Set RIR Target:"+str(p_RIR_main_last_set_RIR_target(w))+"  |  Set Goal:"+str(p_RIR_main_set_goal(w))+"  |  Sets completed:"+str(p_RIR_main_sets_completed[w-1])+"  |  RIR on last set:"+str(p_RIR_main_RIR_on_last_set[w-1]))
def table_main_all(w):
  for n in range(1,22):
    print (table_main(n))
table_main_all(0)
#####################################################################################################################
