Description:
A simple Python script for discovering WLED devices on a local network using mDNS (Zeroconf). The script scans the network and prints the IP address of the first detected WLED device.

Features:

Automatic detection of WLED devices via mDNS
Displays the IP address of the discovered device
Easy and quick to run

# WLED mDNS Scanner

This script uses mDNS (Zeroconf) to discover WLED devices on a local network and prints their IP address.

## How It Works
The script scans the network using the `zeroconf` library and looks for WLED devices via the `_wled._tcp.local.` service. When a device is found, its IP address is displayed.

## Installation

Install the required dependencies:

```bash
pip install zeroconf
