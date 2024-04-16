from django.shortcuts import render, get_object_or_404

from .models import Job
from .filters import JobFilter


def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    job_filter = JobFilter(request.GET, jobs)
    return render(
        request, "jobs/job_list.html", {"jobs": job_filter.qs, "filter": job_filter}
    )


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, "jobs/job_detail.html", {"job": job})
