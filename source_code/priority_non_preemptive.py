ready_list = {
    "P1" : {
        "entry_time_rl" : 2,
        "cpu_burst" : 5,
        "priority" : 2
    },
    "P2" : {
        "entry_time_rl": 0,
        "cpu_burst" : 3,
        "priority" : 4
    },
    "P3" : {
        "entry_time_rl": 1,
        "cpu_burst" : 7,
        "priority" : 2
    },
    "P4" : {
        "entry_time_rl": 4,
        "cpu_burst" : 6,
        "priority" : 3
    },
    "P5" : {
        "entry_time_rl": 4,
        "cpu_burst" : 8,
        "priority" : 1
    },
}

start_time = {}
end_time = {}
delay_time = {}
current_time = 0
process_queue = []
#Sorting entry_time_rl
sorted_ready_list =  dict(sorted(ready_list.items(),key=lambda x:x[1]["entry_time_rl"]))

#Initialize start_time and end_time
for key in sorted_ready_list.keys():
    start_time[key] = None
    end_time[key] = None
    delay_time[key] = None
    process_queue.append(key)

#Calculate the start time, end time of each process
while len(process_queue) > 0:
    if current_time < ready_list[process_queue[0]]['entry_time_rl']:
        current_time = ready_list[process_queue[0]]['entry_time_rl']
    #Filter the process list which compare entry_time_rl of each process with current_time 
    filter_list = filter(lambda x:ready_list[x]["entry_time_rl"]<=current_time,process_queue)
    #Find the highest priority level in this list
    max_priority_process = min(filter_list,key=lambda x:ready_list[x]['priority'])
    #Update start time, end time
    start_time[max_priority_process] = current_time
    end_time[max_priority_process] = current_time + ready_list[max_priority_process]["cpu_burst"]
    #Update current time
    current_time = end_time[max_priority_process]
    #Pop this process out of process_queue
    process_queue.pop(process_queue.index(max_priority_process))

#Calculate the delay time
for process in ready_list.keys():
    delay_time[process] = start_time[process] - ready_list[process]['entry_time_rl']
    
#Display
for process in sorted_ready_list.keys():
    print(f"Process {process}:\n\t Start time: {start_time[process]}\n\t End time: {end_time[process]} \n\t Delay time: {delay_time[process]}\n")
        