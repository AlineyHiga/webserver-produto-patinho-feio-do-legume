# main/models.py
from django.db import models
from main.storage.vercelStorage import VercelBlobStorage
from produtoWebserver.settings import DEFAULT_FILE_STORAGE

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    foto = models.ImageField(max_length=500,upload_to='produto')  # Requer configuração do servidor de mídia
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    id_agricultor = models.IntegerField()
    classificacao = models.DecimalField(max_digits=3, decimal_places=1)
    tipo_produto = models.CharField(max_length=100)
    tipo_medida = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Campo obrigatório

    
    def delete(self, *args, **kwargs):
        if self.foto:
            storage = VercelBlobStorage()
            try:
                # Delete the image file from Vercel Blob storage
                storage.delete(self.foto.name)  # Passes the relative path to storage
                print(f"Deleted image {self.foto.name} from Vercel Blob Storage.")
            except Exception as e:
                print(f"Failed to delete file from Vercel storage: {e}")
        # Call the superclass delete to remove the database record
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'produtoWebserver'

    def __str__(self):
        return self.nome

