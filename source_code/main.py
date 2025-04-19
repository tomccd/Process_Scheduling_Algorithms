import matplotlib.pyplot as plt

# Thông tin tiến trình
processes = ['P1', 'P2', 'P3']
arrival_times = [2, 4, 3]
burst_times = [4, 2, 3]

# Tính toán thời gian bắt đầu và kết thúc cho mỗi tiến trình
start_times = []
end_times = []
current_time = 0

for i in range(len(processes)):
    # Nếu tiến trình đến sau thời gian hiện tại, CPU phải đợi
    if arrival_times[i] > current_time:
        current_time = arrival_times[i]
    start_times.append(current_time)
    end_time = current_time + burst_times[i]
    end_times.append(end_time)
    current_time = end_time

# Vẽ biểu đồ Gantt
fig, gnt = plt.subplots()
gnt.set_title("Biểu đồ FCFS")
gnt.set_xlabel("Thời gian")
gnt.set_ylabel("Tiến trình")

# Set trục y
gnt.set_yticks([10, 20, 30])
gnt.set_yticklabels(processes)
gnt.set_ylim(0, 40)
gnt.set_xlim(0, max(end_times) + 1)

# Vẽ các thanh tiến trình
for i in range(len(processes)):
    gnt.broken_barh([(start_times[i], burst_times[i])], (10 * (i + 1), 5), facecolors='tab:blue')
    gnt.text(start_times[i] + burst_times[i] / 2, 10 * (i + 1) + 2, processes[i],
             ha='center', va='center', color='white')

plt.show()
