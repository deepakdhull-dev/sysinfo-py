try:
    # reads memory info from /proc/meminfo
    with open("/proc/meminfo", "r") as f:
        mem = f.readlines()

    info = dict()

    # Parse each line into key-value pairs
    for line in mem:
        part = line.strip().split(":")
        key = part[0]
        val = (
            part[1].strip().split(" ")[0]
        )  # extracts numerical value and drops unit(kB)
        info[key] = val

    # reads CPU info from /proc/cpuinfo
    with open("/proc/cpuinfo", "r") as f:
        cpu = f.readlines()

    threads = 0

    # Counts logical processors and extracts CPU metadata
    for line in cpu:
        if ":" not in line:
            continue
        part = line.strip().split(":")
        key = part[0].strip()
        val = part[1].strip()
        if key == "processor":  # each "processor" entry is one logical thread
            threads += 1
            continue
        else:
            info[key] = val  # store other fields (model name, cpu cores, etc...)

    # reads Kernel info from /proc/version
    with open("/proc/version", "r") as f:
        kr = f.readline()
    info["kernel"] = kr.split()[2]  # third token is kernel version string

    # Convert memory values from kB to GB
    memtotal = int(info["MemTotal"]) // (1024**2)
    memavailable = int(info["MemAvailable"]) // (1024**2)
    memused = memtotal - memavailable
    memusage = round(memused / memtotal * 100, 2)

    # Convert swap values from kB to GB
    swaptotal = int(info["SwapTotal"]) // (1024**2)
    swapfree = int(info["SwapFree"]) // (1024**2)
    swapused = swaptotal - swapfree
    swapusage = round(swapused / swaptotal * 100, 2) if swapused > 0 else 0.0

    # Column widhts for aligned output
    col2 = 12
    col1 = 10

    # prints kernel info
    print(f"{'-' * 20} KERNEL INFO {'-' * 20}")
    print(f"{'Version':{col1}} : {info['kernel']}")

    # prints CPU info
    print(f"{'-' * 20} CPU INFO {'-' * 20} \n")
    print(f"{'CPU':{col1}} : {info['model name']}")
    print(f"{'Cores':{col1}} : {info['cpu cores']}")
    print(f"{'Threads':{col1}} : {threads}")

    # prints memory info
    print(f"\n{'-' * 20} MEMORY INFO {'-' * 20}")
    print(
        f"{'Resource':{col2}} {'Total':{col2}} {'Used':{col2}} {'Available':{col2}} {'Usage':{col2}}"
    )
    print(
        f"{'Memory':{col2}} {str(memtotal) + ' GB':{col2}} {str(memused) + ' GB':{col2}} {str(memavailable) + ' GB':{col2}} {str(memusage) + '%':{col2}}"
    )
    print(
        f"{'Swap':{col2}} {str(swaptotal) + ' GB':{col2}} {str(swapused) + ' GB':{col2}} {str(swapfree) + ' GB':{col2}} {str(swapusage) + '%':{col2}}"
    )


except FileNotFoundError as e:
    print(f"File missing: {e}")


except PermissionError as e:
    print(f"Cannot read: {e}")


finally:
    print("Always runs — use for cleanup")
