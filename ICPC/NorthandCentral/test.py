from tqdm import tqdm 
import time 
  
n = int(input())

for i in tqdm (range (n),  desc="Loading…",  ascii=False, ncols=75): 
    a = i+i
    time.sleep(0.01) 
      
print("Complete.") 

# import time 
# import progressbar 
  
# widgets = [' [', 
#          progressbar.Timer(format= 'elapsed time: %(elapsed)s'), 
#          '] ', 
#            progressbar.Bar('*'),' (', 
#            progressbar.ETA(), ') ', 
#           ] 
  
# bar = progressbar.ProgressBar(max_value=200,  
#                               widgets=widgets).start() 
  
# for i in range(200): 
#     time.sleep(0.1) 
#     bar.update(i)