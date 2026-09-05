# ⚡ AlgoViz - Interactive Sorting Visualizer

A sleek, modern Python visualizer built with **CustomTkinter** for animating classical sorting algorithms in real time. Designed with a high-contrast theme, dynamic speed controls, and step-by-step logic status updates.

---

## ✨ Features

* **Real-time Status Updates:** Live banner messages showing exact comparison steps (`Comparing X with Y`), swaps, and completion alerts (`ARRAY SORTED! 🎉`).
* **Interactive Controls:** Dynamic speed slider to adjust execution delay on the fly.
* **Modern UI Design:** Clean card-based layout with glowing neon color indicators.
* **Multiple Algorithms Supported:** Selection Sort & Bubble Sort implementations.

---

## 🎨 Color Guide

| State | Indicator Color | Visual Meaning |
| :--- | :--- | :--- |
| **Unsorted** | Cyan (`#38BDF8`) | Default element state |
| **Comparing** | Orange (`#FB923C`) | Currently compared elements |
| **Minimum / Focus** | Yellow (`#EAB308`) | Target element in loop |
| **Sorted** | Emerald Green (`#4ADE80`) | Finalized position |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
Clone the repository and install the required dependencies:
```
pip install customtkinter
