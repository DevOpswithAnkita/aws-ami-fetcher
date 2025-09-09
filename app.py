from flask import Flask
import csv, os

app = Flask(__name__)

def load_csv():
    amis = []
    file_path = os.path.join(os.path.dirname(__file__), "amis.csv")
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amis.append(row)
    return amis

@app.route("/")
def index():
    amis = load_csv()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS AMI Fetcher</title>
        <link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
        <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f7f7f7; }
        h2 { margin-bottom: 20px; color: #232f3e; } /* AWS dark blue */
        table.dataTable thead th {
            background-color: #FF9900; 
            color: #222F3E;
            text-align: left;
        }
        table.dataTable tbody td {
            word-wrap: break-word;  /* wrap long text */
            max-width: 300px;       /* adjust column width */
        }
        table.dataTable tbody tr:nth-child(even) {
            background-color: #f1f3f4;
        }
        table.dataTable tbody tr:nth-child(odd) {
            background-color: #ffffff;
        }
        table.dataTable tbody tr:hover {
            background-color: #e0e7ff; /* light blue hover */
        }
    </style>
    </head>
    <body>
        <h2>AWS AMI Fetcher</h2>
        <table id="amiTable" class="display" style="width:100%">
            <thead>
                <tr>
    """

    # Table headers
    for col in amis[0].keys():
        html += f"<th>{col}</th>"
    html += "</tr></thead><tbody>"

    # Table rows
    for row in amis:
        html += "<tr>"
        for val in row.values():
            html += f"<td>{val}</td>"
        html += "</tr>"

    html += """
            </tbody>
        </table>

        <script>
        $(document).ready(function() {
            $('#amiTable').DataTable({
                "pageLength": 25,
                "order": [[ 4, "desc" ]]  // sort by CreationDate by default
            });
        });
        </script>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
