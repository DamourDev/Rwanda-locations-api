# Rwanda-locations-api

_A Django REST API that provides hierarchical Rwandan location data (from provinces down to villages)._

---

## **Description**

The Rwanda Locations API provides hierarchical location data for Rwanda, including:

- Provinces  
- Districts  
- Sectors  
- Cells  
- Villages  

This API is built with **Django REST Framework (DRF)** and is useful for developers who need accurate administrative location data for applications such as e-government systems, logistics, school management, and census projects.

---

## **Installation / Setup**

1. **Clone the repository**  
   ```bash
   git clone https://github.com/DamourDev/Rwanda-locations-api.git
   cd Rwanda-locations-api

2. **Create & activate a virtual environment**
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run database migrations**
python manage.py migrate

# Usage / Running the API

1. Start the Django development server
-From the project root where manage.py is located, run:
python manage.py runserver

-The server will start at:

http://127.0.0.1:8000/

# Loading Data

1. Make sure your JSON file (data.json) is in the project root.

2. Run the Django management command to load the data:
python manage.py loaddata data.json

# 🔗 API Endpoints

1. List all provinces
GET  http://127.0.0.1:8000/provinces/
Example curl:
curl -s http://127.0.0.1:8000/provinces/ | jq

2. Retrieve one province by ID (replace <id>)
GET  http://127.0.0.1:8000/provinces/<id>/
Example curl (province id = 1):
curl -s http://127.0.0.1:8000/provinces/1/ | jq

3. List all districts
GET  http://127.0.0.1:8000/districts/
Example curl:
curl -s http://127.0.0.1:8000/districts/ | jq

4. List districts for a given province (by province id)
GET  http://127.0.0.1:8000/districts/<province_id>/
Example curl (province id = 1):
curl -s http://127.0.0.1:8000/districts/1/ | jq

5. Retrieve a single district by ID
GET  http://127.0.0.1:8000/districts/<id>/
Example:
curl -s http://127.0.0.1:8000/districts/10/ | jq

6. List sectors (all)
GET  http://127.0.0.1:8000/sectors/
curl -s http://127.0.0.1:8000/sectors/ | jq

7. List sectors for a district (by district id)
GET  http://127.0.0.1:8000/sectors/<district_id>/
.Example:
curl -s http://127.0.0.1:8000/sectors/10/ | jq

8. List cells for a sector (by sector id)
GET  http://127.0.0.1:8000/cells/<sector_id>/
Example:
curl -s http://127.0.0.1:8000/cells/25/ | jq

9. List villages for a cell (by cell id)
GET  http://127.0.0.1:8000/villages/<cell_id>/
Example:
curl -s http://127.0.0.1:8000/villages/60/ | jq

10. Retrieve a single village by ID
GET  http://127.0.0.1:8000/villages/<id>/
Example:
curl -s http://127.0.0.1:8000/villages/200/ | jq

# Contributing

Contributions are welcome!
To contribute:
1.	Fork this repository
2.	Create a feature branch (git checkout -b feature-name)
3.	Commit changes (git commit -m "Add new feature")
4.	Push to branch (git push origin feature-name)
5.	Open a Pull Request

# 👨‍💻 Author

NKURUNZIZA Jean D’Amour
-	🎓 University of Rwanda – IT Student
-	📧 Email: nkurunzizajeandamour20@gmail.com
-	📱 Phone: +250 791 261 144
-	🌍 Kigali, Rwanda
-	💼 GitHub: DamourDev


