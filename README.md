🛍️ Snitch Return Experience Dashboard
A personal project exploring how structured feedback and data storytelling can solve real UX problems in fashion e-commerce.

📌 What This Project Is
This Streamlit dashboard simulates how brands like Snitch can improve their return system using smart review analysis. The idea: by structuring feedback (fit, quality, color mismatch, etc.), we can highlight patterns, identify problem categories, and ultimately create a smoother post-purchase experience.

You can try it live here 👉 Smart Review Dashboard

✨ What You Can Do
Upload a CSV of mock or real review data

Get key insights: average rating, top complaints, return reasons, category-wise sentiment

See where things are breaking for users — and how often

Use it as inspiration for your own product/data case studies!

🧠 Why I Built This
As someone moving from data analysis to product, I’ve always been drawn to UX problems with measurable impact. Returns in fashion e-commerce are often broken — but the data to fix them is already there. We just have to listen better.
This dashboard was my way of showing that.

📂 Sample Data
To get started quickly, I’ve added a small sample CSV in the repo. It contains:

Rating (1 to 5)

NLP_Tag (e.g., "Size Issue", "Color Mismatch")

Category (e.g., Shirts, Trousers)

Return_Reason (e.g., Fit, Late Delivery)

Feel free to modify or expand it to reflect real scenarios.

🚀 Getting Started
Clone the repo

bash
Copy
Edit
git clone https://github.com/parr129/snitch.git
cd snitch
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run snitch2.0.py
🛠️ Built With
Streamlit — for the UI

Pandas — for data wrangling

Seaborn + Matplotlib — for simple, clean visuals

🙌 Want to Contribute?
Yes please! This is meant to be a starter kit, not the final product.
Ideas you could explore:

Better sentiment tagging using NLP

Integration with real product review APIs

Predictive insights or product-level issue detection

More flexible filters and drill-downs in the UI

📫 Connect with Me
If you liked the idea or want to collaborate on something similar, let’s talk!
🔗 LinkedIn
📖 Read the full writeup on Medium
