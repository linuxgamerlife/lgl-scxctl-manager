# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-03-23

### Initial release

- **Setup tab** – detects whether `scxctl` is on the system PATH at startup; if not, displays distro-agnostic installation guidance and disables operational tabs until resolved
- **Status tab** – live view of the active scheduler, mode, and service state; auto-refreshes every 5 seconds with change-detection to suppress log noise when idle; tools status indicators show whether the COPR repo (Fedora) and scx-tools are installed
- **Control tab** – start, stop, and switch schedulers with selectable mode (Auto, Gaming, Lowlatency, Powersave) and optional custom flags; note that not all modes are supported by every scheduler
- **Log tab** – timestamped output of all `scxctl` commands
- **Reference tab** – descriptions of every supported scheduler, recommended workloads, and workloads to avoid
- **Flags tab** – filterable per-scheduler custom flags reference
- **About menu** – version info, creator credits, social links, and licence notice
- System tray icon with colour-coded status indicator (green = running, red = stopped) and quick start/stop actions
- Polkit (`pkexec`) used for privilege elevation; `scxctl list` and `scxctl get` run without root
- "Enable on boot" checkbox to enable or disable `scx_loader.service` via systemctl
- Scheduler list populated dynamically from `scxctl list` with a built-in fallback if `scx_loader` is unavailable
- Input validation on scheduler names and custom flags before passing to privileged commands
- Application icon bundled into the binary via Qt resources
- Uses the system Qt theme — respects the user's light or dark mode preference
- Built with C++20 and Qt6
