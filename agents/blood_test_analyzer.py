from crewai import Agent
import re

class BloodTestAnalyzer(Agent):
    def parse_blood_test(self, blood_test_report):
        # Example of extracting information from a PDF using regex
        results = {}
        pattern = re.compile(r'(\w[\w\s]+?)\s+(\d+\.\d+)\s+\w+/\w+\s+\d+\.\d+\s+-\s+\d+\.\d+')
        for match in pattern.finditer(blood_test_report):
            test_name, result = match.groups()
            results[test_name.strip()] = float(result)
        return results

    def identify_abnormalities(self, extracted_info):
        # Define some reference intervals for simplicity
        reference_intervals = {
            "Hemoglobin": (13.00, 17.00),
            "Packed Cell Volume (PCV)": (40.00, 50.00),
            "RBC Count": (4.50, 5.50),
            # Add other tests as needed
        }
        abnormalities = {}
        for test, result in extracted_info.items():
            if test in reference_intervals:
                low, high = reference_intervals[test]
                if result < low:
                    abnormalities[test] = 'Low'
                elif result > high:
                    abnormalities[test] = 'High'
        return abnormalities
