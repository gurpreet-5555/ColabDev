#views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response 
from .serializers import ProjectSerializer
from projects.models import Project, Review , Tag

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'}, #for expiration time of token

    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects,many=True) #here this serializer will take in projects as query set and convert it into json
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project,many=False) #here this serializer will take in projects as query set and convert it into json
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data=request.data

    # print('DATA:',data)
    review, created = Review.objects.get_or_create(
        owner = user,
        project=project, 
    )

    review.value = data['value']
    review.save()
    project.getVoteCount


    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId=request.data['project']

    project = Project.objects.get(id=projectId)
    tag =Tag.objects.get(id=tagId)

    project.tags.remove(tag)
    
    return Response('Tag is deleted')
