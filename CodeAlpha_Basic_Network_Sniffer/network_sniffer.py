from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Basic Network Sniffer")
print("Capturing packets... Press Ctrl+C to stop.")

sniff(prn=packet_callback, count=20)
