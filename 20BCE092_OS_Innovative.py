from tkinter import *

root = Tk()
root.title("Process Scheduling")
root.geometry("1920x800")
root.configure(bg='#adf0f7')

#---------------------------------------------------Button Functions-----------------------------------------------------------------


def first_come_first_serve():
    n_process = my_entry.get()
    my_entry.delete(0, 'end')

    root1 = Tk()
    root1.title("First Come First Serve")
    root1.geometry("1920x800")
    root1.configure(bg='#adf0f7')

    lbl = Label(root1, text='First Come First Serve(FCFS)', bd=6, relief=RAISED, width=50, height=5, font=15)
    lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    inp_frame = LabelFrame(root1, text='Input')
    inp_frame.grid(row=1, column=0, padx=20, pady=20)

    out_frame = LabelFrame(root1, text='Output')
    out_frame.grid(row=1, column=1, padx=20, pady=20)

    process_frame = Frame(out_frame)
    process_frame.grid(row=0, column=0, columnspan=4, pady=10)

    label_process = Label(inp_frame, text='Process Name', bd=5)
    label_process.grid(row=2, column=0, padx=10)
    label_arrival = Label(inp_frame, text='Arrival Time', bd=5)
    label_arrival.grid(row=2, column=1, padx=10)
    label_burst = Label(inp_frame, text='Burst Time', bd=5)
    label_burst.grid(row=2, column=2, padx=10)

    lst_entries = []
    for i in range(int(n_process)):
        lst_entries.append([Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5)])
        lst_entries[i][0].grid(row=3+i, column=0, padx=15)
        lst_entries[i][1].grid(row=3+i, column=1, padx=15)
        lst_entries[i][2].grid(row=3+i, column=2, padx=15)

    def evaluation():
        lst_value = []
        lst_original = []
        total_time = 0
        completion_time = {}

        for j in range(int(n_process)):
            lst_value.append([lst_entries[j][0].get(),
                              int(lst_entries[j][1].get()),
                              int(lst_entries[j][2].get())])
            lst_original.append([lst_entries[j][0].get(),
                                 int(lst_entries[j][1].get()),
                                 int(lst_entries[j][2].get())])

            #Label(out_frame, text=lst_value[j][0], bd=4, relief=RAISED).grid(row=j, column=0, padx=5, pady=5)
            #Label(out_frame, text=lst_value[j][1], bd=4, relief=RAISED).grid(row=j, column=1, padx=5, pady=5)
            #Label(out_frame, text=lst_value[j][2], bd=4, relief=RAISED).grid(row=j, column=2, padx=5, pady=5)

        for process1 in range(len(lst_value)):
            for process2 in range(len(lst_value)):
                if lst_value[process1][1] < lst_value[process2][1]:
                    lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]

        for process1 in range(len(lst_value)):
            if lst_value[process1][1] > 0:
                time = lst_value[process1][1]
                for x in range(time):
                    Label(process_frame, text='No Process', bd=4, relief=SUNKEN, width=8).grid(row=total_time//16, column=total_time % 16)
                    total_time += 1
                for y in range(len(lst_value)):
                    for z in range(time):
                        if lst_value[y][1] == 0:
                            break
                        else:
                            lst_value[y][1] -= 1
            if lst_value[process1][1] == 0:
                process_time = lst_value[process1][2]
                for j in range(process_time):
                    lst_value[process1][2] -= 1

                    for k in range(process1 + 1, len(lst_value)):
                        if lst_value[k][1] == 0:
                            continue
                        else:
                            lst_value[k][1] -= 1
                    Label(process_frame, text='Process ' + str(lst_value[process1][0]), bd=4, relief=SUNKEN, width=8).grid(row=total_time//16, column=total_time % 16)
                    total_time += 1
                    if lst_value[process1][2] == 0:
                        completion_time[lst_value[process1][0]] = total_time

        for process1 in lst_original:
            process1.append(completion_time[process1[0]])
            process1.append(process1[3]-process1[1])
            process1.append(process1[4]-process1[2])

        #Label(out_frame, text='Total Time=' + str(total_time), bd=4, relief=SUNKEN).grid(row=(total_time // 16) + 1, column=0, columnspan=3)
        #Label(out_frame, text=str(completion_time), bd=4, relief=SUNKEN).grid(row=(total_time // 16)+2, column=0, columnspan=3)
        #Label(out_frame, text=str(lst_original), bd=4, relief=SUNKEN).grid(row=(total_time // 16) + 3, column=0, columnspan=6)

        Label(out_frame, text='Process Name', bd=4, relief=RAISED).grid(row=1, column=0)
        Label(out_frame, text='Completion Time', bd=4, relief=RAISED).grid(row=1, column=1)
        Label(out_frame, text='Turn Around Time', bd=4, relief=RAISED).grid(row=1, column=2)
        Label(out_frame, text='Waiting Time', bd=4, relief=RAISED).grid(row=1, column=3)

        avg_waiting = 0
        avg_turnaround = 0

        for p in range(len(lst_original)):
            Label(out_frame, text=str(lst_original[p][0]), width=15).grid(row=2 + p, column=0)
            Label(out_frame, text=str(lst_original[p][3]), width=15).grid(row=2 + p, column=1)
            Label(out_frame, text=str(lst_original[p][4]), width=15).grid(row=2 + p, column=2)
            Label(out_frame, text=str(lst_original[p][5]), width=15).grid(row=2 + p, column=3)
            avg_waiting += lst_original[p][5]
            avg_turnaround += lst_original[p][4]

        Label(out_frame, text='Average Turn Around Time: '+str(avg_turnaround/int(n_process))).grid(row=3 + len(lst_original), column=0, columnspan=4)
        Label(out_frame, text='Average Waiting Time: '+str(avg_waiting/int(n_process))).grid(row=4 + len(lst_original), column=0, columnspan=4)

    evaluate = Button(inp_frame, text='Go', bd=5, command=evaluation)
    evaluate.grid(row=3+int(n_process), column=0, columnspan=3, pady=5)

    exit_button = Button(root1, anchor='center', text='Close', bd=4, activebackground='dark grey', command=root1.destroy)
    exit_button.grid(sticky=S)
    root1.mainloop()


def shortest_job_first():
    n_process = my_entry.get()
    my_entry.delete(0, 'end')

    root1 = Tk()
    root1.title("Shortest Job First")
    root1.geometry("1920x800")
    root1.configure(bg='#adf0f7')

    lbl = Label(root1, text='Shortest Job First(SJF)', bd=6, relief=RAISED, width=50, height=5, font=15)
    lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    inp_frame = LabelFrame(root1, text='Input')
    inp_frame.grid(row=1, column=0, padx=20, pady=20)

    out_frame = LabelFrame(root1, text='Output', padx=20, pady=20)
    out_frame.grid(row=1, column=1)

    process_frame = Frame(out_frame)
    process_frame.grid(row=0, column=0, columnspan=4, pady=10)

    label_process = Label(inp_frame, text='Process Name', bd=5)
    label_process.grid(row=2, column=0, padx=10)
    label_arrival = Label(inp_frame, text='Arrival Time', bd=5)
    label_arrival.grid(row=2, column=1, padx=10)
    label_burst = Label(inp_frame, text='Burst Time', bd=5)
    label_burst.grid(row=2, column=2, padx=10)

    lst_entries = []
    for i in range(int(n_process)):
        lst_entries.append([Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5)])
        lst_entries[i][0].grid(row=3 + i, column=0, padx=15)
        lst_entries[i][1].grid(row=3 + i, column=1, padx=15)
        lst_entries[i][2].grid(row=3 + i, column=2, padx=15)

    def evaluation():
        lst_value = []
        lst_original = []
        completed = []
        total_time = 0
        completion_time = {}

        for j in range(int(n_process)):
            lst_value.append([lst_entries[j][0].get(),
                              int(lst_entries[j][1].get()),
                              int(lst_entries[j][2].get())])
            lst_original.append([lst_entries[j][0].get(),
                                 int(lst_entries[j][1].get()),
                                 int(lst_entries[j][2].get())])

        while len(lst_value) != 0:
            for process1 in range(len(lst_value)):
                for process2 in range(len(lst_value)):
                    if lst_value[process1][1] < lst_value[process2][1]:
                        lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]
                    elif lst_value[process1][1] == lst_value[process2][1]:
                        if lst_value[process1][2] < lst_value[process2][2]:
                            lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]
                        elif lst_value[process1][2] == lst_value[process2][1]:
                            continue

            if lst_value[0][2] == 0:
                completion_time[lst_value[0][0]] = total_time
                completed.append(lst_value.pop(0))
                continue

            if lst_value[0][1] != 0:
                wait = lst_value[0][1]

                for x in range(wait):
                    Label(process_frame, text='No Process', bd=4, relief=SUNKEN, width=8).grid(row=total_time//16, column=total_time % 16)
                    total_time += 1
                for process1 in range(len(lst_value)):
                    if lst_value[process1][1] == 0:
                        continue
                    lst_value[process1][1] -= wait
            else:
                lst_value[0][2] -= 1
                Label(process_frame, text='Process '+str(lst_value[0][0]), bd=4, relief=SUNKEN, width=8).grid(row=total_time//16, column=total_time % 16)

                for process1 in range(1, len(lst_value)):
                    if lst_value[process1][1] == 0:
                        continue
                    else:
                        lst_value[process1][1] -= 1

                total_time += 1

        #Label(process_frame, text=str(total_time)).grid(row=total_time // 16, column=total_time % 16)

        for process1 in lst_original:
            process1.append(completion_time[process1[0]])
            process1.append(process1[3]-process1[1])
            process1.append(process1[4] - process1[2])

        #Label(out_frame, text=str(completed)).grid(row=1, column=0)
        #Label(out_frame, text=str(completion_time)).grid(row=2, column=0)
        #Label(out_frame, text=str(lst_original)).grid(row=3, column=0)

        Label(out_frame, text='Process Name', bd=4, relief=RAISED).grid(row=1, column=0)
        Label(out_frame, text='Completion Time', bd=4, relief=RAISED).grid(row=1, column=1)
        Label(out_frame, text='Turn Around Time', bd=4, relief=RAISED).grid(row=1, column=2)
        Label(out_frame, text='Waiting Time', bd=4, relief=RAISED).grid(row=1, column=3)

        avg_waiting = 0
        avg_turnaround = 0

        for p in range(len(lst_original)):
            Label(out_frame, text=str(lst_original[p][0]), width=15, bd=5).grid(row=2 + p, column=0)
            Label(out_frame, text=str(lst_original[p][3]), width=15, bd=5).grid(row=2 + p, column=1)
            Label(out_frame, text=str(lst_original[p][4]), width=15, bd=5).grid(row=2 + p, column=2)
            Label(out_frame, text=str(lst_original[p][5]), width=15, bd=5).grid(row=2 + p, column=3)
            avg_waiting += lst_original[p][5]
            avg_turnaround += lst_original[p][4]

        Label(out_frame, text='Average Turn Around Time: ' + str(avg_turnaround / int(n_process))).grid(row=3 + len(lst_original), column=0, columnspan=4)
        Label(out_frame, text='Average Waiting Time: ' + str(avg_waiting / int(n_process))).grid(row=4 + len(lst_original), column=0, columnspan=4)

    evaluate = Button(inp_frame, text='Go', bd=5, command=evaluation)
    evaluate.grid(row=3 + int(n_process), column=0, columnspan=3, pady=5)

    exit_button = Button(root1, anchor='center', text='Close', bd=4, activebackground='dark grey', command=root1.destroy)
    exit_button.grid(sticky=S)
    root1.mainloop()


def preemptive_priority():
    n_process = my_entry.get()
    my_entry.delete(0, 'end')

    root1 = Tk()
    root1.title("Preemptive Priority Scheduling")
    root1.geometry("1920x800")
    root1.configure(bg='#adf0f7')

    lbl = Label(root1, text='Preemptive Priority', bd=6, relief=RAISED, width=50, height=5, font=15)
    lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    inp_frame = LabelFrame(root1, text='Input')
    inp_frame.grid(row=1, column=0, padx=20, pady=20)

    out_frame = LabelFrame(root1, text='Output', padx=20, pady=20)
    out_frame.grid(row=1, column=1)

    process_frame = Frame(out_frame)
    process_frame.grid(row=0, column=0, columnspan=4, pady=10)

    label_process = Label(inp_frame, text='Process Name', bd=5)
    label_process.grid(row=2, column=0, padx=10)
    label_process = Label(inp_frame, text='Priority', bd=5)
    label_process.grid(row=2, column=1, padx=10)
    label_arrival = Label(inp_frame, text='Arrival Time', bd=5)
    label_arrival.grid(row=2, column=2, padx=10)
    label_burst = Label(inp_frame, text='Burst Time', bd=5)
    label_burst.grid(row=2, column=3, padx=10)

    lst_entries = []
    for i in range(int(n_process)):
        lst_entries.append([Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5)])
        lst_entries[i][0].grid(row=3 + i, column=0, padx=15)
        lst_entries[i][1].grid(row=3 + i, column=1, padx=15)
        lst_entries[i][2].grid(row=3 + i, column=2, padx=15)
        lst_entries[i][3].grid(row=3 + i, column=3, padx=15)

    def evaluation():
        lst_value = []
        lst_original = []
        completed = []
        total_time = 0
        completion_time = {}

        for j in range(int(n_process)):
            lst_value.append([lst_entries[j][0].get(),
                              int(lst_entries[j][1].get()),
                              int(lst_entries[j][2].get()),
                              int(lst_entries[j][3].get())])
            lst_original.append([lst_entries[j][0].get(),
                                 int(lst_entries[j][1].get()),
                                 int(lst_entries[j][2].get()),
                                 int(lst_entries[j][3].get())])

        while len(lst_value) != 0:
            for process1 in range(len(lst_value)):
                for process2 in range(len(lst_value)):
                    if lst_value[process1][2] < lst_value[process2][2]:
                        lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]
                    elif lst_value[process1][2] == lst_value[process2][2]:
                        if lst_value[process1][1] < lst_value[process2][1]:
                            lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]
                        elif lst_value[process1][1] == lst_value[process2][1]:
                            if lst_value[process1][3] < lst_value[process2][3]:
                                lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]
                            elif lst_value[process1][3] == lst_value[process2][3]:
                                continue

            if lst_value[0][3] == 0:
                completion_time[lst_value[0][0]] = total_time
                completed.append(lst_value.pop(0))
                continue

            if lst_value[0][2] != 0:
                wait = lst_value[0][2]

                for x in range(wait):
                    Label(process_frame, text='No Process', bd=4, relief=SUNKEN, width=8).grid(row=total_time // 16, column=total_time % 16)
                    total_time += 1
                for process1 in range(len(lst_value)):
                    if lst_value[process1][2] == 0:
                        continue
                    lst_value[process1][2] -= wait
            else:
                lst_value[0][3] -= 1
                Label(process_frame, text='Process ' + str(lst_value[0][0]), bd=4, relief=SUNKEN, width=8).grid(row=total_time // 16, column=total_time % 16)

                for process1 in range(1, len(lst_value)):
                    if lst_value[process1][2] == 0:
                        continue
                    else:
                        lst_value[process1][2] -= 1

                total_time += 1

        #Label(process_frame, text=str(total_time)).grid(row=total_time // 16, column=total_time % 16)

        for process1 in lst_original:
            process1.append(completion_time[process1[0]])
            process1.append(process1[4] - process1[2])
            process1.append(process1[5] - process1[3])

        #Label(out_frame, text=str(completed)).grid(row=1, column=0)
        #Label(out_frame, text=str(completion_time)).grid(row=2, column=0)
        #Label(out_frame, text=str(lst_original)).grid(row=3, column=0)

        Label(out_frame, text='Process Name', bd=4, relief=RAISED).grid(row=1, column=0)
        Label(out_frame, text='Completion Time', bd=4, relief=RAISED).grid(row=1, column=1)
        Label(out_frame, text='Turn Around Time', bd=4, relief=RAISED).grid(row=1, column=2)
        Label(out_frame, text='Waiting Time', bd=4, relief=RAISED).grid(row=1, column=3)

        avg_waiting = 0
        avg_turnaround = 0

        for p in range(len(lst_original)):
            Label(out_frame, text=str(lst_original[p][0]), width=15).grid(row=2 + p, column=0)
            Label(out_frame, text=str(lst_original[p][4]), width=15).grid(row=2 + p, column=1)
            Label(out_frame, text=str(lst_original[p][5]), width=15).grid(row=2 + p, column=2)
            Label(out_frame, text=str(lst_original[p][6]), width=15).grid(row=2 + p, column=3)
            avg_waiting += lst_original[p][6]
            avg_turnaround += lst_original[p][5]

        Label(out_frame, text='Average Turn Around Time: ' + str(avg_turnaround / int(n_process))).grid(row=3 + len(lst_original), column=0, columnspan=4)
        Label(out_frame, text='Average Waiting Time: ' + str(avg_waiting / int(n_process))).grid(row=4 + len(lst_original), column=0, columnspan=4)

    evaluate = Button(inp_frame, text='Go', bd=5, command=evaluation)
    evaluate.grid(row=3 + int(n_process), column=0, columnspan=4, pady=5)

    exit_button = Button(root1, anchor='center', text='Close', bd=4, activebackground='dark grey', command=root1.destroy)
    exit_button.grid(sticky=S)
    root1.mainloop()


def round_robin():
    n_process = my_entry.get()
    my_entry.delete(0, 'end')

    root1 = Tk()
    root1.title("Round Robin")
    root1.geometry("1920x800")
    root1.configure(bg='#adf0f7')

    lbl = Label(root1, text='Round Robin', bd=6, relief=RAISED, width=50, height=5, font=15)
    lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    inp_frame = LabelFrame(root1, text='Input')
    inp_frame.grid(row=1, column=0, padx=20, pady=20)

    out_frame = LabelFrame(root1, text='Output', padx=20, pady=20)
    out_frame.grid(row=1, column=1)

    process_frame = Frame(out_frame)
    process_frame.grid(row=0, column=0, columnspan=4, pady=10)

    quantum = Label(inp_frame, text='Time Quantum:', bd=5)
    quantum.grid(row=0, column=0, padx=5)
    quantum_entry = Entry(inp_frame, bd=5, width=5)
    quantum_entry.grid(row=0, column=1)

    label_process = Label(inp_frame, text='Process Name', bd=5)
    label_process.grid(row=2, column=0, padx=10)
    label_arrival = Label(inp_frame, text='Arrival Time', bd=5)
    label_arrival.grid(row=2, column=1, padx=10)
    label_burst = Label(inp_frame, text='Burst Time', bd=5)
    label_burst.grid(row=2, column=2, padx=10)

    lst_entries = []
    for i in range(int(n_process)):
        lst_entries.append([Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5),
                            Entry(inp_frame, width=5, bd=5)])
        lst_entries[i][0].grid(row=3 + i, column=0, padx=15)
        lst_entries[i][1].grid(row=3 + i, column=1, padx=15)
        lst_entries[i][2].grid(row=3 + i, column=2, padx=15)

    def evaluation():
        lst_value = []
        lst_arrived = []
        lst_original = []
        completed = []
        total_time = 0
        completion_time = {}
        time_quant = int(quantum_entry.get())
        flag = 0

        for j in range(int(n_process)):
            lst_value.append([lst_entries[j][0].get(),
                              int(lst_entries[j][1].get()),
                              int(lst_entries[j][2].get())])
            lst_original.append([lst_entries[j][0].get(),
                                 int(lst_entries[j][1].get()),
                                 int(lst_entries[j][2].get())])

        for process1 in range(len(lst_value)):
            for process2 in range(len(lst_value)):
                if lst_value[process1][1] < lst_value[process2][1]:
                    lst_value[process1], lst_value[process2] = lst_value[process2], lst_value[process1]

        while (len(lst_value) + len(lst_arrived)) != 0:
            if len(lst_value) != 0:
                while lst_value[0][1] == 0:
                    lst_arrived.append(lst_value.pop(0))

            if len(lst_arrived) != 0:
                for n in range(time_quant):

                    if lst_arrived[0][2] != 0:
                        Label(process_frame, text='Process ' + str(lst_arrived[0][0]), bd=4, relief=SUNKEN, width=8).grid(row=total_time // 16, column=total_time % 16)
                        lst_arrived[0][2] -= 1
                        total_time += 1

                        if lst_arrived[0][2] == 0:
                            completion_time[lst_arrived[0][0]] = total_time
                            completed.append(lst_arrived.pop(0))
                            flag = 1
                            break

                        if len(lst_value) != 0:
                            x = 0
                            while x < len(lst_value):

                                if lst_value[x][1] != 0:
                                    lst_value[x][1] -= 1

                                if lst_value[x][1] == 0:
                                    lst_arrived.append(lst_value.pop(x))
                                    x -= 1

                                x += 1

                        flag = 0

                if flag == 0:
                    lst_arrived.append(lst_arrived.pop(0))

            else:
                for n in range(lst_value[0][1]):
                    Label(process_frame, text='No Process', bd=4, relief=SUNKEN, width=8).grid(row=total_time // 16, column=total_time % 16)
                    for j in lst_value:
                        j[1] -= 1
        for process1 in lst_original:
            process1.append(completion_time[process1[0]])
            process1.append(process1[3]-process1[1])
            process1.append(process1[4] - process1[2])

        #Label(out_frame, text=str(completed)).grid(row=1, column=0)
        #Label(out_frame, text=str(completion_time)).grid(row=2, column=0)
        #Label(out_frame, text=str(lst_original)).grid(row=3, column=0)

        Label(out_frame, text='Process Name', bd=4, relief=RAISED).grid(row=1, column=0)
        Label(out_frame, text='Completion Time', bd=4, relief=RAISED).grid(row=1, column=1)
        Label(out_frame, text='Turn Around Time', bd=4, relief=RAISED).grid(row=1, column=2)
        Label(out_frame, text='Waiting Time', bd=4, relief=RAISED).grid(row=1, column=3)

        avg_waiting = 0
        avg_turnaround = 0

        for p in range(len(lst_original)):
            Label(out_frame, text=str(lst_original[p][0]), width=15, bd=5).grid(row=2 + p, column=0)
            Label(out_frame, text=str(lst_original[p][3]), width=15, bd=5).grid(row=2 + p, column=1)
            Label(out_frame, text=str(lst_original[p][4]), width=15, bd=5).grid(row=2 + p, column=2)
            Label(out_frame, text=str(lst_original[p][5]), width=15, bd=5).grid(row=2 + p, column=3)
            avg_waiting += lst_original[p][5]
            avg_turnaround += lst_original[p][4]

            Label(out_frame, text='Average Turn Around Time: ' + str(avg_turnaround / int(n_process))).grid(row=3 + len(lst_original), column=0, columnspan=4)
            Label(out_frame, text='Average Waiting Time: ' + str(avg_waiting / int(n_process))).grid(row=4 + len(lst_original), column=0, columnspan=4)

    evaluate = Button(inp_frame, text='Go', bd=5, command=evaluation)
    evaluate.grid(row=3 + int(n_process), column=0, columnspan=3, pady=5)

    exit_button = Button(root1, anchor='center', text='Close', bd=4, activebackground='dark grey', command=root1.destroy)
    exit_button.grid(sticky=S)

    root1.mainloop()

#--------------------------------------------------Home Page Content-----------------------------------------------------------------


title_label = Label(root, text="Process Scheduling", font=15, width=100, height=3, bd=5, relief=RIDGE, pady=3)
title_label.place(relx=0.5, rely=0.05, anchor=CENTER)

my_label = Label(root, text="Number of Processes:", font=3, bd=4, relief=RAISED)
my_label.place(relx=0.5, rely=0.15, anchor=CENTER, width=300, height=40)
my_entry = Entry(root, font=10, justify=CENTER, bd=4, relief=SUNKEN)
my_entry.place(relx=0.5, rely=0.2, anchor=CENTER, width=50, height=40)


fcfs = Button(root, anchor='center', text='First Come First Serve', bd=4, activebackground='dark grey', font=3, command=first_come_first_serve)
fcfs.place(relx=0.5, rely=0.3, anchor=CENTER, width=300, height=40)
sjf = Button(root, anchor='center', text='Shortest Job First', bd=4, activebackground='dark grey', font=3, command=shortest_job_first)
sjf.place(relx=0.5, rely=0.4, anchor=CENTER, width=300, height=40)
pps = Button(root, anchor='center', text='Preemptive Priority Scheduling', bd=4, activebackground='dark grey', font=3, command=preemptive_priority)
pps.place(relx=0.5, rely=0.5, anchor=CENTER, width=300, height=40)
rr = Button(root, anchor='center', text='Round Robin', bd=4, activebackground='dark grey', font=3, command=round_robin)
rr.place(relx=0.5, rely=0.6, anchor=CENTER, width=300, height=40)
exit_window = Button(root, anchor='center', text='Exit', command=root.destroy, bd=4, activebackground='dark grey', font=3)
exit_window.place(relx=0.5, rely=0.7, anchor=CENTER, width=300, height=40)


root.mainloop()
