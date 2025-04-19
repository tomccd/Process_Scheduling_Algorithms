
ready_list = {
    "P1" : {
        "entry_time_rl" : 2,
        "cpu_burst" : 4
    },
    "P2" : {
        "entry_time_rl": 4,
        "cpu_burst" : 2
    },
    "P3" : {
        "entry_time_rl": 3,
        "cpu_burst" : 3
    }
}

start_time = {}
end_time = {}
delay_time = {}
current_time = 0
#Sorting entry_time_rl
ready_list =  dict(sorted(ready_list.items(),key=lambda x:x[1]["entry_time_rl"]))

#Initialize start_time and end_time
for key in ready_list.keys():
    start_time[key] = None
    end_time[key] = None
    delay_time[key] = None

#Calculate the start time, end time and delay time of each process
for process in ready_list.keys():
    if current_time<ready_list[process]["entry_time_rl"]:
        current_time = ready_list[process]["entry_time_rl"]
    #Update start time
    start_time[process] = current_time
    #Update end time
    end_time[process] = start_time[process]+ready_list[process]["cpu_burst"]
    #Update delay time
    delay_time[process] = start_time[process]-ready_list[process]["entry_time_rl"]
    #Update current time
    current_time = end_time[process]
    

for process in ready_list.keys():
    print(f"Process {process}:\n\t Start time: {start_time[process]}\n\t End time: {end_time[process]} \n\t Delay time: {delay_time[process]}\n")


