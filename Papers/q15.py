
T = int(input())
total =0
aleart = []
sensor_id = set()

with open("readings.txt", "r") as readings:
    for items in readings:
        items = items.strip()
        sensor, value = items.split(",")
        total += 1

        if float(value) > 30:
            aleart.append(items)
            sensor_id.add(sensor)

with open("alerts.txt","w") as alerts:
    for i in alerts:
        alerts.write(i + "\n")

if len(aleart) == 0:
    print("No alerts")
else:
    print(f"Total readings={total}, Alerts={len(alerts)}, Sensors={sorted(sensors)}")

