Task Setting
● You can hire some bandwidth
○ 1 bandwidth costs 60 money units
● You can resell bandwidth for different kind of subscribers (claims): bronze, silver, gold
● Each kind of claim has the following parameters:
○ bw: bandwidth needed to host the claim
○ duration: time units a claim spends in the system until it is served
○ value: money units earned by hosting the claim
○ damage: money units lost if kicking out the claim before it ends
○ pr: probability that in the next time unit this kind of claim will arrive
● claim_types=
○ {'bronze':{'bw': 1, 'value': 2, 'damage':4, 'duration': 100, 'pr': 0.4}, 
○ 'silver': {'bw': 3, 'value': 5, 'damage':6, 'duration': 50, 'pr': 0.3}, 
○ 'gold':{'bw': 10, 'value': 30, 'damage':80, 'duration': 70, 'pr': 0.1}}
● One simulation lasts 2000 time units 
● Your score will be your average profit of 100 simulations
● The team with maximal score will be the winner
Additional info
● Some additional info:
○ You get the value if it is fully served
○ You get the damage if you kick it out before it is fully served