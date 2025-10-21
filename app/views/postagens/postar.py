from django.shortcuts import render, redirect
from app.forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def postar_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(request, 'postar.html', {'form': form})