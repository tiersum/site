#!/usr/bin/env python3
"""Kill process listening on a given port."""

import argparse
import os
import signal
import subprocess
import sys


def kill_port(port):
    if sys.platform == "darwin":
        result = subprocess.run(["lsof", "-ti", f":{port}"], capture_output=True, text=True)
        pids = [p.strip() for p in result.stdout.strip().split("\n") if p.strip()]
    elif sys.platform.startswith("linux"):
        result = subprocess.run(["fuser", f"{port}/tcp", "2>/dev/null"], capture_output=True, text=True, shell=True)
        pids = [p.strip() for p in result.stdout.strip().split() if p.strip()]
    else:
        print(f"Unsupported platform: {sys.platform}")
        sys.exit(1)

    if not pids:
        print(f"Port {port} is free — no process found.")
        return

    for pid in pids:
        try:
            os.kill(int(pid), signal.SIGKILL)
            print(f"Killed PID {pid} (port {port})")
        except ProcessLookupError:
            print(f"PID {pid} already gone")
        except Exception as e:
            print(f"Failed to kill PID {pid}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kill process by port")
    parser.add_argument("port", type=int, help="Port number")
    args = parser.parse_args()
    kill_port(args.port)
