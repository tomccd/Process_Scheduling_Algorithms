ready_list = {
    "P1" : {
        "entry_time_rl" : 2,
        "cpu_burst" : 6,
        "remain_time" : 6,
        "is_ready" : False,
        "priority" : 3
    },
    "P2" : {
        "entry_time_rl": 5,
        "cpu_burst" : 2,
        "remain_time" : 2,
        "is_ready" : False,
        "priority" : 1
    },
    "P3" : {
        "entry_time_rl": 1,
        "cpu_burst" : 8,
        "remain_time" : 8,
        "is_ready" : False,
        "priority" : 4
    },
    "P4" : {
        "entry_time_rl": 0,
        "cpu_burst" : 3,
        "remain_time" : 3,
        "is_ready" : False,
        "priority" : 5
    },
    "P5" : {
        "entry_time_rl": 4,
        "cpu_burst" : 4,
        "remain_time" : 4,
        "is_ready" : False,
        "priority" : 2
    },
}

start_time = {}
end_time = {}
delay_time = {}
current_time = 0
process_queue = []
current_time = 0
#Sorting entry_time_rl
sorted_ready_list =  dict(sorted(ready_list.items(),key=lambda x:x[1]["entry_time_rl"]))

#Initialize start_time and end_time
for key in sorted_ready_list.keys():
    start_time[key] = []
    end_time[key] = []
    delay_time[key] = None
    process_queue.append(key)

#Calculate start_time and end_time
current_index = 0
previous_process = None
running_time = None

while len(process_queue) > 0:
    #Reset current_index
    if current_index >= len(process_queue):
        current_index = 0
    if current_time < ready_list[process_queue[current_index]]['entry_time_rl']:
        current_time = ready_list[process_queue[current_index]]['entry_time_rl']
        #Initialize running status of current process
        ready_list[process_queue[current_index]]['is_ready'] = True
    
    for process in process_queue:
        if process != process_queue[current_index]:
            #Check the priority of the next process
            if ready_list[process]['priority'] < ready_list[process_queue[current_index]]['priority']:
                #Check if next process is ready ?
                if ready_list[process]['is_ready'] is False:
                    #Update start time
                    start_time[process_queue[current_index]].append(current_time)
                    #Update running time
                    running_time = ready_list[process]['entry_time_rl'] - current_time
                    #Update end_time of this process in this phase
                    end_time[process_queue[current_index]].append(start_time[process_queue[current_index]][len(start_time[process_queue[current_index]])-1] + running_time)
                    #Update the current_time
                    current_time = end_time[process_queue[current_index]][len(end_time[process_queue[current_index]])-1]
                    #Update remain time of this process
                    ready_list[process_queue[current_index]]['remain_time'] -= running_time
                    #Change the current_index
                    current_index = process_queue.index(process)
                    #Change the status
                    ready_list[process_queue[current_index]]['is_ready'] = True
                    break
                else:
                    #Update the higher index
                    current_index = process_queue.index(process)
                    break
            else:
                #Check if current process has the highest priority --> then put the effort of running this process
                if sorted_ready_list[process_queue[current_index]]['priority'] == min(sorted_ready_list.items(),key=lambda x: x[1]['priority'])[1]['priority']:
                    #Update start time
                    start_time[process_queue[current_index]].append(current_time)
                    #Update running time
                    running_time = sorted_ready_list[process_queue[current_index]]['remain_time']
                    ready_list[process_queue[current_index]]['remain_time'] = 0
                    #Update the end time of this process
                    end_time[process_queue[current_index]].append(current_time+running_time)
                    #Update the status of this process
                    ready_list[process_queue[current_index]]['is_ready'] = False
                    #Update the current time
                    current_time = end_time[process_queue[current_index]][len(end_time[process_queue[current_index]])-1]
                    #Remove this process out of process queue and sorted_ready_list
                    del sorted_ready_list[process_queue[current_index]]
                    process_queue.pop(current_index)
                    current_index +=1
                    break
                else:
                    continue
        else:
            #If process queue has only 1 process
            if len(process_queue) == 1:
                #Update start time
                start_time[process_queue[current_index]].append(current_time)
                #Update running time
                running_time = ready_list[process_queue[current_index]]['remain_time']
                ready_list[process_queue[current_index]]['remain_time'] = 0
                #Update the end time of this process
                end_time[process_queue[current_index]].append(current_time+running_time)
                #Update the status of this process
                ready_list[process_queue[current_index]]['is_ready'] = False
                #Update the current time
                current_time = end_time[process_queue[current_index]][len(end_time[process_queue[current_index]])-1]
                #Remove this process out of process queue and sorted_ready_list
                del sorted_ready_list[process_queue[current_index]]
                process_queue.pop(current_index)
                current_index +=1
                break

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
                    
            


