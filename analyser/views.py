from django.shortcuts import render, get_object_or_404
from .models import Application
from job.models import Job  # Import Job if you need to fetch job details

def create_application(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    # Process the application creation
    application = Application.objects.create(
        user=request.user,
        job_name=job.title,
        job_category=job.category,
        job_skills=job.skills,  # Assuming skills are stored as a comma-separated string or similar
    )
    # Redirect or render response

def application_analysis(request):
    applications = Application.objects.filter(user=request.user)
    total_applications = applications.count()
    accepted = applications.filter(status='accepted').count()
    rejected = applications.filter(status='rejected').count()

    common_reasons = applications.filter(status='rejected').values('feedback').annotate(count=models.Count('feedback')).order_by('-count')

    context = {
        'total_applications': total_applications,
        'accepted': accepted,
        'rejected': rejected,
        'common_reasons': common_reasons,
    }
    return render(request, 'analyser/application_analysis.html', context)
