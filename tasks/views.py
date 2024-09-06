from rest_framework import  status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def tasks_list_api_view(request):
    if request.method == 'GET':
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






