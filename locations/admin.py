# ----- creating admin with list_ display-----

# Import Django admin module
from django.contrib import admin

# Import all location models
from .models import Province, District, Sector, Cell, Village

# ---------------- Province ----------------
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    # Show code first, then name in list view
    list_display = ('code', 'name')
    # Allow searching by name or code
    search_fields = ('name', 'code')
    # Order objects ascending by code (01, 02, …)
    ordering = ('code',)


# ---------------- District ----------------
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    # Show code, name, and parent province
    list_display = ('code', 'name', 'province')
    # Allow searching by name or code
    search_fields = ('name', 'code')
    # Filter districts by province in sidebar
    list_filter = ('province',)
    # Order ascending by code
    ordering = ('code',)


# ---------------- Sector ----------------
@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    # Show code, name, and parent district
    list_display = ('code', 'name', 'district')
    search_fields = ('name', 'code')
    # Filter sectors by district
    list_filter = ('district',)
    ordering = ('code',)


# ---------------- Cell ----------------
@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    # Show code, name, and parent sector
    list_display = ('code', 'name', 'sector')
    search_fields = ('name', 'code')
    # Filter cells by sector
    list_filter = ('sector',)
    ordering = ('code',)


# ---------------- Village ----------------
@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    # Show code, name, and parent cell
    list_display = ('code', 'name', 'cell')
    search_fields = ('name', 'code')
    # Filter villages by cell
    list_filter = ('cell',)
    ordering = ('code',)

