from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Produto
from ..serializers import ProdutoSerializer

@api_view(['GET'])
def buscar_produtos_disponiveis(request):
    produtos = Produto.objects.filter(quantidade__gt=0)  # Produtos com quantidade > 0
    serializer = ProdutoSerializer(produtos, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def buscar_produto(request, produto_id):
    produtos = Produto.objects.filter(id_produto=produto_id)  # Produtos com quantidade > 0
    serializer = ProdutoSerializer(produtos, many=True, context={'request': request})
    return Response(serializer.data[0])
