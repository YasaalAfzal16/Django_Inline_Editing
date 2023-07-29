from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import EditablePage

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import re
import pathlib

# Create your views here.


def index(req):
    data = EditablePage.objects.all()
    key_count = len(data)
    print("backend data length:", key_count)

    for i in data:
        img_path = i.image_img.url

        print("image_path:", img_path)

    # def extract_image_name(image_path):
    #     # Define the regex pattern to extract the image name
    #     pattern = r'[^\\/]+(?=\.[^\\/]+$)'

    #     # Use regex to find the image name in the path
    #     match = re.search(pattern, image_path)

    #     if match:
    #         image_name = match.group()
    #         image_ext = pathlib.Path(str(img_path)).suffix
    #         return image_name+image_ext
    #     else:
    #         return None

    # img_nm = (extract_image_name(str(img_path)))

    # # Save the image file to media/images directory
    # default_storage.save(
    #     'images/' + img_nm, ContentFile(img_path.read()))
    # "image_name_with_ext": img_nm

    return render(req, 'base.html', {"backEnd_data": data, "data_length": key_count, "image_path": img_path})


@csrf_exempt
def addContent(req):
    nm_head = req.POST.get('nm_head')
    nm_cont = req.POST.get('nm_cont')

    ocptn_head = req.POST.get('ocptn_head')
    ocptn_cont = req.POST.get('ocptn_cont')

    ctry_head = req.POST.get('ctry_head')
    ctry_cont = req.POST.get('ctry_cont')

    bg_img = req.POST.get('bg_img')

    txt_over_img = req.POST.get('txt_over_img')

    EditablePage.objects.create(
        name_heading=nm_head,
        name_content=nm_cont,
        occupation_heading=ocptn_head,
        occupation_content=ocptn_cont,
        country_heading=ctry_head,
        country_content=ctry_cont,
        image_img=bg_img,
        txt_over_img=txt_over_img,
    )

    return JsonResponse('Data ADDED Successfully!', safe=False)


@csrf_exempt
def updateContent(req):
    try:
        # if 'bg_img' in req.FILES:
        #     img_file = req.FILES['bg_img']

        #     # Saving img to path
        #     default_storage.save(
        #         'app/media/images/'+img_file.name, ContentFile(img_file.read()))

        objId = req.POST.get('id')

        nm_head = req.POST.get('nm_head')
        nm_cont = req.POST.get('nm_cont')

        ocptn_head = req.POST.get('ocptn_head')
        ocptn_cont = req.POST.get('ocptn_cont')

        ctry_head = req.POST.get('ctry_head')
        ctry_cont = req.POST.get('ctry_cont')

        bg_img = req.FILES.get('bg_img')

        txt_over_img = req.POST.get('txt_over_img')

        EditablePage.objects.update(
            id=objId,
            name_heading=nm_head,
            name_content=nm_cont,
            occupation_heading=ocptn_head,
            occupation_content=ocptn_cont,
            country_heading=ctry_head,
            country_content=ctry_cont,
            # image_img=bg_img,
            txt_over_img=txt_over_img,
        )

        obj = EditablePage.objects.all().filter(id=objId)[0]

        if bg_img:
            obj.image_img = bg_img

        else:
            print("Error in saving image....")

        obj.save()

        updated_data = EditablePage.objects.all()

        for i in updated_data:
            new_id = i.id
            img_path = i.image_img.url

            print("image_path:", img_path)

        return JsonResponse({'message': 'Data UPDATED Successfully !', "image_path": img_path, "new_id": new_id})

    except:
        return JsonResponse({'error': 'Failed to update data...'}, status=404)
