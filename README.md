# auto-visualization

This project uses Matplotlib for real-time data visualization and AWS Lambda + S3 for dynamic data generation.

# Features
- Real-time plotting using Python and Matplotlib.
- Automated data updates stored in AWS S3.
- AWS Lambda generates random data every minute.

# Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/simonlee2216/auto-visualization.git
   cd auto-visualization

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Update the S3 bucket name in main.py and aws_lambda_function.py.
