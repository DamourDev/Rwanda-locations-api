import json
import os
from django.core.management.base import BaseCommand
from locations.models import Province, District, Sector, Cell, Village

class Command(BaseCommand):
    help = "Load Rwanda locations from JSON file into database with short hierarchical codes"

    def handle(self, *args, **kwargs):
        # ---------------------------
        # Step 1: Locate the JSON file
        # ---------------------------
        # Since the command is in locations/management/commands/, we go up 3 levels to project root
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

        # Join project root with the JSON filename
        json_file_path = os.path.join(project_root, 'data.json')
        # Normalize path to avoid OS issues
        json_file_path = os.path.normpath(json_file_path)

        try:
            # ---------------------------
            # Step 2: Open and load JSON
            # ---------------------------
            with open(json_file_path, encoding='utf-8') as f:
                data = json.load(f)

            # Print JSON for verification
            print(json.dumps(data, indent=2, ensure_ascii=False))

            # ---------------------------
            # Step 3: Insert Provinces
            # ---------------------------
            # Initialize province counter
            province_counter = 1

            for province_name, districts in data.items():
                # Generate province code: 01, 02, ...
                province_code = f"{province_counter:02d}"
                # Create province object
                province_obj = Province.objects.create(name=province_name, code=province_code)
                
                # Initialize district counter for this province
                district_counter = 1

                for district_name, sectors in districts.items():
                    # Generate district code: ProvinceCode-DistrictCode e.g. 01-01
                    district_code = f"{province_code}-{district_counter:02d}"
                    # Create district object linked to province
                    district_obj = District.objects.create(
                        name=district_name, 
                        code=district_code, 
                        province=province_obj
                    )

                    # Initialize sector counter for this district
                    sector_counter = 1

                    for sector_name, cells in sectors.items():
                        # Generate sector code: Province-District-Sector e.g. 01-01-01
                        sector_code = f"{district_code}-{sector_counter:02d}"
                        # Create sector object linked to district
                        sector_obj = Sector.objects.create(
                            name=sector_name, 
                            code=sector_code, 
                            district=district_obj
                        )

                        # Initialize cell counter for this sector
                        cell_counter = 1

                        for cell_name, villages in cells.items():
                            # Generate cell code: Province-District-Sector-Cell e.g. 01-01-01-01
                            cell_code = f"{sector_code}-{cell_counter:02d}"
                            # Create cell object linked to sector
                            cell_obj = Cell.objects.create(
                                name=cell_name, 
                                code=cell_code, 
                                sector=sector_obj
                            )

                            # Initialize village counter for this cell
                            village_counter = 1

                            for village_name in villages:
                                # Generate village code: Province-District-Sector-Cell-Village e.g. 01-01-01-01-01
                                village_code = f"{cell_code}-{village_counter:02d}"
                                # Create village object linked to cell
                                Village.objects.create(
                                    name=village_name, 
                                    code=village_code, 
                                    cell=cell_obj
                                )
                                # Increment village counter
                                village_counter += 1

                            # Increment cell counter
                            cell_counter += 1

                        # Increment sector counter
                        sector_counter += 1

                    # Increment district counter
                    district_counter += 1

                # Increment province counter
                province_counter += 1

            # Final message when all data is loaded
            print("All locations loaded successfully with hierarchical short codes!")

        except FileNotFoundError:
            # Handle file not found error
            print(f"File not found: {json_file_path}")
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            self.stdout.write(self.style.ERROR(f"JSON decode error: {e}"))
