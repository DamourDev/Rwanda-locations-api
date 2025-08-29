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
```bash
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

6. **Run database migrations**
```bash
python manage.py migrate
```

# Usage / Running the API

- Start the Django development server
- From the project root where manage.py is located, run:
```bash
python manage.py runserver
```
- The server will start at:

```
http://127.0.0.1:8000/
```

# Loading Data

1. Make sure your JSON file (data.json) is in the project root.

2. Run the Django management command to load the data:
```bash
python manage.py loaddata data.json
```

# 🔗 API Endpoints

1. List all provinces
```
http://127.0.0.1:8000/provinces/
```
2. Retrieve one province by ID (replace <id>)
```
http://127.0.0.1:8000/provinces/<id>/
Example (province id = 1):
http://127.0.0.1:8000/provinces/1/ 
```
3. List all districts
```
http://127.0.0.1:8000/districts/
Example curl:
http://127.0.0.1:8000/districts/
```
4. List districts for a given province (by province id)
```
http://127.0.0.1:8000/districts/<province_id>/
Example  (province id = 1):
http://127.0.0.1:8000/districts/1/ 
```
5. Retrieve a single district by ID
```
http://127.0.0.1:8000/districts/<id>/
Example:
http://127.0.0.1:8000/districts/10/
```
6. List sectors (all)
```
http://127.0.0.1:8000/sectors/
Example:
http://127.0.0.1:8000/sectors/
```
7. List sectors for a district (by district id)
```
http://127.0.0.1:8000/sectors/<district_id>/
.Example:
http://127.0.0.1:8000/sectors/10/
```
8. List cells for a sector (by sector id)
```
http://127.0.0.1:8000/cells/<sector_id>/
Example:
http://127.0.0.1:8000/cells/25/
```
9. List villages for a cell (by cell id)
```
http://127.0.0.1:8000/villages/<cell_id>/
Example:
http://127.0.0.1:8000/villages/60/
```
10. Retrieve a single village by ID
```
http://127.0.0.1:8000/villages/<id>/
Example:
http://127.0.0.1:8000/villages/200/
```

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


