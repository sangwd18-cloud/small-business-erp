from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """用户个人资料"""
    DEPARTMENT_CHOICES = [
        ('sales', '销售部'),
        ('finance', '财务部'),
        ('inventory', '库存部'),
        ('purchasing', '采购部'),
        ('admin', '管理部'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_department_display()}"
    
    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'
