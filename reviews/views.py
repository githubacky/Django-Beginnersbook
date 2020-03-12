from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from django.http import Http404
from .forms import ReviewCreateForm	# 追加
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class ReviewList(generic.ListView):
	model = Review
	
class ReviewDetail(generic.DetailView):
	model = Review
	
class ReviewCreate(generic.CreateView):
	model = Review
	form_class = ReviewCreateForm
	success_url = reverse_lazy('reviews:review_list')
	
class ReviewUpdate(generic.UpdateView):
	model = Review
	form_class = ReviewCreateForm
	success_url = reverse_lazy('reviews:review_list')
	
class ReviewDelete(generic.DeleteView):
	model = Review
	success_url = reverse_lazy('reviews:review_list')

#--------------------------------------------------------
def review_list(request):
	context = {
		'review_list': Review.objects.all().order_by('-created_at'),
	}
	return render(request, 'reviews/review_list.html', context)

def review_detail(request, pk):
	# 関数定義はしたいけど、処理をまだ決めていない場合、passと書く
	# 書かないと関数定義に不備があるとしてエラーになる
	#pass

#	try:
#		review = Review.objects.get(pk=pk)
#	except Review.DoesNotExist:
#		raise Http404

#	review = Review.objects.get(pk=pk)
	context = {
		#'review': review,
		'review': get_object_or_404(Review, pk=pk),
	}
	return render(request, 'reviews/review_detail.html', context)

def review_create(request):
	form = ReviewCreateForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('reviews:review_list')

	context = {
		'form': form
	}
	return render(request, 'reviews/review_form.html', context)

'''
def review_create_send(request):
	name = request.POST.get('store_name')
	print('送信されたデータ→ {}'.format(name))
	return redirect('reviews:review_list')

def review_create_send(request):

	form = ReviewCreateForm(request.POST)
	# 入力内容に問題がなけれは、保存してリダイレクト
	if form.is_valid():
		form.save()
		return redirect('reviews:review_list')
	
	# 問題があれば、入力画面のテンプレートファイルに
	# エラーメッセージ入りのformオブジェクトを渡す
	else:
		context = {
			'form': form,
		}
		return render(request, 'reviews/review_form.html', context)

'''
def review_update(request, pk):
	review = get_object_or_404(Review, pk=pk)
	form = ReviewCreateForm(request.POST or None, instance=review)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('reviews:review_list')

	context = {
		'form': form
	}
	return render(request, 'reviews/review_form.html', context)

def review_delete(request, pk):
	review = get_object_or_404(Review, pk=pk)
	if request.method == 'POST':
		review.delete()
		return redirect('reviews:review_list')

	context = {
		'review': review
	}
	return render(request, 'reviews/review_confirm_delete.html', context)

