def generate_html_report(data_dict, filename="report.html"):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Netmapper-Z Report: {data_dict.get('target')}</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #121212; color: #e0e0e0; padding: 20px; }}
            h1 {{ color: #00ffcc; }}
            pre {{ background: #1e1e1e; padding: 15px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>Netmapper-Z Scan Report</h1>
        <p><strong>Target:</strong> {data_dict.get('target')}</p>
        <h2>Results Overview</h2>
        <pre>{data_dict}</pre>
    </body>
    </html>
    """
    with open(filename, "w") as f:
        f.write(html_content)
