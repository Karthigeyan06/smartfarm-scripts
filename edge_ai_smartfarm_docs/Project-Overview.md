
# Project Overview – Edge AI Smart Farm Monitor

## 🌟 Overview and Goals

The "Edge AI Smart Farm Monitor" aims to enhance precision farming by using an edge AI model to analyze environmental sensor data and issue real-time alerts to a Node-RED dashboard. Sensors like DHT11 and soil moisture sensors are interfaced with an STM32 microcontroller, which communicates with a Raspberry Pi acting as a gateway and AI inference engine. The goal is to reduce unnecessary irrigation, detect drought conditions, and support automated monitoring.

### 📊 System Diagram
```
+-----------------+        +---------------+        +---------------------+
| STM32 Sensor Hub| -----> | Raspberry Pi  | -----> | Node-RED Dashboard  |
| (Soil, Temp)    | UART   | (Edge AI w/   | MQTT   | + Alert + Logging   |
|                 |        | TensorFlow)   |        |                     |
+-----------------+        +---------------+        +---------------------+
```

## 🛠️ Build System
**Yocto Project** will be used to create a custom embedded Linux image for Raspberry Pi, including support for Python3, MQTT clients, TensorFlow Lite, and GPIO/I2C support.

## 🧰 Hardware Platform
- **Primary Gateway:** Raspberry Pi 4
- **Sensor Hub:** STM32 Bluepill
- **Sensors:** DHT11 (Temp/Humidity), Soil Moisture Sensor (Analog), optional: PIR for motion or camera

## 🧩 Open Source Tools Used
- [TensorFlow Lite](https://www.tensorflow.org/lite): Edge inference
- [Mosquitto MQTT](https://mosquitto.org/): Lightweight messaging
- [Node-RED](https://nodered.org/): Dashboard and alert system
- [WiringPi/Python RPi.GPIO]: GPIO access

## ♻️ Reused Course Content
- Device Tree customization for I2C/UART
- Yocto meta-layer design (from previous assignments)
- Basic GPIO and peripheral drivers (reused and enhanced)

## ➕ New Topics to Explore
- AI inference using .tflite models
- MQTT communication to Node-RED
- OTA updates using shell scripts

## 🧾 Course-Specific Work
This project is implemented solely for this course. No overlapping assignments from other courses are reused.

## 📁 Code Organization
| Component            | Repository                                              |
|----------------------|----------------------------------------------------------|
| Shared Project Wiki  | https://github.com/yourname/edge-ai-smartfarm/wiki     |
| Yocto Config Layer   | https://github.com/yourname/yocto-layer-smartfarm      |
| Scripts & Inference  | https://github.com/yourname/smartfarm-scripts          |
| Individual Submission| https://github.com/yourname/edge-ai-smartfarm-yourname |

## 👥 Team and Roles
- **Alice** – Yocto build setup and device tree overlays  
- **Bob** – AI model training, MQTT implementation  
- **You** – Sensor interfacing (STM32), dashboard setup, scripting

## 📅 Schedule Page Link
👉 [Schedule & Sprint Planning](https://github.com/yourname/edge-ai-smartfarm/wiki/Schedule)
