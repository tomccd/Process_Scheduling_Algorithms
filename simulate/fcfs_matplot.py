import matplotlib.pyplot as plt

ready_list = {
    "P1" : {
        "entry_time_rl" : 2,
        "cpu_burst" : 6,
    },
    "P2" : {
        "entry_time_rl": 5,
        "cpu_burst" : 2,
    },
    "P3" : {
        "entry_time_rl": 1,
        "cpu_burst" : 8,
    },
    "P4" : {
        "entry_time_rl": 0,
        "cpu_burst" : 3,
    },
    "P5" : {
        "entry_time_rl": 4,
        "cpu_burst" : 4,
    },
}

start_time = {}
end_time = {}
delay_time = {}
current_time = 0
#Sorting entry_time_rl
sorted_ready_list =  dict(sorted(ready_list.items(),key=lambda x:x[1]["entry_time_rl"]))

#Initialize start_time and end_time
for key in sorted_ready_list.keys():
    start_time[key] = None
    end_time[key] = None
    delay_time[key] = None

#Calculate the start time, end time and delay time of each process
for process in sorted_ready_list.keys():
    if current_time<sorted_ready_list[process]["entry_time_rl"]:
        current_time = sorted_ready_list[process]["entry_time_rl"]
    #Update start time
    start_time[process] = current_time
    #Update end time
    end_time[process] = start_time[process]+sorted_ready_list[process]["cpu_burst"]
    #Update delay time
    delay_time[process] = start_time[process]-sorted_ready_list[process]["entry_time_rl"]
    #Update current time
    current_time = end_time[process]
    

for process in sorted_ready_list.keys():
    print(f"Process {process}:\n\t Entry time: {sorted_ready_list[process]['entry_time_rl']} \n\t Start time: {start_time[process]}\n\t End time: {end_time[process]} \n\t Delay time: {delay_time[process]}\n")

print(f"Average delay time: {sum(int (items[1]) for items in delay_time.items())/len(delay_time)}\n")
#Draw gantt graphic
fig, gnt = plt.subplots()
gnt.set_title("Biểu đồ FCFS")
gnt.set_xlabel("Thời gian")
gnt.set_ylabel("Tiến trình")

y_ticks = []
value = 10
for process in ready_list.keys():
    y_ticks.append(value)
    value+=10

#Set trục y
gnt.set_yticks(y_ticks)
gnt.set_yticklabels(ready_list.keys())
gnt.set_ylim(0,max(y_ticks)+10)
gnt.set_xlim(0,list(max(end_time.items(),key=lambda x:x[1]))[1]+1)


#Vẽ thanh tiến trình
for process in ready_list.keys():
    index = list(ready_list.keys()).index(process)
    gnt.broken_barh([(start_time[process],ready_list[process]['cpu_burst'])],(10 * (index+1),5),facecolors='tab:red')
    gnt.text(start_time[process] + ready_list[process]['cpu_burst']/2,10 * (index+1) +2,process,ha='center',va='center',color='white')

plt.show()
