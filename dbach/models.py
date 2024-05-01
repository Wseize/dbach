from django.db import models


class Pub(models.Model):    
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='pub/', null=True, blank=True)


class Category(models.Model):    
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='category/', null=True, blank=True)



class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)    
    # image = models.ImageField(upload_to='gallery/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    CHOICES = [
        ('To Sell', 'To Sell'),('To Edit', 'To Edit')    
    ]

    choice = models.CharField(max_length=20, choices=CHOICES, default='To Sell')


    CHOICES_TYPE = [
        ('Hoodie', 'Hoodie'),('TShirt', 'TShirt'),('Sock', 'Sock'),('Other', 'Other')  
    ]

    choice_type = models.CharField(max_length=20, choices=CHOICES_TYPE, default='Other')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"
    

class Logo(models.Model):
    name = models.CharField(max_length=255)    
    image = models.ImageField(upload_to='logo/', null=True, blank=True)

    def __str__(self):
        return self.name



class Message(models.Model):
    username = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    adress = models.CharField(max_length=255, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True)    
    image = models.ImageField(upload_to='message_images/', null=True, blank=True)
    xposition_image = models.CharField(max_length=255, null=True, blank=True)
    yposition_image = models.CharField(max_length=255, null=True, blank=True)
    text_added = models.CharField(max_length=255, null=True, blank=True)
    text_size = models.CharField(max_length=255, null=True, blank=True)
    text_font_family = models.CharField(max_length=255, null=True, blank=True)
    xposition_text = models.CharField(max_length=255, null=True, blank=True)
    yposition_text = models.CharField(max_length=255, null=True, blank=True)
    gallery = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='messages', null=True, blank=True)

    TAILLE_CHOICES = [
        ('S', 'S'),('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL'),    
    ]

    taille = models.CharField(max_length=20, choices=TAILLE_CHOICES, default='L')

    def __str__(self):
        return f"Message from {self.email} at {self.date_sent}"
    


class MessageList(models.Model):
    username = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    date_sent = models.DateTimeField(auto_now_add=True)
    galleries = models.ManyToManyField(Product, related_name='messagesList', blank=True)

    TAILLE_CHOICES = [
        ('S', 'S'),('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL'),    
    ]

    taille = models.CharField(max_length=20, choices=TAILLE_CHOICES, default='L')

    def __str__(self):
        return f"Message from {self.email} at {self.date_sent}"



class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderedProduct')
    date_ordered = models.DateTimeField(auto_now_add=True)
    sender_name = models.CharField(max_length=255, null=True, blank=True)
    sender_mobile = models.CharField(max_length=13, null=True, blank=True)
    sender_email = models.EmailField(null=True, blank=True)    
    sender_adress = models.CharField(max_length=255, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return f"Order {self.id} placed on {self.date_ordered}"


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    TAILLE_CHOICES = [
        ('S', 'S'),('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL'),    
    ]

    taille = models.CharField(max_length=20, choices=TAILLE_CHOICES, default='L')

    

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"