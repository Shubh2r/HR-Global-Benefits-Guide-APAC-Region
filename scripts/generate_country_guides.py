import pandas as pd
import os

# Load Excel with headers
df = pd.read_excel("data/Copy of APAC Country Details.xlsx")

# Ensure output folder exists
os.makedirs("country-guides", exist_ok=True)

# Loop through each country
for _, row in df.iterrows():
    country = str(row["Countries"]).strip()
    filename = f"country-guides/{country.lower().replace(' ', '-')}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {country} HR Compliance Guide\n\n")

        # 📜 Official Sources
        f.write("## 📜 Official Sources\n")
        if country == "India":
            f.write("- [Ministry of Labour & Employment](https://labour.gov.in)\n")
        elif country == "Indonesia":
            f.write("- [Ministry of Manpower](https://kemnaker.go.id)\n")
        elif country == "South Korea":
            f.write("- [Ministry of Employment and Labor](https://www.moel.go.kr/english/)\n")
        elif country == "Pakistan":
            f.write("- [Pakistan Labour Department](https://labour.kp.gov.pk)\n")
            f.write("- [Pakistan Code](https://pakistancode.gov.pk)\n")
        elif country == "Hong Kong":
            f.write("- [Labour Department](https://www.labour.gov.hk/eng/index.htm)\n")
            f.write("- [GovHK Labour](https://www.gov.hk/en/residents/employment/labour/)\n")
            f.write("- [Hong Kong e-Legislation](https://www.elegislation.gov.hk)\n")
        elif country == "Singapore":
            f.write("- [Ministry of Manpower](https://www.mom.gov.sg/employment-practices)\n")
        elif country == "Malaysia":
            f.write("- [Department of Labour](https://jtksm.mohr.gov.my)\n")
        elif country == "Philippines":
            f.write("- [Department of Labor and Employment](https://www.dole.gov.ph)\n")
        elif country == "Japan":
            f.write("- [Ministry of Health, Labour and Welfare](https://www.mhlw.go.jp/english/)\n")
        elif country == "Thailand":
            f.write("- [Department of Labour Protection and Welfare](https://www.labour.go.th)\n")
        elif country == "Vietnam":
            f.write("- [Ministry of Labour, Invalids and Social Affairs](http://www.molisa.gov.vn)\n")
        elif country == "China":
            f.write("- [Ministry of Human Resources and Social Security](http://www.mohrss.gov.cn)\n")
        elif country == "Australia":
            f.write("- [Fair Work Ombudsman](https://www.fairwork.gov.au)\n")

        f.write("\n## 🧾 Summary of Benefits\n")
        for col in df.columns:
            if col != "Countries":
                val = str(row[col]).strip()
                if val and val.lower() != "nan":
                    f.write(f"**{col}**: {val}\n\n")

        f.write("## 🏷️ Tags\n")
        f.write("`#leave` `#termination` `#insurance` `#probation` `#severance`\n\n")

        f.write("## ✅ Compliance Checklist\n")
        f.write("- [ ] Minimum wage defined\n")
        f.write("- [ ] Statutory leave policies documented\n")
        f.write("- [ ] Termination notice period specified\n")
        f.write("- [ ] Severance rules explained\n")
        f.write("- [ ] Insurance or pension coverage noted\n")
        f.write("- [ ] Probation period clarified\n")

print("✅ Country guides generated in /country-guides/")
