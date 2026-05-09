try :
    with open("/proc/meminfo","r") as f:
        mem=f.readlines()
    info=dict()
    for line in mem:
        part=line.strip().split(":")
        key=part[0]
        val=part[1].strip().split(" ")[0]
        info[key]=val
    with open("/proc/cpuinfo","r") as f:
        cpu=f.readlines()
    threads=0
    for line in cpu:
        if  ":" not in line:
            continue
        part=line.strip().split(":")
        key=part[0].strip()
        val=part[1].strip()
        if key=="processor":
            threads+=1
            continue
        else:
            info[key]=val
    with open("/proc/version","r") as f:
        kr=f.readline()
    info["kernel"]=kr.split()[2]
    memtotal=int(info["MemTotal"])//(1024**2)
    memavailable=int(info["MemAvailable"])//(1024**2)
    memused=memtotal-memavailable
    memusage=round(memused/memtotal*100,2)
    swaptotal=int(info["SwapTotal"])//(1024**2)
    swapfree=int(info["SwapFree"])//(1024**2)
    swapused=swaptotal-swapfree
    swapusage=swapused/swaptotal*100
    col3=12
    col2=10
    col1=5
    print(f"{'-'*20} KERNEL INFO {'-'*20}")
    print(f"{'Version':{col2}} : {info['kernel']}")
    print(f"{"-"*20} CPU INFO {"-"*20} \n")
    print(f"{'CPU':{col2}} : {info['model name']}")
    print(f"{'Cores':{col2}} : {info['cpu cores']}")
    print(f"{'Threads':{col2}} : {threads}")
    print(f"\n{"-"*20} MEMORY INFO {"-"*20}")
    print(f"{'Resource':{col3}} {'Total':{col3}} {'Used':{col3}} {'Available':{col3}} {'Usage':{col3}}")
    print(f"{'Memory':{col3}} {str(memtotal)+' GB':{col3}} {str(memused)+' GB':{col3}} {str(memavailable)+' GB':{col3}} {str(memusage)+'%':{col3}}")
    print(f"{'Swap':{col3}} {str(swaptotal)+' GB':{col3}} {str(swapused)+' GB':{col3}} {str(swapfree)+' GB':{col3}} {str(swapusage)+'%':{col3}}")
except FileNotFoundError as e:
    print(f"File missing: {e}")
except PermissionError as e:
    print(f"Cannot read: {e}")
finally:
    print("Always runs — use for cleanup")
