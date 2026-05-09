# sysinfo-py
A minimal Linux system info tool that reads directly from /proc — no external dependencies, no pip, just Python 3 and the kernel.

## What it shows:
- Kernel version
- CPU model, core count, thread count
- RAM and swap — total, used, available, usage %

## Requirements
- Python 3.x
- Linux (reads /proc/meminfo, /proc/cpuinfo, /proc/version)

## Run
```bash 
python3 sysinfo.py
```
No install. No virtualenv. No dependencies.

## Sample output
```
-------------------- KERNEL INFO --------------------
Version    : 6.6.87-1-lts

-------------------- CPU INFO --------------------

CPU        : AMD Ryzen 5 5625U with Radeon Graphics
Cores      : 6
Threads    : 12

-------------------- MEMORY INFO --------------------
Resource     Total        Used         Available    Usage
Memory       15 GB        2 GB         13 GB        13.56%
Swap         3 GB         0 GB         3 GB         0.0%
```
## Why
Most system info tools either pull in psutil or shell out to lscpu/free. This reads kernel-exposed data directly from /proc — no subprocess, no third-party libs, works on any Linux system with a Python 3 interpreter.
