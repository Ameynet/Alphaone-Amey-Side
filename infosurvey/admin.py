from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'mobile', 'email', 'city', 'user_type', 'urgency', 'budget']
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="waitlist.csv"'
        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Mobile', 'Email', 'City', 'User Type', 'Urgency', 'Security Needs', 'Budget', 'Notes', 'Consent'])

        for obj in queryset:
            writer.writerow([
                obj.full_name,
                obj.mobile,
                obj.email,
                obj.city,
                obj.user_type,
                obj.urgency,
                obj.security_needs,
                obj.budget,
                obj.notes,
                'Yes' if obj.consent else 'No'
            ])

        return response

    export_as_csv.short_description = "Export Selected to CSV"

