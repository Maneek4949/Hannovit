from django.http import HttpResponse
from django.shortcuts import render
import json


#filtering the specific content from json using id
def get_content(request,id, template_name ,file , name):
    with open(file, encoding="utf8") as f:
        datas = json.load(f)
    data = next((b for b in datas if str(b['id']) == id), None)
    if data:
        if name == 'blog':
            context = {name: data, 'content': generate_content(data['content'])}
            return render(request, template_name, context)
        else:
            context = {name: data, 'content': generate_content_service(data['content'])}
            return render(request, template_name, context)

    else:
        return HttpResponse("Data not found", status=404)

def generate_content(content):
    html_content = ""

    for heading_info in content["headings"]:
        heading_title = heading_info["title"]
        heading_image = heading_info.get("image", "")

        html_content += f'<h2>{heading_title}</h2>'

        if heading_image:
            html_content += f'<img src="{heading_image}" class="img-fluid rounded mx-auto d-block m-4" alt="Image">'

        if heading_info["title"] in content["subheadings"]:
            subheadings = content["subheadings"][heading_info["title"]]

            for subheading_info in subheadings:
                subheading_title = subheading_info["title"]
                subheading_image = subheading_info.get("image", "")

                html_content += f'<h3 class="px-3">{subheading_title}</h3>'

                if subheading_image:
                    html_content += f'<img src="{subheading_image}" class="img-fluid rounded mx-auto d-block m-4" alt="Image">'

                if content["contents"][heading_title][subheading_title]:
                    html_content += f'<p class="px-4">{content["contents"][heading_title][subheading_title]}</p>'
        else:
            if content["contents"][heading_title]:
                html_content += f'<p>{content["contents"][heading_title]}</p>'

    return html_content

def generate_content_service(content):
    html_content = ""

    for heading_info in content["headings"]:
        heading_title = heading_info["title"]
        heading_image = heading_info.get("image", "")

        if heading_title == "":
            # Special layout for the Introduction heading
            html_content += f'<div class="row">'
            if heading_image:
                html_content += f'<div class="col-lg-6 col-12"><img src="{heading_image}" class="img-fluid rounded mx-auto d-block mb-4" alt="Image"></div>'
            html_content += f'<div class="col-lg-6 col-12">'
        else:
            # Regular layout for other headings
            html_content += f'<div class="row">'
            html_content += f'<div class="col-lg-12">'
            
        html_content += f'<h2>{heading_title}</h2>'

        if heading_info["title"] in content["subheadings"]:
            subheadings = content["subheadings"][heading_info["title"]]

            for subheading_info in subheadings:
                subheading_title = subheading_info["title"]
                subheading_image = subheading_info.get("image", "")

                html_content += f'<h3>{subheading_title}</h3>'

                if subheading_image:
                    html_content += f'<img src="{subheading_image}" class="img-fluid rounded mx-auto d-block m-4" alt="Image">'

                if content["contents"][heading_title][subheading_title]:
                    html_content += f'<p>{content["contents"][heading_title][subheading_title]}</p>'
        else:
            if content["contents"][heading_title]:
                html_content += f'<p>{content["contents"][heading_title]}</p>'

        html_content += '</div></div>'

    return html_content
