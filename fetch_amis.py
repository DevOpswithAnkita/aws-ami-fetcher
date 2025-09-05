import boto3, csv, yaml

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

session = boto3.Session()
all_amis = []

for region in config["regions"]:
    print(f"Fetching from region: {region}...")
    ec2 = session.client("ec2", region_name=region)
    for name, owner in config["owners"].items():
        try:
            images = ec2.describe_images(Owners=[owner])["Images"]
            for img in images:
                all_amis.append([
                    region, name, img["ImageId"], img.get("Name", "N/A"), img["CreationDate"]
                ])
        except Exception as e:
            print(f"Error fetching {name} in {region}: {e}")

# Save to CSV
with open("amis.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Region", "Owner", "ImageId", "Name", "CreationDate"])
    writer.writerows(all_amis)

print("Saved amis.csv ✅")
