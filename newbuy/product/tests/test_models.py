from mixer.backend.django import mixer 
import pytest

@pytest.mark.django_db
class TestModels:

    def test_product_is_in_stock(self):
        product = mixer.blend('product.Product',quantity=12)
        assert product.have_stock == True
    
    def test_product_is_not_in_stock(self):
        product = mixer.blend('product.Product',quantity=0)
        assert product.have_stock == False
