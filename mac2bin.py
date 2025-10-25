import re

def convert_mac(mac):
    binary_mac_addr = ""
    binary_octets = []

    # Break down the MAC address into octets
    for i in range(0, len(mac), 2):
        octet = mac[i:i+2]

        # Convert octet from hexadecimal to binary
        binary = bin(int(octet, 16))[2:].zfill(8)
        binary_mac_addr += binary
        binary_octets.append(binary)

    print(f"Separate version: {':'.join(binary_octets)}")
    print(f"Compact version: {binary_mac_addr}")

def check_mac(mac):
    # Define allowed formats
    patterns = [
        r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$',   # AA:BB:CC:DD:EE:FF
        r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$',   # AA-BB-CC-DD-EE-FF
        r'^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$',  # AABB.CCDD.EEFF
        r'^[0-9A-Fa-f]{12}$'                       # AABBCCDDEEFF
    ]

    # Check if the input MAC matches any allowed format
    if any(re.fullmatch(p, mac) for p in patterns):
        # Remove separators for conversion
        mac_clean = mac.replace(":", "").replace("-", "").replace(".", "")
        convert_mac(mac_clean)
    else:
        print("The MAC address is invalid (incorrect format)")

def main():
    mac_addr = input("MAC Address: ")
    check_mac(mac_addr)

if __name__ == "__main__":
    main()
