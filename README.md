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

## References

- **Ubuntu (Canonical)**: [cloud-images.ubuntu.com](https://cloud-images.ubuntu.com/locator/ec2/) – Official Ubuntu AMI locator.
- **Amazon Linux 2**: [AWS Blog](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/) – How to query the latest Amazon Linux AMIs using Systems Manager Parameter Store.
- **Red Hat Enterprise Linux (RHEL)**: [EC2 Console](https://console.aws.amazon.com/ec2/) – Search for RHEL AMIs with owner alias `309956199498`.
- **SUSE Linux Enterprise Server (SLES)**: [EC2 Console](https://console.aws.amazon.com/ec2/) – Search for SLES AMIs with owner alias `013907871322`.
- **Debian**: [EC2 Console](https://console.aws.amazon.com/ec2/) – Search for Debian AMIs with owner alias `136693071363`.
- **Microsoft Windows Server**: [EC2 Console](https://console.aws.amazon.com/ec2/) – Search for Windows Server AMIs with owner alias `801119661308`.

