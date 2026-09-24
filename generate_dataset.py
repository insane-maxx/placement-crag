import os

DATASET = {
    "amazon": {
        "2023-2024": "Company: Amazon | Academic Year: 2023-2024 | Notice Date: 2024-01-15 | Document Type: Placement Notice\nEligibility Criteria for Amazon (2023-2024): Minimum CGPA required is 6.5. Maximum active backlogs: 1 allowed at the time of recruitment. Eligible Degrees: B.Tech, MCA, M.Tech. Package Offered: 18 LPA.",
        "2024-2025": "Company: Amazon | Academic Year: 2024-2025 | Notice Date: 2025-01-10 | Document Type: Placement Notice\nEligibility Criteria for Amazon (2024-2025 - UPDATED): Minimum CGPA required is 7.0. Maximum active backlogs: 0 backlogs allowed (Strict policy update). Eligible Degrees: B.Tech, MCA, M.Tech. Package Offered: 20 LPA."
    },
    "tcs": {
        "2023-2024": "Company: TCS | Academic Year: 2023-2024 | Notice Date: 2023-09-10 | Document Type: Placement Notice\nEligibility Criteria for TCS (2023-2024): Minimum CGPA required is 6.0. No active backlogs allowed at the time of joining. Eligible Degrees: All streams B.Tech, MCA. Package Offered: 4.5 LPA (Ninja) / 7 LPA (Digital).",
        "2024-2025": "Company: TCS | Academic Year: 2024-2025 | Notice Date: 2024-09-05 | Document Type: Placement Notice\nEligibility Criteria for TCS (2024-2025 - UPDATED): Minimum CGPA required is 6.5. Zero active backlogs. Eligible Degrees: All streams B.Tech, MCA. Package Offered: 5.0 LPA (Ninja) / 9.0 LPA (Prime). "
    },
    "deloitte": {
        "2023-2024": "Company: Deloitte | Academic Year: 2023-2024 | Notice Date: 2023-11-20 | Document Type: Placement Notice\nEligibility Criteria for Deloitte (2023-2024): Minimum CGPA required is 6.0. Active backlogs: Max 1 permitted. Eligible Degrees: B.Tech (CSE/IT), MCA. Package Offered: 7.6 LPA.",
        "2024-2025": "Company: Deloitte | Academic Year: 2024-2025 | Notice Date: 2024-11-15 | Document Type: Placement Notice\nEligibility Criteria for Deloitte (2024-2025 - UPDATED): Minimum CGPA required is 6.5. Active backlogs: 0 permitted. Eligible Degrees: B.Tech, MCA, M.Tech. Package Offered: 9.2 LPA."
    },
    "infosys": {
        "2023-2024": "Company: Infosys | Academic Year: 2023-2024 | Notice Date: 2023-08-01 | Document Type: Placement Notice\nEligibility Criteria for Infosys (2023-2024): Minimum CGPA: 6.0 or 60% throughout academics. Backlogs: No active backlogs. Package Offered: 4.0 LPA.",
        "2024-2025": "Company: Infosys | Academic Year: 2024-2025 | Notice Date: 2024-08-10 | Document Type: Placement Notice\nEligibility Criteria for Infosys (2024-2025 - UPDATED): Minimum CGPA: 6.5 or 65% throughout academics. Backlogs: Zero tolerance. Package Offered: 5.0 LPA (System Engineer) / 8.0 LPA (Specialist Programmer)."
    }
}

def generate_files():
    os.makedirs("./placement_docs", exist_ok=True)
    count = 0
    for company, years in DATASET.items():
        for year, content in years.items():
            year_tag = year.replace("-", "_")
            filename = f"./placement_docs/{company}_{year_tag}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
    print(f"Successfully generated {count} mock placement files inside './placement_docs/'!")

if __name__ == "__main__":
    generate_files()
