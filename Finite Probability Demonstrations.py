"""
Probability concepts visualization using sets

Example:
- Universe S = students numbered 1 to 9
- Group A = students 1–5
- Group B = students 6–9 (disjoint from A)
- Art club = some students from both groups

Shows: marginal probs, joint, conditional, union, complement, total prob, Bayes
"""



import matplotlib.pyplot as plt

def intersection_size(A,B):
    return len(set(A) & set(B))

# probability of any event is p(E) = |E|/|S| , here E is event and S is a sample , each and not be negative
def probability(sample , Event ):
    formula = Event/sample
    return formula

def Complement(sample , A):
    formula = 1 - probability(sample,len(A))
    return formula

def joint_probability(sample,A , B):
    intersection = intersection_size(A,B)
    formula  = intersection/sample
    return formula  

#the condotion probability P(A|B) = p(A intersection B)/p(B)
def conditional_probability(sample_L ,A , B ):
    pro_intersection = joint_probability(sample_L , A , B )
    pro_occured = probability(sample_L , len(B) )
    conditional_probability = pro_intersection / pro_occured
    return conditional_probability

def union_probability(S,A ,B):
    A_pro = probability(S,len(A))
    B_pro = probability(S,len(B))
    formula =  A_pro + B_pro  -  joint_probability(S , A , B)
    return formula

def law_of_total_probability(sample , A , B , Art):
    P_A = probability(sample , len(A))
    P_B = probability(sample , len(B))

    P_Art_given_A = conditional_probability(sample , Art , A)
    P_Art_given_B = conditional_probability(sample , Art , B)

    formula = P_Art_given_A * P_A + P_Art_given_B * P_B
    return formula    

def bayes_theorem( sample , A , B):
    P_A = probability(sample , len(A))
    P_B = probability(sample , len(B))
    P_B_given_A = conditional_probability(sample , B , A)
    formula = (P_B_given_A * P_A) / P_B
    return formula , P_B_given_A 

def start(full_sp,A,B,art_club):
    sample_L = len(full_sp)
    A_L = len(A)
    B_L = len(B)
    art_club_L = len(art_club)
    fig, axes = plt.subplots(1,7 , figsize=(18,5))

    # probability 
    pro_A = probability(sample_L , A_L)
    pro_B = probability(sample_L , B_L)
    pro_Art = probability(sample_L , art_club_L)
    axes[0].bar(["A", "B", "Art"],[pro_A , pro_B ,pro_Art])
    axes[0].set_ylim(0,1)
    axes[0].set_title("probability")

    #relation probability
    pro_A_Art = joint_probability(sample_L , A , art_club)
    pro_B_Art = joint_probability(sample_L , B , art_club)
    axes[1].bar(["pro_A_Art", "pro_B_Art"],[ pro_A_Art , pro_B_Art])
    axes[1].set_ylim(0,1)
    axes[1].set_title("relation probability")

    #condition probability
    pro_A_art = conditional_probability(sample_L ,A , art_club)
    pro_B_art = conditional_probability(sample_L ,B , art_club)
    axes[2].bar(["pro_A_art", "pro_B_art"] , [pro_A_art , pro_B_art])
    axes[2].set_ylim(0,1)
    axes[2].set_title("condition probability")
    
    #Union probability
    uni_A_Art =  union_probability(sample_L,A,art_club)
    uni_B_Art =  union_probability(sample_L,B,art_club)
    axes[3].bar(["uni_A_Art", "uni_B_Art"] , [uni_A_Art , uni_B_Art])
    axes[3].set_ylim(0,1)
    axes[3].set_title("Union probability")

    #Complement (not of a event like , A will not occur )
    not_A = Complement(sample_L , A)
    not_B = Complement(sample_L , B)
    axes[4].bar(["not_A","not_B"], [not_A, not_B])
    axes[4].set_ylim(0,1)
    axes[4].set_title("Complement")


    #Total Probability , here A and B are Partition of S and they are Disjoint and Art will be new event intersecting A and B
    total_Art = law_of_total_probability(sample_L , A, B, art_club)
    axes[5].bar(["Total of Art"], [total_Art])
    axes[5].set_ylim(0,1)
    axes[5].set_title("Total of Art")


    #bayes_theorem
    baye_A_art , given_event = bayes_theorem(sample_L , A , art_club )
    axes[6].bar(["P(A | Art)", "P(Art | A)"],
    [baye_A_art, given_event],
    color=['#1f77b4', '#ff7f0e']
    )
    axes[6].set_ylim(0,1)
    axes[6].set_title("Bayes Theorem\nP(A | Art) and P(Art | A)")
    axes[6].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()
    return



full_sp = [1,2,3,4,5,6,7,8,9]
A = [1,2,3,4,5]
B = [6,7,8,9]
art_club = [4,5,6,8,9]
start(full_sp,A,B,art_club)
