from trains.models import Train

def dfs_paths(graph, start, goal):
        '''Функция для поиска всевозможных маршрутов'''
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            if vertex in graph.keys():
                for next_ in graph[vertex] - set(path):
                    if next_ == goal:
                        yield path + [next_]
                    else:
                        stack.append((next_, path + [next_]))

def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city.id].add(q.to_city.id)
    return graph

def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    traveling_time = data['traveling_time']
    all_ways = dfs_paths(graph, from_city.id, to_city.id)
    if not len(list(all_ways)):
        raise ValueError('Маршрута, удовлетворяющего условиям нет.')
    return context
