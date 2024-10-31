from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Produto
from main.serializers import ProdutoSerializer

@api_view(['PATCH'])
def atualizar_produto(request,id_agricultor, id_produto):
    try:
        print("Dados recebidos:", request.data)  # Para depuração
        produto = Produto.objects.get(id_produto=id_produto)
        if produto.id_agricultor != id_agricultor:
            return Response(
                {"detail": "Você não tem permissão para deletar este produto."},
                status=status.HTTP_403_FORBIDDEN
            )
    except Produto.DoesNotExist:
        return Response({"detail": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    # Partial update para aplicar apenas os campos enviados
    serializer = ProdutoSerializer(produto, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)