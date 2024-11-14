from django.shortcuts import render, get_object_or_404, redirect
from .models import Route
from .forms import RouteForm
from django.http import JsonResponse

# List all Routes
def route_list(request):
    routes = Route.objects.all()
    print("Route list view triggered")
    return render(request, 'route/route_list.html', {'routes': routes})

# Create a New Route
def route_create(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                return redirect('route_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': form.errors.as_json()})
    else:
        form = RouteForm()
    return render(request, 'route/route_form.html', {'form': form})

# Update an Existing Route
def route_update(request, route_id):  # Change pk to route_id
    route = get_object_or_404(Route, route_id=route_id)  # Use route_id here
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'route/route_form.html', {'form': form})

# Delete a Route
def route_delete(request, route_id):  # Change pk to route_id
    route = get_object_or_404(Route, route_id=route_id)  # Use route_id here
    if request.method == 'POST':
        route.delete()
        return redirect('route_list')
    return render(request, 'route/route_confirm_delete.html', {'route': route})

def home(request):
    return render(request, 'home.html')
