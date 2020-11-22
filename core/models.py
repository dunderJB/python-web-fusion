import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename): # função criada para nomear um arquivo na hora em é feito o upload para o sistema, ele irá gerar um nome com decimais que será impossivel ter outro igual e caso tenha o django irá ver e renomear para que seja único
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criaçao', auto_now_add=True) # o auto now add serve para quando um novo obejto é criado assim dando a data de criação
    modificado = models.DateField('Modificado', auto_now=True) # somente o auto now server para obejtos modificados marcando a data de modificação
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONES_CHOICE = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete')
    )
    servico = models.CharField('Serviço', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONES_CHOICE)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}) # Usar para qualquer tipo de imagem o get_file_path
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Feature(Base):
    ICONES_CHOICE = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Layer')
    )
    nome = models.CharField('Nome', max_length=50)
    icone = models.CharField('Icone', max_length=16, choices=ICONES_CHOICE)
    descricao = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Feture'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.nome
