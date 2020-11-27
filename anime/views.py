from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from . models import Galeria, Anime
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import redirect
from . forms import AnimeForm, GaleriaForm


# Create your views here.
# objects.all() es como un select * from
# objects.filter es como un where


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


def anime(request):
    num_animes = Anime.objects.all()

    return render(
        request,
        'anime.html',
        context={'num_animes':  num_animes}
    )


def galeria(request):
    num_fotos = Galeria.objects.all()

    return render(
        request,
        'galeria.html',
        context={'num_fotos':  num_fotos}
    )


def login(request):

    return render(
        request,
        'login.html',
    )


def register(request):

    return render(
        request,
        'register.html',
    )


@method_decorator(staff_member_required, name='dispatch')
class AnimeCreate(CreateView):
    model = Anime
    fields = '__all__'


@method_decorator(staff_member_required, name='dispatch')
class AnimeUpdate(UpdateView):
    model = Anime
    fields = '__all__'


@method_decorator(staff_member_required, name='dispatch')
class AnimeDelete(DeleteView):
    model = Anime
    success_url = reverse_lazy('anime')


class AnimeDetailView(generic.DetailView):
    model = Anime


class AnimeListView(generic.ListView):
    model = Anime


class GaleriaCreate(CreateView):
    model = Galeria
    fields = '__all__'


class GaleriaUpdate(UpdateView):
    model = Galeria
    fields = '__all__'


class GaleriaDelete(DeleteView):
    model = Galeria
    success_url = reverse_lazy('galeria')


class GaleriaDetailView(generic.DetailView):
    model = Galeria


def anime_new(request):
    if request.method == "POST":
        form = AnimeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('anime-detail', pk=post.pk)
    else:
        form = AnimeForm()
        return render(request, 'anime/anime_form.html', {'form': form})


def anime_edit(request, pk):
    post = get_object_or_404(Anime, pk=pk)
    if request.method == "POST":
        form = AnimeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('anime-detail', pk=post.pk)
    else:
        form = AnimeForm(instance=post)
    return render(request, 'anime/anime_form.html', {'form': form})


def galeria_new(request):
    if request.method == "POST":
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('galeria-detail', pk=post.pk)
    else:
        form = GaleriaForm()
        return render(request, 'anime/galeria_form.html', {'form': form})


def galeria_edit(request, pk):
    post = get_object_or_404(Galeria, pk=pk)
    if request.method == "POST":
        form = GaleriaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('galeria-detail', pk=post.pk)
    else:
        form = GaleriaForm(instance=post)
    return render(request, 'anime/galeria_form.html', {'form': form})
