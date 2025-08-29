# Rwanda-locations-api
A Django REST API that provides hierarchical Rwandan location data ( from provinces down to villages 

Rwanda Locations API
Simple location API for Rwanda built with Django REST Framework.

 Description
 
The Rwanda Locations API provides hierarchical location data for Rwanda, including:
- Provinces
- Districts
- Sectors
- Cells
- Villages  
This API is built with Django REST Framework (DRF) and is useful for developers who need accurate administrative location data for applications such as e-government systems, logistics, school management, and census projects.

Installation / Setup

1. Clone the repository
git clone https://github.com/DamourDev/Rwanda-locations-api.git
cd Rwanda-locations-api
2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
3. Install dependencies
pip install -r requirements.txt
4. Run database migrations
python manage.py migrate

Usage / Running the API

To start the Django development server, run:
python manage.py runserver
Then visit:
•	API Root: http://127.0.0.1:8000/
•	Example Endpoint: http://127.0.0.1:8000/provinces/
________________________________________
📥 Loading Data

The location data is provided in data.json.
To load it into your database, run:
python manage.py loaddata data.json
________________________________________
🔗 API Endpoints

Here are the main endpoints exposed by the API:
•	Provinces
GET /provinces/ – List all provinces
GET /provinces/id/ – Retrieve a specific province
•	Districts
GET /districts/ – List all districts
GET /districts/id/ – Retrieve a specific district
•	Sectors
GET /sectors/ – List all sectors
•	Cells
GET /cells/ – List all cells
•	Villages
GET /villages/ – List all villages

Contribution

Contributions are welcome!
To contribute:
1.	Fork this repository
2.	Create a feature branch (git checkout -b feature-name)
3.	Commit changes (git commit -m "Add new feature")
4.	Push to branch (git push origin feature-name)
5.	Open a Pull Request
________________________________________
👨‍💻 Author
NKURUNZIZA Jean D’Amour
•	🎓 University of Rwanda – IT Student
•	📧 Email: nkurunzizajeandamour20@gmail.com
•	📱 Phone: +250 791 261 144
•	🌍 Kigali, Rwanda
•	💼 GitHub: DamourDev


