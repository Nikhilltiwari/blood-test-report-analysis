def identify_abnormalities(extracted_info):
    # Example abnormality detection logic (customize as needed)
    abnormalities = {}
    for test, value in extracted_info.items():
        if value < 10 or value > 100:  # Example threshold values
            abnormalities[test] = value
    return abnormalities

def load_medical_knowledge():
    # Example static knowledge base
    return {
        "Test1": {"Anomalous": "Condition1"},
        "Test2": {"Anomalous": "Condition2"}
    }

def generate_recommendations(conditions, articles):
    recommendations = []
    for condition, detail in conditions.items():
        for article in articles:
            if condition in article['title']:
                recommendations.append({
                    "condition": condition,
                    "recommendation": f"Based on your condition ({condition}), you should read: {article['title']}",
                    "link": article['link']
                })
    return recommendations
