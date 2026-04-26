from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Comment
from .forms import CommentForm

def comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    return render(request, 'security_app/comments.html', {
        'form': form,
        'comments': comments,
    })

def no_csrf_view(request):
    message = ""
    if request.method == 'POST':
        message = "✅ Форма жіберілді (CSRF тексеруі ӨШІРУЛі — бұл қауіпті!)"

    return render(request, 'security_app/no_csrf.html', {'message': message})
