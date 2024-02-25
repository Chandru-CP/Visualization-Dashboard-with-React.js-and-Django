from datetime import datetime
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import Analysis



def upload_json(request):
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        json_data = json.load(json_file)
        for item in json_data:
            analysis = Analysis.objects.create()
            # Map the JSON data to the model fields
            for key, value in item.items():
                if key == 'end_year':
                    if value:
                        analysis.end_year = value
                elif key == 'intensity':
                    if value:
                        analysis.intensity = value
                elif key == 'sector':
                    if value:
                        analysis.sector = value
                elif key == 'topic':
                    if value:
                        analysis.topic = value
                elif key == 'insight':
                    if value:
                        analysis.insight = value
                elif key == 'url':
                    if value:
                        analysis.url = value
                elif key == 'region':
                    if value:
                        analysis.region = value
                elif key == 'start_year':
                    if value:
                        analysis.start_year = value
                elif key == 'impact':
                    if value:
                        analysis.impact = value
                elif key == 'added':
                    if value:
                        # Convert the date to the expected format
                        added_date = datetime.strptime(value, "%B, %d %Y %H:%M:%S")
                        analysis.added = added_date.strftime("%Y-%m-%d,%H:%M:%S")
                    else:
                        # Map the other fields as before
                        if key in ['end_year', 'intensity', 'sector', 'topic', 'insight', 'url', 'region',
                                   'start_year', 'impact', 'published', 'country', 'relevance', 'pestle']:
                            if value:
                               analysis.__setattr__(key, value)
                elif key == 'published':
                    if value:
                        # Convert the date to the expected format
                        published_date = datetime.strptime(value, "%B, %d %Y %H:%M:%S")
                        analysis.published = published_date.strftime("%Y-%m-%d,%H:%M:%S")
                    else:
                        # Map the other fields as before
                        if key in ['end_year', 'intensity', 'sector', 'topic', 'insight', 'url', 'region',
                                   'start_year', 'impact', 'published', 'country', 'relevance', 'pestle']:
                            if value:
                               analysis.__setattr__(key, value)
                elif key == 'country':
                    if value:
                        analysis.country = value
                elif key == 'relevance':
                    if value:
                        analysis.relevance = value
                elif key == 'pestle':
                    if value:
                        analysis.pestle = value
                elif key == 'source':
                    if value:
                        analysis.source = value
                elif key == 'title':
                    if value:
                        analysis.title = value
                elif key == 'likelihood':
                    if value:
                        analysis.likelihood = value
            analysis.save()
        return render(request, 'Data/uploaded_data.html', {'json_data': model_to_dict(analysis)})

    return render(request, 'Data/upload.html')

def get_form_data(request):
    form_data = Analysis.objects.all()
    response_data = [
        {
            'end_year': user.end_year or "",
            'intensity': user.intensity or "",
            'sector': user.sector or "",
            'topic': user.topic or "",
            'insight': user.insight or "",
            'url': user.url or "",
            'region': user.region or "",
            'start_year': user.start_year or "",
            'impact': user.impact or "",
            'added': user.added  or "",
            'published': user.published or "",
            'country': user.country or "",
            'relevance': user.relevance or "",
            'pestle': user.pestle or "",
            'source': user.source or "",
            'title': user.title or "",
            'likelihood': user.likelihood or "",
        } for user in form_data
    ]
    return JsonResponse(response_data, safe=False)

def delete_form_data(request):
    if request.method == 'GET':
        form_data = Analysis.objects.all()
        form_data.delete()
        return JsonResponse({'error': 'DELETE request required'}, status=405)

def get_end_year_data(request, end_year=None):
    if end_year:
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(end_year=end_year)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            end_year_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or "",
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(end_year_data, safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)

def get_topic_data(request, topic=None):
    if topic:
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(topic=topic)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            topic_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or "",
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(topic_data, safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)

def get_sector_data(request, sector=None):
    if sector :
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(sector=sector)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            sector_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or "",
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(sector_data , safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)

def get_region_data(request, region=None):
    if region:
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(region=region)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            region_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or "",
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(region_data, safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)

def get_pestle_data(request, pestle=None):
    if pestle:
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(pestle=pestle)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            pestle_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or "",
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(pestle_data, safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)

def get_source_data(request, source=None):
    if source:
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(source=source)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            source_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or "",
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(source_data, safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)

def get_country_data(request, country=None):
    if country:
        # Query the database for a patient with the given ID
        queryset = Analysis.objects.filter(country=country)

        if queryset.exists():
            # Convert queryset to a list of dictionaries
            country_data = [
                {
                    'end_year': user.end_year or "",
                    'intensity': user.intensity or "",
                    'sector': user.sector or "",
                    'topic': user.topic or "",
                    'insight': user.insight or "",
                    'url': user.url or "",
                    'region': user.region or "",
                    'start_year': user.start_year or "",
                    'impact': user.impact or 0,
                    'added': user.added or "",
                    'published': user.published or "",
                    'country': user.country or "",
                    'relevance': user.relevance or "",
                    'pestle': user.pestle or "",
                    'source': user.source or "",
                    'title': user.title or "",
                    'likelihood': user.likelihood or "",
                }
                for user in queryset]
            return JsonResponse(country_data, safe=False)
        else:
            # Return an error response if the patient is not found
            return JsonResponse({"error": "not Data found"}, status=404)


def get_swot_data(request):
    analyses = Analysis.objects.all()
    swot = {
        'strengths': [],
        'weaknesses': [],
        'opportunities': [],
        'threats': []
    }

    for analysis in analyses:
        print(analysis.likelihood)
        try:
            likelihood = int(analysis.likelihood)
            if likelihood > 2:
                if analysis.impact is not None:
                    impact = int(analysis.impact)
                    if impact > 2:
                        swot['opportunities'].append({
                        'title': analysis.title,
                        'insight': analysis.insight,
                        'url': analysis.url,
                        'region': analysis.region
                    })
                    elif impact < 2:
                        swot['threats'].append({
                        'title': analysis.title,
                        'insight': analysis.insight,
                        'url': analysis.url,
                        'region': analysis.region
                    })
            if int(analysis.relevance) > 2:
                impact = int(analysis.impact)
                if impact > 2:
                    swot['strengths'].append({
                        'title': analysis.title,
                        'insight': analysis.insight,
                        'url': analysis.url,
                        'region': analysis.region
                    })
                elif impact < 2:
                    swot['weaknesses'].append({
                        'title': analysis.title,
                        'insight': analysis.insight,
                        'url': analysis.url,
                        'region': analysis.region
                    })
        except TypeError:
            print("Error: Impact field is None")

    return JsonResponse(swot)

