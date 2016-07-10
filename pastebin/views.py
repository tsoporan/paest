from django.shortcuts import render, redirect, get_object_or_404
from pastebin.models import Snippet
from pastebin.forms import SnippetForm
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

def paste(request, template="paste.html"):

    if request.method == 'POST' and request.POST:
        if "url" in request.POST:
            url = request.POST['url']
            snippet = Snippet.objects.get(url__exact=url)

            if snippet.locked:
                messages.error(request, "Error: This snippet is locked.")
                return redirect('detail', url=url)

            form = SnippetForm(request.POST, instance=snippet)
            if form.is_valid():
                snippet = form.save()
                messages.success(request, "Snippet updated!")

                return redirect('detail', url=url)
            else: return redirect('detail', url=url)

        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            messages.success(request, "Snippet saved!")

            return redirect('detail', url=snippet.url)
    else:
        form = SnippetForm(initial=request.POST)

    context = {
        'form': form,
    }

    return render(request, template, context)

def detail(request, url, raw=False, template="detail.html"):
    snippet = get_object_or_404(Snippet, url__exact=url)

    if snippet.is_expired():
        messages.error(request, "Snippet has expired =(")
        return redirect('paste')

    if raw:
        response = HttpResponse(snippet.code, content_type="text/plain")
        return response

    form = SnippetForm(instance=snippet)

    lines = range(1, snippet.line_count()+1)

    context = {
        'snippet': snippet,
        'lines': lines,
        'form': form,
    }


    return render(request, template, context)
