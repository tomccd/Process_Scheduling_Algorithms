import matplotlib.pyplot as plt
ready_list = {
    "P1" : {
        "entry_time_rl" : 2,
        "cpu_burst" : 6,
        "remain_time" : 6,
    },
    "P2" : {
        "entry_time_rl": 5,
        "cpu_burst" : 2,
        "remain_time" : 2,
    },
    "P3" : {
        "entry_time_rl": 1,
        "cpu_burst" : 8,
        "remain_time" : 8,
    },
    "P4" : {
        "entry_time_rl": 0,
        "cpu_burst" : 3,
        "remain_time" : 3,
    },
    "P5" : {
        "entry_time_rl": 4,
        "cpu_burst" : 4,
        "remain_time" : 4,
    },
}

start_time = {}
end_time = {}
queue_process = []
delay_time = {}
quantum_time = 4
current_time = 0
#Sorting entry_time_rl
sorted_ready_list =  dict(sorted(ready_list.items(),key=lambda x:x[1]["entry_time_rl"]))

#Initialize start_time, end_time and queue_process
for process in sorted_ready_list.keys():
    start_time[process] = []
    end_time[process] = []
    delay_time[process] = None
    queue_process.append(process)

#Calculate start_time and end_time of each process and process the queue_process
while len(queue_process)>0:
    if current_time < ready_list[queue_process[0]]['entry_time_rl']:
        current_time = ready_list[queue_process[0]]['entry_time_rl']
    #Update start time
    start_time[queue_process[0]].append(current_time)
    #Based on remain_time -> calculate end_time, current_time and process the queue
    previous_remain_time = ready_list[queue_process[0]]['remain_time']
    ready_list[queue_process[0]]['remain_time'] -= quantum_time
    if ready_list[queue_process[0]]['remain_time'] <= 0:
        end_time[queue_process[0]].append(current_time+previous_remain_time)
        current_time += previous_remain_time
        ready_list[queue_process[0]]['remain_time'] = 0
        queue_process.pop(0)
    else:
        end_time[queue_process[0]].append(current_time+quantum_time)
        current_time += quantum_time
        queue_process.append(queue_process.pop(0))


# #Calculate waiting time
for process in ready_list.keys():
    total_delay = 0
    for x in range(len(start_time[process])):
        if x == 0:
            total_delay += (start_time[process][x]-ready_list[process]['entry_time_rl'])
        else:
            total_delay += (start_time[process][x]-end_time[process][x-1])
    delay_time[process] = total_delay

#Display
print(f"Quantum time: {quantum_time}\n")
for process in sorted_ready_list.keys():
    for x in range(len(start_time[process])):
        print(f"Process {process}: \n\t Start time ({x}): {start_time[process][x]} \t End time ({x}): {end_time[process][x]}\n")
    print(f"\n\t Total Delay time of Process {process}: {delay_time[process]}\n")

print(f"Average delay time: {sum(int (items[1]) for items in delay_time.items())/len(delay_time)}\n")

#Draw gantt graphic
fig, gnt = plt.subplots()
gnt.set_title("Biểu đồ Round Robin")
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