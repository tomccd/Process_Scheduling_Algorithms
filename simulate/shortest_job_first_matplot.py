import matplotlib.pyplot as plt
# ready_list = {
#     "P1" : {
#         "entry_time_rl" : 0,
#         "cpu_burst" : 8,
#         "remain_time" : 8,
#         "is_ready" : False
#     },
#     "P2" : {
#         "entry_time_rl": 1,
#         "cpu_burst" : 6,
#         "remain_time" : 6,
#         "is_ready" : False
#     },
#     "P3" : {
#         "entry_time_rl": 2,
#         "cpu_burst" : 4,
#         "remain_time" : 4,
#         "is_ready" : False
#     },
#     "P4" : {
#         "entry_time_rl": 3,
#         "cpu_burst" : 2,
#         "remain_time" : 2,
#         "is_ready" : False
#     },
# }
# ready_list = {
#     "P1" : {
#         "entry_time_rl" : 2,
#         "cpu_burst" : 5,
#         "remain_time" : 5,
#         "is_ready" : False
#     },
#     "P2" : {
#         "entry_time_rl": 0,
#         "cpu_burst" : 3,
#         "remain_time" : 3,
#     },
#     "P3" : {
#         "entry_time_rl": 1,
#         "cpu_burst" : 7,
#         "remain_time" : 7,
#     },
#     "P4" : {
#         "entry_time_rl": 4,
#         "cpu_burst" : 6,
#         "remain_time" : 6,
#     },
#     "P5" : {
#         "entry_time_rl": 4,
#         "cpu_burst" : 8,
#         "remain_time" : 8,
#     },
# }

ready_list = {
    "P1" : {
        "entry_time_rl" : 2,
        "cpu_burst" : 6,
        "remain_time" : 6,
        "is_ready" : False
    },
    "P2" : {
        "entry_time_rl": 5,
        "cpu_burst" : 2,
        "remain_time" : 2,
        "is_ready" : False
    },
    "P3" : {
        "entry_time_rl": 1,
        "cpu_burst" : 8,
        "remain_time" : 8,
        "is_ready" : False
    },
    "P4" : {
        "entry_time_rl": 0,
        "cpu_burst" : 3,
        "remain_time" : 3,
        "is_ready" : False
        
    },
    "P5" : {
        "entry_time_rl": 4,
        "cpu_burst" : 4,
        "remain_time" : 4,
        "is_ready" : False
    },
}

start_time = {}
end_time = {}
delay_time = {}
current_time = 0
current_process = None
process_queue = []
running_time = 0

#Sorting entry_time_rl
sorted_ready_list =  dict(sorted(ready_list.items(),key=lambda x:x[1]["entry_time_rl"]))

#Initialize start_time and end_time
for key in sorted_ready_list.keys():
    start_time[key] = []
    end_time[key] = []
    delay_time[key] = None
    process_queue.append(key)

while(len(process_queue)):
    #filt process
    filter_list = list(filter(lambda x:ready_list[x]["remain_time"] > 0 and ready_list[x]["entry_time_rl"]<=current_time,process_queue))
    if len(filter_list) > 0:
        #find the process whose remain_time is the smallest
        smallest_remain_time_process = min(filter_list,key=lambda x:ready_list[x]["remain_time"])
        if smallest_remain_time_process != current_process:
            if current_process is not None and ready_list[current_process]["is_ready"] == True:
                end_time[current_process].append(current_time)
                ready_list[current_process]["is_ready"] = False
            current_process = smallest_remain_time_process
            start_time[current_process].append(current_time)
            ready_list[current_process]["is_ready"] = True
        ready_list[current_process]["remain_time"]-=1
        if ready_list[current_process]["remain_time"] == 0:
            end_time[current_process].append(current_time)
            ready_list[current_process]["is_ready"] = False
            process_queue.remove(current_process)
            current_process = None
    current_time+=1

#Calculate waiting time
for process in ready_list.keys():
    total_delay = 0
    for x in range(len(start_time[process])):
        if x == 0:
            total_delay += (start_time[process][x]-ready_list[process]['entry_time_rl'])
        else:
            total_delay += (start_time[process][x]-end_time[process][x-1])
    delay_time[process] = total_delay

#Display
for process in ready_list.keys():
    for x in range(len(start_time[process])):
        print(f"Process {process}: \n\t Start time ({x}): {start_time[process][x]} \t End time ({x}): {end_time[process][x]}\n")
    print(f"\n\t Total Delay time of Process {process}: {delay_time[process]}\n")

print(f"Average delay time: {sum(int (items[1]) for items in delay_time.items())/len(delay_time)}\n")

#Draw gantt graphic
fig, gnt = plt.subplots()
gnt.set_title("Biểu đồ Shortest Job First")
gnt.set_xlabel("Thời gian")
gnt.set_ylabel("Tiến trình")

y_ticks = []
value = 10
for process in ready_list.keys():
    y_ticks.append(value)
    value+=10

gnt.set_yticks(y_ticks)
gnt.set_yticklabels(ready_list.keys())
gnt.set_ylim(0,max(y_ticks)+10)

max_endtime_element = list(max(end_time.items(),key=lambda x:max(x[1])))
max_xvalue = max(max_endtime_element[1])
gnt.set_xlim(0,max_xvalue+1)

#Dwaw graphic
for process in ready_list.keys():
    index = list(ready_list.keys()).index(process)
    for x in range(len(start_time[process])):
        duration = end_time[process][x] - start_time[process][x]
        gnt.broken_barh([(start_time[process][x],duration)],(10 * (index+1),5),facecolors='tab:blue')
        gnt.text(start_time[process][x] + duration/2,10* (index+1)+2,process,ha='center',va='center',color='white')

plt.show()