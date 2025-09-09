import boto3, csv, yaml, os

# Load config.yaml
config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(config_path, "r") as f:
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
                    region,
                    name,
                    img["ImageId"],
                    img.get("Name", "N/A"),
                    img["CreationDate"],
                    img.get("Architecture", "N/A"),
                    img.get("RootDeviceType", "N/A"),
                    img.get("BlockDeviceMappings", [{}])[0].get("Ebs", {}).get("VolumeType", "N/A")
                ])
        except Exception as e:
            print(f"Error fetching {name} in {region}: {e}")

# Save to CSV (8 columns)
csv_path = os.path.join(os.path.dirname(__file__), "amis.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Region", "Owner", "ImageId", "Name", "CreationDate",
        "Architecture", "RootDeviceType", "VolumeType"
    ])
    writer.writerows(all_amis)

print("Saved amis.csv with full details")
