# Filename  : forms.py
# Date  : 2018/9/26
from django import forms

from goods.models import GoodsCategory


class GoodsForm(forms.Form):
	name = forms.CharField(required=True, error_messages={'required': '商品名称必填'})
	goods_sn = forms.CharField(required=True, error_messages={'required': '商品货号必填'})
	category = forms.CharField(required=True, error_messages={'required': '商品分类必填'})
	goods_nums = forms.CharField(required=True, error_messages={'required': '库存必填'})
	market_price = forms.CharField(required=True, error_messages={'required': '市场价格必填'})
	shop_price = forms.CharField(required=True, error_messages={'required': '超市价格必填'})
	goods_brief = forms.CharField(required=True, error_messages={'required': '商品简介必填'})
	goods_front_image = forms.ImageField(required=False)

	def clean_category(self):
		# 验证字段，返回category对象
		category_id = self.cleaned_data['category']
		# 获取分类对象
		category = GoodsCategory.objects.filter(category_type=category_id).first()
		if category:
			# 返回分类对象
			return category
		else:
			raise forms.ValidationError({'category': '商品分类选择有误'})

		# 验证所有
		# def clean(self):