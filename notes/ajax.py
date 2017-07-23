
# we manage all ajax call in this module.

from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Note

# ajax calling function that is receiving a note id from front-end and
# delete that note from database.


def delete_note(request):
    note_id = request.GET.get('note_id', None)
    data = {}

    if note_id:
        try:
            Note.objects.get(id=note_id).delete()
            data['success_message'] = "Note Deleted successfully."
        except Exception as e:
            data['error_message'] = 'Record Does Not exist.'
    return JsonResponse(data)
