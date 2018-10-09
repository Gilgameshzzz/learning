from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from cart.models import ShoppingCart
from goods.models import Goods


def add_cart(request):
	if request.method == 'POST':
		# 添加到session中数据格式为：
		# key==>goods
		# value==>[[id1，num, 1],[id2,num, 0],[id3,num, 1]...]
		# id商品的id num商品数量 1或0 商品选中或未选中（在结算页面起作用）
		# 1.1添加到购物车的数据，其实就是添加到session中
		# 1.2 如果商品已加入到session中，就修改session中商品的个数
		# 1.3 如果商品没有添加到session中，则添加

		# 获取从ajax中传递商品的id和商品个数
		goods_id = request.POST.get('goods_id')
		goods_num = request.POST.get('goods_num')
		# 组装存储的数据结构
		goods_list = [goods_id, goods_num, 1]
		# 判断在session中是否存储了商品信息
		if request.session.get('goods'):
			# 标识符：用于判断当前加入到购物车的商品
			# 如果购物车已经存在了该商品，则修改flag为1，否则flag还是为0
			flag = 0
			# 说明购物车已存储了商品信息
			seisson_goods = request.session['goods']
			for goods in seisson_goods:
				# 循环判断，判断加入到session中的商品是否已经存在于session中
				if goods_id == goods[0]:
					goods[1] = int(goods[1]) + int(goods_num)
					# 标识符，修改session中的商品后，标识符修改为1
					flag = 1
			# flag为0，表示添加到session中的商品之前并没有添加
			if not flag:
				seisson_goods.append(goods_list)
			# 	修改成功session中商品的信息
			request.session['goods'] = seisson_goods
			cart_count = len(seisson_goods)

		else:
			# 说明购物车还没有存储商品信息
			data = []
			data.append(goods_list)
			request.session['goods'] = data
			cart_count = 1

		return JsonResponse({'cde': 200, 'cart_count': cart_count})


def cart(request):
	if request.method == 'GET':
		# 需要判断用户是否登录，session['user_id']
		# 1、如果登录，则购物车展示当前登录用户的购物车中的数据
		# 2、如果没有登录，则购物车页面中展示session的数据
		user_id = request.session.get('user_id')
		if user_id:
			# 	登录系统用户
			shop_cart = ShoppingCart.objects.filter(user_id=user_id)
			goods_all = [(cart.goods, cart.is_select, cart.nums) for cart in shop_cart]
			return render(request, 'cart.html', {'goods_all': goods_all})
		else:
			# 没有登录
			session_goods = request.session.get('goods')
			# 拿到session中所有商品id值
			if session_goods:
				goods_all = [(Goods.objects.get(pk=good[0]), good[2], good[1])
				             for good in session_goods]
			else:
				goods_all = ''

			return render(request, 'cart.html', {'goods_all': goods_all})


def f_price(request):
	"""
	返回购物车或session中商品的价格，和总价
	{key1:[[id1, price1],[id2, price2]],key2:total_price}
	"""

	user_id = request.session.get('user_id')

	if user_id:
		# 获取当前登录系统的用户购物车信息
		carts = ShoppingCart.objects.filter(user_id=user_id)
		cart_data = {}
		cart_data['goods_price'] = [(cart.goods_id, cart.nums*cart.goods.shop_price)
		 for cart in carts]

		all_price = 0
		# 总的价格
		for cart in carts:
			if cart.is_select:
				all_price += cart.nums*cart.goods.shop_price
		cart_data['all_price'] = all_price
	else:
		# 拿到session中所有商品信息
		session_goods = request.session.get('goods')
		# 返回数据结构，{'goods_price':[[id1,price1],[id2,price2],...]}
		cart_data = {}
		data_all = []
		# 计算总价
		all_price = 0
		for goods in session_goods:
			data = []
			data.append(goods[0])
			g = Goods.objects.get(pk=goods[0])
			data.append(int(goods[1]) * g.shop_price)
			data_all.append(data)
			# 判断如果商品勾选了，才计算总价格
			if goods[2]:
				all_price += int(goods[1]) * g.shop_price
		cart_data['goods_price'] = data_all
		cart_data['all_price'] = all_price
	return JsonResponse({'code': 200, 'cart_data': cart_data})