# AWS AMI Fetcher

A simple Python tool to fetch AMI (Amazon Machine Image) IDs across AWS regions and save them into a CSV file.

## 📦 Files
- `fetch_amis.py` → Main script.
- `config.yaml` → Configuration for owners (publishers) and AWS regions.
- `amis.csv` → Output file (generated after running the script).

## ⚙️ Requirements
- Python 3.7+
- AWS credentials configured (`~/.aws/credentials` or environment variables).
- Minimum IAM permissions(Your IAM user/role needs permissions for:)
  ```json
          {
            "Version": "2012-10-17",
            "Statement": [
              {
                "Effect": "Allow",
                "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeImages"
                ],
                "Resource": "*"
              },
              {
                "Effect": "Allow",
                "Action": "sts:GetCallerIdentity",
                "Resource": "*"
              }
            ]
          }
- Install dependencies:
  ```bash
  pip install boto3 pyyaml
>>>>>>> b53d982 (Initial commit: AWS AMI Fetcher script)
