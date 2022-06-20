from django.test import TestCase
from rest_framework.test import APIClient
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(nome="User1", telefone='(62) 92345-6789', email='User1@gmail.com')

    def test_criar_alvo(self):
        usuario = {'nome':'UserTeste', 'telefone': '(11) 98765-4321', 'email': 'Userteste@gmail.com'}
        response = self.client.post('/add_user/', usuario, format='json')
        self.assertTrue(User.objects.filter(nome='UserTeste').exists())

    def test_editar_alvo(self):
        usuario = {
                'nome': 'UserNovoNome',
                'telefone': '(85) 92345-6789',
                'email': 'usernovonome@gmail.com'
        }
        response = self.client.put(f'/edit_user/{self.user1.id}/', usuario, format='json')
        self.assertTrue(User.objects.get(id=self.user1.id).nome == usuario['nome'])
        self.assertTrue(User.objects.get(id=self.user1.id).telefone == usuario['telefone'])
        self.assertTrue(User.objects.get(id=self.user1.id).email == usuario['email'])


    def test_excluir_alvo(self):
        response = self.client.delete(f'/delete_user/{self.user1.id}/')
        self.assertFalse(User.objects.filter(id=self.user1.id).exists())
