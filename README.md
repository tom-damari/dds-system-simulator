# DDS System Simulator

A distributed IoT simulation system based on the DDS (Data Distribution Service) protocol, Pub/Sub architecture.  
This project includes multiple components (sensors, actuators, dashboard, camera, etc.) that communicate over a DDS data bus, demonstrating real-time message exchange, QoS policies, and system reactivity.

**Course:** Web-Based Information Systems  
**Department:** Industrial Engineering and Management, Ben-Gurion University of the Negev  
**Submission Date:** June 30, 2024  
**Team Members:** Tom Damari, Shira Monk  
**Instructor:** Mr. Moshe Bardea

## Components
- `camera_pub.py` – Sends timestamp messages at 10Hz
- `button_pub.py` – Sends start/stop commands every 20 seconds
- `temperature_sensor1_pub.py` – Publishes random temperatures (10–60°C) at 1Hz
- `temperature_sensor2_pub.py` – Publishes random temperatures (0–50°C) at 10Hz
- `actuator1.py` – Changes and publishes status based on temperature 1 and start/stop
- `actuator2.py` – Changes and publishes status based on temperature 2 and start/stop
- `dashboard_sub.py` – Displays system state every 5s, including last 10 statuses/temperatures
- `DDS.xml` – Configures DDS QoS settings (e.g., durability, reliability, history)
Each component runs as an individual Python script, publishing/subscribing via DDS.
