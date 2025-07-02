

## ✅ Final Project Documentation: Edge AI Smart Farm Monitor



### `smartfarm-scripts`

# Final Project Documentation: Edge AI Smart Farm Monitor

## 1. Overview and Goals

The "Edge AI Smart Farm Monitor" aims to enhance precision farming by using an edge AI model to analyze environmental sensor data and issue real-time alerts to a Node-RED dashboard. Sensors like DHT11 and soil moisture sensors are interfaced with an STM32 microcontroller, which communicates with a Raspberry Pi acting as a gateway and AI inference engine. The goal is to reduce unnecessary irrigation, detect drought conditions, and support automated monitoring.

### System Diagram

```
+-----------------+        +---------------+        +---------------------+
| STM32 Sensor Hub| -----> | Raspberry Pi  | -----> | Node-RED Dashboard  |
| (Soil, Temp)    | UART   | (Edge AI w/   | MQTT   | + Alert + Logging   |
|                 |        | TensorFlow)   |        |                     |
+-----------------+        +---------------+        +---------------------+
```

---

## 2. Build System

**Yocto Project** will be used to create a custom embedded Linux image for Raspberry Pi, including support for Python3, MQTT clients, TensorFlow Lite, and GPIO/I2C support.

---

## 3. Hardware Platform

* **Primary Gateway:** Raspberry Pi 4
* **Sensor Hub:** STM32 Bluepill
* **Sensors:** DHT11 (Temp/Humidity), Soil Moisture Sensor (Analog), optional: PIR for motion or camera

---

## 4. Open Source Tools Used

* [TensorFlow Lite](https://www.tensorflow.org/lite): Edge inference
* [Mosquitto MQTT](https://mosquitto.org/): Lightweight messaging
* [Node-RED](https://nodered.org/): Dashboard and alert system
* \[WiringPi / Python RPi.GPIO]

---

## 5. Previous Course Content Reused

* Device Tree customization for I2C/UART
* Yocto meta-layer design (from previous assignments)
* Basic GPIO and peripheral drivers (reused and enhanced)

---

## 6. New Topics to Explore

* AI inference using `.tflite` models
* MQTT communication to Node-RED
* OTA updates using shell scripts

---

## 7. Course-Specific Work

This project is implemented solely for this course. No overlapping assignments from other courses are reused.

---

## 8. Code Organization

| Component             | Repository                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Shared Project Wiki   | [https://github.com/Karthigeyan06/edge-ai-smartfarm/wiki](https://github.com/Karthigeyan06/edge-ai-smartfarm/wiki)                   |
| Yocto Config Layer    | [https://github.com/Karthigeyan06/yocto-layer-smartfarm](https://github.com/Karthigeyan06/yocto-layer-smartfarm)                     |
| Scripts & Inference   | [https://github.com/Karthigeyan06/smartfarm-scripts](https://github.com/Karthigeyan06/smartfarm-scripts)                             |
| Individual Submission | [https://github.com/Karthigeyan06/edge-ai-smartfarm-Karthigeyan06](https://github.com/Karthigeyan06/edge-ai-smartfarm-Karthigeyan06) |

---

## 9. Team and Roles

* **Alice** – Yocto build setup and device tree overlays
* **Bob** – AI model training, MQTT implementation
* **You (Karthigeyan06)** – Sensor interfacing (STM32), dashboard setup, scripting

---

## 10. 📅 Project Schedule

### 🔗 GitHub Project Board

👉 [https://github.com/Karthigeyan06/edge-ai-smartfarm-schedule/projects/1](https://github.com/Karthigeyan06/edge-ai-smartfarm-schedule/projects/1)

---

### 🛠 Sprint 1 Tasks

| Student       | Task                       | Issue Link                                                              | DoD                                        | Status      |
| ------------- | -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------ | ----------- |
| Karthigeyan06 | STM32 UART + Sensor Script | [Issue #1](https://github.com/Karthigeyan06/edge-ai-smartfarm/issues/1) | Script collects sensor data + UART working | In Progress |
| Alice         | Yocto Image Config         | [Issue #2](https://github.com/Karthigeyan06/edge-ai-smartfarm/issues/2) | Boots Pi with required packages            | To Do       |
| Bob           | Train TFLite Model         | [Issue #3](https://github.com/Karthigeyan06/edge-ai-smartfarm/issues/3) | Model accuracy >90%, pushed to repo        | To Do       |

---

### 📆 Sprint Overview Table

| Sprint   | Dates           | Deliverables                     |
| -------- | --------------- | -------------------------------- |
| Sprint 1 | Jul 1 – Jul 8   | Sensor + Yocto Setup             |
| Sprint 2 | Jul 9 – Jul 16  | AI Inference + MQTT Integration  |
| Sprint 3 | Jul 17 – Jul 23 | Dashboard + Testing + Final Demo |

---

