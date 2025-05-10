from jinja2 import Environment, FileSystemLoader
import os

# Define input parameters
params = {
    "base_db": "base_db",
    "domain_db": "domain_db"
}

# Set template folder path (local or mounted from blob)
TEMPLATE_FOLDER = "./templates"  # Or your blob-mount path

# Jinja setup
env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
template = env.get_template("transform_corp_v.sql.j2")

# Render the SQL
rendered_sql = template.render(params)

# Save or print
with open("rendered_transform.sql", "w") as f:
    f.write(rendered_sql)

print("✅ SQL template rendered.")
