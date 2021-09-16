from projects.models import project as pj ,Review
from django.http import JsonResponse, response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework.response import Response
from .serializers import projectSerializer

@api_view(['GET'])
def getRoutes(request):

    routes=[
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getProjects(request):
    projects=pj.objects.all()
    serializer=projectSerializer(projects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    projects=pj.objects.get(id=pk)
    serializer=projectSerializer(projects,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getProjectVote(request,pk):
    project=pj.objects.get(id=pk)
    data=request.data
    user=request.user.profile
    review,created =Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    review.value=data['value']
    review.save()
    project.getVoteCount
    
    serializer=projectSerializer(project,many=False)
    return Response(serializer.data)