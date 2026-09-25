<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:2c5364,100:00c6ff&height=220&section=header&text=Airline%20Delay%20%26%20Operations&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Why%20flights%20run%20late%20%E2%80%94%20and%20who%20flies%20on%20time&descAlignY=58&descSize=18" width="100%" alt="Airline Delay & Operations Analysis"/>

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=900&color=00C6FF&center=true&vCenter=true&width=640&lines=%E2%9C%88%EF%B8%8F+3M+US+flights+analysed+(2019%E2%80%932023);%F0%9F%95%92+Delay+causes%2C+routes%2C+seasons+%26+carriers;%F0%9F%93%8A+Interactive+dashboard+included" alt="Typing SVG" /></a>

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly_Dash-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)

**Built by Pragya Sharma · Data Analyst Project**

</div>

---

## 🚀 Overview

A deep dive into **US domestic flight delays**: what causes them, when and where they peak, and which airlines run the most reliable operations. Everything is wrapped up in an **interactive dashboard**.

## 📦 Dataset

🔗 [**Flight Delay and Cancellation Dataset (2019-2023)**](https://www.kaggle.com/datasets/patrickzel/flight-delay-and-cancellation-dataset-2019-2023) by *patrickzel*

Downloaded automatically with `kagglehub` inside the notebook, so **no manual CSV download** is needed (~140 MB, ~3M flight sample).

## 📄 Project Report

[Download the project report (.docx)](PragyaSharma_ProjectReport.docx)

## 🛠️ Tech Stack

| | Tool | Used for |
|:-:|---|---|
| 🐍 | **Python** | Core language |
| 🐼 | **pandas · numpy** | Cleaning and analysis |
| 📥 | **kagglehub** | Dataset download |
| 📈 | **Matplotlib · Seaborn · Plotly** | Visualisation |
| 🖥️ | **Plotly Dash** | Interactive dashboard |
| 📓 | **Jupyter Notebook** | Analysis workflow |

## ✨ Key Findings

| | Insight |
|:-:|---|
| 🛫 | **Airline-side problems dominate.** Carrier and late-aircraft delays outweigh weather, security and NAS delays combined. |
| ☀️ | **Summer is the worst.** June and July peak, especially Sundays in June (~12 min avg). **September is the best month**, often with flights arriving early. |
| 🗺️ | **Worst route: ABQ → JFK** (40.1 min avg), followed by ACK → LGA and ASE → ORD. Small airports feeding congested hubs. **Best route: ABE → CLT** (14.5 min early). |
| 🏆 | **Most punctual:** Endeavor Air, Horizon Air and Delta (~87-88% on time). **Least:** JetBlue, Frontier and Allegiant (~74%). |
| ❌ | **Cancellations:** PSA Airlines is highest (3.08%). **Hawaiian Airlines is lowest (1.21%)** and also punctual, making it the most reliable overall. |
| 📅 | **Best days to fly:** Tuesday and Wednesday. **Worst:** Thursday and Friday. |

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd AirlineDelayAnalysis

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the notebook (run all cells top to bottom)
jupyter notebook PragyaSharma_AirlineDelayAnalysis.ipynb

# 5. Launch the dashboard
cd dashboard
python app.py                  # then open http://localhost:8050
```

> 💡 If `kagglehub` asks for credentials, place your `kaggle.json` in `~/.kaggle/` (Kaggle → Account → *Create New API Token*).

## 📁 Project Structure

```
AirlineDelayAnalysis/
├── 📓 PragyaSharma_AirlineDelayAnalysis.ipynb   # Full analysis
├── 📄 PragyaSharma_ProjectReport.docx           # Project report
├── 📜 requirements.txt                           # Dependencies
├── 📘 README.md                                  # You are here
├── 🗂️ data/                                      # Local data (not submitted)
├── 🖼️ outputs/figures/                           # Charts
└── 📊 dashboard/                                 # Interactive dashboard
```

<div align="center">

**⭐ If you found this useful, give it a star! ⭐**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,50:2c5364,100:0f2027&height=100&section=footer" width="100%" alt="footer"/>

</div>
