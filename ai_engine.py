from ultralytics import YOLO

# أول تشغيل سيقوم بتنزيل النموذج تلقائياً
model = YOLO("yolov8n.pt")

def analyze_image(image):
    results = model(image)

    persons = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "person":
                persons += 1

    violations = []
    recommendations = []

    if persons > 0:
        recommendations.append(
            f"Detected {persons} worker(s). Verify helmet and safety vest."
        )

    return {
        "safety_score": 85,
        "workers_detected": persons,
        "violations": violations,
        "recommendations": recommendations
    }
