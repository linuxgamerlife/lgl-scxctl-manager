# SCX Scheduler Manager

A Qt6 GUI application for managing sched-ext BPF schedulers via `scxctl`.

**USE AT OWN RISK**

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Features

- **Setup tab** – detects whether `scx-tools` is installed at startup; if not, displays installation guidance for your distribution
- **Status tab** – live view of the running scheduler, mode, and service state; auto-refreshes every 5 seconds with change-detection (no log noise when idle); shows whether the COPR repo and scx-tools are installed
- **Control tab** – start, stop, or switch schedulers with a chosen mode/profile and optional custom flags
- **Log tab** – timestamped output of all `scxctl` commands
- **Reference tab** – descriptions of every scheduler and what workloads each is best suited to
- **Flags tab** – filterable reference of per-scheduler custom flags with accepted values and descriptions
- **System tray** – colour-coded indicator (green = running, red = stopped) with quick start/stop actions
- **About menu** – version info, links, and licence
- Polkit (`pkexec`) used for privilege elevation; `scxctl list` and `scxctl get` run without root
- Uses the system Qt theme — respects the user's light or dark mode preference
- Input validation on scheduler names and custom flags before passing to privileged commands

## Prerequisites

### scx-tools (provides `scxctl` and `scx_loader`)

**Fedora (via COPR):**
```bash
sudo dnf copr enable bieszczaders/kernel-cachyos-addons
sudo dnf install scx-tools scx-scheds
```

**Other distributions:**
See [github.com/sched-ext/scx](https://github.com/sched-ext/scx) for packaging and build instructions.

### Build dependencies

**Fedora:**
```bash
sudo dnf install cmake gcc-c++ qt6-qtbase-devel
```

## Building

```bash
git clone https://github.com/linuxgamerlife/scxctl-manager
cd scxctl-manager
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
```

## Running

```bash
./build/scxctl-manager
```

A polkit agent must be running (e.g. `polkit-gnome-authentication-agent-1` or `lxqt-policykit-agent`).

## Installing system-wide

```bash
sudo cmake --install build
```

Installs:
- Binary to `/usr/local/bin/scxctl-manager`
- `.desktop` file to `/usr/local/share/applications/`
- Icon to `/usr/local/share/icons/hicolor/256x256/apps/scxctl-manager.png`

## Uninstalling

```bash
sudo rm /usr/local/bin/scxctl-manager
sudo rm /usr/local/share/applications/scxctl-manager.desktop
sudo rm /usr/local/share/icons/hicolor/256x256/apps/scxctl-manager.png
```

## Usage

### Status Tab
Shows the currently running scheduler, mode, and service state. The **Stop Scheduler** button is only enabled when a scheduler is actually running. Status auto-refreshes every 5 seconds.

Also shows tool status at the bottom:
- **COPR (kernel-cachyos-addons)** – whether the COPR repo is enabled (Fedora only; shows N/A on other distributions)
- **scx-tools installed** – whether `scxctl` is detected on the system PATH

### Control Tab
1. Select a scheduler from the dropdown (populated live via `scxctl list`)
2. Choose a mode: **Auto**, **Gaming**, **Lowlatency**, or **Powersave**
   - Note: not all modes are supported by every scheduler — Auto is safe for all
3. Optionally enter custom flags (see the Flags tab for reference)
4. Click **Start** (when no scheduler is running) or **Switch** (to change the active one)
5. Check **"Enable scx_loader service on boot"** to persist the service across reboots

### Reference Tab
A table of all supported schedulers with descriptions of what each is best for, what workloads to avoid, and technical notes.

### Flags Tab
A filterable table of per-scheduler custom flags. Use the dropdown to narrow by scheduler. Flags from this table can be pasted directly into the Custom flags field on the Control tab.

### Tray Icon
- Green dot = scheduler running
- Red dot = no scheduler active
- Double-click to show/hide the window
- Right-click for quick start/stop

## Available Schedulers

The scheduler list is populated dynamically from `scxctl list`. On a typical install this includes:

| Scheduler         | Best for |
|------------------|----------|
| `scx_bpfland`     | General desktop, interactive apps — recommended default |
| `scx_beerland`    | Like bpfland but lower overhead |
| `scx_cake`        | CachyOS experimental — desktop/gaming |
| `scx_cosmos`      | General desktop and server, locality-first |
| `scx_flash`       | Batch jobs, compilation, encoding |
| `scx_lavd`        | Gaming, audio, low-latency workloads |
| `scx_layered`     | Power users wanting per-app scheduling policies |
| `scx_nest`        | Lightly-loaded desktops, turbo-boost workloads |
| `scx_p2dq`        | Mixed desktop/server, fair load balancing |
| `scx_pandemonium` | CachyOS experimental — dynamic task learning |
| `scx_rusty`       | Multi-core desktops and servers, NUMA systems |
| `scx_rustland`    | Experimentation and userspace scheduler research |
| `scx_simple`      | Testing and benchmarking only |
| `scx_tickless`    | Cloud, virtualisation, HPC, server batch workloads |

See the in-app **Reference** tab for full descriptions and the **Flags** tab for tuning options.

## Notes

- `scxctl start`, `scxctl stop`, and `scxctl switch` require root; the app uses `pkexec` for elevation
- `scxctl list` and `scxctl get` run without root
- Do **not** run `scx.service` and `scx_loader.service` simultaneously
- Disable `ananicy-cpp` if you experience scheduler watchdog timeouts
- If the scheduler list shows a built-in fallback, ensure `scx_loader.service` is running: `systemctl start scx_loader`
