timeprompt = str(input("Do you want to print with time? (Y/N): "))
if timeprompt == "Y" or timeprompt == "y" or timeprompt == "":

    pcap = rdpcap('<name_of_file_here.pcap')
    s = pcap.sessions()
    print("------- SUMMARY OF CAPTURE ------")
    print(pcap.summary)
    print("------- SESSIONS --------")
    for a in s.items():
        print(a)
    print("-------- TIME ----------")
    for b, c in s.items():
        for x in c:
            print(x.time, b)
else:
    pcap = rdpcap('<name_of_file_here.pcap')
    s = pcap.sessions()
    print("------- SUMMARY OF CAPTURE ------")
    print(pcap.summary)
    print("------- SESSIONS --------")
    print(s)
    for a in s.items():
        print(a)
