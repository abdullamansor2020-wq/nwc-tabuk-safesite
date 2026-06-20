def analyze_image(image_path):

    result = {
        "safety_score": 78,
        "violations": [
            "Missing Helmet",
            "Missing Safety Vest",
            "Excavation Hazard"
        ],
        "recommendations": [
            "Wear Helmet",
            "Wear Safety Vest",
            "Secure Excavation Area"
        ]
    }

    return result
